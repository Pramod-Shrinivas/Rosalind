#!/usr/bin/python
'''
Problem Title: A Rapid Introduction to Molecular Biology
Problem ID: DNA
URL: http://rosalind.info/problems/dna/
'''
from collections import Counter
def dna_count(dna):
    dna_counts = Counter(dna)
    return [dna_counts[i] for i in 'ACGT']
def main():
    with open('C:/Users/Pramod/Desktop/rosalind_dna.txt') as input_data:
        dna_sequence = input_data.read().strip()
    count = map(str, dna_count(dna_sequence))
    print(' '.join(count))
   
if __name__ == "__main__":
   main()
