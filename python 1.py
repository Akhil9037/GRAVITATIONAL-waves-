from numpy import*
from matplotlib.pyplot import*
from scipy.integrate import odeint   #p1=orbital period #e1= eccentricity
def f(p,e):
    p1=(-192*3.14/(5*c**5))*(2*3.14*G/p)**(5/3)*(m1*m2/(m1+m2)**(1/3))*(1+(73/24)*e**2+(37/96)*e**4)*(1-e**2)**(-7/2)
    e1=(-608*3.14*e/(15*c**5*p))*(m1*m2/(m1+m2)**(1/3))*(1+(121/304)*e**2)*(1-e**2)**(-5/2)
    return [p1,e1]
m1=10*1.989*10**30
m2=10*1.989*10**30
c=3*10**8
G=6.6743*10**-11
e=0.4
p=0.3
t=0.0

    
