def evens(start, end):
    even = start + start % 2
    while even <= end:
        yield even
        even += 2
        
       
        
def countdown(n):
    if n > 0:
        yield n
        yield from countdown(n - 1)  # "from"不能丢
      # for i in countdown(n - 1):
      #     yield i   



def prefixes(x):
    if x:
        yield from prefixes(x[:-1])
        yield x
        
print(list(prefixes("abc")))

def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])
        
print(list(substrings("tops")))