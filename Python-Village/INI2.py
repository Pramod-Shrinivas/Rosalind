#!/usr/bin/python
'''
Problem Title: Variables and Some Arithmetic
Problem ID: INI2
URL: http://rosalind.info/problems/ini2/
'''
def main():
    with open('C:/Users/Pramod/Desktop/rosalind_ini2.txt') as input_data:
        a, b = map(int, input_data.read().strip().split())
    c = a**2 + b**2
    print(c)

if __name__ == "__main__":
   main()
