from Pymol import get_resis_by_selection, mutate_all
from pymol import cmd

cmd.delete('all')
cmd.load('structure/PsLac1.pdb', 'PsLac')
resis = get_resis_by_selection(
    "(br. all within 5 of /PsLac//A/CU`901/CU) and (not resn CU)")
cmd.delete('all')
print(resis)
mutate_all('PsLac', 'structure/PsLac1.pdb', 'A', resis, save_path='mutate')
