# dock.py
from vina import Vina
import os
import json
from openbabel import openbabel as ob
from pymol import cmd
import regex as re


class molucule:

    def __init__(self, name: str, file: str):
        self.name = name
        self.file = file


class receptor(molucule):

    def __init__(self, name: str, file: str):
        super().__init__(name, file)


class single_muted_receptor(receptor):

    def __init__(self, name: str, file: str, affinity: float = 0.000):
        super().__init__(name, file)
        self.protein, self.chain, self.ori_res, self.resi, self.mute_res = self.__split_name(
        )
        self.muted = not self.ori_res == self.mute_res
        self.affinity = affinity

    def __split_name(self) -> tuple:
        return tuple(self.name.split('_'))


class ligand(molucule):

    def __init__(self, name: str, file: str):
        super().__init__(name, file)


class dock_result:

    def __init__(self, receptor: receptor, ligand: ligand, path: str) -> None:
        self.receptor = receptor
        self.ligand = ligand
        self.path = path
        self.result = self.analyse_dock_result()

    def __repr__(self) -> str:
        return f'{self.receptor.name} docked to {self.ligand.name} saved to {self.path}'

    def __str__(self) -> str:
        return f'{self.receptor.name} docked to {self.ligand.name} saved to {self.path}'

    def combine_docked_ligand_and_receptor(self, output: str) -> None:
        save_dir = os.path.join(output, f'{self.ligand.name}_{self.receptor.name}')
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        # ligand_pdpqt = self.read(self.path)
        receptor_pdbqt = self.read(self.receptor.file)
        receptor_pdb = self.transform_pdbqt_to_pdb(receptor_pdbqt)
        receptor_path = os.path.join(save_dir, f'{self.receptor.name}.pdb')
        self.write(receptor_path, receptor_pdb)
        ligand_pdb = [item['pdb'] for item in self.result]
        for i, pdb in enumerate(ligand_pdb):
            ligand_path = os.path.join(save_dir, f'{self.ligand.name}_{i + 1}.pdb')
            save_path = os.path.join(save_dir, f'{self.ligand.name}_{self.receptor.name}_{i + 1}.pdb')
            self.write(ligand_path, pdb)
            cmd.delete('all')
            cmd.load(ligand_path)
            cmd.load(receptor_path)
            cmd.save(save_path)
            cmd.delete('all')
    
    def read(self, path: str) -> str:
        with open(path, 'r') as f:
            return f.read()

    def write(self, path: str, content: str) -> None:
        assert content is not None, 'content is None'
        with open(path, 'w') as f:
            f.write(content)

    def transform_pdbqt_to_pdb(self, pdbqt_str: str) -> str:
        conv = ob.OBConversion()
        conv.SetInAndOutFormats('pdbqt', 'pdb')
        mol = ob.OBMol()
        conv.ReadString(mol, pdbqt_str)
        pdb_str = conv.WriteString(mol)
        return pdb_str

    def analyse_dock_result(self) -> list:
        result = self.split_dock_result()
        vina_pattern = re.compile('(REMARK VINA RESULT:)(.*?)(\n)', re.S)
        model_pattern = re.compile('MODEL [0-9]{1,}\n', re.S)
        res = []
        for item in result:
            _, vina_result, _ = vina_pattern.findall(item)[0]
            pdbqt_str = model_pattern.sub('', item)
            vina_result = vina_result[4:].split(' ')
            vina_result = [float(i) for i in vina_result if i != '']
            affinity = float(vina_result[0])
            lb = float(vina_result[1])
            ub = float(vina_result[2])
            # transform pdbqt string to pdb string
            # conv = ob.OBConversion()
            # conv.SetInAndOutFormats('pdbqt', 'pdb')
            # mol = ob.OBMol()
            # conv.ReadString(mol, pdbqt_str)
            # pdb_str = conv.WriteString(mol)
            pdb_str = self.transform_pdbqt_to_pdb(pdbqt_str)
            # print(pdb_str)
            res.append({
                'receptor': self.receptor.name,
                'ligand': self.ligand.name,
                'affinity': affinity,
                'rmsd_lb': lb,
                'rmsd_ub': ub,
                'pdbqt': pdbqt_str,
                'pdb': pdb_str,
            })
        res.sort(key=lambda x: x['affinity'])
        return res

    def write_results_pdb_file(self, output: str, name: str = '') -> None:
        assert os.path.exists(self.path), f'{self.path} does not exist'
        for i in range(len(self.result)):
            item = self.result[i]
            save_path = os.path.join(
                output, f'{name if name != "" else "model"}_{i + 1}.pdb')
            with open(save_path, 'w') as f:
                f.write(item['pdb'])

    def best_result(self) -> dict:
        return self.result[0]

    def split_dock_result(self,
                          pattern: str = '(?=MODEL)(.*?)(ENDMDL)') -> list:
        result_file = self.path
        assert os.path.exists(
            result_file), f'File {result_file} does not exist'
        res = []
        p = re.compile(pattern, re.S)
        with open(result_file, 'r') as f:
            content = f.read()
            # print(content)
            res = p.findall(content, overlapped=True)
        return [start for start, _ in res]


