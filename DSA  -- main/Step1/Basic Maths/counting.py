
def digitCount(num):
    count=0
    while num>0:
        lastDigit=num%10
        num=int(num/10)
        count=count+lastDigit
    return(count)

num=19
c=0
while num>0:
    lastDigit=num%10
    if num%lastDigit==0:
        num=int(num/10)
        c+=1
print(c)
    
    
