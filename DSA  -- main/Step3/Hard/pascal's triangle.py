#variation 1 , Find the element at given row


def nCr(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res

def pascalTriangle(r, c):
    element = nCr(r - 1, c - 1)
    return element

print(pascalTriangle(5,3))
    
#variation 2 , Find the elements at given row

n=10
ans=1
print(1,end=" ")
for i in range(1,n):
    ans*=n-i
    ans/=i
    print(int(ans),end=" ")

#variation 3 , return the pascal's triangle

def pascal(row):
    res=[]
    for i in range(1,row+1):
        r=[]
        for j in range(1,i+1):
            r.append(nCr(i-1,j-1))
        res.append(r)
    return res

print("\n",pascal(10))

