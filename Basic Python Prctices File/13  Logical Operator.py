# Logical Operator...................................................

a = 20
b = 10
c = 50

d  = a<c and a>b
print("\n d = ",d)
e = c==50 or c<=100
print(" e = ",e)
f = not(c < 100 and b<c)
print(" f = ",f)



# Use if Else And Check Logical Operator.......

x = 100
y = 200
z = 300
if x>y and x > z:
    print(" The X is Large")
elif y > x and y > z:
    print(" The Y is Large")
elif not(x==y or y==z and z>y>x):
    print(" Z is large")
else:
    print(" In Condition Wrong")