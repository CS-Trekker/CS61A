def test(*args):
	print(type(args))
	print(args)
	print(*args)
	for arg in args:
		print(arg)
  
test(1, 2, 3)