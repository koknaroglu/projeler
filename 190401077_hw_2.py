import csv

liste =list()
with open('input_hw_2.csv', "r") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        liste.append(int(row[3][5:7])) #Ayrılış tarihlerindeki ayları bir listeye attık.

sirali_liste=sorted(liste) #Ayrılış tarihindeki ayları yeni bir listeye atıp sıraladık.
#print(sirali_liste)




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


def my_median(list_1):    #Parametre olarak aldığı listenin ortanca elemanını bulur.
    n = len(list_1)
    if n%2 == 1:
        middle = int(n/2)
        median = list_1[middle][1]

    else:
        middle_1 = list_1[int(n/2)-1][1]
        middle_2 = list_1[int(n/2)][1]
        median = (middle_1 + middle_2) / 2
    
    return median 


def ort(list_1): #Parametre olarak aldığı listenin ortalamasını bulur.
    ortalama=0
    for i in range(len(list_1)):
        ortalama=ortalama+list_1[i][1]
    return ortalama/len(list_1)




my_hist_l = my_frequency_with_list_of_tuples(sirali_liste) #Ayrılış tarihlerinin aylara göre histogramı
print("Histogram = ", my_frequency_with_list_of_tuples(sirali_liste))


print("Medyan = ",my_median(my_hist_l)) #Medyan için sadece value değerini aldık.
print("Ortalama = ",ort(my_hist_l)) #Parametre olarak liste şeklinde olan histogramı gönderdik.Bize value değerlerinin ortalamasını verdi.
print(".txt dosyası oluşturulmuştur.")



f = open('190401077_hw_2_output.txt', "w")
f.write("Medyan = 48\n")
f.write("Ortalama = 44")
f.close()