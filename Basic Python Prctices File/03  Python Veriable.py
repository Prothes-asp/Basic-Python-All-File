# Simply Print Veriable in Python
print("\nSimply Print Veriable in Python")
s = "SM"
p = "PB"
sp = 1916
print(s)
print(p)
print(sp)


# Use Data-Type Function In python....
print("\nUse Data-Type Function In python....")
a = str(3)
b = int(3)
c = float(3)
print(a)
print(b)
print(c)


# Python Veriable Print In One Line
print("\nPython Veriable Print In One Line")
x = 23
y = "44"
z = "Asp"
print(x,y,z)


# Multiple Variable Assign In Python.........
print("\nMultiple Variable Assign In Python---type 1")
m1,m2,m3 = 19,"SP",16
print(m1)
print(m1,m2)
print(m1,m2,m3)

print("\nMultiple Variable Assign In Python---type 2")
m4 = {"Asp","Sm","Sp"}
s1,s2,s3 = m4
print(s1)
print(s2)
print(s3)

print("\nMultiple Variable Assign In Python---type 3")
p1 = p2 = p3 = "Asp"
print(p1)
print(p2)
print(p3)


# Ouput Variables
print("\nOuput Variables in python...............")

x1 = "Awesome"
print(" Python is " + x1)

Name = "Asp Prothes"
Age = 24
Year = 2020
print(" My name is " + Name + "." + " I am " , Age , " years old." + " In " , Year)



# Global Veriable  in Python.........................
print("\nGlobal Veriable  in Python")

print("\nGlobal Veriable  in Python.....type...1")
g1 = "Awesome"
def my_function():
    print("Python is " + g1)
my_function()


print("\nGlobal Veriable  in Python.....type..2")
g2 = "Awesome"
def my_function1():
    g2 = "Fantastic"
    print("Python is " + g2)
my_function1()
print("Python is " + g2)


print("\nGlobal Veriable  in Python.....type..3")
def my_func():
    global gl
    gl = "Awesome"
    print("Python is " + gl)
my_func()
print("Python is "+ gl)