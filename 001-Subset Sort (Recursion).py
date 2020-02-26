
#Programın Amacı: Verilen bir listenin alt kümelerindeki elemanların toplamının en fazla olduğu değeri bulmak.

def max_of_two(a,b):
    if (a>b):
        return a
    else:
        return b

def max_of_three(a,b,c):
    return max_of_two(a,max_of_two(b,c))

def my_function_1(list1=[4,-3,5,-2,-1,2,6,-2]):
    n = len(list1)
    if(n==1):
        return list1[0]
    
    #listeyi ortadan 2 eş parçaya bölüyoruz
    left_i = 0 #soldaki parçanın ilk elemanı indeksi 0
    left_j = n//2 #soldaki parçanın son elamanı indeksi. Yani 4

    right_i = n//2 #sağdaki parçanın ilk elemanı indeksi. Yani 4
    right_j = n #sağdaki parçanın son elemanı indeksi. Yani 8

    left_sum = my_function_1(list1[left_i:left_j])
    right_sum = my_function_1(list1[right_i:right_j])

    t=0
    temp_left_sum=0
    for i in range (left_j-1,left_i-1,-1): #-2 den 4 e kadar olan sayıları dahil etmek için. -2 ve 4 dahl olmalı
        t=t+list1[i]
        if (t>temp_left_sum):
            temp_left_sum=t

    t=0
    temp_right_sum=0
    for i in range(right_i,right_j):
        t=t+list1[i]
        if (t>temp_right_sum):
            temp_right_sum=t
    
    center_sum = temp_left_sum+temp_right_sum
    return max_of_three(left_sum,right_sum,center_sum)


print(my_function_1([4,-3,5,-2,-1,2,6,-2]))



    
