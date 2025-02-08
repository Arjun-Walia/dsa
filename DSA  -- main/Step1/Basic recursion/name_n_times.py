i=int(input("Enter an integer:"))
n=int(input("Enter number of times to run:"))

def Name(i,n):
    if i<n:
        print("Arjun")
        Name(i+1,n)
Name(i,n)



