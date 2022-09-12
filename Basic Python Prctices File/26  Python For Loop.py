# For loop...................

print("\nPrint All Item")
a = [1,2,3,4,'asp',5.00]
for x in a:
    print(x)



# List er jogfol ber korte hole........................
print("\nList er Jogfol Ber Korte.....")
b = [1,2,3,4,5,6]
total = 0
for y in b:
    total = total+y
print('Total =',total)



# Akta Word er alada alada letter print...............
print('\nAkta Word er alada alada letter print Korte')
c = 'kutta'
for k in c:
    print(k)



# For Loop In Break Statement.............
print('\nFor Loop In Break Statement.............')
d = ['DDL','DML','DCL','DTL']
for dd in d:
    print(dd)
    if dd == 'DCL':
        break


# For Loop In Continue State-ment...................
print('\nFor loop in Continue Statement')
e = ['Eat','Ate','Eatten','Ethernet']
for ee in e:
    if ee == 'Ate':
        continue
    print(ee)



# Python range() Method Use.......................
# Range e joto projonto daoya hobe tar theke 1 kom hobe......
print('\n0 theke 9 Projonto Print')
for r in range(10):
    print(r)



# 5 theke 10 projonto print
# Akhane 1st value holo koto theke suru hobe r last value holo kothay ses hobe tar theke 1 kom
print('\n5 theke 10 projonto print')
for rr in range(5,11):
    print(rr)



# 2 ghor gap deye 4 theke 16 projonto print.....
# Akhane 1st value holo koto theke suru hobe r Middle value holo kothay ses hobe tar theke 1 kom
# r last value holo koto kore gap hobe,,,,,,
print('\n2 ghor gap deye print')
for rrr in range(4,17,2):
    print(rrr)


# 5 Bar name print korte for loop
print('\n5 Bar Name Print Korte For Loop')
for Name in range(5):
    print('Asp')


# 1 theke 100 projonto jog korte...........
print('\n1 theke 100 projonto print')
Total = 0
for Jog in range(101):
    Total =Total + Jog
print(Total)



# 50 Theke 100 Projonto Jog Korte.........
print('\n50 Theke 100 Projonto Jog Korte.........')
Total1 = 0
for Jog1 in range(50,101):
    Total1 = Total1 + Jog1
print(Total1)



# Dhara Jog Nirnoy 2+4+6+8+.........+20
print('\n2 Ghor Gap Deye Deye Dhara Jog Nirnoy')
Total2 = 0
for Jog2 in range(2,21,2):
    Total2 = Total2 + Jog2
print(Total2)



# 1 theke 20 projonto 2 Dara vag jay amn number gulur jog fol.......
print('\n1 theke 20 projonto 2 Dara vag jay amn number gulur jog fol.......')
Total3 = 0
for Jog3 in range(1,21):
    if (Jog3 % 2 == 0):
        Total3 = Total3+Jog3
print(Total3)



# Loop er sathe else use.................
# Jokhon Loop Ses Hobe Tokhon Else Print Hobe.............
print('\nLoop Ses Hole else er print')
elements = ['Love','Loves','Loved']
for element in elements:
    print(element)
else:
    print('Closed----All Items Printed')



# Nested For Loop...................
# Nested Looper kaj holo 1st loop er element er akta item er sathe next loop er all item
# avabe 1st loop er all item gulu next loop er sthe hobe avabe joto nested loop thakuk avabe kaj hobe.....
print('\nNested For Loop')
Nested1 = [1,2,3,4]
Nested2 = [1,2,3,4]
for N in Nested1:
    for NN in Nested2:
        print(N,NN)
