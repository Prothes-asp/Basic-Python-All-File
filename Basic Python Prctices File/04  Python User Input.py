# Python Simple User Input Here.............................
# Sudu Input Function deye input nele seta string hoye jay......
# Se jonno amader Input function er purbe data type function use korte hobe.... Example :-------

print("\nPython Simple User Input Here........ Type--1")
a = input("Enter Any Number = ")
b = input("Enter Any Name = ")
print(a)
print(b)


print("\nPython Simple User Input Here........ Type--2")
c = input("Enter Any Number = ")
d = input("Enter Any Number = ")
e = input("Enter Any Name = ")
f = c + d
g = c+d+e
print(f)
print(g)



# Use Data Type Function With Input Function ............

h = int(input("Enter Ineger Number = "))
i = float(input("Enter FLoat Number = "))
j = str(input("Enter String Here = "))
k = h + i
l = k,j
print(k)
print(l)




# aksathe akadhik input Grohon ..... Example   1 2 3 4 5 = 15
data_store = input("\nInput Many Data Example (1 2 3 4 5...) = ").split()
a,b,c,d,e = data_store
Sum = int(a) + int(b) + int(c) + int(d) + int(e)
print('Sum = ',Sum)