'''
Wojciech Gorzynski
10-05-2025
Uses the Miller-Rabin test to check for a numbers primality
More efficient than traditional algorithm for numbers bigger than 10^6 (million) 

sufficient bases to check
n < 9080191 bases [31, 73]
n < 4759123141 bases [2,7,61]
n < 341550071728321 bases [2,3,5,7,11,13,17]

for any n probabilistic rather than deterministic (probability exponential 1-0.25^k with k random bases from range <2, n-2> checked)
'''
from random import randint
# -------------- supporting Functions -------------
def decompose(n): #return d and s where n-1 = 2^s * d and d is odd
    n -= 1
    s = 0
    while n%2 == 0:
        s += 1
        n //= 2
    return n, s


SMALL_PRIMES = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
    157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
    239, 241
]


def miller_rabin(n, a): #miller_rabin primality test with some check at the beggining
    d, s = decompose(n)
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(s - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False

# -------------- Final Functions ------------------

def isPrime_mini(n): #for n less than 4759123141
    if n <= 4:
        if n in [2, 3]:
            return True
        else:
            return False
    if n % 2 == 0:
        return False
    
    for prime in SMALL_PRIMES:
        if n == prime:
            return True
        if n % prime == 0:
            return False

    for base in [2,7,61]:
        if not miller_rabin(n, base):
            return False
    return True

    
def isPrime_max(n): #for n less than 341550071728321
    if n <= 4:
        if n in [2, 3]:
            return True
        else:
            return False
    if n % 2 == 0:
        return False
    
    for prime in SMALL_PRIMES:
        if n == prime:
            return True
        if n % prime == 0:
            return False
        
    for base in [2,3,5,7,11,13,17]:
        if not miller_rabin(n, base):
            return False
    return True


def isPrime_any(n, k=7): #for any n but probabilistic (0.25**k chance to be wrong) k bases tried
    if n <= 4:
        if n in [2, 3]:
            return True
        else:
            return False
    if n % 2 == 0:
        return False
    
    for prime in SMALL_PRIMES:
        if n == prime:
            return True
        if n % prime == 0:
            return False
    
    if n < 4759123141:
        bases = [2,7,61]
    elif n < 341550071728321:
        bases = [2,3,5,7,11,13,17]
    else:
        bases = [randint(2, n-2) for _ in range(k)]
    
    for base in bases:
        if not miller_rabin(n, base):
            return False
    return True


if __name__ == "__main__":
    low = int(input("lower border: "))
    high = int(input("high border: "))
    tries = int(input("number of tries for a probabilistic test: "))
    for i in range(low, high+1):
        if isPrime_any(i, tries):
            print(f"{i}: {(1-0.25**tries)*100:.6f}%")
        