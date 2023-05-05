# utils.py
import os
import glob


RESIDUES = [
    'ALA', 'ILE', 'LEU', 'MET', 'VAL', 'PHE', 'TRP', 'TYR', 'ASN', 'CYS',
    'GLN', 'SER', 'THR', 'ASP', 'GLU', 'ARG', 'HIS', 'LYS', 'GLY', 'PRO'
]


def get_typed_files_from_dir(file_dir: str, type: str):
    """
    USAGE:
    get_typed_files_from_dir file_dir type

    DESCRIPTION:
    Get all files with a specific type in a directory

    ARGUMENTS:
    file_dir = string: path of directory
    type = string: type of file

    RETURNS:
    list: list of files
    """
    assert os.path.exists(file_dir), f'The directory {file_dir} is not exist!'
    files = glob.glob(f'{file_dir}/*.{type}')
    return files


def get_pdb_files(path: str = 'structure') -> list:
    """
    USAGE:
    get_pdb_files path

    DESCRIPTION:
    Get all pdb files in a directory

    ARGUMENTS:
    path = string: path of directory

    RETURNS:
    list: list of pdb files
    """
    return get_typed_files_from_dir(path, 'pdb')


amino_trans = {
    'ALA': 'A',
    'ARG': 'R',
    'ASN': 'N',
    'ASP': 'D',
    'CYS': 'C',
    'GLN': 'Q',
    'GLU': 'E',
    'GLY': 'G',
    'HIS': 'H',
    'ILE': 'I',
    'LEU': 'L',
    'LYS': 'K',
    'MET': 'M',
    'PHE': 'F',
    'PRO': 'P',
    'SER': 'S',
    'THR': 'T',
    'TRP': 'W',
    'TYR': 'Y',
    'VAL': 'V',
}


def get_file_suffix(file_name: str) -> str:
    # Get the suffix of the file
    assert '.' in file_name, f'The file name {file_name} dose not having suffix!'
    suffix = file_name.split('.')[-1]
    return suffix


def prepare_ligand(file_name: str,
                   prepare_ligand4_py: str,
                   ligand_file_type: list = ['pdb', 'mol2']) -> str:
    """
    USAGE:
    prepare_ligand file_name

    DESCRIPTION:
    Prepare ligand file for docking

    ARGUMENTS:
    file_name = string: file name of ligand
    prepare_ligand4_py = string: path of prepare_ligand4.py

    RETURNS:
    string: file name of prepared ligand
    """
    suffix = get_file_suffix(file_name)
    assert suffix in ligand_file_type, f'The ligand file {file_name} is not an allowed file!'
    assert os.path.exists(
        file_name), f'The ligand file {file_name} is not exist!'
    assert os.path.exists(
        prepare_ligand4_py
    ), f'The prepare_ligand4.py file {prepare_ligand4_py} is not exist!'
    new_name = file_name.replace(f'.{suffix}', '.pdbqt')
    os.system(
        f'pythonsh {prepare_ligand4_py} -l {file_name} -o {new_name} -A hydrogens'
    )
    return new_name


def prepare_receptor(file_name: str,
                     prepare_receptor4_py: str,
                     receptor_file_type: list = ['pdb']) -> str:
    """
    USAGE:
    prepare_receptor file_name

    DESCRIPTION:
    Prepare receptor file for docking

    ARGUMENTS:
    file_name = string: file name of receptor
    prepare_receptor4_py = string: path of prepare_receptor4.py

    RETURNS:
    string: file name of prepared receptor
    """
    suffix = get_file_suffix(file_name)
    assert suffix in receptor_file_type, f'The receptor file {file_name} is not an allowed file!'
    assert os.path.exists(
        file_name), f'The receptor file {file_name} is not exist!'
    assert os.path.exists(
        prepare_receptor4_py
    ), f'The prepare_receptor4.py file {prepare_receptor4_py} is not exist!'
    new_name = file_name.replace(f'.{suffix}', '.pdbqt')
    os.system(
        f'pythonsh {prepare_receptor4_py} -r {file_name} -o {new_name} -A checkhydrogens'
    )
    return new_name


def prepare_ligands(prepare_ligand4_py: str,
                    ligands_dir: str = "",
                    ligands_files: list = [],
                    ligand_file_type: list = ['pdb', 'mol2']) -> list:
    """
    USAGE:
    prepare_ligands ligands_dir

    DESCRIPTION:
    Prepare ligand files for docking

    ARGUMENTS:
    ligands_dir = string: path of ligands directory
    prepare_ligand4_py = string: path of prepare_ligand4.py
    ligands_files = list: list of ligand files

    RETURNS:
    list: list of prepared ligand files
    """
    assert os.path.exists(
        ligands_dir) or len(ligands_files) > 0, 'There is no ligands files!'
    assert os.path.exists(
        prepare_ligand4_py
    ), f'The prepare_ligand4.py file {prepare_ligand4_py} is not exist!'
    if len(ligands_files) > 0:
        ligands = ligands_files
    else:
        ligands = get_pdb_files(ligands_dir)
    ligands = [
        prepare_ligand(ligand, prepare_ligand4_py, ligand_file_type=ligand_file_type) for ligand in ligands
    ]
    return ligands


def prepare_receptors(prepare_receptor4_py: str,
                      receptors_dir: str = "",
                      receptors_files: list = [],
                      receptor_file_type: list = ['pdb']) -> list:
    """
    USAGE:
    prepare_receptors receptors_dir

    DESCRIPTION:
    Prepare receptor files for docking

    ARGUMENTS:
    receptors_dir = string: path of receptors directory
    prepare_receptor4_py = string: path of prepare_receptor4.py
    receptors_files = list: list of receptor files

    RETURNS:
    list: list of prepared receptor files
    """
    assert os.path.exists(receptors_dir) or len(
        receptors_files) > 0, 'There is no receptors files!'
    assert os.path.exists(
        prepare_receptor4_py
    ), f'The prepare_receptor4.py file {prepare_receptor4_py} is not exist!'
    if len(receptors_files) > 0:
        receptors = receptors_files
    else:
        receptors = get_pdb_files(receptors_dir)
    receptors = [
        prepare_receptor(receptor, prepare_receptor4_py, receptor_file_type=receptor_file_type)
        for receptor in receptors
    ]
    return receptors