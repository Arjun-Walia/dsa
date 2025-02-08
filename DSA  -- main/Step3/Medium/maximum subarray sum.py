#Kaddane's Algorithm

arr=[-2,1,-3,4,-1,2,1,-5,4]

#method1

Sum=0
maxSum=float("-inf")

for i in arr:
    Sum+=i
    maxSum=max(Sum,maxSum)
    if Sum<0:
        Sum=0
print(maxSum)

#method2

sum1=0
maxi=float("-inf")

for i in arr:
    sum1+=i
    if sum1>maxi:
        maxi=sum1
    if sum1<0:
        sum1=0
print(maxi)
