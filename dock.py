from vina import Vina
import os
import json


class molucule:

    def __init__(self, name: str, file: str):
        self.name = name
        self.file = file


class receptor(molucule):

    def __init__(self, name: str, file: str):
        super().__init__(name, file)


class ligand(molucule):

    def __init__(self, name: str, file: str):
        super().__init__(name, file)


class dock_result:

    def __init__(self, receptor: receptor, ligand: ligand, path: str) -> None:
        self.receptor = receptor
        self.ligand = ligand
        self.path = path


def dock(receptor: receptor,
         ligand: ligand,
         center: list,
         box_size: list,
         output: str = '',
         n_poses: int = 20,
         save_pose: int = 5,
         spacing: float = 0.375,
         cpu: int = 1) -> dock_result:
    v = Vina(cpu=cpu)
    v.set_receptor(receptor.file)
    v.set_ligand_from_file(ligand.file)
    v.compute_vina_maps(center, box_size, spacing)
    print(f'----------{receptor.name}----------')
    print(f'Starting docking {ligand.name} to {receptor.name}')
    v.dock(exhaustiveness=32, n_poses=n_poses)
    save_path = os.path.join(output,
                             f'{ligand.name}_{receptor.name}_docked.pdbqt')
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
                 save_pose: int = 5) -> None:
        self.center = center
        self.box_size = box_size
        self.spacing = spacing
        self.cpu = cpu
        self.output = output
        self.n_poses = n_poses
        self.save_pose = save_pose


def get_config_from_json(file: str) -> dock_config:
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
            result = dock(
                rec,
                lig,
                config.center,
                config.box_size,
                spacing=config.spacing,
                cpu=config.cpu,
                output=config.output,
                n_poses=config.n_poses,
                save_pose=config.save_pose,
            )
            self.done.append(result)
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
        index = 0
        for error in self.errors:
            errors += f'{index}/{len(self.errors)}:\n{error}\n' if isinstance(
                error,
                dock_error) else f'{index}/{len(self.errors)}:\n{error}\n'
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
