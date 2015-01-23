#!/usr/bin/python
'''
Problem Title: Rabbits and Recurrence Relations
Problem ID: FIB
URL: http://rosalind.info/problems/fib/
'''
def rabbit_fib(n,k):
    r1,r2 = 1,1
    for i in range(n-2):
        r3 =  r1*k + r2
        r1,r2 = r2,r3
    return r3  
def main():
    with open('C:/Users/Pramod/Desktop/rosalind_fib.txt') as input_data:
        n,k = map(int, input_data.read().strip().split())
    rabbits = rabbit_fib(n,k)
    print(rabbits)
        
if __name__ == '__main__':
    main()
