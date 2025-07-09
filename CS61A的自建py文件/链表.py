class Link:
    empty = ()
    
    def __init__(self, first, rest) -> None:
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
        
def add(s, v):
    original_s = Link(s.first, s.rest)
    if s.first == v:
        return original_s
    if s.first > v:
        return Link(v,s)
    while s.first < v:
        if s.rest == Link.empty:
            return Link(s.first, Link(v, Link.empty))
        return Link(s.first,add(s.rest, v))
        