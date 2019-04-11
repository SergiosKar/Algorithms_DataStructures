 # https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
 
 #1) Write three functions that compute the sum of the numbers in a given list 
 #   using a for-loop, a while-loop, and recursion.

A=[2,4,3,1]

def sum(A):
    if len(A)<=0:
        return 0
    
    return A[0] + sum(A[1:])



 #2) Write a function that combines two lists by alternatingly taking elements.
 #   For example: given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].

A=['a','b','c']
B=[1,2,3]
res=[]
for i in range(len(A)):
    res.append(A[i])
    res.append(B[i])
res

 #3) Write a function that computes the list of the first 100 Fibonacci numbers.
 #   By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two. 
 #   As an example, here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

def fib(N):
    dp=[0,1]
    for i in range(2,N):
        dp.append(dp[i-1]+dp[i-2])
    return dp

fib(10)

def fib2(N):
    dp_i_1=0
    dp_i_2=1
    for i in range(2,N):
        dp_i_2,dp_i_1=dp_i_1+dp_i_2,dp_i_2
        
    return dp_i_2

fib2(10)

 
 
 