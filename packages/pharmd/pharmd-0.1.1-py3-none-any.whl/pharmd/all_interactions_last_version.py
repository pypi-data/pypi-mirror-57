import argparse
import itertools
import os
import numpy
import pybel
import mdtraj as md
from collections import defaultdict
from plip.modules.preparation import PDBComplex
from pmapper.pharmacophore import Pharmacophore
from pmapper.customize import load_smarts
from rdkit import Chem


def create_parser():
    parser = argparse.ArgumentParser(description='Extract pharmacophore models from an MD trajectory of a '
                                                 'protein-ligand complex.')
    parser.add_argument('-i', '--input', metavar='input.xtc', required=False, type=str,
                        help='Input file with MD trajectory. Formats are the same as MDTraj supports.')
    parser.add_argument('-t', '--topology', metavar='input.pdb', required=False, type=str,
                        help='PDB file with topology')
    parser.add_argument('-f', '--first', metavar='INTEGER', required=False, type=int,
                        help='Staring frame number.')
    parser.add_argument('-l', '--last', metavar='INTEGER', required=False, type=int,
                        help='Last frame number.')
    parser.add_argument('-s', '--stride', metavar='INTEGER', required=False, type=int,
                        help='Step using to extract frames.')
    parser.add_argument('-o', '--output', metavar='output.pdb', required=False,
                        help='output PDB file with all extracted frames. Solvent will be omitted.')
    parser.add_argument('-p', '--pdb_input', metavar='frames.pdb', required=False, type=str, default=None,
                        help='PDB file with multiple frames of a trajectory - an alternative input to MD trajectory. '
                             'Output pharmacophore models will be stored in the same directory; '
                             'output argument would be ignored as all other arguments related to extraction of frames '
                             'from MD trajectory..')
    parser.add_argument('-g', '--lig_id', metavar='STRING', required=True, type=str,
                        help='three-letter ligand ID')
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        help='print progress to STDERR.')
    return parser


def load_complex_from_string(pdb_string, lig_id):
    complex = PDBComplex()  # plip molecule
    complex.load_pdb(pdb_string, as_string=True)
    mol = pybel.readstring('pdb', pdb_string)  # openbabel molecule
    lig_pdb_string = []
    for line in pdb_string.split('\n'):
        if line[17:20] == lig_id:
            lig_pdb_string.append(line)
    lig_pdb_string = '\n'.join(lig_pdb_string)
    lig = Chem.MolFromPDBBlock(lig_pdb_string, removeHs=False)  # rdkit molecule
    return complex, mol, lig


def plip_analysis(my_mol, lig_index):
    true_lig = my_mol.ligands[lig_index]

    hetid = true_lig.hetid
    chain = true_lig.chain
    position = true_lig.position
    my_bsid = f'{hetid}:{chain}:{position}'
    my_mol.analyze()
    my_interactions = my_mol.interaction_sets[my_bsid]  # find interactions only for one ligand
    return my_interactions


def center_interactions(interaction):
    # find geometry center of the group
    x = []
    y = []
    z = []
    for coords in interaction:
        x.append(coords[0])
        y.append(coords[1])
        z.append(coords[2])
    l = len(interaction)
    center_coords = (round(sum(x)/l, 3), round(sum(y)/l, 3), round(sum(z)/l, 3))
    return center_coords


def center_interactions_el(all_coords):
    # find the center of group participating in electrostatic interactions
    centers = []
    for interact in all_coords:
        center_coords = center_interactions(interact)
        centers.append(center_coords)
    return centers


def dist_euclidean(check):
    # returns the list of the distances between ligand and protein
    # and the dict of the ligand coordinates with the distance to the protein
    distance = {}
    d = []
    for center, prot in check.items():
        xl = center[0]
        yl = center[1]
        zl = center[2]
        xp = prot[0]
        yp = prot[1]
        zp = prot[2]
        dist = numpy.sqrt((xl-xp)**2+(yl-yp)**2+(zl-zp)**2)
        d.append(dist)
        distance[center] = dist
    return d, distance


def find_right_distance(all_one_type, group_coords_el):
    # returnes the list of dicts with idex and coords of ligand atom
    #with distance between ligand atom and protein below the threshold
    dist = []
    for Type_atoms_coords in all_one_type:
        for group_coords in group_coords_el:
            for prot, lig in itertools.product(Type_atoms_coords, group_coords):
                euc_dist = numpy.sqrt((prot[0]-lig[0])**2+(prot[1]-lig[1])**2+(prot[2]-lig[2])**2)
                if 0.5 < euc_dist < 4:
                    dist.append(group_coords)
    return set(dist)


