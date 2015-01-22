#!/usr/bin/python
'''
Problem Title: Intro to Python dictionary
Problem ID: INI6
URL: http://rosalind.info/problems/ini6/
'''
def main():
    with open('C:/Users/Pramod/Desktop/rosalind_ini6.txt') as input_data:
        words = input_data.read().strip().split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key,value in word_count.items():
        print("{0} {1}".format(key,value))
       
if __name__ == "__main__":
   main()
