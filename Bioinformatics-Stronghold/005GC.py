#!/usr/bin/python
'''
Problem Title: Computing GC Content
Problem ID: GC
URL: http://rosalind.info/problems/gc/     
'''
def main():
    with open('C:/Users/Pramod/Desktop/rosalind_gc.txt') as input_data:
        lines = input_data.readlines()

    samples = {}
    dna = ''
    for line in lines:
        if line[0] == '>':
            dna = line[1:].rstrip()
            samples[dna] = ''
        else:
            samples[dna] += line.rstrip()
    for rosalind_id,dna_string in samples.items():
        samples[rosalind_id] = ((dna_string.count('G') + dna_string.count('C'))/len(dna_string)) * 100
    gc_count = max(samples.values())
    rosalind_id = [key for key,value in samples.items() if value==gc_count]
    print(str(rosalind_id)[2:15])
    print(gc_count)
        
if __name__ == '__main__':
    main()
        
