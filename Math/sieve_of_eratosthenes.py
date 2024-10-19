def sieve_of_eratosthenes(n):
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if prime[p]]
    return primes


n = int(input("Enter the number up to which you want to find primes: "))
print("Prime numbers up to", n, "are:", *sieve_of_eratosthenes(n))
