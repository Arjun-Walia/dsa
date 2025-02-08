def countGoodNumbers(n):
    mod = 1000000007
    odd = n//2
    even = n//2 + n%2
    return (binaryExp(5, even)%mod *binaryExp(4, odd)%mod)%mod

def binaryExp(x, n):
    mod = 1000000007
    if n==0:
        return 1
    if n < 0:
        return 1/binaryExp(x, -n)
    
    if n%2==0:
        return binaryExp((x*x)%mod, n//2)
    else:
        return x *binaryExp((x*x)%mod, (n-1)//2)
    

    
print(countGoodNumbers(1))