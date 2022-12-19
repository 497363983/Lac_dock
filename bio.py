import os
import regex as re
"""
code to translate a gene sequence into a protein sequence

| /   |  U  |  C  |  A  |  G  |  /  |
| --- | --- | --- | --- | --- | --- |
|     |  F  |  S  |  Y  |  C  |  U  |
|     |  F  |  S  |  Y  |  C  |  C  |
|  U  |  L  |  S  |  *  |  *  |  A  |
|     |  L  |  S  |  *  |  W  |  G  |
| --- | --- | --- | --- | --- | --- |
|     |  L  |  P  |  H  |  R  |  U  |
|     |  L  |  P  |  H  |  R  |  C  |
|  C  |  L  |  P  |  Q  |  R  |  A  |
|     |  L  |  P  |  Q  |  R  |  G  |
| --- | --- | --- | --- | --- | --- |
|     |  I  |  T  |  N  |  S  |  U  |
|     |  I  |  T  |  N  |  S  |  C  |
|  A  |  I  |  T  |  K  |  R  |  A  |
|     |  M  |  T  |  N  |  S  |  G  |
| --- | --- | --- | --- | --- | --- |
|     |  V  |  A  |  D  |  G  |  U  |
|     |  V  |  A  |  D  |  G  |  C  |
|  G  |  V  |  A  |  E  |  G  |  A  |
|     |  V  |  A  |  E  |  G  |  G  |
"""
codon_table = [
    [['F', 'S', 'Y', 'C'], ['F', 'S', 'Y', 'C'], ['L', 'S', '*', '*'],
     ['L', 'S', '*', 'W']],
    [['L', 'P', 'H', 'R'], ['L', 'P', 'H', 'R'], ['L', 'P', 'Q', 'R'],
     ['L', 'P', 'Q', 'R']],
    [['I', 'T', 'N', 'S'], ['I', 'T', 'N', 'S'], ['I', 'T', 'K', 'R'],
     ['M', 'T', 'K', 'R']],
    [['V', 'A', 'D', 'G'], ['V', 'A', 'D', 'G'], ['V', 'A', 'E', 'G'],
     ['V', 'A', 'E', 'G']],
]

start_codon = ['AUG', 'GUG', 'AUA', 'UUG', 'ATG', 'GTG', 'ATA', 'TTG']

stop_codon = ['UAG', 'UGA', 'UAA', 'TAG', 'TGA', 'TAA']


class sequence:

    def __init__(self,
                 type: str,
                 seq: str,
                 code: list | dict,
                 name='') -> None:
        self.seq = seq.upper()
        self.code = code
        self.type = type
        self.name = name

    def __repr__(self) -> str:
        return f'>{self.name} {self.type}\n{self.seq}'

    def __str__(self) -> str:
        return f'>{self.name} {self.type}\n{self.seq}'

    def output(self, target: str) -> None:
        content = f'>{self.name}\n{self.seq}'
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(os.path.dirname(target))
        with open(target, 'w') as f:
            f.write(content)


class protein(sequence):

    def __init__(self, seq, name, code=codon_table) -> None:
        super().__init__('Protein', seq, code, name)


class rna(sequence):

    def __init__(self, seq: str, name: str, code=codon_table) -> None:
        super().__init__('RNA', seq, code, name)

    def reverse_transcription(self):
        return dna(self.seq.replace('U', 'T'), self.name)


class dna(sequence):

    def __init__(self,
                 seq: str,
                 name: str,
                 sense_strand: bool = True,
                 code: list | dict = codon_table) -> None:
        super().__init__('DNA',
                         seq if sense_strand else self.reverse_complement(seq),
                         code, name)
        self.rna: rna = self.transcription()
        self.protein: protein = self.translation()

    def transcription(self) -> rna:
        return rna(self.seq.replace('T', 'U'), self.name)

    def translation(self) -> protein:
        proteinSeq = ''
        seq = max(self.find_orf(), key=len)
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            if len(codon) < 3:
                break
            proteinSeq += self.__translateCodon(codon)
        return protein(proteinSeq.replace('*', ''), self.name)

    def __translateCodon(self, codon: str) -> str:
        return self.code['UCAG'.find(codon[0])]['UCAG'.find(
            codon[2])]['UCAG'.find(codon[1])]

    def reverse_complement(self, seq: str) -> str:
        tran_tab = str.maketrans('ATCGatcg', 'TAGCtagc')
        return seq[::-1].translate(tran_tab)

    def find_orf(self) -> list:
        tran_tab = str.maketrans('[],', '()|')
        pattern = re.compile(
            eval("r'" + str(start_codon).translate(tran_tab).replace(
                '\'', '').replace(' ', '') + "((...)+)" +
                 str(stop_codon).translate(tran_tab).replace('\'', '').replace(
                     ' ', '') + "'"))
        orf = pattern.findall(self.rna.seq, overlapped=True)
        return [start + mid + end for (start, mid, _, end) in orf]
