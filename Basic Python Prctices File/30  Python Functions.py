# Python Simple Function................
# Simple Example ------------------ 1
def my_function1(x,y):
    print('\nOutput = ',x+y)
my_function1(10,20)






# Example-----------2
def my_function2():
    print('Example--- 2 = Hello !')
my_function2()






# Example ------------ 3 ..... akta argument er sathe akadhik Argument er jog...Type--1
print('\nExample ----- 3....Akta Argument er sathe Akadhik Argument er Jog--Type--1')
def my_function3(country):
    print(country + " " +'In Earth')
my_function3('India')
my_function3('America')
my_function3('Russia')
my_function3('Bangladesh')






# Example----4 ..... akta argument er sathe akadhik Argument er jog.....Type--2
print('\nExample--4....Akta Argument er sathe Akadhik Argument er Jog--Type--2')
def my_function4(address = 'Email'):
    print(address + " " +'Address')
my_function4('Home')
my_function4('Office')
my_function4()
my_function4('Personal')





# Example ------- 5
def my_function5(m,n):
    return (n*(n+m))-(m*n)
p=my_function5(2,4)
print('\nOutput5 = ',p)





# Example------6
def my_function6(s,p,a):
    fm = s+p+a
    print('\nOutput6 = ',fm)
my_function6(2,4,6)






# Example ------ 7
def my_function7(f,g):
    return f*g
fg=my_function7(2,1619)
print('\nOutput7 = ',fg)





# Example --------- 8
def my_function8(i,j):
    print('\nOutput8 = ',i**j)
my_function8(2,5)






# Function er Re-Use Benifit........................
print('\nFunction er Re-Use Benifit')
def my_function9(t,l,w):
    return t+l+w
result1 = my_function9(2,4,6)
print('Output1 = ',result1)

result2 = my_function9(4,6,8)
print('Output2 = ',result2)

result3 = my_function9(6,8,10)
print('Output3 = ',result3)






"""
 ------------------------------Non Keyword Argument-----------------------------------------
 Non Keyword Argument (*args) er age akta * sign Thake............ 
 Ai Argument er kaj holo jode argument theke value besi thake sei extra value nijer maje store kora......
"""


# Example -----------------1
print('\nNon Keyword argument..Example----1')
def my_func1(*args):
    return args
ab=my_func1(1,2,3,4)
print('Output = ',ab)




# Example -----------------2
print('\nNon Keyword Argument...Example----2')
def my_func2(*argss):
    output = 0
    for jk in argss:
        output = output + jk
    print('Output = ',output)
my_func2(1,2,3,4)





# Example -------------------- 3
print('\nNon Keyword Argument....Example----3')
def my_func3(nums,*argsss):
    output2 = 0
    FinalResult = 0
    for xcv in argsss:
        output2 = output2 + xcv
        FinalResult = output2 * nums
    print("Final Result = ",FinalResult)
my_func3(2,1,2,3,4)





# Example-------------------------4
print('\nExample-----------------4')
def my_func4(*history):
    for xy in history:
        print(xy)
my_func4('Asp','sm','sp','ab','pb')





# Example--------------------------5
print('\nExample---------------5')
def my_func5(num12,num13,*sum14):
    output11 = 0
    FinalR = 0
    for cvx in sum14:
        output11 = output11 + cvx
        FinalR = (num12 + (output11 * num12) - num13)
    print(FinalR)
my_func5(2,4,1,2,3,4)





# Example---------------------------6
print('\nExample------6....Item Theke akta item Select By index')
def my_func6(*kids):
    print("You Are My Life " + kids[2])
my_func6('Asp','Shampa','Shereyase')









"""
 ------------------------------Keyword Argument-----------------------------------------
 Keyword Argument (**args) er age akta ** sign Thake............ 
 Ai Argument er kaj holo Value er sathe key set kora,,Same as kicuta Dictionary Er Moto......
"""
print('\n------------------------------------------------------------------------------------------')

# Example-----------1
print('\n\nKeyword Argument ... Example----1')
def Func1(**argu):
    print(argu)
Func1(age = 24,Name = 'Prothes',Year = '2022')




# Example-----------2
print('\nKeyword Argument Key Print... Example----2')
def Func2(**argus):
    for dds in argus:
        print(dds)
    print()
Func2(Name = 'Asp',Year = 24,Gpa = 5.00)





# Example ------------------------- 3
print('\nPrint One Line Sentense Use keyword Argument')
def Func3(**kidss):
    print("My Favourite Color is " + kidss['Clr3'])
Func3(Clr0 = 'Red' , Clr1 = 'Blue' ,Clr2 = 'Green' ,Clr3 = 'Navy-Blue' ,Clr4 = 'Gold')





"""
---------------------------------------------Recursion Function--------------------------------------------
Recursion Function Holo Amn Function Ja nejei nejeke call korte pare....
r sei call infinite hobe jode na sei call na thamano hoy..........................
"""
print('\n-----------------------------------------------------------------------------------------------------')


# Example -------------------- 1
print('\nRecursion Function .... Example ----1')
def recursion(kks):
    if (kks > 0):
        result16 = kks + recursion(kks - 1)
        print(result16)
    else:
        result16 = 0
    return result16
print('Recursion Example Result')
recursion(5)









# Same As Again Print.................
print('\nPrivious Same as Again Print')
def recursion(cse):
    if (cse > 0):
        result19 = cse + recursion(cse-1)
        print(result19)
    else:
        result19 = 0
    return result19
recursion(7)









# Akta List K 5 Deye Gun kore onno akta list e rakte hole......
print('\nAkta List K 5 Deye Gun kore onno akta list e rakte hole......')
aspsm = []
aspsmsp = [1,2,3,4,5]
def My_FuNc(number):
    return number * 5
for ii in aspsmsp:
    aspsm.append(My_FuNc(ii))
print(aspsm)