'''
Wojciech Gorzynski
10-05-2025
Uses the Miller-Rabin test to check for a numbers primality
More efficient than traditional algorythm for numbers bigger than 10^6 (million) 

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

def miller_rabin_improved(n, base): #miller_rabin primality test with some check at the beggining
    if n == 2:
        return True
    if n % 2  or n < 2 == 0:
        return False
    
    d = n-1
    if pow(base, d, n) != 1:
        return False
    while d % 2 == 0:
        d //= 2
        if pow(base, d, n) != 1:
            if pow(base, d, n) == n-1:
                return True
            else: 
                return False
    return True

def miller_rabin(n, base): #miller_rabin for n bigger than 2
    d = n-1
    if pow(base, d, n) != 1:
        return False
    while d % 2 == 0:
        d //= 2
        if pow(base, d, n) != 1:
            if pow(base, d, n) == n-1:
                return True
            else: 
                return False
    return True
    

# -------------- Final Functions ------------------
def isPrime_mini(n): #for n less than 9080191
    for base in [31, 73]:
        if not miller_rabin_improved(n, base):
            return False
    return True


def isPrime_mid(n): #for n less than 4759123141
    for base in [2,7,61]:
        if not miller_rabin_improved(n, base):
            return False
    return True

    
def isPrime_max(n): #for n less than 341550071728321
    for base in [2,3,5,7,11,13,17]:
        if not miller_rabin_improved(n, base):
            return False
    return True


def isPrime_any_prob(n, k=10): #for any n but probabilistic k bases tried return with probability
    if n <= 4:
        if n in [2, 3]:
            return True, 1
        else:
            return False, 1
        
    for i in range(k):
        base = randint(2, n-2)
        if not miller_rabin_improved(n, base):
            return False, 1
    return True, 1 - 0.25**k



def isPrime_any(n, k=10): #for any n but probabilistic k bases tried
    if n <= 4:
        if n in [2, 3]:
            return True
        else:
            return False
    
    for i in range(k):
        base = randint(2, n-2)
        if not miller_rabin(n, base):
            return False
    return True


if __name__ == "__main__":
    low = int(input("lower border: "))
    high = int(input("high border: "))
    for i in range(low, high+1):
        result = isPrime_any_prob(i)
        if result[0]:
            print(f"{i}: {result[1]}")
    