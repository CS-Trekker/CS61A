def cascade1(x):
    if x < 10:
        print(x)
    else:
        print(x)
        cascade1(x // 10)
        print(x)
        
cascade1(12345)   # 想想cascade1(12345)会打印什么

def cascade2(x):
	print(x)
	if x > 10:
		cascade2(x // 10)
		print(x)
  
cascade2(12345)   # 想想cascade2(12345)会打印什么

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
  
grow = lambda n: f_then_g(grow,print,n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)

inverse_cascade(1234)  # 想想inverse_cascade(1234)会打印什么
