#Using recursion

def submation(n,sum1):
    if n<1:
        print(sum1)
        return
    submation(n-1,sum1+n)
    
n=int(input("Enter a number:"))
submation(n,0)

#Another way

def f(n):
    if n==0:
        return(0)
    return(n+f(n-1))

i=int(input("Enter a number:"))
print(f(i))

#Using formula

a=int(input("Enter a number:"))
sum1=int(a/2*(2+a-1))
print(sum1)
