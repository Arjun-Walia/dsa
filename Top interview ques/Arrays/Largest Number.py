from functools import cmp_to_key

def compare(x,y):
    if x+y>y+x:
        return -1
    elif x+y<y+x:
        return 1
    else:
        return 0
def largestNumber(A):
    A=list(map(str,A))
    # A.sort(key=cmp_to_key(compare))
    A.sort(key=lambda x: x*10 , reverse=True)
    res="".join(A)
    
    return '0' if res[0]=='0' else res