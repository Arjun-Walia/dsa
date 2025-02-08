
i=int(input("Enter a number:"))

def numbers(i):
    if i<1:
        return
    print(i)
    numbers(i-1)

numbers(i)

#Backtrack

n=int(input("Enter number:"))
def numbers(i,n):
    if i<1:
        return
    numbers(i-1,n)
    print(i)
numbers(n,n)
    

    