def find_negative(mol, atom_ids, conf):
    # returnes the list of list of nitrogen atoms in residue which can interact with ligand
    positive_reses = []
    all_mol_residues = mol.residues
    for res in all_mol_residues:
        if res.name == 'LYS' or res.name == 'ARG' or res.name == 'HIS':
            positive_reses.append(res)
    groups_atoms = []
    for res in positive_reses:
        groups_atoms.append(res.atoms)
    all_type_N = []
    for group in groups_atoms:
        type_N_atom = []
        for atom in group:
            if 'N' in atom.type and not 'Nam' in atom.type:
                type_N_atom.append(atom.coords)
        all_type_N.append(type_N_atom)
    for features, groups in atom_ids.items():
        if features == 'N':
            group_coords_negative = []
            for group in groups:
                coords = []
                for ids in group:
                    xyz = conf.GetAtomPosition(ids)
                    coords.append((xyz.x, xyz.y, xyz.z))
                group_coords_negative.append(tuple(coords))
    return all_type_N, group_coords_negative


def find_positive(mol, atom_ids, conf):
    # returnes the list of list of oxygen  atoms in residue which can interact with ligand
    name_res_neg = []
    negative_reses = []
    all_mol_residues = mol.residues
    for res in all_mol_residues:
        if res.name == 'GLU' or res.name == 'ASP':  # find GLU and ASP in protein
            negative_reses.append(res)
            name_res_neg.append(res.name)
    groups_atoms_neg = []  # add pybel.atoms in each residue GLU and ASP
    for res in negative_reses:
        groups_atoms_neg.append(res.atoms)
    all_type_O = []  # add atoms of GLU and ASP which can participate in electrostatic interations as positive center
    for group in groups_atoms_neg:
        type_O_atom = []
        for atom in group:
            if 'O.co2' in atom.type:
                type_O_atom.append(atom.coords)
        all_type_O.append(type_O_atom)
    for features, groups in atom_ids.items():
        if features == 'P':
            group_coords_positive = []
            for group in groups:
                coords = []
                for ids in group:
                    xyz = conf.GetAtomPosition(ids)
                    coords.append((xyz.x, xyz.y, xyz.z))
                group_coords_positive.append(tuple(coords))
    return all_type_O, group_coords_positive


def find_hydrogen_bonds(interactions, centers_pmapper):
    hb_ldon = [('D', tuple(hb_ldon.d.coords)) for hb_ldon in interactions.hbonds_ldon]
    hb_pdon = [('A', tuple(hb_pdon.a.coords)) for hb_pdon in interactions.hbonds_pdon]
    donor = set(hb_ldon).intersection(centers_pmapper)
    acceptor = set(hb_pdon).intersection(centers_pmapper)
    return donor, acceptor


def find_aromatic(interactions, centers_pmapper):
    pistacking = [('a', tuple(pistacking.ligandring.center)) for pistacking in interactions.pistacking]
    true_pistacking = set()
    for feature, interaction in pistacking:
        rounded = []
        for coords in interaction:
            rounded.append(round(coords, 3))
        true_pistacking.add(('a', tuple(rounded)))
    rounded_centers = set()
    for feature, interaction in centers_pmapper:
        if feature == 'a':
            rounded = []
            for coords in interaction:
                rounded.append(round(coords, 3))
            rounded_centers.add(('a', tuple(rounded)))
    aromatic = true_pistacking.intersection(rounded_centers)
    return aromatic


