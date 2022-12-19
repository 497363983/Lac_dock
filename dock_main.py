from dock import receptor, ligand, jobs, get_config_from_json
import glob

if __name__ == "__main__":
    Lacs = ['TvLac', 'PsLac', 'PoLac', 'BspLac']
    lig = ligand('Guaiacol', 'structure/pdbqt/Guaiacol.pdbqt')
    ligands = [lig]
    for j in Lacs:
        config = get_config_from_json(f'config/{j}.json')
        receptors = []
        for file in glob.glob(f'mutate/{j}/*.pdbqt'):
            receptors.append(receptor(file.split('/')[2].split('.')[0], file))
            # jobs[j].append(file.split('/')[2].split('.')[0])
        dock_jobs = jobs(j, receptors, ligands, config)
        # print(dock_jobs)
        dock_jobs.run()
