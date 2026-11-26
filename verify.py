"""Exact cross-checks for the analytic counting proof."""
from itertools import product
def count(n, length):
    def valid(w):
        return all(a+b != c+d and a+c != b+d and a+d != b+c
                   for a,b,c,d in zip(w,w[1:],w[2:],w[3:]))
    return sum(map(valid, product(range(n+1),repeat=length)))

def formula(n):
    return n**4+2*n**3+3*n**2+2*n

if __name__ == "__main__":
    for n in range(11):
        assert count(n,4)==formula(n),n
    print("A247727: exact brute-force checks n=0..10 passed.")
