

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    low = int(input("lower border: "))
    high = int(input("high border: "))
    for i in range(low, high+1):
        if isPrime(i):
            print(i)