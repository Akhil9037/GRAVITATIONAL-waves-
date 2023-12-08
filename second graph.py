from numpy import*
from math import*
from scipy.integrate import odeint
from matplotlib.pyplot import*
def h(t,r1,th,ph,ph1,ph2):

    
    a11=mu/(2*D)
    a1=(1-cos(2*th)*cos**2(ph(t))-3*cos(2*ph(t)))*r1**2(t)
    a2=(3+cos(2*th))*(2*cos(2*ph(t))*ph1(t)**2+sin(2*ph(t))*ph*2(t))*(r(t)**2)
    a3=4*(3+cos(2*th))*(sin(2*ph(t))*ph1(t)*r1(t))
    a4=(1-2*cos(2*th)*cos(ph(t))**2-3*cos(2*ph(t)))*r2(t)
    a5=r(t)
    A=a11*(a1+a2+a3+a4)*a5
    b1=(-2*mu*cos(th))/D
    b2=sin(2*ph(t))*r1(t)**2
    b3=(cos(2*ph(t))*ph2(t)-2*sin(2*ph(t))*ph2(t))*r(t)
    b4=(4*cos(2*ph(t))*ph1(t)*r1(t)+sin(2*ph(t))*r2(t))*r(t)
    B=b1*(b2+b3+b4)

    LO=(G*M*mu*a*(1-e**2))**(.5)

    L=LO/mu
    a=(pob**2(G*(m1+m2)/4*3.14**2))**(1/3)
    r=a*(1-e**2)/(1+e*cos(py))
    Vt=E*r**4/(r**2-2*r)
    ph1=L/Vt


    E=1+(Eo/mu)
    Eo=(-G*M*mu)/2*a
    ph1=(1-E**2)**(.5)/(Vt*(1-e))*(a*(1-e**2)-c0*(1-e)-e*a*(1-e**2)-e*c0*(1-e)*cos(ph))**(.5)*(a*(1-e**2)*(1+e**2))**(.5)
    ph=a/r
    c0=2/(1-E**2)-2*a
    
    return [A,B]

x=[3.14/4,.1]
G=6.6743*10**-11
mu=10*1.989*10**30
D=1000*3.086*10**25
t=arange(0,100,.10)
pob=0.3
m1=10
m2=10
sol=odeint(h,x,t)
y=sol[:,0]
y1=sol[:,1]
print(y,y1)
plot(t,sol[:,0])
plot(t,sol[:,1])
show()
