# Bitwise Operator.....................................................
"""
Bitwise Operator Fiesrtly All Input Number ke Binary te Convert kore then Binary jog beyog vag complement etc
kore again Dashomik e Convert kore Output Day...
"""

"""
Sign Details.....................
      ~ = Complement -> 12 er complement holo -12-1 = -13
      & = And -> er kaj holo Input number ke binary kore gun kora , dui ta 1 holei 1 noy 0
      | = Or -> er kaj holo Input number ke binary kore jog kora , akta ta 1 holei 1 noy 0
      ^ = Xor -> er kaj holo Input number ke binary kore , same hole 0 noy 1
      << = Left-shift -> Left Dik sore Jaoya
      >> = Right-shift -> Right Dik Sore Jaoya....
"""

a = 10
b = 5
c = ~ a
d = a & b
e = a | b
f = a ^ b
g = a << b
h = a >> b
print("\nA value er Complement ~ a =",c)
print("a & b =",d)
print("a | b =",e)
print("a ^ b =",f)
print("a << b =",g)
print("a >> b =",h)

