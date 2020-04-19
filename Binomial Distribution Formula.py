
#Batuhan KÖKNAROĞLU -- 190401077


import sympy as sym
from sympy import Symbol
from sympy import pprint

p = Symbol('p')  #Olayın olma olasılığı
x = Symbol('x')
n = Symbol('n')  #Tekrar etme sayısı

my_f_1 = sym.factorial(n) / (sym.factorial(x) * sym.factorial(n-x))
my_f_2 = (p**x) * (1-p)**(n-x)
my_f = my_f_1 * my_f_2
pprint(my_f)

sym.plot(my_f.subs({p:0.6,n:90}) , (x , 0 , 90) , title = 'Binom Distribution')


x_values = []
y_values = []
for value in range (0,90):
        y = my_f.subs({p:0.6,n:90,x:value}).evalf()
        y_values.append(y)
        x_values.append(value)
        #print(value,y)
import matplotlib.pyplot as plt
plt.plot(x_values,y_values)
plt.show()