class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return f"Ratio({self.numer}, {self.denom})"
    
    def __str__(self):
        # return f"{self.numer} / {self.denom}"
        return f"{self.numer}/{self.denom}"
    
    def __add__(self, other):
        if isinstance(other, float):
            return float(self) + other
        elif isinstance(other, int):
            n = self.numer + other * self.denom
            d = self.denom
        else:
            n = self.numer * other.denom + other.numer * self.denom
            d = self.denom * other.denom
        g = gcd(n, d)
        return Ratio(n // g, d // g)
    
    __radd__ = __add__

    def __float__(self):
        return self.numer / self.denom
            
def gcd(n, d):
    while d > 0:
        n, d = d, n % d
    return n

        
        
        