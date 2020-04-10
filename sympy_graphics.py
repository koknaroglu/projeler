import sympy as sym
from sympy import Symbol
from sympy import pprint 
import sympy.plotting as syp
sigma = Symbol("sigma")
x = Symbol("x")
mu = Symbol("mu")
part_1 = 1 / (sym.sqrt(2*sym.pi*sigma**2))
part_2 = sym.exp(-1 * ((x-mu)**2) / (2*sigma**2))
my_gauss_function = part_1 * part_2
pprint(my_gauss_function)
syp.plot(my_gauss_function.subs({mu:10,sigma:30}) , (x , -1000 , 1000) , title = 'gauss distrbition')


x_values = []
y_values = []
for value in range (-50,50):
        y = my_gauss_function.subs({mu:0,sigma:10,x:value}).evalf()
        y_values.append(y)
        x_values.append(value)
        print(value,y)
import matplotlib.pyplot as plt
plt.plot(x_values,y_values)
plt.show()