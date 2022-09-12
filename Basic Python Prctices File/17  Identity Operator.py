# Identity Operator..........................
# Identity Operator Mainly Two Types....
# 1. is
# 2. is not
# is er ulta holo is not

# Example.....................................1
a = 10
b = 5
c = a is b
d = a is not b
print("\n C = a is b =",c)
print(" D = a is not b =",d)



# Example......................................2
x = int(input("\nEnter Integer Input Here = "))
y = int(input("Enter Integer Input Here = "))
if x is y:
    print("Matching")
elif x is not y:
    print("Not Match")