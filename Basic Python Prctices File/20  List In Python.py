# List Always [] Third Bracket er maje lekha hoy..............
"""
List Holo Single veriable er maje Multiple Value / element Store Korte Help Kore............
List er Syntax...............
                My_List = [element1,element2,element3]
                My_List = []-----This is empty List
i.e. List e kicu na thakle sei list k bola hoy empty list.....
"""

# Example.........1
My_List1 = []
My_List2 = [1,2,True,3.50,"Asp"]
My_List3 = [1,2,True,[2,True,3.50,"Asp"],3.50,"Asp"]
print("\nEmpty List =",My_List1)
print("Simple List =",My_List2)
print("Nested List =",My_List3)



# List er Kono akta Item ke Single vabe Print Kore hole Indexing Use Kora Hoy...
# Positive Index Use Kore First Theke Print Kora Hoy
My_List4 = [1,2,True,3.50,"Asp"]
print("\nSingle Item Print Use Positive Indexing =",My_List4[4])



# List er Kono akta Item ke Single vabe Print Kore hole Indexing Use Kora Hoy...
# Negative Index Use Kore Last Theke Print Kora Hoy
My_List5 = [1,2,True,3.50,"Asp"]
print("Single Item Print Use Negative Indexing =",My_List5[-4])



# List er First 2 Number theke 5 Number Projonto item Print Korte hole Indexing Use Kora Hoy...
# Positive Index Use Kore
List1 = [1,2,True,3.50,"Asp","sm"]
print("List er index 2 theke 5 Projonto item print =",List1[2:6])
print("List er Prothom 3 ta bad deye baki gulo print =",List1[3:])
print("List er Last 3 ta bad deye baki gulo print =",List1[:3])




# Dui Ta List Jog Kora Simple Method............../Join List
My_List6 = [1,2,True,3.50,"Asp"]
My_List7 = [1,2,True,3.50,"Asp"]
My_List8 = My_List6 + My_List7
My_List9 = My_List8 + [2,True,3.50,"Asp"]
print("\nList Addition 2 Ta =",My_List8)
print("List Addition 3 Ta =",My_List9)


# List e Item Add Korar Jonno
# Added List Item
# Dui Ta List Jog Kora extend() Method..............Sathe sets Tuple Dict o add kora jay.....
My_List10 = [2,True,3.50,"Asp"]
My_List11 = (3,True,3.50,"Asp")
My_List12 = [1,True,3.50,"Asp"]
My_List10.extend(My_List11)
print("The Addition List Extend Method..... = ",My_List10)
My_List10.extend(My_List12)
print("The Addition List Extend Method..... = ",My_List10)



# List e Only akta item add korte hole.....without index sara bosbe.........append() method
My_List13 = [1,True,3.50,"Asp"]
My_List13.append("Sm")
print("Add One Item Use Append Method = ",My_List13)



# List e Only akta item add korte hole.....with index neye bosbe.........insert() method
# Akhane Positive / Negative Index Use Hobe...
My_List14 = [1,True,3.50,"Asp"]
My_List14.insert(0,"Sm")
print("Add One Item Use insert Method = ",My_List14)




# List e Item Change Korar Jonno
# Change List Item
# Simply List er akta item k change korar jonno.............with index
My_List15 = [1,True,5.00,"Asp"]
My_List15[0] = "Sm"
print("\nChange One Item = ",My_List15)




# List e dui ta position e item Change Two item jonno............with index
My_List16 = [1,True,"Sm",5.00,"Asp"]
My_List16[1:3] = ["Sp","Ps"]
print("Change Two item = ",My_List16)



# insert Method Deye item Add Kora.......................... insert()
My_List17 = [1,True,"Sm",5.00,"Asp"]
My_List17.insert(1,"Python")
print("Insert Method Deye Change item = ",My_List17)




# List e Item Remove Korar Jonno
# Remove List Item
# List er maje item call kore remove() method deye Item Remove kora................
My_List18 = ["apple", "banana", "cherry"]
My_List18.remove("cherry")
print("\nRemove Item = ",My_List18)




