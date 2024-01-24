# Basic implementation of recursion
# def recursionMethod(paramters):
#     if exit from condition satisfied:
#         return some value
#     else: 
#         recursionMethod(modified paramters)

# How do you know that the subproblem is similar in nature? in other words,
# that the problem is a recursive one
# 	Design an algorithm to compute nth…
# 	Write code to list the n…
# 	Implement a method to compute all.


def recursiveMethod(n):
    if n < 1:
        print(" n is less than 1")
    else:
        recursiveMethod(n - 1)
        print(n)
        
# RECURSIVE VS ITERATIVE SOLUTIONS
# RECURSIVE POWER OF TWO SOLUTION
        
def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2
    
# ITERATIVE POWER OF TWO SOLUTION

def powerOfTwo(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power
    
# HOW TO WRITE RECURSION IN 3 STEPS
# Step 1: Recursive case – the flow
# Step 2: Base case – the stopping criteria
# Step 3: Unintentional case - the constraint
# import sys
# sys.setrecursionlimit(10000) this increases the stack memory

def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be a positive integer only.'
    if n in [0, 1]: 
        return 1
    else:
     return n * factorial(n - 1)
 
print(factorial(3))


def fibonacci(n):
    assert n >= 0 and int(n) == n, 'Fibonacci number cannot be negative number or non integer'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(-5))