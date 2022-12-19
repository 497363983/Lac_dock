from bio import dna
import numpy as np


def run():
    data = np.loadtxt(open('./gene/data.csv', 'rb'), delimiter=',', dtype=str)
    for i in range(1, len(data)):
        temp = dna(data[i][1], data[i][0])
        temp.protein.output(f'./output/{temp.name}.fasta')
        print(temp)


if __name__ == '__main__':
    run()
