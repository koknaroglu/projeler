def function1(list_1):
    maxSum=0
    n=len(list_1)
    for i in range(n):
        t=0
        for j in range(i,n):
            t=t+list_1[j]
            if (t>maxSum):
                maxSum=t

    return maxSum
print(function1([4,-3,5,-2,-1,2,6,-2]))