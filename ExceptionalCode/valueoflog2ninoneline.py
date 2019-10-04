def log2n(n):
    return 1+log2n(n/2) if n>1 else 0 

n=1024
print(log2n(n))