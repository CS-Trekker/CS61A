# 示例 1：普通赋值（引用传递，两个变量指向同一个列表对象）
lst1 = [10, 20, 30]
ref_lst1 = lst1          # ref_lst1 是 lst1 的引用，修改其中一个会影响另一个

ref_lst1[0] = 999
print("lst1 =", lst1)       # → [999, 20, 30]
print("ref_lst1 =", ref_lst1) # → [999, 20, 30]


# 示例 2：浅拷贝（仅复制列表外壳，内部元素仍是同一对象）
lst2 = [10, 20, 30]
copy_lst2 = lst2[:]        # 使用切片创建浅拷贝

copy_lst2[0] = 888
print("lst2 =", lst2)         # → [10, 20, 30] 原列表未被修改
print("copy_lst2 =", copy_lst2) # → [888, 20, 30]


# 示例 3：浅拷贝对嵌套列表无效（元素仍是原始对象的引用）
lst3 = [[1, 2], 3, 4]
copy_lst3 = lst3[:]

copy_lst3[0][1] = 999        # 修改嵌套列表内部元素
print("lst3 =", lst3)         # → [[1, 999], 3, 4] 被修改
print("copy_lst3 =", copy_lst3) # → [[1, 999], 3, 4]


# 示例 4：深拷贝（完全复制，包括嵌套结构）
import copy

lst4 = [[1, 2], 3, 4]
deepcopy_lst4 = copy.deepcopy(lst4)

deepcopy_lst4[0][1] = 777    # 修改 deepcopy 中的嵌套元素
print("lst4 =", lst4)           # → [[1, 2], 3, 4] 原始列表未受影响
print("deepcopy_lst4 =", deepcopy_lst4) # → [[1, 777], 3, 4]
