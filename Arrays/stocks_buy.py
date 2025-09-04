# Brute Force
# def stocks_buy(prices):
#     n= len(prices)
#     max_profit=0
    
#     for i in range(0,n):
#         for j in range(i+1,n):
#             if prices[j]>prices[i]:
#                 p=prices[j]=prices[i]
#                 max_profit=max(max_profit,p)
#     return max_profit

# arr=[7,2,1,5,6,4,8]
# res=stocks_buy(arr)
# print(res)

#optimal solution
def stocks_buy(prices):
    n= len(prices)
    max_profit=0
    min_price=float("inf")
    
    for i in range(0,n):
        min_price=min(min_price,prices[i])
        max_profit=max(max_profit,prices[i]-min_price)
        
    return max_profit

arr=[7,2,1,5,6,4]
res=stocks_buy(arr)
print(res)