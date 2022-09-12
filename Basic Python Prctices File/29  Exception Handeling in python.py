# Exception Handaling are mainly 3 types...
"""
    1. Compilar  time Error / [Syntax Error]
    2. Logical Error / [Calculation Error]
    3. Run Time error / [User Input Error]
"""

# Jode kono Number K Zero Deye Devided Kora Hoy Ta error ase....
# But seta Jode User K bole Daoya Jay Tobe R error hbe na....Se jonno.....
# Example -------------1
# Ai example e except Exception command use kora hoyece except Exception command deye over all sob error k Bujay...
# Ai Command Multiple Exception e Use hoy.................
a = 5000
b = int(input('\nInput int Data 2nd = '))
try:
    c = a / b
    print('Example--1 = ',c)
except Exception:
    print('Example---1...Please Cannot Devided By Zero ! Input 0 < any int number')





# Example -------------2
d = 10000
try:
    e = d / b
    print('\nExample--2 = ',e)
except ZeroDivisionError:
    print('\nExample---2...Please Cannot Devided By Zero ! Input 0 < any int number')





# Error Handaling e Resource Open and close............
# Example-----------3
f = 2000
try:
    print('\nResource Open')
    g = f / b
    print('Example--3 = ',g)
except Exception as asp:
    print('Example---3...Please Cannot Devided By Zero ! Input 0 < any int number')
finally:
    print('Resource Closed')




# Specifiq Vabe Jode Kono Error Bole Daoya Hoy....... Se--jonnno
# Example-------------------4
h = 88000
try:
    print('\nResource Open')
    i = h / b
    print('Example--4 = ',i)
    s = int(input('Only Integer Number = '))
    p = s * s
    print("S*S = ",p)
except ZeroDivisionError:
    print('Example---4...Please Cannot Devided By Zero ! Input 0 < any int number')
except ValueError:
    print('Please Type Only Integer Number,Example :- 1,2,3,4,5........')
finally:
    print('Resource CLosed')




# Example--------------5 [Value Error]
try:
    print('\nResource Open')
    sp = int(input('Please Only Integer Number Here = '))
    Asp = ((sp * sp)-sp)
    print('Example -- 5 = ',Asp)
except ValueError:
    print('Please Type Only Integer Number,Example :- 1,2,3,4,5........')
finally:
    print('Resource Closed')