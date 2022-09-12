"""
Python e Map() Function Onk Power full FUnctions....Ai Functions nejer Perameter Hisabe
Onno arekta Function() K Nete Pare...and sathe onno arekta ittareable Object k nete pare....
"""

# Map Function Dekhar age Akta Simple Function Dekha Jak................
# Example Simple Function With out map()
print('\nExample Simple Function With out map()')
asp1 = []
asp2 = [1,2,3,4,5,6,7,8,9,10]
def my_func(argument):
    return argument * 5
for i in asp2:
    asp1.append(my_func(i))
print('asp =',asp1)







# Now We Show map()  Functions....1
print('\n\n---------------------------------------------------------------------------------------------------')
print('Now We Show map()  Functions')
print('---------------------------------------------------------------------------------------------------')
asp3 = [1,2,3,4,5,6,7,8,9,10]
def my_func1(nums):
    return nums * 5
output = list(map(my_func1,asp3))
print('asp3 = ',output)






# Example ----- 2
asp4 = [2,4,6,8,10]
def my_func11(nums11):
    return nums11 * 10
output1 = list(map(my_func11,asp4))
print('asp4 = ',output1)






# Example------------------3
asp5 = ['A','P','S']
asp6 = ['B','B','M']
def my_func12(a,b):
    return a + b
output2 = list(map(my_func12,asp5,asp6))
print('asp5 = ',output2)