x = 100

def f():
    nonlocal x
    print(x)
    
f()