def dock(receptor: receptor,
         ligand: ligand,
         center: list,
         box_size: list,
         output: str = '',
         n_poses: int = 20,
         save_pose: int = 5,
         spacing: float = 0.375,
         cpu: int = 1,
         result_file_type: str = 'pdbqt') -> dock_result:
    assert os.path.exists(
        receptor.file), f'File {receptor.file} does not exist'
    assert os.path.exists(ligand.file), f'File {ligand.file} does not exist'
    assert len(center) == 3, 'Center should be a list of 3 numbers'
    assert len(box_size) == 3, 'Box size should be a list of 3 numbers'
    assert spacing > 0, 'Spacing should be a positive number'
    assert cpu >= 0, 'CPU should be a positive number'
    assert n_poses > 0, 'Number of poses should be a positive number'
    assert save_pose > 0, 'Number of poses to save should be a positive number'
    assert save_pose <= n_poses, 'Number of poses to save should be less than or equal to number of poses'
    if not os.path.exists(output):
        os.makedirs(output)
    v = Vina(cpu=cpu)
    v.set_receptor(receptor.file)
    v.set_ligand_from_file(ligand.file)
    v.compute_vina_maps(center, box_size, spacing)
    print(f'----------{receptor.name}----------')
    print(f'Starting docking {ligand.name} to {receptor.name}')
    v.dock(exhaustiveness=32, n_poses=n_poses)
    save_path = os.path.join(
        output, f'{ligand.name}_{receptor.name}_docked.{result_file_type}')
    v.write_poses(save_path, n_poses=save_pose, overwrite=True)
    print(f'Finished docking {ligand.name} to {receptor.name}')
    print(f'Poses saved to {save_path}')
    print('------------------------------------')
    return dock_result(receptor, ligand, save_path)


def dock_process():
    pass


class dock_config:

    def __init__(self,
                 center: list,
                 box_size: list,
                 spacing: float = 0.375,
                 cpu: int = 1,
                 output: str = '',
                 n_poses: int = 20,
                 save_pose: int = 5,
                 result_file_type: str = 'pdbqt') -> None:
        self.center = center
        self.box_size = box_size
        self.spacing = spacing
        self.cpu = cpu
        self.output = output
        self.n_poses = n_poses
        self.save_pose = save_pose
        self.result_file_type = result_file_type


def get_config_from_json(file: str) -> dock_config:
    assert os.path.exists(file), f'File {file} does not exist'
    with open(file, 'r') as f:
        data = json.load(f)
    return dock_config(**data)


class dock_error:

    def __init__(self, receptor: receptor, ligand: ligand,
                 message: Exception) -> None:
        self.message = message
        self.receptor = receptor
        self.ligand = ligand

    def __str__(self) -> str:
        return f'Error:\nReceptor: {self.receptor.name}\nLigand: {self.ligand.name}\nMessage: {self.message}'


