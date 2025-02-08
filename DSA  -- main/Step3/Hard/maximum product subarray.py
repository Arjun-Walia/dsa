Nums =[1,2,3,4,5,0]

pre=1
suf=1
maxi=float("-inf")
n=len(Nums)
for i in range(n):
    if pre==0:
        pre=1
    if suf==0:
        suf=1
    pre*=Nums[i]
    suf*=Nums[n-i-1]
    maxi=max(maxi,max(pre,suf))
print(maxi)
    
