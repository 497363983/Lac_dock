from Pymol import get_resis_by_selection, mutate_all
from pymol import cmd

if __name__ == "__main__":
    for i in ['TvLac', 'PsLac', 'PoLac', 'BspLac']:
        cmd.delete('all')
        cmd.load(f'structure/{i}.pdb', i)
        resis = get_resis_by_selection(
            f"(br. all within 5 of /{i}//_/CU`6/CU) and (not resn CU)")
        cmd.delete('all')
        mutate_all(i, f'structure/{i}.pdb', 'A', resis, save_path='mutate')
