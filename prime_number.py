''' program to check given number is a prime or not '''

def is_prime(n):

    for i in range(2, n):
        if n % i == 0:
            return f"{n} is not a prime number"
    else:
        return f"{n} is a prime number"

out = is_prime(11)
print(out) # 11 is a prime number


# list all prime numbers in a given number
n = int(input('Enter any value: '))

def all_primes(n):
    l = []
    for j in range(2, n):
        for i in range(2, j):
            if j % i == 0:
                break
        else:
            l.append(j)
    return l

out = all_primes(25)
print(out) # [2, 3, 5, 7, 11, 13, 17, 19, 23]