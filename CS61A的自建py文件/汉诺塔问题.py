def hanoi(n, source, target):
    """
    将 n 个盘子从 source 移动到 target。
    辅助柱自动通过 6 - source - target 计算得到。
    """
    if n == 1:
        print(f"{source} -> {target}")
    else:
        auxiliary = 6 - source - target
        hanoi(n-1, source, auxiliary)
        print(f"{source} -> {target}")
        hanoi(n-1, auxiliary, target)

# 调用示例
hanoi(3, 1, 2)
