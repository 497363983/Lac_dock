from pymol import cmd
import utils
import os

RESIDUES = [
    'ALA', 'ILE', 'LEU', 'MET', 'VAL', 'PHE', 'TRP', 'TYR', 'ASN', 'CYS',
    'GLN', 'SER', 'THR', 'ASP', 'GLU', 'ARG', 'HIS', 'LYS', 'GLY', 'PRO'
]


def get_resname(molecule: str, chain: str, resi: str) -> str:
    """
    USAGE
    get_resname molecule, chain, resi

    DESCRIPTION
    Get residue name of a residue

    ARGUMENTS
    molecule = string: name of molecule
    chain = string: chain ID
    resi = string: residue number

    RETURNS
    string: residue name
    """
    selection = "/%s//%s/%s" % (molecule, chain, resi)
    print(selection)
    return cmd.get_model(selection).atom[0].resn


def mutate(molecule: str,
           file: str,
           chain: str,
           resi: str,
           target: str,
           mutframe: int = 1,
           save_path="./mutate",
           add_h: bool = True) -> None:
    """
    USAGE
    mutate molecule, chain, resi, target, mutframe=1

    DESCRIPTION
    Mutate a residue in a molecule

    ARGUMENTS
    molecule = string: name of molecule
    chain = string: chain ID
    resi = string: residue number
    target = string: target residue name
    mutframe = int: frame number for mutation

    RETURNS
    None
    """
    target = target.upper()
    cmd.load(file, molecule)
    name = f'{molecule}_{chain}_{utils.amino_trans[get_resname(molecule, chain, resi)]}_{resi}_{utils.amino_trans[target]}'
    cmd.wizard("mutagenesis")
    cmd.refresh_wizard()
    cmd.get_wizard().set_mode("%s" % target)
    selection = "/%s//%s/%s" % (molecule, chain, resi)
    cmd.get_wizard().do_select(selection)
    cmd.frame(str(mutframe))
    cmd.get_wizard().apply()
    cmd.set_wizard()
    cmd.h_add(molecule) if add_h else None
    cmd.save(os.path.join(save_path, molecule, f'{name}.pdb'), molecule)
    cmd.delete('all')


def mutate_residues(molecule: str,
                    file: str,
                    chain: str,
                    resi: str,
                    mutframe: int = 1,
                    save_path="./mutate") -> None:
    """
    USAGE
    mutate_residues molecule, chain, resis, target, mutframe=1

    DESCRIPTION
    Mutate a list of residues in a molecule

    ARGUMENTS
    molecule = string: name of molecule
    chain = string: chain ID
    resis = string: residue number
    target = string: target residue name
    mutframe = int: frame number for mutation

    RETURNS
    None
    """
    for resn in RESIDUES:
        mutate(molecule, file, chain, resi, resn, mutframe, save_path)


def mutate_all(molecule: str,
               file: str,
               chain: str,
               resis: list,
               mutframe: int = 1,
               save_path="./mutate") -> None:
    """
    USAGE
    mutate_all molecule, chain, mutframe=1

    DESCRIPTION
    Mutate all residues in a molecule

    ARGUMENTS
    molecule = string: name of molecule
    chain = string: chain ID
    mutframe = int: frame number for mutation

    RETURNS
    None
    """
    for resi in resis:
        mutate_residues(molecule, file, chain, resi, mutframe, save_path)


def get_resis_by_selection(selection: str = "") -> list:
    """
    USAGE
    get_resis_by_selection selection

    DESCRIPTION
    Get residue numbers of a molecule by selection

    ARGUMENTS
    selection = string: selection of ligand

    RETURNS
    list: residue numbers
    """
    return list(set([item.resi for item in cmd.get_model(selection).atom]))
