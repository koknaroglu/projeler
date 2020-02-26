def bubble(list_1):
    n=len(list_1)
    for i in range(n,0,-1):
        for j in range(i-1):
            if (list_1[j]>list_1[j+1]):
                t=list_1[j+1]
                list_1[j+1]=list_1[j]
                list_1[j]=t
    return list_1
print(bubble([4,-3,5,-2,-1,2,6,-2]))