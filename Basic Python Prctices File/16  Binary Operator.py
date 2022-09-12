# Binary Operator .......
# Binary Operator Use Hoy Tokhon Jokhon Binary Input Deye Binary Output Paoya Jay......
# 0b means - binary ja Digit er Agy bose..... binary Function--- bin()
# 0x means - Hexadecimal ja Digit er Agy bose..... Hexadecimal Function--- hex()
# 0o means - Octal ja Digit er Agy bose ..... Octal Function ---- oct()



# Binary Input Deye Binary Output
a = 0b00010101
b = 0b00001101
c = a & b
print("\nThe Binary Is = ",bin(c))



# HexaDecimal Input Deye HexaDecimal Output
x = 0xAA78
y = 0xBB78
z = x + y
print("The HexaDecimal Is = ",hex(z))



# Octal Input Deye Octal Output.........
o = 0o566
p = 0o763
q = o + p
print("The Octal Is = ",oct(q))



# Now Convert Decimal To Binary , Octal, Hexadecimal.........
D1 = 3
D2 = 3
D3 = D1 + D2
print("\nDecimal To Binary = ",bin(D3))
print("Decimal To Octal = ",oct(D3))
print("Decimal To Hexadecimal = ",hex(D3))




# Now Convert Binary To Binary , Octal, Hexadecimal.........
B1 = 0b110
B2 = 0b110
B3 = B1 + B2
print("\nBinary To Binary = ",bin(B3))
print("Binary To Octal = ",oct(B3))
print("Binary To Hexadecimal = ",hex(B3))



# Now Convert Octal To Binary , Octal, Hexadecimal.........
O1 = 0o5
O2 = 0o5
O3 = O1 + O2
print("\nOctal To Binary = ",bin(O3))
print("Octal To Octal = ",oct(O3))
print("Octal To Hexadecimal = ",hex(O3))



# Now Convert Hexadecimal To Binary , Octal, Hexadecimal.........
H1 = 0x8
H2 = 0x3
H3 = H1 + H2
print("\nHexadecimal To Binary = ",bin(H3))
print("Hexadecimal To Octal = ",oct(H3))
print("Hexadecimal To Hexadecimal = ",hex(H3))




# Now Complement Number.......
# Complement Mane Holo Kono Value ke Minus(-) Korar Pore J man Pabo Tar Sathe -1 Besi Add Kora...
# Jmn 12 er Complement Hobe -12-1 = -13........
# Example...........................................................................

AnyNumber = 12
Complement = ~ 12
print("\n\n12 Complement is =",Complement)
