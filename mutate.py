# mutate.py
from Pymol import get_resis_by_selection, mutate_all, mutate
from pymol import cmd
import argparse
import os
from Bio.PDB import PDBParser
from utils import amino_trans, get_file_suffix, prepare_ligand, prepare_receptor
# import threading
from dock import receptor, ligand, jobs, get_config_from_json
import glob
import csv


def pase_args():
    parser = argparse.ArgumentParser(
        description='Mutate all residues in a protein')
    parser.add_argument('-i',
                        '--input',
                        type=str,
                        help='Input PDB file',
                        required=True)

    parser.add_argument('-mu',
                        '--mutate',
                        type=bool,
                        help='Mutate',
                        default=True)

    parser.add_argument('-n',
                        '--name',
                        type=str,
                        help='Protein name',
                        default='')

    parser.add_argument('-r',
                        '--resis',
                        type=str,
                        help='Mutation string',
                        nargs='+',
                        default=[])
    parser.add_argument('-m',
                        '--mode',
                        type=str,
                        help='Mutation mode',
                        default='all',
                        choices=['all', 'selection', 'resis'])

    parser.add_argument('-ex',
                        '--exclude',
                        type=int,
                        help='Exclude residues',
                        nargs='+',
                        default=[])

    parser.add_argument('-s',
                        '--selection',
                        type=str,
                        help='Pymol selection string',
                        default='all')

    parser.add_argument('-c',
                        '--chain',
                        type=str,
                        help='Chain ID',
                        default='all',
                        nargs='+')

    parser.add_argument('-d', '--dock', type=bool, help='Dock', default=False)

    parser.add_argument('-l',
                        '--ligand',
                        type=str,
                        help='Ligand file',
                        default='')

    parser.add_argument('-ld',
                        '--ligand_dir',
                        type=str,
                        help='Ligand directory',
                        default='')

    parser.add_argument('-rd',
                        '--receptor_dir',
                        type=str,
                        help='Receptor directory',
                        default='')

    parser.add_argument('-prel',
                        '--prel4py',
                        type=str,
                        help='The path of prepare_ligand4.py',
                        default='')

    parser.add_argument('-prer',
                        '--prer4py',
                        type=str,
                        help='The path of prepare_receptor4.py',
                        default='')

    parser.add_argument('-dc',
                        '--dock_config',
                        type=str,
                        help='Dock config file',
                        default='')

    parser.add_argument('-o',
                        '--output',
                        type=str,
                        help='Output path',
                        default='./mutate')

    return parser.parse_args()


def split_mutation_str(mutation_str: str) -> tuple:
    """
    mutation_str: chain:resi:target_resn eg: A:1:A
    """
    split = mutation_str.split(':')
    assert len(split) == 3, f'{mutation_str} is not a valid mutation string'
    amino_trans_reverse = dict(zip(amino_trans.values(), amino_trans.keys()))
    return (split[0], split[1], amino_trans_reverse[split[2].upper()])


def get_residues(pdb: str, chains: list, exclude: list = []) -> dict:
    assert os.path.exists(pdb), f'{pdb} file not exists'
    parser = PDBParser()
    structure = parser.get_structure('protein', pdb)
    pdb_chains = [chain.id for chain in structure.get_chains()]
    assert "all" in chains or all([chain in pdb_chains for chain in chains
                                   ]), f'Not all chain exists in {pdb}'
    residues = {chain: [] for chain in (chains if 'all' not in chains else pdb_chains)}
    if "all" in chains:
        chains = pdb_chains
    for residue in structure.get_residues():
        full_id = residue.get_full_id()
        chain = full_id[2]
        resn = residue.get_resname().upper()
        resi = full_id[3][1]
        # print(resi, type(resi), resi in exclude)
        if (chain in chains) and (full_id[
                0] == 'protein') and (resn in amino_trans.keys()) and (int(
                    resi) not in exclude):
            residues[chain].append((resi, resn))
    return residues


# def mutate_and_dock(mutate_func: function, mutate_args: tuple,
#                     dock_func: function, dock_args: tuple):
#     mutate_func(*mutate_args)
#     dock_func(*dock_args)

