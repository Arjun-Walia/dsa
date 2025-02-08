prices = [7,1,5,3,6,4]

minp=float("inf")
maxpro=0
for i in prices:
    minp=min(minp,i)
    maxpro=max(maxpro,i-minp)
print(maxpro)

low = 0  
high = 1  
max_profit = 0 

while high < len(prices):
    if prices[high] > prices[low]:
        profit = prices[high] - prices[low]
        max_profit = max(max_profit, profit)
    else:
        low = high
    high += 1

print(max_profit)
