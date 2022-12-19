import os
import glob

if __name__ == "__main__":
    for infile in glob.glob(os.path.join('mutate/TvLac', '*.pdbqt')):
        os.remove(infile)
