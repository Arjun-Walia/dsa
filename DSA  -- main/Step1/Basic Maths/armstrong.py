num=371
dup=num
sum1=0
while num>0:
    ld=num%10
    sum1=sum1+(ld*ld*ld)
    num=int(num/10)

print(True if dup==sum1 else False )
    
