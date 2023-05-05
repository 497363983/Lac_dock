# translate.py
"""
USAGE:
python translate.py -i input.csv -o output_dir

DESCRIPTION:
Translate DNA to protein

ARGUMENTS:
-i, --input = string: Input DNA csv file
-o, --output = string: Output directory

NOTE:
The input csv file should be like this:
name,sequence
name1,sequence1
...
namen,sequencen
"""
from bio import dna
import numpy as np
import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(description='Translate DNA to protein')
    parser.add_argument('-i',
                        '--input',
                        type=str,
                        help='Input DNA csv file',
                        required=True)
    parser.add_argument('-o',
                        '--output',
                        type=str,
                        help='Output file',
                        required=True)
    args = parser.parse_args()
    return args


def run(csv_file: str, output: str = ''):
    data = np.loadtxt(open(csv_file, 'rb'), delimiter=',', dtype=str)
    for i in range(1, len(data)):
        temp = dna(data[i][1], data[i][0])
        save_path = os.path.join(output, f'{temp.name}.fasta')
        temp.protein.output(save_path)
        print(temp.protein)


if __name__ == '__main__':
    args = parse_args()
    run(args.input, args.output)
