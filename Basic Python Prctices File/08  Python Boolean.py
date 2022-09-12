# Python Boolean........................
a = 10
b = 20.99
c = 10
d = ["Apple","Banana","Stawvary"]
e = None
f = False
g = 0
h = ""
i = "abc"
j = ()
k = {}
l = []

print("\na = ",bool(a))
print("\nb = ",bool(b))
print("\nc = ",bool(c))
print("\nd = ",bool(d))
print("\ne = ",bool(e))
print("\nf = ",bool(f))
print("\ng = ",bool(g))
print("\nh = ",bool(h))
print("\ni = ",bool(i))
print("\nj = ",bool(j))
print("\nk = ",bool(k))
print("\nl = ",bool(l))



# Check Boolean Use Function......................
def myfunction():
    return True
print("\nFunction = ",myfunction())



# Again Check...............................................................................
# When Return True Then Output True
print("\nWhen Return True Then Output True")
def Myfunction():
    return True
if Myfunction():
    print("yes")
else:
    print("no")



# Again Check...............................................................................
# When Return False Then Output False
print("\nWhen Return False Then Output False")
def Myfunction():
    return False
if Myfunction():
    print("yes")
else:
    print("no")