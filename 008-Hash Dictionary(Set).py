def my_hash(arr):  #Gönderdiğimiz listedeki elemanların her birinden kaç tane olduğunu yazdırır.
    my_dict=dict()
    for i in arr:
        if i in my_dict:
            my_dict[i]=my_dict[i]+1
        else:
            my_dict[i]=1
    return my_dict

print(my_hash([8,7,4,6,9,1,4,7,5,2,0,1,5,9,6,3]))




print("--------------------------------------------------------------------------------------")






def lookup(d,v):   #d -> gönderdiğimiz dictionary ......  v -> gönderdiğimiz value değeri
    for k in d:
        if d[k]==v:
            print(k)   #Gönderdiğimiz value değerine karşılık gelen key değerleri


print(lookup({8: 1, 7: 2, 4: 2, 6: 2, 9: 2, 1: 2, 5: 2, 2: 1, 0: 1, 3: 1},2))





print("--------------------------------------------------------------------------------------")




known = {0:0,1:1}
def fibo_rec(n):
    if n in known:
        return known[n]
    else:
        result = fibo_rec(n-1)+fibo_rec(n-2)
        known[n]=result
        return result

print(fibo_rec(9))