def find_hydrophobic(interactions, atom_ids, conf):
    hc = [hydrophobic_contacts for hydrophobic_contacts in interactions.hydrophobic_contacts]
    hydrophobic = {}  # dict ligand coords, which participates in hydrophobic interactions - protein coords
    for contact in hc:
        hydrophobic[contact.ligatom.coords] = contact.bsatom.coords
    f_hydrophobic_group = []
    for features, groups in atom_ids.items():
        if features == 'H':
            group_coords_hydraphobic = []
            for group in groups:
                coords = []
                for ids in group:
                    xyz = conf.GetAtomPosition(ids)
                    coords.append((xyz.x, xyz.y, xyz.z))
                f_hydrophobic_group.append(tuple(coords))
    true_hydrophobic_group = {}  # key hydrophobic atom's coords in group - value protein coords
    for atom, protein in hydrophobic.items():  # matching with smarts
        for group in f_hydrophobic_group:
            if atom in group:
                true_hydrophobic_group[group] = protein
    hyd_centers = {}  # key coordinates of center of group - value coordinates of protein
    for group, prot in true_hydrophobic_group.items():
        hyd_centers[center_interactions(group)] = prot
    need_check = {}
    tmp = []
    for protein in hyd_centers.values():
        tmp.append(protein)
    for group, protein in hyd_centers.items():
        if tmp.count(protein) > 1:
            need_check[group] = protein
    d, distance = dist_euclidean(need_check)
    min_distance = []
    for center, dist in distance.items():
        if min(d) == dist:
            min_distance.append(center)
    hydrophobic_centers = set(hyd_centers).difference(set(need_check))
    hydrophobic_centers.update(set(min_distance))
    hydrophobic_true = []
    for coords in hydrophobic_centers:
        hydrophobic_true.append(('H', coords))
    return hydrophobic_true


def find_electrostatic(mol, atom_ids, conf):
    all_type_N, group_coords_negative = find_negative(mol, atom_ids, conf)
    all_type_O, group_coords_positive = find_positive(mol, atom_ids, conf)
    all_coords_negative = find_right_distance(all_type_N, group_coords_negative)
    all_coords_positive = find_right_distance(all_type_O, group_coords_positive)
    negative = center_interactions_el(all_coords_negative)
    positive = center_interactions_el(all_coords_positive)
    return positive, negative


def check_interactions(interactions, mol, lig, atom_ids, centers_pmapper, conf):
    checked_interactions = []
    aromatic = find_aromatic(interactions, centers_pmapper)
    if aromatic:
        checked_interactions.append(aromatic)
    donor, acceptor = find_hydrogen_bonds(interactions, centers_pmapper)
    if acceptor:
        checked_interactions.append(acceptor)
    if donor:
        checked_interactions.append(donor)
    hydrophobic = find_hydrophobic(interactions, atom_ids, conf)
    if hydrophobic:
        checked_interactions.append(hydrophobic)
    positive, negative = find_electrostatic(mol, atom_ids, conf)
    if positive:
        checked_interactions['P'].append(positive)
    if negative:
        checked_interactions['N'].append(negative)
    return checked_interactions


def writeInteractions(fname, interactions):
    # writes xyz file with all interactions for one frame
    with open(fname, 'wt') as xyz:
        xyz.write('\n\n')
        for feature in interactions:
            for label, coords in feature:
                xyz.write('{0:s}{1:12.5f}{2:12.5f}{3:12.5f}\n'.format(label, coords[0], coords[1], coords[2]))


def read_pdb_models(fname):
    with open(fname) as f:
        lines = []
        for line in f:
            if not line.startswith("MODEL") and not line.startswith("ENDMDL"):
                lines.append(line)
            if line.startswith("ENDMDL"):
                yield ''.join(lines)
                lines = []


def get_lig_index(complex, lig_id):
    index = None
    for ligand in complex.ligands:
        if lig_id in ligand:
            index = complex.ligands.index(ligand)
    return index


def entry_point():

    parser = create_parser()
    args = parser.parse_args()
    args.lig_id = args.lig_id.upper()

    if args.pdb_input is None:
        traj = md.load(args.input, top=args.topology)
        traj.remove_solvent(inplace=True)
        traj[args.first:args.last:args.stride].save_pdb(args.output)
        pdb_input = args.output
    else:
        pdb_input = args.pdb_input

    for i, pdb_string in enumerate(read_pdb_models(pdb_input)):
        complex, mol, lig = load_complex_from_string(pdb_string, args.lig_id)
        lig_index = get_lig_index(complex, args.lig_id)
        p = Pharmacophore()
        p.load_from_mol(lig)
        centers_pmapper = set(p.get_feature_coords())
        smarts = load_smarts()
        atom_ids = p._get_features_atom_ids(lig, smarts)
        conf = lig.GetConformer(0) 
        interactions = plip_analysis(complex, lig_index)
        all_interactions = check_interactions(interactions, mol, lig, atom_ids, centers_pmapper, conf)
        writeInteractions(os.path.splitext(pdb_input)[0] + f'{i:05d}.xyz', all_interactions)


if __name__ == '__main__':
    entry_point()

