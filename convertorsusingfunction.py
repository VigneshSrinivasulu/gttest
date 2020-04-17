def temp(c):
    f = (9/5)*c + 32
    print f

def hours(m,s):
    h = m/60 + s/3600
    print h

c = input("enter the temperature in celsius")
c = int(c)
temp(c)

m = input("please enter the minute value")
m = int(m)
s = input("enter the seconds")
s = int(s)
hours(m,s)
