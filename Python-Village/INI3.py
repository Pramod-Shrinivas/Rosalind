#!/usr/bin/python
'''
Problem Title: Strings and lists
Problem ID: INI3
URL: http://rosalind.info/problems/ini3/
'''
def main():
    with open('C:/Users/Pramod/Desktop/rosalind_ini3.txt') as input_data:
        string,points = [line.strip() for line in input_data.readlines()]
        a,b,c,d = map(int, points.split())
    print("{0} {1}".format(string[a:b+1],string[c:d+1]))
    
if __name__ == "__main__":
   main()
