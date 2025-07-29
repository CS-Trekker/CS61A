## %
```python
a = '小明'
b = 12
c = 5.8
print("我是%s，今年%d岁了，我的王者KD是%f"%(a, b, c))

print("%4.2f"%1234.5678)  # 总宽度至少 4 个字符，小数点后显示 2 位
# 1234.57
```
## 枚举算法/布尔值相加
> 4个人中有一人做了好事，已知有三个人说了真话，根据下面对话判断是谁做的好事。
> A说：不是我；
> B说: 是C;
> C说：是D;
> D说: C胡说。
```python
for N in "ABCD":
	if (N != "A")+(N == "C")+(N =="D")+(N != "D") == 3:
	        print(N+"做了好事")
# True 在数值上等于 1
# False 在数值上等于 0
```
## 字符串判断方法

| 方法              | True 的条件                   | False 的情况示例              |
| --------------- | -------------------------- | ------------------------ |
| **s.isalnum()** | 字符串只包含 **字母（含中英文）或数字**，且非空 | 含空格、标点、符号，或为空            |
| **s.isdigit()** | 字符串只包含 **0-9 的数字**         | 含空格、小数点、字母、符号（如 ²、¾），或为空 |
| **s.isalpha()** | 字符串只包含 **字母（含中文）**         | 含数字、空格、标点，或为空            |
| **s.islower()** | **所有字母都是小写**（数字和标点不影响判断）   | 有至少一个大写字母，或为空            |
> ⚠️ **补充说明**  
> - 这些方法在 **字符串为空时都会返回 False**。  
> - `isalnum()` 和 `isalpha()` **会把中文当作“字母”**，如 `'你好'.isalpha()` 返回**True**

## 字符串查找
```python
str1 = "nananananana na na na"

# 在索引2到14之间查找"nana"的个数(不重叠)
print(str1.count("nana", 2, 14))                 # 2

str2 = "Hello World, Hello Python"

# 基本查找
print(str2.find("World"))                            # 输出：6
print(str2.find("Java"))                              # 输出：-1（找不到返回-1）

# 指定开始和结束位置查找 (含start，不含end)
print(str2.find("Hello", 5, 18))                   # 输出：13
print(str2.find("Hello", 5, 10))                   # 输出：-1（在指定范围内找不到）
``` 

## 取整
```python
> int(-3.2)
> -3

> import math
> math.floor(-3.2)
> -4

> math.ceil(-3.2)
> -3
```

## 素数判断
```python
import math

def is_prime(n: int):
    assert n >= 2
    for i in range(2, math.isqrt(n) + 1):         # math.isqrt(9) -> 3; math.isqrt(10) -> 3
        if n % i == 0:
            return False
    return True
```

> 进一步优化：
```python
def better_is_prime(n: int):
    assert n >= 2
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, math.isqrt(n) + 1, 2):
            if n % i == 0:
                return False
        return True
```
## 四舍五入
### round
```python
num = 3.14159
rounded_num = round(num, 2)
print(rounded_num)                   # 结果是float, 3.14
```
### f-string
```python
num = 3.14159
formatted_num = f"{num:.2f}"
print(formatted_num)                # 字符串
```
```python
round(num, 1)                               # 3.0
round(num, 0)                               # 3       (int类型)
```
## 字符串比大小
```python
 # 空字符串 < 数字 < 大写字母 < 小写字母
print("hello" > "hEllo World") 
print("Hello" > "86")
print("hello" < "helloworld")
print("" < "1") 
```
## chr、ord
```python
# chr -> 把一个 整数（Unicode码点） 转换成对应的 字符
# ord -> 把一个 字符 转换成对应的 Unicode码点
> chr(999)
'ϧ'
> ord("a")
97
> chr(128512)
'😀'
```
## r-string
```python
# 原始字符串
print(r"C:\new\test.txt")    # 输出：C:\new\test.txt
# 反斜杠保持原样输出   
```

| 转义字符 | 说明  | 作用示例                      |
| ---- | --- | ------------------------- |
| `\n` | 换行符 | 用于换行                      |
| `\t` | 制表符 | 表示一个水平制表符（Tab键）           |
| `\r` | 回车符 | 将光标移到行首                   |
| `\a` | 响铃符 | 使计算机发出警告声                 |
| `\b` | 退格符 | 删除前一个字符                   |
| `\'` | 单引号 | 表示单引号字符 `'`               |
| `\"` | 双引号 | 表示双引号字符 `"`               |
| `\\` | 反斜杠 | 表示反斜杠字符 `\`               |
| `\`  | 续行符 | 用于将代码或字符串拆成多行，表示下一行是同一行内容 |
## 深浅拷贝
### 浅拷贝
```python
# 浅拷贝只复制外层对象，内部嵌套对象仍是同一个引用

