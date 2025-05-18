from Miller_Rabin_test import isPrime_any
from prime import isPrime
from measuretime import measuretime_print

@measuretime_print
def isPrime_any_util(low, high):
    for n in range(low, high+1):
        isPrime_any(n, 5)

@measuretime_print
def isPrime_util(low, high):
    for n in range(low, high+1):
        isPrime(n)

if __name__ == "__main__":
    low = int(input("Lower bound:  "))
    high = int(input("Higher bound: "))
    isPrime_any_util(low, high)
    isPrime_util(low, high)