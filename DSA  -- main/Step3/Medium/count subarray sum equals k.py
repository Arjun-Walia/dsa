from collections import defaultdict

arr=[1,1,1]
k=2
n=len(arr)
dic=defaultdict(int)
cnt=0
preSum=0
dic[0]=1

for i in range(n):
    preSum+=arr[i]
    remove=preSum-k
    cnt+=dic[remove]
    dic[preSum]+=1
print(cnt)
