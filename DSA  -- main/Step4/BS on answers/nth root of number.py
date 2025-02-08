def fnc(mid,n,v):
    ans = 1
    for i in range(1,n+1):
        ans*=mid
        if ans>v:
            return 2
    if ans==v:
        return 1
    return 0

def nRoot(n,v):
    low=1
    high=v
    while low<=high:
        mid=(low+high)//2
        val=fnc(mid,n,v)
        if val==1:
            return mid
        elif val==2:
            high=mid-1
        else:
            low=mid+1
    return -1

print(nRoot(3,69))
