def fractional_knapsack(weight,profit,capacity):
    fraction=[0]*len(weight)
    objects=list(range(len(profit)))
    max_profit=0

    #getting the ratio
    ratio=[profit/weight for profit,weight in zip(profit,weight)]
    # sorting the object index based on the high value to low value of ratio
    objects.sort(key=lambda i:ratio[i],reverse=True)
    #calcualtion the max_profit
    for i in objects:
        if weight[i]<=capacity:
            fraction[i]=1
            max_profit+=profit[i]
            capacity-=weight[i]
        else:
            fraction[i]=capacity/weight[i]
            max_profit+=profit[i]*capacity/weight[i]
            break
    return max_profit,fraction








weight=[12,8,5,10]
profit=[300,270,200,260]
capacity=22

max_profit,fraction=fractional_knapsack(weight,profit,capacity)
print("max profit is ",max_profit," fraction value is ",fraction)
