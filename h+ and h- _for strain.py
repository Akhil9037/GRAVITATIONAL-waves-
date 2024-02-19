from numpy import*
from math import*
from scipy.integrate import odeint
from matplotlib.pyplot import*
def h(t,r1,th,ph,ph1,ph2):

    
    a11=mu/(2*D)
    a1=(1-cos(2*th)*cos**2(ph(t))-3*cos(2*ph(t)))*r1(t)**2
    a2=(3+cos(2*th))*(2*cos(2*ph(t))*ph1(t)**2+sin(2*ph(t))*ph2(t))*(r(t)**2)                           # a11*a1*a2*a3*a4*a5= eqn 7 in miller pdf for plus polarization 
    a3=4*(3+cos(2*th))*(sin(2*ph(t))*ph1(t)*r1(t))
    a4=(1-2*cos(2*th)*cos(ph(t))**2-3*cos(2*ph(t)))*r2(t)
    a5=r(t)
    A=a11*(a1+a2+a3+a4)*a5

    
    b1=(-2*mu*cos(th))/D
    b2=sin(2*ph(t))*r1(t)**2
    b3=(cos(2*ph(t))*ph2(t)-2*sin(2*ph(t))*ph2(t))*r(t)
    b4=(4*cos(2*ph(t))*ph1(t)*r1(t)+sin(2*ph(t))*r2(t))*r(t)                                            #b1*b2*b3*b4= eqn 8 in miller pdf for cross polarization
    
    B=b1*(b2+b3+b4)                                                                                     # Lo=eqn 10 in miller pdf    angular momntum       ,     a=eqn 5 in miller pdf semi major axis 

    LO=(G*M*mu*a*(1-e**2))**(.5)                                                                        # r=eqn 12 in miller pdf distance between BBh's    ,     

    L=LO/mu
    a=(pob**2(G*(m1+m2)/4*3.14**2))**(1/3)                    #Vt= potential eqn 15  in miller pdf ,  phi= eqn 16 in miller pdf   , co=eqn 14 in miller pdf    ,  E and L =eqn 11 in miller pdf
    r=a*(1-e**2)/(1+e*cos(py))
    Vt=E*r**4/(r**2-2*r)                                     # mu reduced mass ,  m1 =m2 = solar mass , G= the gra.const c= light spped  ,    Eo=eqn 9S in miller pdf
    ph1=L/Vt


    E=1+(Eo/mu)
    Eo=(-G*M*mu)/2*a
    ph1=(1-E**2)**(.5)/(Vt*(1-e))*(a*(1-e**2)-c0*(1-e)-e*a*(1-e**2)-e*c0*(1-e)*cos(ph))**(.5)*(a*(1-e**2)*(1+e**2))**(.5)
    ph=a/r
    c0=2/(1-E**2)-2*a
    Vt=(E*r**4)/((r**2)-2*r)
    return [A,B]

x=[3.14/4,.1]
G=6.6743*10**-11
mu=10*1.989*10**30
D=1000*3.086*10**25
Eo=10
th=arange(0.0,180)
ph=arange(0.0,180)
ph2=arange(0.0,180)
t=arange(0,100,.10)
E=1+(Eo/mu)
pob=0.3
a=0.3
m1=10
m2=10
Eo=10
M=(mu)
po=.1
r=0.3
c0=.3
ph=a/r
#c0=(2/(1-E**2))-2*a
#=(a(1-e**2))/(1+e*cos(ph))
E=1+((-G*M*mu/2*a))/mu
a=.3
Vt=(E*r**4)/((r**2)-2*r)
#a=((.3)**2(G(m1+m2)/4*3.14*3.14))**(1/3)
E=1+(Eo/mu)
Eo=(-G*M*mu)/2*a
ph1=(1-E**2)**(.5)/(Vt*(1-e))*(a*(1-e**2)-c0*(1-e)-e*a*(1-e**2)-e*c0*(1-e)*cos(ph))**(.5)*(a*(1-e**2)*(1+e**2))**(.5)
ph=a/r
#c0=2/(1-E**2)-2*a
sol=odeint(h,t,th,ph,ph1,ph2)
y=sol[:,0]
y1=sol[:,1]
print(y,y1)
plot(t,sol[:,0])
plot(t,sol[:,1])
show()
