#!/usr/bin/python
'''
Problem Title: Fibonacci Numbers
Problem ID: FIBO
URL: http://rosalind.info/problems/fibo/
'''
def fibonacci(n):
    f1,f2= 0,1
    for i in range(n-1):
        f1,f2 = f2,f1+f2
    return f2
    
def main():
    with open('C:/Users/Pramod/Desktop/rosalind_fibo.txt') as input_data:
        n = int(input_data.read().strip())
        fib_n = fibonacci(n)
        print(fib_n)
        
if __name__ == '__main__':
    main()
