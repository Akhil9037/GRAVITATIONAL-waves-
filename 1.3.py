from numpy import*
from matplotlib.pyplot import*
def f(p,e):
    p1=(-192*3.14/(5*c**5))*(2*3.14*G/p)**(5/3)*(m1*m2/(m1+m2)**(1/3))*(1+(73/24)*e**2+(37/96)*e**4)*(1-e**2)**(-7/2)
    return p1

def g(p,e):
    e1=(-608*3.14/(15*(c**5)))
    e2=e/p
    e3=(2*3.14*G/(p))**(5/3)
    e4=m1*m2/((m1+m2)**(1/3))
    e5=(1+((121/304)*e**2))/((1-e**2)**(5/2))
    e7=e1*e2*e3*e4*e5

    #e1=(-608*3.14*e/(15*c**5*p))*(m1*m2/(m1+m2)**(1/3))*(1+(121/304)*e**2)*(1-e**2)**(-5/2)
    return e7

plist=[]
elist=[]
tlist=[]
m1=10*1.989*10**30
m2=10*1.989*10**30
c=3*10**8
G=6.6743*10**-11
e=0.1
p=0.1
t=0.00
h=.10
tlist.append(t)
elist.append(e)
plist.append(p)

#while(e<1.0):
while (t<=100):
    e=e+h*f(p,e)
    p=p+h*f(p,e)
    t=t+h
    tlist.append(t)
    elist.append(e)
    plist.append(p)
       

figure(1)
plot (tlist,plist)

grid("true")
xlabel("time period")
xlim(0,7)
ylim(0.00,.10)
ylabel("orbital period")
#show()
#figure(2)
#plot(tlist,elist)
xlim(0,7)
ylim(0.00,.10)   
show()
