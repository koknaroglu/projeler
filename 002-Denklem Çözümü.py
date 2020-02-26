a=int(input("İkinci Dereceden Terimin Katsayısı : "))
b=int(input("Birinci Dereceden Terimin Katsayısı : "))
c=int(input("Sabit Terim : "))
delta = b**2 -4*a*c
if delta <0:
    print("Reel Kök Yok")
elif delta==0:
    x= -b/(2*a)
    print(x)
    
else:
    x1= (-b+delta**(1/2))/2*a
    x2=(-b-delta**(1/2))/2*a
    print("Kökler: ",x1,x2)
