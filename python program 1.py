from numpy import*
from matplotlib.pyplot import*
from scipy.integrate import odeint
def f(p,e):
    a1=(-192*3.14/(5*c**5))       # a1,a2,a2,a4,a5 b1 b2,b3,b4= dummy variable
    a2=(2*3.14*G/p)**(5/3)        # p1 orbital period , e1= eccentricity
    a3=(m1*m2/(m1+m2)**(1/3))
    a4=(1+(73/24)*e**2+(37/96)*e**4)
    a5=(1-e**2)**(-7/2)
    
    p1=a1*a2*a3*a4*a5


    b1=(-608*3.14*e/(15*c**5*p))
    b2=(m1*m2/(m1+m2)**(1/3))
    b3=(1+(121/304)*e**2)
    b4=(1-e**2)**(-5/2)

    e1=b1*b2*b3*b4
    
    return[p1,e1]


m1=10*1.989*10**30     # initial conditions
m2=10*1.989*10**30
c=3*10**8
G=6.6743*10**-11
e=0.4
p=0.3


    
y0=[e,p,m1,m2,c,G]

t=linspace (0,10,101)
sol=odeint (f,y0,t,args=(m1,m2,p,e,c,G))
plot(t,sol[:,0])
plot(t,sol[:,1])
show()
