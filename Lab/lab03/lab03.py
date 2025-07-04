from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
    str_x = str(x)
    Flag = True
    for i in range(0,len(str_x) - 1):
        if str_x[i] > str_x[i+1]:
            Flag = False
            break
    return Flag


def get_k_run_starter(n, k):
    """Returns the 0th digit of the kth increasing run within n.
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    # i = 0
    # final = None
    # while ____________________________:
    #     while ____________________________:
    #         ____________________________
    #     final = ____________________________
    #     i = ____________________________
    #     n = ____________________________
    # return final
    i = 0
    final = None
    while i <= k:
        # 寻找一个递增序列
        while n // 10 and (n % 10) > (n // 10) % 10:
            n //= 10
        final = n % 10
        i += 1
        n //= 10
    return final


def make_repeater(func, n):
    """Return the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    "*** YOUR CODE HERE ***"
    def f(x):
        result = x
        for _ in range(n):
            result = func(result)
        return result
    return f


def composer(func1, func2):
    """Return a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f


def apply_twice(func):
    """ Return a function that applies func twice.

    func -- a function that takes one argument

    >>> apply_twice(square)(2)
    16
    """
    "*** YOUR CODE HERE ***"
    def f(x):
        return func(func(x))
    return f


def div_by_primes_under(n):
    """
    >>> div_by_primes_under(10)(11)
    False
    >>> div_by_primes_under(10)(121)
    False
    >>> div_by_primes_under(10)(12)
    True
    >>> div_by_primes_under(5)(1)
    False
    """
    # checker = lambda x: False
    # i = ____________________________
    # while ____________________________:
    #     if not checker(i):
    #         checker = (lambda f, i: lambda x: __________)(checker, i)
    #     i = ____________________________
    # return ____________________________
    checker = lambda x: False
    i = 2
    while i <= n:
        if not checker(i):
            checker = (lambda f, i: lambda x: f(x) or x % i == 0)(checker, i)
        i += 1
    return checker



def div_by_primes_under_no_lambda(n):
    """
    >>> div_by_primes_under_no_lambda(10)(11)
    False
    >>> div_by_primes_under_no_lambda(10)(121)
    False
    >>> div_by_primes_under_no_lambda(10)(12)
    True
    >>> div_by_primes_under_no_lambda(5)(1)
    False
    """
    # def checker(x):
    #     return False
    # i = ____________________________
    # while ____________________________:
    #     if not checker(i):
    #         def outer(____________________________):
    #             def inner(____________________________):
    #                 return ____________________________
    #             return ____________________________
    #         checker = ____________________________
    #     i = ____________________________
    # return ____________________________
    # 定义一个函数checker，返回False
    def checker(x):
        return False
    i = 2
    while i <= n:
        if not checker(i):
            def outer(f,i):
                def inner(x):
                    return f(x) or x % i == 0
                return inner
            checker = outer(checker,i)
        i += 1
    return checker