#!/usr/bin/python
'''
Problem Title: Conditions and Loops
Problem ID: INI4
URL: http://rosalind.info/problems/ini4/
'''
def oddSum(num1,num2):
    sum=0
    if(num1%2 == 0):
        num1+=1
    for i in range(num1,(num2+1),2):
        sum+=i
    return sum
        
def main():
    with open('C:/Users/Pramod/Desktop/rosalind_ini4.txt') as input_data:
        a,b = map(int, input_data.read().strip().split())
    res = oddSum(a,b)
    print(res)
    
if __name__ == "__main__":
   main()
