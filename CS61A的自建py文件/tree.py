def tree(label, branches = []):
    for branch in branches:
        assert is_tree(branch), "branches must be trees"
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left = fib_tree(n - 1)
        right = fib_tree(n - 2)
        return tree(label(left) + label(right), [left, right])
    
def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        return sum([count_leaves(branch) for branch in branches(tree)])
    
def leaves(tree):
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(branch) for branch in branches(tree)], [])
    
def print_tree(tree, indent = 0):
    print(" " * indent + str(label(tree)))
    for branch in branches(tree):
        print_tree(branch, indent + 2)
        
def increment_leaves(t):
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(branch) for branch in branches(t)]
        return tree(label(t), bs)
    
def increment(t):
    return tree(label(t) + 1, [increment(branch) for branch in branches(t)])

def fact_times(n, k):
    if n == 0:
        return k
    else:
        return fact_times(n - 1, k * n)
    
def fact(n):
    return fact_times(n, 1)

haste = tree("h", [tree("a", [tree("s"),
                                                            tree("t")]),
                                  tree("e")])
# print(haste)                                  ['h', ['a', ['s'], ['t']], ['e']]
# print(tree(3, [tree(4), tree(5)]))            [3, [4], [5]]
# print(branches(tree(3, [tree(4), tree(5)])))  [[4], [5]]

def print_sum(t, so_far):
    so_far += label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sum(b, so_far)
            
# print_sum(haste, "")
# has
# hat
# he