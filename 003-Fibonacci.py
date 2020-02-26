
#Program Amacı: Fibonacci dizisinde n. elemana kadar olan tek ve ç,ft sayıların toplamlarını gösterir.

a = 1
b = 1
çiftsayilartoplamı = 0
teksayilartoplami = 2
n = int(input("Kaçıncı Sayı Hesaplansın: "))
for i in range (3,n+1):
    c = a + b
    a=b
    b=c
    if c%2==0 :
        çiftsayilartoplamı+=c
    else:
        teksayilartoplami+=c
    
print("Çift Sayıların Toplamı: ",çiftsayilartoplamı)
print("Tek Sayıların Toplamı: ",teksayilartoplami)
