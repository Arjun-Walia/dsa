num=10
c=0
for i in range(1,num):
    if num%i==0:
        c+=1


print(True if c<=2 else False)
