import random 

def get_n_random_number(n=10, min_=-5, max_=5):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(min_, max_))
    return numbers


my_list = get_n_random_number(9,-10,5)  #Bu dosyadaki rastgele liste oluşturucu.Sadece 1 tanedir.Tüm dosyadaki listeleri etkiler.
print("Liste = ",my_list)
print("Listenin Sıralı Hali = ",sorted(my_list))




def my_frequency_with_dict(list):  #Parametre olarak aldığı listenin elemanlarının frekanslarını bulur. Dictionary kullanır. 
    frequency_dict = {}
    for item in list:
        if item in frequency_dict:
            frequency_dict[item] = frequency_dict[item]+1
        else:
            frequency_dict[item]  = 1
    return frequency_dict

my_hist_d = my_frequency_with_dict(my_list)
print("Histogram(dictionary) ",my_frequency_with_dict(my_list))


def my_frequency_with_list_of_tuples(list_1):  #Parametre olarak aldığı listenin elemanlarının frekanslarını bulur. Liste kullanır.
    frequency_list = []
    for i in range(len(list_1)):
        s = False
        for j in range(len(frequency_list)):
            if list_1[i] == frequency_list[j][0]: 
                frequency_list[j][1] = frequency_list[j][1] + 1
                s = True
        if s == False :
            frequency_list.append([list_1[i],1])
    return frequency_list        

my_hist_l = my_frequency_with_list_of_tuples(my_list)
print("Histogram(liste) ",my_frequency_with_list_of_tuples(my_list))




def my_mode_with_dict(my_hist_dict):  #Parametre olarak aldığı dictionarynin modunu bulur. Hash yardımı ile.
    frequency_max = -1
    mode = -1
    for key in my_hist_d.keys():
        if my_hist_d[key] > frequency_max:
            frequency_max = my_hist_d[key]
            mode = key
    return mode, frequency_max

print("Dictionary Mode = ",my_mode_with_dict(my_hist_d))    


def my_mode_with_list(my_hist_list):   #Parametre olarak aldığı listenin modunu bulur. List of Tuples yardımı ile.
    frequency_max = -1
    mode =-1
    for item,frequency in my_hist_list:
        if frequency > frequency_max :
            frequency_max = frequency
            mode = item
    return mode, frequency_max

print("List Mode =",my_mode_with_list(my_hist_l))


def my_linear_search(list_1,item_search):  #Parametre olarak aldığı listeyi 
    found = (-1,-1)                        #ve listedeki bir elemanın kaçıncı indiste olduğunu bulur.
    n = len(list_1)
    for indis in range(n):
        if list_1[indis] == item_search:
            found = (list_1[indis],indis)
    return found

print("5 elemanının bulunduğu indis(linear) = ",my_linear_search(my_list,5))  #listedeki 5 elemanının hangi indiste olduğunu yazacak.




def my_mean(list_1):   #Parametre olarak aldığı listenin ortalamasını bulur.
    s,t =0,0
    for item in list_1:
        s=s+1
        t=t+item
        mean_ = t/s
    return mean_

print("Ortalama(mean) = ",my_mean(my_list))


def my_bubble_sort(list_1):
    n=len(list_1)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not (list_1[j]<list_1[j+1]):
                temp=list_1[j]
                list_1[j]=list_1[j+1]
                list_1[j+1]=temp
    return list_1

print("Bubble Sort = ",my_bubble_sort(my_list))
my_sorted_list = my_bubble_sort(my_list)



def my_binary_search(list_1,item_search):  #Parametre olarak aldığı  SIRALI listeyi 
    found = (-1,-1)                        #ve listedeki bir elemanın kaçıncı indiste olduğunu bulur.
    low = 0
    high = len(list_1)-1
    while low <= high:
        mid = (low + high) // 2
        if list_1[mid] == item_search:
            return list_1[mid],mid
        elif list_1[mid] > item_search:
            high = mid - 1
        else:
            low = mid + 1
    return found

print("5 elemanının bulunduğu indis(binary) = ",my_binary_search(my_sorted_list,5))




def my_median(list_1):    #Parametre olarak aldığı listeyi sıralar ve  ortanca elemanını bulur.
    my_list_2 = my_bubble_sort(list_1)
    n = len(my_list_2)
    if n%2 == 1:
        middle = int(n/2)
        median = my_list_2[middle]

    else:
        middle_1 = my_list_2[int(n/2)-1]
        middle_2 = my_list_2[int(n/2)]
        median = (middle_1 + middle_2) / 2
    
    return median 

print("Sıralı Listenin Medyanı = ", my_median(my_list))