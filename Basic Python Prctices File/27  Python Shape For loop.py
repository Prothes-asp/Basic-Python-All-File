# Design Pattern Square............
print('\nDesign Pattern Square Print')
for a in range(4):
    for b in range(4):
        print('#',end=' ')
    print()


# Triangle Create ...........Pattern--1
print('\nTriangle Generate--1')
n=5
for c in range(n):
    for d in range(c+1):
        print('#',end=' ')
    print()


# Triangle Create ...........Pattern--2
print('\nTriangle Generate--2')
for e in range(4):
    print((e+1)*'# ')


# Vartical Triangle Generate...............1
print('\nVertical Triangle Generate----1')
for f in range(5):
    for g in range(5-f):
        print('#',end=' ')
    print()


# Vartical Triangle Generate...............2
print('\nVertical Triangle Generate----2')
for h in range(4):
    print((4-h)*'# ')


# 1,3,5,7 avabe Shape Create Korte Hole............
print('\n1,3,5,7 avabe Shape Create Korte Hole............')
for i in range(4):
    print((2*(i+1)-1)*'# ')


# Triangle Sequence Number Print........................1
print('\nTriangle Sequence Number Print--------1')
def contnum(n):
    num = 1
    for j in range(0,n):
        for k in range(0,j+1):
            print(num,end=' ')
            num = num + 1
        print()
n = 4
contnum(n)



# Triangle Sequence Number Print........................2
print('\nTriangle Sequence Number Print--------2')
num1 = 1
for l in range(0,4):
    for m in range(0,l+1):
        print(num1,end=' ')
        num1 = num1 + 1
    print()



# Triangle Sequence Number Print........................3
print('\nTriangle Sequence Number Print odd--------3')
num2 = 1
for n in range(0,4):
    for o in range(0,n+1):
        print(num2,end=' ')
        num2 = num2+2
    print()




# Triangle Sequence Letter Print.....................
print('\nTriangle Sequence Number Print')
def contalpha(n):
    numbr = 65
    for p in range(0,n):
        for s in range(0,p+1):
            ch = chr(numbr)
            print(ch,end=' ')
            numbr = numbr + 1
        print()
n = 7
contalpha(n)



# Dymond Up Shape....................
print('\nDymond Up Shape')
q = 5
for r in range(q):
    for t in range(r+1):
        print(' ',end=' ')
    for t in range(r,q-1):
        print('#',end=' ')
    for t in range(r,q):
        print("#",end=' ')
    print()




# Dymond Down Shape....................
print('\nDymond Down Shape')
q = 5
for r in range(q):
    for t in range(r,q):
        print(' ',end=' ')
    for t in range(r):
        print('#',end=' ')
    for t in range(r+1):
        print("#",end=' ')
    print()




# Dymond Shape Create ................
print('\nDymond Shape Create')
q = 5
for r in range(q):
    for t in range(r,q):
        print(' ',end=' ')
    for t in range(r):
        print('#',end=' ')
    for t in range(r+1):
        print("#",end=' ')
    print()
for r in range(q):
    for t in range(r + 1):
        print(' ', end=' ')
    for t in range(r, q - 1):
        print('#', end=' ')
    for t in range(r, q):
        print("#", end=' ')
    print()



# Create Reverse Break Dymond Shape
print('\nCreate Reverse Break Dymond Shape')
q = 5
for r in range(q):
    for t in range(r+1):
        print(' ',end=' ')
    for t in range(r,q-1):
        print('#',end=' ')
    for t in range(r,q):
        print("#",end=' ')
    print()
for r in range(q):
    for t in range(r,q):
        print(' ',end=' ')
    for t in range(r):
        print('#',end=' ')
    for t in range(r+1):
        print("#",end=' ')
    print()





# Double Up Shape
print('\nDouble Up shape')
print('\n')
q = 5
for r in range(q):
    for t in range(r+1):
        print(' ',end=' ')
    for t in range(r,q-1):
        print('#',end=' ')
    for t in range(r,q):
        print("#",end=' ')
    print()
q = 5
for r in range(q):
    for t in range(r+1):
        print(' ',end=' ')
    for t in range(r,q-1):
        print('#',end=' ')
    for t in range(r,q):
        print("#",end=' ')
    print()





print('\n')
# Dymond Up and Up Dymond Shape
print('\nDymond Up and Up Dymond Shape')
q = 5
for r in range(q):
    for t in range(r+1):
        print(' ',end=' ')
    for t in range(r,q-1):
        print('#',end=' ')
    for t in range(r,q):
        print("#",end=' ')
    print()
for r in range(q):
    for t in range(r,q):
        print(' ',end=' ')
    for t in range(r):
        print('#',end=' ')
    for t in range(r+1):
        print("#",end=' ')
    print()
for r in range(q):
    for t in range(r + 1):
        print(' ', end=' ')
    for t in range(r, q - 1):
        print('#', end=' ')
    for t in range(r, q):
        print("#", end=' ')
    print()
for r in range(q):
    for t in range(r,q):
        print(' ',end=' ')
    for t in range(r):
        print('#',end=' ')
    for t in range(r+1):
        print("#",end=' ')
    print()
for r in range(q):
    for t in range(r+1):
        print(' ',end=' ')
    for t in range(r,q-1):
        print('#',end=' ')
    for t in range(r,q):
        print("#",end=' ')
    print()
for r in range(q):
    for t in range(r,q):
        print(' ',end=' ')
    for t in range(r):
        print('#',end=' ')
    for t in range(r+1):
        print("#",end=' ')
    print()