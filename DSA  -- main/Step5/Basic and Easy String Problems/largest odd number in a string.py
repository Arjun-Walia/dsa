num = "53427"
n=len(num)-1

for i in range(n,-1,-1):
    if int(num[i])%2:
        print(num[:i+1])


