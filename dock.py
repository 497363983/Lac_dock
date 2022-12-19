from vina import Vina
import os
import json


class molucule:

    def __init__(self, name, file):
        self.name = name
        self.file = file


class receptor(molucule):

    def __init__(self, name, file):
        super().__init__(name, file)


class ligand(molucule):

    def __init__(self, name, file):
        super().__init__(name, file)


def dock(receptor: receptor,
         ligand: ligand,
         center: list,
         box_size: list,
         output: str = '',
         n_poses: int = 20,
         save_pose: int = 5,
         spacing: float = 0.375,
         cpu: int = 1) -> None:
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
        self.working = None
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

    def next(self):
        if len(self.queue) == 0:
            return None
        self.working = self.queue.pop(0)
        rec, lig = self.working
        config = self.dock_config
        dock(
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

    def run(self, callback=None):
        while len(self.queue) != 0:
            try:
                self.next()
            except Exception as e:
                if self.working is not None:
                    rec, lig = self.working
                    self.errors.append(dock_error(rec, lig, e))
                else:
                    self.errors.append(e)
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

    def log_errors(self) -> str:
        errors = 'Errors:\n'
        index = 0
        for error in self.errors:
            errors += f'{index}/{len(self.errors)}:\n{error}\n' if isinstance(
                error,
                dock_error) else f'{index}/{len(self.errors)}:\n{error}\n'
        return errors

    def __len__(self) -> int:
        return len(self.queue) + len(self.done) + len(
            self.errors) + (1 if self.working is not None else 0)

    def __str__(self) -> str:
        return f'Name: {self.name}\nReceptors: {len(self.receptor)}\nLigands: {len(self.ligands)}\nQueue: {len(self.queue)}\nWorking: {1 if self.working is not None else 0}\nDone: {len(self.done)}\nErrors: {len(self.errors)}\n'


# if __name__ == '__main__':
#     r = receptor('TvLac_A_C_439_A', 'mutate/TvLac/TvLac_A_C_439_A.pdbqt')
#     l = ligand('ligand', 'structure/pdbqt/ligend.pdbqt')
#     dock(r, l, [-44.682, -34.179, -20.558], [30, 30, 30], '', 1)