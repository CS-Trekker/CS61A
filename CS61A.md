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
# 9、树递归
```python
### 级联函数
def cascade(x):
    if x < 10:
        print(x)
    else:
        print(x)
        cascade(x // 10)
        print(x)
        
cascade(12345)   # 想想cascade(12345)会打印什么,可看看环境图
```
```python
def cascade(x):
	print(x)
	if x > 10:
		cascade(x // 10)
		print(x)
```
## 有关递归调用的顺序
```python
def inverse_cascade(x):
    '''
    >>> inverse_cascade(1234)
    1
    12
    123
    1234
    123
    12
    1
    '''
    grow(x)
    print(x)
    shrink(x)
 
def f_then_g(f, g, n) :
	if n:
		f(n)
		g(n)

# grow = lambda n: f_then_g(_________________)
# shrink = lambda n: f_then_g(________________)

grow = lambda n: f_then_g(grow,print,n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)
```
## counting partitions问题
![[PixPin_2025-06-24_21-38-18.png|250]]
```python
def count_partitions(n,m):
    '''用若干个不超过 m 的正整数的和表示 n 的方法数'''
    if n == 0:
        return 1
    elif m == 0:
        return 0
    elif n < 0:
        return 0
    else:
        return count_partitions(n - m, m) + count_partitions(n, m - 1)
    
print(count_partitions(6,4))
```
[原题地址↓](https://chillyhigh.github.io/CS61A-CN/hw/hw02/#q4)
```python
def count_coins(total):
    def helper(total, smallest_coin):
        if total == 0:
            return 1
        elif total < 0 or smallest_coin is None:
            return 0
        else:
            next_coin = next_largest_coin(smallest_coin)
            return helper(total - smallest_coin, smallest_coin) + helper(total,next_coin)
    return helper(total, 1)
```
# 12、树
## sum函数的参数
```python
sum(iterable[, start])

sum(1, 2)                        # ❌ 报错：sum() 的第一个参数必须是可迭代对象（如 list、tuple、set、dict、generator 等）

# 第二个参数是 start，默认为 0，且 start 与 iterable 中的元素类型必须一致
sum([[2, 3], [4]], [])          # ✅ [2, 3, 4]

sum([2, 3, 4], 5)               # ✅ 14 （即 2 + 3 + 4 + 5）

sum([[2, 3, 4], [5]])           # ❌ 报错：start 默认为 0，无法与 list 相加； iterable 中所有元素也必须与 start 类型一致
```
## all、any函数
```python
all(iterable) -> bool   # 用于判断 可迭代对象中的所有元素是否都为 True
any(iterable) -> bool # 用于判断 可迭代对象中的元素中是否有一个为True
```
# 13、二进制数
## 补码表示法
> 以 8位二进制 为例（可以推广到 16位、32位、64位）：

| 十进制  | 补码（二进制）  |
| ---- | -------- |
| +0   | 00000000 |
| -0   | 00000000 |
| +1   | 00000001 |
| -1   | 11111111 |
| +2   | 00000010 |
| -2   | 11111110 |
| 0    | 00000000 |
| -128 | 10000000 |
| 128  | 无        |
| 127  | 01111111 |
> 8位可以表示`127`~`-128` ($2^7 = 128$)

> 最高位是0代表正数，1代表负数，`10000000`是负数

### 计算负数补码
- 写出正数的二进制：`5 = 00000101`
- 取反（即反码）：`11111010`
- 加一：`11111010 + 1 = 11111011`

所以，**-5 的补码为：`11111011`**
# 15、可变值
## 在列表中插入元素
```python
a = [1, 2, 3]
a[1:1] = [9, 8]
# 结果：[1, 9, 8, 2, 3]
```
## 列表的自引用
```python
t = [1, 2, 3]
>>> t[1: 3] = [t]
>>> t
[1, [...]]
# t = [1, [1, [1, [1, ...]]]]

>>> s = [1]
>>> s.append(s)
>>> s
[1, [...]]
```

```python
# 没发生列表自引用
>>> s = [1]
>>> s.extend(s)
>>> s
[1, 1]
# s.extend(s) 会先复制一份 s 的当前元素（值引用），然后把这些元素加到原 s 的末尾
```
## 切片赋值
```python
t = [1, 2, 3] 
>>> t[1: 3] = 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only assign an iterable
>>> t[1: 3] = [1]
>>> t
[1, 1]
```

```python
>>> t = [[1, 2], [3, 4]]
>>> t[0].append(t[1: 2])
 
>>> t
[[1, 2, [[3, 4]]], [3, 4]]    # 注意前面的t[1: 2]得到的不是 [3, 4] 而是 [[3, 4]]
```
# 16、可变函数
```python
x = 100

def f():
    x = 1
    def g():
        def h():
            nonlocal x
            print(x)
        h()
    g()
f()
# 结果： 1
```
```python
x = 100

def f():
    nonlocal x
    print(x)
    
f()
# 报错
```
# 17、迭代器
```python
def prefixes(x):
    if x:
        yield from prefixes(x[:-1])    # x[:-1]执行的是“取尾”操作
        yield x

ls = list(prefixes("abc"))                         # ['a', 'ab', 'abc']
```
```python
def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])
        
print(list(substrings("tops")))               # ['t', 'to', 'top', 'tops', 'o', 'op', 'ops', 'p', 'ps', 's']
```
# HW难点
## hw01
在 Python 中，函数体（def 里面）可以没有 return 语句，此时函数的返回值默认为 None。
但函数体中仍然可以有 print() 语句，比如 print(42) 或 print(47)，这些语句会在函数被调用时立即输出内容到控制台，不影响返回值。
## hw02
### 用递归代替while循环解题
[原题地址](https://chillyhigh.github.io/CS61A-CN/hw/hw02/#q2)
```python
def pingpong(n):
    def helper(index,value,direction):
        if index == n:
            return value
        elif n == 1:
            return 1
        else:
            if (index + 1) % 8 == 0 or num_eights(index + 1) > 0:
                return helper(index + 1, value + direction, - direction)
            else:
                return helper(index + 1, value + direction, direction)
    return helper(1, 1, 1)
    
    # index, value, direction = 1, 1, 1
    # while index < n:
    #     value += direction
    #     index += 1
    #     if index % 8 == 0 or num_eights(index) > 0:
    #         direction *= -1
    # return value
```
[原题地址](https://chillyhigh.github.io/CS61A-CN/proj/cats/#problem-6-2-pts)
```python
def shifty_shifts(start, goal, limit):
    def helper(start, goal, diff):
        if diff > limit:
            return limit + 1
        elif len(start) == 0 or len(goal) == 0:
            return diff + abs(len(start) - len(goal))
        else:
            if start[0] == goal[0]:
                return helper(start[1:], goal[1:], diff)
            else:
                return helper(start[1:], goal[1:], diff + 1)
    return helper(start, goal, 0)
```
### 匿名递归函数问题
[原题地址](https://chillyhigh.github.io/CS61A-CN/hw/hw02/#q5)
```python
from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.
    >>> make_anonymous_factorial()(5)
    120
    """
    return (lambda f: (lambda x: f(f, x)))(lambda f, x: 1 if x == 0 else mul(x, f(f, sub(x, 1))))
```
## hw03
```python
h = float('inf') # 表示一个浮点数的正无穷大
# float('-inf') 表示负无穷大（-∞）
```
## hw04
### 高阶生成器
[原题地址](https://chillyhigh.github.io/CS61A-CN/hw/hw04/#q6)
```python
def remainders_generator(m):
    i = 0
    while i < m:
        def gen():
            n = naturals()                       # 这里是为了让之后不重复进行naturals（会导致全部的  next(naturals())  都是  1  ）
            if i > 0:
                yield i
            while True:
                yield i + m * next(n)
        yield gen()
        i += 1

def naturals():
    i = 1
    while True:
        yield i
        i += 1
```

> 更思路清晰的做法
```python
def remainders_generator(m):
    def helper(i):
        for x in natural_generator:
            if x % m == i:
                yield x
    
    for i in range(m):
        natural_generator = naturals()
        yield helper(i)
```
# LAB难点
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
## lab05
### zip函数并行遍历([原题地址](https://chillyhigh.github.io/CS61A-CN/lab/lab05/#q10))
```python
names = ['Alice', 'Bob', 'Charlie']
scores = [90, 85, 88]

for a, b in zip(names, scores):
    print(f"{a}, {b}")
```
# PROJECT难点
## Hog
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
## Cats
### 数据抽象/抽象屏障
#### ✅ 正确写法：使用抽象构造函数
```python
def time_per_word(times_per_player, words):
    times = [
        [end - start for start, end in zip(player[:-1], player[1:])]
        for player in times_per_player
    ]
    return game(words, times)  # ✅ 正确地返回抽象对象
```
#### ✅ 抽象接口定义（ADT 函数）
```python
def game(words, times):
    return [words, times]

def all_words(game):
    return game[0]

def all_times(game):
    return game[1]
```
#### 🚫 不要这样写（违反抽象屏障）
```python
def time_per_word(...):
    return [words, times]  # ❌ 错误：直接返回 list，不能通过属性访问 `.a`
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