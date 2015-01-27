#!/usr/bin/python
'''
Problem Title: Counting Point Mutations
Problem ID: HAMM
URL: http://rosalind.info/problems/hamm/     
'''
def hamm_dist(dna1,dna2):
    hamm_dist=0
    for i in range(len(dna1)):
        if dna1[i]!=dna2[i]:
            hamm_dist+=1
    return hamm_dist
            
def main():
    with open('C:/Users/Pramod/Desktop/rosalind_hamm.txt') as input_data:
        lines = input_data.readlines()
        length=len(str(lines[0]).rstrip('\n'))
        hamm_distance = hamm_dist(str(lines[0]).rstrip('\n'),str(lines[1]).rstrip('\n'))
        print(hamm_distance)
       
if __name__ == '__main__':
    main()
        