original_list = [10, 20, 30]

# 方法1：使用切片操作创建浅拷贝
shallow_copy_slice = original_list[:]

# 方法2：使用 list() 构造函数创建浅拷贝
shallow_copy_list = list(original_list)

# 方法3：使用 copy 模块的 copy() 函数创建浅拷贝（更通用）
import copy
shallow_copy_copyfunc = copy.copy(original_list)

# 修改浅拷贝的第一个元素，原列表不受影响
shallow_copy_slice[0] = 888
print("original_list =", original_list)          # → [10, 20, 30]
print("shallow_copy_slice =", shallow_copy_slice) # → [888, 20, 30]
```

```python
# 浅拷贝对嵌套列表无效，嵌套对象仍共享引用
nested_list = [[1, 2], 3, 4]
shallow_copy_nested = nested_list[:]

shallow_copy_nested[0][1] = 999  # 修改嵌套列表内部元素
print("nested_list =", nested_list)               # → [[1, 999], 3, 4]
print("shallow_copy_nested =", shallow_copy_nested)  # → [[1, 999], 3, 4]
```

### 深拷贝
```python
# 深拷贝会递归复制所有对象，包括嵌套的子对象

import copy

nested_list_2 = [[1, 2], 3, 4]
deep_copy_nested = copy.deepcopy(nested_list_2)

deep_copy_nested[0][1] = 777  # 修改深拷贝后的嵌套元素
print("nested_list_2 =", nested_list_2)          # → [[1, 2], 3, 4] 原始列表未受影响
print("deep_copy_nested =", deep_copy_nested)    # → [[1, 777], 3, 4]
```
## decimal
```python
a = 0.1 + 0.2
print(a)
# 0.30000000000000004

import decimal
a = decimal.Decimal(0.1) + decimal.Decimal(0.2)
# 这里 0.1 和 0.2 仍然是 Python 的浮点数（float），在传给 Decimal() 之前，已经带着浮点误差了
print(a)
# 0.3000000000000000166533453694

a = decimal.Decimal('0.1') + decimal.Decimal('0.2')
# 直接从字符串转换为 Decimal，不经过浮点数，结果完全精确
print(a) 
# 0.3
```
## 多关键词排序
```python
#         进球 失球 净胜球 积分
teams = [
    ("荷兰", 13, 16, -3, 9),
    ("巴西", 24, 8, 16, 21),
    ("克罗地亚", 8, 20, -12, 3),
    ("英格兰", 16, 13, 3, 12),
    ("波兰", 6, 22, -16, 1),
    ("法国", 17, 11, 6, 15),
    ("葡萄牙", 15, 18, -3, 9),
    ("德国", 19, 12, 7, 18),
    ("比利时", 11, 17, -6, 6),
    ("西班牙", 20, 15, 5, 15),
    ("意大利", 14, 14, 0, 12),
    ("阿根廷", 22, 10, 12, 21)
]

rankings = sorted(teams, key= lambda x: (x[4], x[3], x[1], -x[2]), reverse= True)
print(rankings)
```
## re模块
```python
import re

```
# 零零碎碎
```python
print(len("\n^_^n/"))    # 换行符是一个字符
# 6
```

```python
# 列表解包
lst = [1,3,45,6,7,8,99,3]
print(*lst)

# 把列表 lst 中的所有元素逐个拆开，作为独立的参数传递给 print 函数
```

```python
dic = {"a" : 898,"b" : 978,"c" : 272}
max_letter = max(dic,key = dic.get)    # max的key参数应该是一个函数
print(max_letter)
```

```python
name = ["A","B","C","D"]
i = name.index("C")           # index查找某个元素在列表中第一次出现的位置
print(i)
# 2
```

```python
from collections.abc import Iterable, Iterator

print(isinstance([1, 2, 3], Iterable))                         # True
print(isinstance([1, 2, 3], Iterator))                         # False
```

```python
# str.join(iterable)

words = ["hello", "world", "python"]

# 用空格连接
result = " ".join(words)
print(result)  # 输出: hello world python
```

```python
# 字典推导式（dict comprehension）
lst = [("a",1),("b",2),("c",3)]
dic = {key:val for key,val in lst}
print(dic)
```

