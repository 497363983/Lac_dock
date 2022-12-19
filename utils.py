import os


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
    f = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == '.pdb':
                f.append(os.path.join(root, file))
    return f


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