if __name__ == "__main__":
    args = pase_args()
    print(args)
    receptors = []
    ligands = []
    if args.mutate:
        assert args.mode in ['all', 'selection',
                             'resis'], 'Mode must be all, selection or resis'
        assert os.path.exists(args.input), f'{args.input} file not exists'
        if not os.path.exists(args.output):
            os.mkdir(args.output)
        name = args.name if args.name else os.path.basename(
            args.input).split('.')[0]
        save_path = os.path.join(args.output, name)
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        wt_file = os.path.join(save_path, f'{name}_wt.pdb')
        cmd.delete('all')
        cmd.load(args.input, name)
        cmd.save(wt_file, name)
        cmd.delete('all')
        receptors.append(prepare_receptor(wt_file, args.prer4py))
        if args.mode == 'all':
            residues = get_residues(args.input, args.chain, args.exclude)
            # print(residues, args.exclude, type(args.exclude[0]))
            for chain in residues.keys():
                resis = [residue[0] for residue in residues[chain]]
                mutate_all(
                    name,
                    wt_file,
                    chain,
                    resis,
                    save_path=save_path,
                    callback=lambda f: receptors.append(
                        prepare_receptor(f, args.prer4py)))  # type: ignore
        elif args.mode == 'selection':
            assert args.selection != '', 'Selection string must be provided'
            resis = get_resis_by_selection(args.selection, args.exclude)
            mutate_all(name,
                       wt_file,
                       args.chain,
                       resis,
                       save_path=save_path,
                       callback=lambda f: receptors.append(
                           prepare_receptor(f, args.prer4py)))  # type: ignore
        elif args.mode == 'resis':
            assert len(args.resis) != 0, 'Resis must be provided'
            for resi in args.resis:
                chain, resi, resn = split_mutation_str(resi)
                mutate(name,
                       wt_file,
                       chain,
                       resi,
                       resn,
                       save_path=save_path,
                       callback=lambda f: receptors.append(
                           prepare_receptor(f, args.prer4py)))  # type: ignore
    if args.dock:
        assert os.path.exists(args.ligand_dir) or os.path.exists(
            args.ligand), f'{args.ligand_dir} or {args.ligand} file not exists'
        assert args.mutate or os.path.exists(args.receptor_dir) or len(
            receptors) != 0, f'{args.receptor_dir} or receptor file not exists'
        assert os.path.exists(
            args.dock_config
        ), f'Dock config {args.dock_config} file not exists'
        dock_result_path = os.path.join(args.output, 'dock_result')
        if not os.path.exists(dock_result_path):
            os.mkdir(dock_result_path)
        receptors = [
            receptor(os.path.basename(f).replace('.pdbqt', ''), f)
            for f in receptors
        ]
        if os.path.exists(args.ligand_dir):
            ligands = [
                ligand(os.path.basename(f).replace('.pdbqt', ''), f)
                for f in glob.glob(os.path.join(args.ligand_dir, '*.pdbqt'))
            ]
        elif os.path.exists(args.ligand):
            ligands = [
                ligand(
                    os.path.basename(args.ligand).replace('.pdbqt', ''),
                    args.ligand)
            ]
        dock_config = get_config_from_json(args.dock_config)
        dock_jobs = jobs('', receptors, ligands, dock_config)
        dock_jobs.run()
        res = [{
            key: val
            for key, val in item.best_result().items()
            if key not in ['pdb', 'pdbqt']
        } for item in dock_jobs.done]
        res.sort(key=lambda x: x['affinity'])
        # print(res)
        res_csv_path = os.path.join(dock_result_path, 'dock_results.csv')
        print(f'Saving results to {res_csv_path}...')
        with open(res_csv_path, 'w') as f:
            fieldnames = [
                'receptor', 'ligand', 'affinity', 'rmsd_lb', 'rmsd_ub'
            ]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for item in res:
                writer.writerow(item)

    # for i in ['TvLac', 'PsLac', 'PoLac', 'BspLac']:
    #     cmd.delete('all')
    #     cmd.load(f'structure/{i}.pdb', i)
    #     resis = get_resis_by_selection(
    #         f"(br. all within 10 of /{i}//_/CU`6/CU) and (not resn CU)")
    #     cmd.delete('all')
    #     mutate_all(i, f'structure/{i}.pdb', 'A', resis, save_path='mutate')
    # print(split_mutation_str('A:11:A'))