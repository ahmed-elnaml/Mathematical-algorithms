"""composite numbers"""
# def compositeList(n):
#     l=[]
#     while len(l)<n:
#         for i in range()
def eratosthenes(n):
    primes = list (range(2, n+1))
    for i in primes:
        j=2
        while i*j<= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j=j+1
def weak_goldbach(N):
    x, y, z = 0, 0, 0
    result = 0
    if not N % 2 or N < 7:
        raise Exception("Bad input - must be odd number greater than 5.")
    prime = eratosthenes(N)
    for i in range(len(prime)):
        x = prime[i]
        for j in range(i, len(prime)):
            y = prime[j]
            for k in range(j, len(prime)):
                z = prime[k]
                if x + y + z == N:
                    return x, y, z
    raise Exception("Looks like %d is the exception to the weak Goldbach conjecture!" % N)
print(weak_goldbach(15))