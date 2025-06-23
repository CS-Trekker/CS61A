# 1、计算机科学
# 2、函数
# 3、控制语句
## pure function
```python
counter = 0

def increment():
    global counter
    counter += 1         # 这里修改了global frame中的counter的值（有副作用），所以increment()是non-pure function
    return counter
```
```python
def print_sum(x, y):
    print(x + y)           # 这里print了东西，所以non-pure
```
```python
def add(x, y):
    return x + y
# 只返回了值，所以pure
```

![[Pasted image 20250618181716.png|450]]
## UnboundLocalError
```python
x = 1
def f():
    print(x)   # UnboundLocalError: local variable 'x' referenced before assignment
    x = 2
    print(x)

f()
# 如果在函数体中对变量进行了赋值操作，那么该变量会被视为局部变量；在赋值之前使用它会导致 UnboundLocalError
```
## global x
```python
x = 1
def f():
    global x
    print(x)
    x = 2        # 注意这个地方修改的是global的x
    print(x)

f()
```
## 质因数分解
```python
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
```
# 4、高阶函数
## 裴波那契数列
```python
def fib(n):
    k = 0
    pre = 1
    cur = 0
    while k < n:
        pre, cur = cur, cur + pre
        k += 1
    return cur

n = int(input())
print(fib(n))
```
## assert语句
```python
>>> assert 3 < 2, "That means 3 < 2 is False."
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: That means 3 < 2 is False.

def area(a):
	assert a > 0, "a must be positive"
	return a * a
```
## 短路运算符
```python
>>> 1 and 0
0
>>> 1 and 1
1
>>> 0 and 0
0
>>> 0 and 1
0
# 前面真就看后面（是否为真），前面假就全假
#########################################
# 前面真就全真，前面假就看后面（是否为真）
>>> 1 or 0
1
>>> 1 or 1
1
>>> 0 or 0
0
>>> 0 or 1
1
##########################################
# 条件表达式
y = 1 if x > 5 else 0
```

```python
def is_16(x):
"""判断x是不是16"""
	return x == 16   # 这里比你用if……else……语句简洁的多
```
## 匿名函数
**lambda 参数列表: 表达式**
参数列表：和普通函数参数相同。
表达式：必须是单一表达式，不能是代码块。
执行后自动返回表达式的值
## 反函数
```python
def square(x):
    return x * x

def search(f):
	i = 0
	while not f(i):
		i += 1
	return i
```
```python
def inverse1(f):
    return lambda y : search(lambda x :f(x) == y)             # 这里两次使用lambda，需关注

g = inverse1(square)
print(g(16))                                                                           # 4
```
```python
# 三重函数嵌套
def inverse2(f): 
    def inverse_of_f(y): 
        def is_inverse_of_y(x): 
            return f(x) == y
        return search(is_inverse_of_y)
    return inverse_of_f

s = inverse2(square)
print(s(16))
```
> 以上两种写法都可以，都要看懂
# 5、环境
![[Pasted image 20250622152307.png|500]]
```python
from operator import add

def curry2(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g
    
m = curry2(add)

add_three = m(3)

add_three(2)
##########################
curry2 = lambda f : lambda x : lambda y : f(x, y)
```
## 没有参数的lambda函数
```python
>>> (lambda: 3)()
3
# lambda: 3 定义了一个没有参数、返回 3 的 lambda 函数
# 紧接着 () 把这个 lambda 当作函数调用
```
```python
>>> b = lambda x: lambda: x      # 想想这里的b和c都是什么
>>> c = b(88)
>>> b        
<function <lambda> at 0x000002B9AD2D0700>
>>> c
<function <lambda>.<locals>.<lambda> at 0x000002B9AD2D0670>
>>> c()
88
>>>b(88)()
88
```
## 返回自己的函数
```python
def print_all(x):

    print(x)

    return print_all

print_all(1)(2)(3)(4)(5)
```
# 6、设计
## intrinsic name
> intrinsic name就是函数对象自带的 **\_\_name\_\_** 属性，与你用什么变量去引用这个函数对象无关
```python
def foo(x):
    return x + 1

print(foo.__name__)    # foo

bar = foo

print(bar.__name__)    # foo
```
# 作业难点
## hw1
在 Python 中，函数体（def 里面）可以没有 return 语句，此时函数的返回值默认为 None。
但函数体中仍然可以有 print() 语句，比如 print(42) 或 print(47)，这些语句会在函数被调用时立即输出内容到控制台，不影响返回值。
## project1
### \*args
```python
def test(*args):
	print(type(args))   # <class 'tuple'>
	print(args)              # (1, 2, 3)
	print(*args)            # 1 2 3
	for arg in args:
		print(arg)
# 1
# 2
# 3
```
## lab02
### chocolate是什么？
```python
>>> def cake():
...    print('beets')
...    def pie():
...        print('sweets')
...        return 'cake'
...    return pie
>>> chocolate = cake()
? 'cake'
-- Not quite. Try again! --

? 'beets'
-- Not quite. Try again! --

? Function
-- Not quite. Try again! --

? cake
-- Not quite. Try again! --

? Nothing
-- Not quite. Try again! --

? pie
-- Not quite. Try again! --

? beets
-- OK! --
```
## lab03
### incremental run（递增游程问题）
```python
def get_k_run_starter(n, k):
    """Returns the 0th digit of the kth increasing run within n.
    >>> get_k_run_starter(123444345, 0)
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
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
        while n // 10 and (n % 10) > (n // 10) % 10:    # 这个地方要看懂
            n //= 10                                                      # 进行“去尾”操作
        final = n % 10                                                       # 进行“取尾”操作
        i += 1
        n //= 10                                                                # “取尾”完成后还是要“去尾”
    return final
```
### 关于素数、整除的一个问题
```python
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
```
### YY图问题
```python
y = "y"
h = y
def y(y):
    h = "h"
    if y == h:
        return y + "i"
    y = lambda y: y(h)
    return lambda h: y(h)
y = y(y)(y)                                 # 最后y的结果是"hi"
```
### 交换两个函数问题
```python
def funny(joke):
    hoax = joke + 1
    return funny(hoax)       # 这个地方的funny在交换后换成了sad，

def sad(joke):
    hoax = joke - 1
    return hoax + hoax

funny, sad = sad, funny         
result = funny(sad(1))             # 最后是有结果的，result = 2
```
# 零零碎碎
```python
python ok --local

python3 ok -q with_if_function --local
# 仅运行名为 with_if_function 的题目/函数的测试用例

python -m doctest lab00.py
python -m doctest -v lab00.py
# 自动检查函数文档字符串（docstring，即被"""包裹起来的部分）中带有 >>> 的示例代码是否正确
# -v 查看更详细检查过程
```

```powershell
# 查看使用的是什么shell，pwsh指的是powershell
oh-my-posh get shell

# 查看所有themes
Get-PoshThemes

# 编辑PowerShell 配置文件脚本
notepad $PROFILE

# 重新加载配置文件
. $PROFILE
```