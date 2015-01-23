#!/usr/bin/env python
'''
Problem Title: Complementing a Strand of DNA
Problem ID: REVC
URL: http://rosalind.info/problems/revc/
'''
import string
def main():
    with open('C:/Users/Pramod/Desktop/rosalind_revc.txt') as input_data:
        dna = input_data.read().strip()
    revc = dna.translate(str.maketrans('ATGC','TACG'))[::-1]
    print(revc)
if __name__ == '__main__':
    main()
