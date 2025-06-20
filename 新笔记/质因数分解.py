def prime_factors(n):
    """打印出n的所有质因数
    >>> prime_factors(3)
    3
    >>> prime_factors(858)
    2
    3
    11
    13
    """
    while n > 1:
        k = smallest_prime_factor(n)
        n = n // k
        print(k)

def smallest_prime_factor(n):
    """打印出n的最小质因数
    >>> smallest_prime_factor(10)
    2
    >>> smallest_prime_factor(15)
    3
    """
    m = 2
    while n % m != 0:
        m += 1
    return m

prime_factors(858)