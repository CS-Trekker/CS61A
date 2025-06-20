def search(f):
    i = 0
    while not f(i):
        i += 1
    return i

def square(x):
    return x * x

def positive(x):
    """always return 0 until (square(x) - 100) is positive."""
    return max(0,square(x)-100)

print(search(positive))


def inverse1(f):
    return lambda y : search(lambda x :f(x) == y)   # 这个地方两次使用lambda需关注

g = inverse1(square)
print(g(16))

def inverse2(f):
    def inverse_of_f(y):
        def is_inverse_of_y(x):
            return f(x) == y
        return search(is_inverse_of_y)
    return inverse_of_f

s = inverse2(square)
print(s(16))