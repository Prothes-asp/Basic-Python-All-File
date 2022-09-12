"""
kono akta itterable objects / suppose any list theke condition use kore some value khuje ber korai
holo filter() Function er kaj
"""

# akta list theke adult person gulo dekhar jonno
print('\nAkta list theke adult person gulo dekhar jonno')
num = [10,17,19,14,18,22,23,13]
def my_function(x):
  if x >= 18:
    return True
  else:
    return False
Adult = list(filter(my_function,num))
for i in Adult:
  print('Adult Age = ',i)







# Akta List er Item 3 theke boro ta dekha
print('\nAkta List er Item 3 theke boro ta dekha')
num1 = [1,2,3,4,5,6]
def my_func1(x1):
  if x1 > 3:
    return True
  else:
    return False
output = list(filter(my_func1,num1))
print('Output = ',output)





# Lambda Function Use Kore List Theke Even Number Ber Kora
print('\nLambda Function Use Kore List Theke Even Number Ber Kora')
num2 = [1,2,3,4,5,6,7,8,9,10]
Even = list(filter(lambda n : n%2==0,num2))
print('Even',Even)





# Lambda Use kore Filter function deye odd Number ber kora................
print('\nLambda Use kore Filter function deye odd Number ber kora')
Nums11 = [1,2,3,4,5,6,7,8,9]
Odd = list(filter(lambda n1 : n1%2,Nums11))
print('Odd',Odd)






# 50 Theke Boro Amn Number Gulor Jog Fol Ber Koro.................
print('\n50 Theke Boro Amn Number Gulor Jog Fol Ber Koro.................')
bigAddition = [10,20,30,40,50,60,70,80,90,100]
bigTotal = 0
def bigFunction(bigADD):
  if 50 < bigADD:
    return True
  else:
    return False
bigFuncAdd = list(filter(bigFunction,bigAddition))
for bigOutput in bigFuncAdd:
  bigTotal = bigTotal + bigOutput
print('Output = ',bigTotal)

