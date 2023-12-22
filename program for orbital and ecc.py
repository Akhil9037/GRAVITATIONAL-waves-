from numpy import*
from matplotlib.pyplot import*
from scipy.integrate import odeint
def f(x,t):
    a,e = x
    
    a1=(-64/(5))*(G**3/(c**5))       # a1,a2,a2,a4,a5 b1 b2,b3,b4= dummy variable
    a2=(m1*m2*mt)/(a**3)*(1-e**2)**(7/2)      # p1 orbital period , e1= eccentricity
    
    a3=(1+(73/24)*e**2+(37/96)*e**4)
    a4=(1-e**2)**(-7/2)
    
    a=a1*a2*a3*a4


    b1=(-304/15)*(G**3/(c**5))
    b2=(m1*m2*mt)/(a**4)*(1-e**2)**(5/2)
    b3=e*(1+(121/304)*e**2)
    

    e1=b1*b2*b3
    
    
    return[a,e1]


m1=10*1.989*10**30     # initial conditions
m2=10*1.989*10**30
c=3*10**8
mt=20*1.989*10**30 
G=6.6743*10**-11
x=[0.4,0.4]



t=arange(0,100,10)
sol=odeint (f,x,t)
p=sol[0]
e=sol[1]
xlim(0,40)
figure(1)
title("orbital period")
plot(t,sol[:,0])
#ylim(0,.40)
figure(2)
title("Eccentricity")
xlim(0,40)
plot(t,sol[:,1])

'''figure(3)
y=(f(x,t)**2*(G*(m1+m2)/(4*3.14*3.14)))**(1/3)
plot( t,(f(x)**t*(G*(m1+m2)/(4*3.14*3.14)))**(1/3))
plot(t,y)'''

show()




