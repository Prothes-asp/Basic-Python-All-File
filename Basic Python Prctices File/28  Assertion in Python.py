"""
Firstly Asert Syntax.....
assert <condition>, "message"


Explain Assertion : akjon manuser salary positive number e hoy ta kono somoy negative number e hoy ne but user jode
kokhono negative value dey tobe ta bole debe je ata  right noy . ai assertion assert keyword use kore asob kora hoy.
"""


#Exammple----------------1 [Ata Error Asbe Na ..karon akhane assert keyword use kora hoy ni]
print('\nExample------------------1')
def my_func(salary):
    print("My Salary is",salary)
my_func(-2000)



print('\n')


# Example-----------2 [Use assert Keyword][akhane negative value dele error asbe.....]
salary1 = int(input("Enter Salary = "))
def my_function(salary1):
    assert salary1 > 0,"Negative Value Not Allow Please Input Positive Value"
    print("My salary is = ",salary1)
my_function(salary1)




# Assertion error Handeling.......................
print('\nAssertion error handling.............')
salary2 = int(input("Enter Salary = "))
try:
    def My_functions(salary2):
        assert salary2 > 0 ,'Negative value Not allow plz input positive value'
        print('My Salary = ', salary2)
    My_functions(salary2)
except Exception:
    print('Negative Salary Not Possiable Calculate')


