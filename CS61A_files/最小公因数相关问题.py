# 最小质因数   (质因数≠因数)
def smallest_prime_factor(n):
    result = 2
    while n % result != 0:
        result += 1
    return result

# 所有质因数(有重复，确切来讲应该是在进行质因数分解) 
def prime_factors(n):
    result = []
    while n > 1:
        k = smallest_prime_factor(n)
        n //= k
        result.append(k)
    return result

# 最大公因数（使用辗转相除法）
# gcd(a, b)=gcd(b, a mod b)
def gcd(n, d):
    while d != 0:
        n, d = d, n % d
    return n

# 最小公倍数
def lcm(n, d):
    return abs(n * d) // gcd(n, d)
