def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr



def shellSort(arr):
    n=len(arr)
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            temp=arr[i]
            j=i
            while j>=gap and arr[j-gap]>temp:
                arr[j]=arr[j-gap]
                j=j-gap
            arr[j]=temp
        gap//=2
    return arr

print(insertionSort([5,9,7,1,3,5,2,0,7,9,4]))
print(shellSort([8,4,1,0,8,7,9,6,2,0,4]))