class jobs:

    def __init__(self, name: str, recepters: list, ligands: list,
                 dock_config: dock_config) -> None:
        self.queue = self.pairs(recepters, ligands)
        self.working = []
        self.errors = []
        self.done = []
        self.dock_config = dock_config
        self.name = name
        self.receptor = recepters
        self.ligands = ligands

    def pair(self, receptor: receptor, ligand: ligand) -> tuple:
        return (receptor, ligand)

    def pairs(self, recepters: list = [], ligands: list = []) -> list:
        pairs = []
        for rec in recepters:
            for lig in ligands:
                pairs.append(self.pair(rec, lig))
        return pairs

    def next(self) -> None:
        if len(self.queue) == 0:
            return None
        working = self.queue.pop(0)
        self.working.append(working)
        rec, lig = working
        config = self.dock_config
        try:
            result = dock(rec,
                          lig,
                          config.center,
                          config.box_size,
                          spacing=config.spacing,
                          cpu=config.cpu,
                          output=config.output,
                          n_poses=config.n_poses,
                          save_pose=config.save_pose,
                          result_file_type=config.result_file_type)
            self.done.append(result)
            result.combine_docked_ligand_and_receptor(config.output)
        except Exception as e:
            if len(self.working) != 0:
                self.errors.append(dock_error(rec, lig, e))
            else:
                self.errors.append(e)  # type: ignore
        self.working.remove(working)

    def run(self, callback=None):
        while len(self.queue) != 0:
            self.next()
            self.log()
            if callback is not None:
                callback(self)

    def add(self, receptor: receptor, ligand: ligand):
        self.queue.append(self.pair(receptor, ligand))

    def add_receptor(self, receptor: receptor):
        for lig in self.ligands:
            self.add(receptor, lig)

    def add_ligand(self, ligand: ligand):
        for rec in self.receptor:
            self.add(rec, ligand)

    def add_receptors(self, receptors: list):
        for rec in receptors:
            self.add_receptor(rec)

    def add_ligands(self, ligands: list):
        for lig in ligands:
            self.add_ligand(lig)

    def log(self):
        with open(f'{self.name}.log', 'w') as f:
            f.write(str(self))
        with open(f'cache/{self.name}.json', 'w') as f:
            f.write(self.export_to_json())

    def log_errors(self) -> str:
        errors = ''
        index = 1
        for error in self.errors:
            errors += f'{index}/{len(self.errors)}:\n{error}\n' if isinstance(
                error,
                dock_error) else f'{index}/{len(self.errors)}:\n{error}\n'
            index += 1
        return errors

    def export_to_json(self) -> str:
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          indent=4,
                          sort_keys=True)

    def export_to_json_file(self, file: str) -> None:
        with open(file, 'w') as f:
            f.write(self.export_to_json())

    def import_from_json(self, json: dict):
        self.name = json['name']
        self.receptor = [
            receptor(i.name, i.file) for i in json['receptor'] or []
        ]
        self.ligands = [ligand(i.name, i.file) for i in json['ligands'] or []]
        self.queue = [(receptor(i[0].name,
                                i[0].file), ligand(i[1].name, i[1].file))
                      for i in json['queue'] or []]
        self.working = [(receptor(i[0].name,
                                  i[0].file), ligand(i[1].name, i[1].file))
                        for i in json['working'] or []]
        self.errors = [(dock_error(receptor(i.receptor.name, i.receptor.file),
                                   ligand(i.ligand.name, i.ligand.file),
                                   i.message) if not isinstance(i, str) else i)
                       for i in json['errors'] or []]
        self.done = [
            dock_result(i.receptor.name, i.ligand.name, i.path)
            for i in json['done'] or []
        ]
        self.dock_config = dock_config(**json['dock_config'])

    def import_from_json_file(self, file: str):
        with open(file, 'r') as f:
            data = json.load(f)
            self.import_from_json(data)

    def __len__(self) -> int:
        return len(self.queue) + len(self.done) + len(self.errors) + len(
            self.working)

    def __str__(self) -> str:
        return f'Name: {self.name}\nReceptors: {len(self.receptor)}\nLigands: {len(self.ligands)}\nQueue: {len(self.queue)}\nWorking: {len(self.working)}\nDone: {len(self.done)}\nErrors: {len(self.errors)}\n{self.log_errors()}'


if __name__ == '__main__':
    print('This is a module, not a script. Please import it.')
    test = dock_result(
        'test', 'test',
        '/home/qww/develop/model/funclib/PsLac_desgin_1/PDB/Guaiacol_010104110102030901_-1643_docked.pdb'
    )
    # print(test.result)
    test.write_results_pdb_file('/home/qww/develop/model/test/funlib/', 'test')