# List er maje item call na kore index use kore pop() method deye Item Remove kora.......
My_List19 = ["Sp","Ps",1,True,"Sm",5.00]
My_List19.pop(2)
print("Remove Item with index = ",My_List19)



# del keyword deye list er item index use kore delete kora.............
My_List20 = ["Sp","Ps",1,True,"Sm",5.00]
del My_List20[3]
print("Del key word deye item remove = ",My_List20)



# Akta List er All Item Clear Korte Hole clear() method use kora hoy............
My_List21 = ["Sp","Ps",1,True,"Sm",5.00]
My_List21.clear()
print("Remove All Item In list = ",My_List21)




# Loop In List...
# List e loop use kora///////
My_List22 = ["Sp",1,True,"Sm",5.00]
print("\nThe Loop Item Print = ")
for i in My_List22:
    print(i)



# Loop er Maje Length Dekhar Jonno len() method Use kora hoy........
My_List23 = ["Sp",1,True,"Sm",5.00]
Length = len(My_List23)
print("\nList Length = ",Length)




# List Comprehension...................
""" 
List comprehension offers a shorter syntax when you want to create a new
list based on the values of an existing list.
"""
My_List24 = ["apple","banana","orange","chili","kiwi"]
New_List = []
for i in My_List24:
    if "a" in i:
        New_List.append(i)
print("\na je sob item e ase se gulu print = ",New_List)


# Type ------------------ 2
My_List25 = ["apple","banana","orange","chili","kiwi"]
New_List1 = [x for x in My_List25 if "i" in x]
print("Type------2 = ",New_List1)



# Sorted List.............
# Alphabet Sort korar jonno........sort() method use kora hoy......
My_List26 = ["z","s","p","m","b","a"]
My_List27 = [9,8,6,7,5,4,2,3,0,1]
My_List28 = ["a","l","b","s","p","m","d"]
My_List29 = [1,3,5,2,6,8,7,9,0,4]
My_List26.sort()
My_List27.sort()
My_List28.sort(reverse=True)
My_List29.sort(reverse=True)
print("\nSorted Alphabet Assending order = ",My_List26)
print("Sorted Number Assending Order = ",My_List27)
print("Sorted Alphabet Dessending order = ",My_List28)
print("Sorted Number Dessending Order = ",My_List29)



# Sorted Lower Case And Upper Case ...............
My_List30 = ["banana", "Orange", "Kiwi", "cherry","stawvery","Poteto"]
My_List30.sort(key = str.lower)
print("\nThe Sorted A to Z Letter Check Word = ",My_List30)



# Reverse Item Sorted Print................
My_List31 = ["Asp","Sm","Sp",1,3,4]
My_List31.reverse()
print("\nReverse Item Print = ",My_List31)



# abs() Method Uses...............................
"""
সাজানোর ফাংশন কাস্টমাইজ করুন
আপনি কীওয়ার্ড আর্গুমেন্ট কী = ফাংশন ব্যবহার করে আপনার নিজস্ব ফাংশন কাস্টমাইজ করতে পারেন।
ফাংশনটি এমন একটি সংখ্যা প্রদান করবে যা তালিকা বাছাই করতে ব্যবহৃত হবে (প্রথমে সর্বনিম্ন সংখ্যা):
"""
def myfunc(p):
  return abs(p - 50)
thislist = [100, 50, 65, 82, 23,44,99]
thislist.sort(key = myfunc)
print("\n 50 ke Base Dhore Sorted Kora = ",thislist)





# Akta List K copy Kore Then R akta List er Maje Rakte hole...............
# Example -------------------------------1
My_List32 = ["Asp","Sm","Sp",1,3,4]
My_List33 = My_List32.copy()
print("\nCopy List Example - 1 = ",My_List33)



# Example -------------------------------2
My_List34 = [1,3,4,"Asp","Sm","Sp"]
My_List35 = list(My_List34)
print("Copy List Example - 2 = ",My_List35)



