'''
a=9
b=6
c=0
def add():
    pass

def sub(a,b):
    c=a-b
    print(c,a)
sub(12,3);
'''
#function arguments
'''
1]default arguments
2]keyword arguments
3] variable length arguments
4] required  arguments
'''
#default arguments
def product(r=9,s=3):
    t=r*s
    print(t)
#product(); this is also right
product(6,3);
product(s=9);
product(6)
#keyword arguments
def product(r,s,u,t):
    v=r*s*u*t
    print(v)
product(8,9,7,6); #this is also right
product(s=8,r=7,t=9,u=3);
#required arguments
def product(r,s,u,t):
    v=0
    v=r*s*u*t
    print(v)
product(8,9,7,6); #this is also right
#variable length arguments
def avg(*numbers): #gets converted into tuple
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print(sum/len(numbers))
avg(9,4,2,3,5)

def NAME(**name): #gets converted into dictionary
    print(type(name))
    print("HELLO,",name["fname"],name["mname"],name["sname"])
NAME(fname='KUMUD',mname='MOHAN',sname='ZIMAL');


