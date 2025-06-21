# 1、计算机科学
# 2、函数
# 3、控制语句
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

```python
x = 1
def f():
    print(x)   # UnboundLocalError: local variable 'x' referenced before assignment
    x = 2
    print(x)

f()
# 如果在函数体中对变量进行了赋值操作，那么该变量会被视为局部变量；在赋值之前使用它会导致 UnboundLocalError
```
```python
x = 1
def f():
    global x
    print(x)
    x = 2        # 注意这个地方修改的是global的x
    print(x)

f()
```

# 4、高阶函数
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