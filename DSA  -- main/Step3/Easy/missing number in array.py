nums=[1,2,4,5]

#optimal solution 1

n=len(nums)+1
sum1=(n*(n+1))/2
sum2=0
for i in nums:
    sum2+=i
print(int(sum1-sum2))

#optimal solution 2

xor1=0
for i in range(1,len(nums)+2):
    xor1=xor1^i
xor2=0
for i in nums:
    xor2=xor2^i
print(xor1^xor2)
