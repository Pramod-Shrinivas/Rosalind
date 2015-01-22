#!/usr/bin/python
'''
Problem Title: Reading and Writing
Problem ID: INI5
URL: http://rosalind.info/problems/ini5/
'''
        
def main():
    with open('C:/Users/Pramod/Desktop/rosalind_ini5.txt') as input_data:
        lines = [line.strip() for line in input_data.readlines()]
    for i in range(1,len(lines),2):
        print(lines[i])
    
if __name__ == "__main__":
   main()
