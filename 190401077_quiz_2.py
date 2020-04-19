from sympy import Symbol, Limit, pprint ,exp ,sqrt ,pi, Integral

t = Symbol('t')
t1 = Symbol('t1')
delta_t = Symbol('delta_t')

St = 4*t**3 + 3*t + 41

St1 = St.subs({ t:t1 })
St1_delta = St.subs({t:t1 + delta_t})

limit = Limit((St1_delta-St1)/delta_t , delta_t , 0).doit()
pprint(limit)




x = Symbol('x')
p = exp(-(x - 10)**2/2) / sqrt(2*pi)
integral = Integral(p , (x,11,12)).doit().evalf()
print(integral)