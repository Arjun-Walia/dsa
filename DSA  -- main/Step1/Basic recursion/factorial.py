#using recursion

def factorial(n,f):
    if n<1:
        print(f)
        return
    factorial(n-1,f*n)
    
n=int(input("Enter a number:"))    
factorial(n,1)

#Another way

def f(n):
    if n==0:
        return(1)
    return(n*f(n-1))

i=int(input("Enter a number:"))
print(f(i))

