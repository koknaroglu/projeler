def power(a,b):  #Girilen sayı ve kuvvetinin sonucunu yazdırır 
    if b == 0 :
        return 1
    elif b == 1:
        return a
    else:
        t=1
        for i in range(b):
            t=t*a
        return t

print(power(2,3))




def power_Recursive(a,b):  #Girilen sayı ve kuvvetinin sonucunu yazdırır
    if b == 0 :
        return 1
    elif b == 1:
        return a
    if b>1 :
        return power_Recursive(a,b-1)*a

print(power_Recursive(3,3))
