# Python If - Else Condition...................

# Simply If - else......................
a = 20
b = 50
if a<b:
    print("\nA is Small")
else:
    print("\nA is Big")



# Double Condition And Nested elif, If Else...................
c = 50
d = 10
e = 20
if c < e and d < e:
    print("\nE is Big Value")
elif d < c and e < c:
    print("\nC is Big Value")
elif c < d and e < d:
    print("\nD is Big Value")



# One line Print If Condition And Print.......................
f = 20
g = 25
if f < g : print("\nOne Line Print True")



# One line Print If Else Condition And Print.......................
h = 50
i = 70
j = 40
print("\nYes") if h<i and i<j  else print("\nNo")



# Nested If And Else ............... Use
k = 40
l = 20
m = 50
n = 10
if k>l and k>m:
    if k > n:
        print("\nK is Big Value")
    else:
        print("\nN is Big value")
elif l>k and l>m:
    if l > n:
        print("\nL is Big value")
    else:
        print("\nN is Big Value")
elif m > k and m > l:
    if m > n:
        print("\nM is Big Value")
    else:
        print("\nN is Big Value")
else:
    print("\nN is Big Value")




# Marks Grade Ber Kora If Else And elif Deye.................
marks = int(input("\nEnter Marks Input Here = "))
if marks >= 90:
    print("The Result is Golden A+")
elif marks >= 80:
    print("The Result is A+")
elif marks >= 70:
    print("The Result is A")
elif marks >= 60:
    print("The Result is A-")
elif marks >= 50:
    print("The Result is B")
elif marks >= 40:
    print("The Result is C")
elif marks >= 33:
    print("The Result is D")
else:
    print("You Are Failed")