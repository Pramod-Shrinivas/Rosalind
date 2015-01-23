#!/usr/bin/env python
'''
Problem Title: Transcribing DNA into RNA
Problem ID: RNA
URL: http://rosalind.info/problems/rna/
'''
def main():
    with open('C:/Users/Pramod/Desktop/rosalind_rna.txt') as input_data:
        dna = input_data.read().strip()
    rna = dna.replace('T', 'U')
    print(rna)
if __name__ == '__main__':
    main()
