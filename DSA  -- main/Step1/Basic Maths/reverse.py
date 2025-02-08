num=7789
rev=0
while num>0:
    ld=num%10
    rev=rev*10+ld
    num=int(num/10)

print(rev)
    
    
