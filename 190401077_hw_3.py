#Batuhan Köknaroğlu -- 190401077

import sympy as sym
from sympy import Symbol
from sympy import pprint 
import sympy.plotting as syp
sigma = Symbol("sigma")
x = Symbol("x")
mu = Symbol("mu")
part_1 = 1 / ((3*sym.pi**2)*sigma**2)
part_2 = sym.exp(-1 * ((mu-x)**2) / (5*sigma**4))
my_gauss_function = part_1 * part_2
pprint(my_gauss_function)
syp.plot(my_gauss_function.subs({mu:50,sigma:5}) , (x , -100 , 300) , title = 'Binom Distribution')


x_values = []
y_values = []
for value in range (-200,200):
        y = my_gauss_function.subs({mu:40,sigma:-5,x:value}).evalf()
        y_values.append(y)
        x_values.append(value)
        #print(value,y)
import matplotlib.pyplot as plt
plt.plot(x_values,y_values)
plt.show()