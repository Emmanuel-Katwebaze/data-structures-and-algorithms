# How to find the sum of digits of a positive integer number using recursion

def sumOfDigits(n):
    assert n >= 0 and int(n) == n, 'The number must be a positive integer only.'
    if n == 0: 
        return 0
    else:
        return int(n%10) + sumOfDigits(int(n//10))

print(sumOfDigits(122))

# How to calculate power of a number using recursion

def power(base, exponent):
    assert exponent >= 0 and int(exponent) == exponent, 'The exponent must be a positive integer only.'
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    return base * power(base, exponent - 1)


print(power(2.2, 4))

# How to find the GCD (Greatest Common Divisor) of two numbers using recursion?

def gcd(a, b):
    assert int(a) == a and int(b) == b, 'The numbers must be integers only!'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(48, 18))
print(gcd(48, -18))

# How to convert a number from Decimal to Binary using recursion
def decimalToBinary(n):
    assert int(n) == n, 'The parameter must be an integer only!'
    if n == 0: 
        return 0
    else:
        return n % 2 + 10 * decimalToBinary(int(n / 2))

print(decimalToBinary(13))