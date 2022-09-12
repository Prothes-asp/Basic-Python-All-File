# Python String.....................
# Onk Gulu character er sommonoy Holo String....


# Simple String Print....
a = "Prothes Barai"
print("String =",a)


# String Add....
b = "Prothes"
c = " Barai"
d = b+c
print("\n Name = ",d)



# Kono String er First theke j-kono Akta Character Print Korte Caile (Use Positive Index)
# Program e Positive Index Suru Hoy 0 Theke And Negative Index Suru Hoy -1 Theke
sp = "Prothes"
print("\n First Theke Akta String Print = ",sp[6])



# Kono String er First theke 4 ta Character Print Korte Caile (Use Positive Index)
spa = "Prothes"
print("\n P theke h Projonto Print = ",spa[0:5])



# Kono String er Last theke j-kono Akta Character Print Korte Caile (Use Negative Index)
Asp = "Prothes"
print("\n Last Theke Akta String Print = ",Asp[-1])



# Kono String Er length Ber Korar Jonno ...................
# White Space o akta Chracter  Count Hobe...
l = "Asp Prothes"
print("\n Length = ",len(l))


# Kono String er Age Ba Pore White Space Remove Korte Hole..  strip() Method Use hoy
R = "   Asp Prothes   "
print("\n Simple Print =",R)
print(" Remove First And Last Space =",R.strip())


# Akta String er All Letter Ke Uppercase Banate Hole..
Up = "prothes"
print("\n Uppercase =",Up.upper())


# Akta String er All Letter Ke Lowercase Banate Hole..
Lo = "PROTHES"
print("\n Uppercase =",Lo.lower())


# Akta Sentence er akta word ke replace kore onno word bosate hole..............
Replace = "Python is my like Language"
print("\n Simple Print = ",Replace)
print(" Replace =",Replace.replace("like","favourite"))



# Akta Sentence er word ke alada alada vabe dekhate chaileo dekhano jay ..use   split()  Method..
Brw = "Python is my favourite Language"
print("\n Word Alada =",Brw.split())


# Jode Python e At first 3 Ta Word Print korte hoy.............
Fwp = "Prothes"
print("\n Print At First 5 letter =",Fwp[:3])



# First Theke Word Bad deye deye Print..........
First = "Prothes"
print("\n First Theke Bad Deye Deye Print")
print(First[1:])
print(First[2:])
print(First[3:])
print(First[4:])
print(First[5:])
print(First[6:])



# Jode Python e akta akta word Barte barte jay .............
print("\n First Theke Print" )
Fwp = "Prothes"
Add = ""
for i in Fwp:
    Add = Add + i
    print(Add)



# Kono String er Last theke 4 ta Character Print Korte Caile
# Negative index e last er Character Print Korar Jonno Last Character Ses e akta Space Dete Hoy...
Spa = "Prothes "
print("\n s theke t Projonto Print = ",Spa[-5:-1])



# Again Jode Ses Theke  word Print Korte hoy ...
Last = "Prothes"
print("\n Last Theke Print" )
print(Last[-1:])
print(Last[-2:])
print(Last[-3:])
print(Last[-4:])
print(Last[-5:])
print(Last[-6:])
print(Last[-7:])




# Ses Theke Akta Akta Word Bad Deye Deye  Print..................
Ses = "Prothes"
print("\n Ses Theke Word Bad Deye Deye Print")
print(Ses[:-1])
print(Ses[:-2])
print(Ses[:-3])
print(Ses[:-4])
print(Ses[:-5])
print(Ses[:-6])





# Format Method Using In Python.................
# Addition String or Number Use Format Method .................Without Order
age = 24
year = 2022
gpa = 5.00
ASP = "I am {} years old and Year in {}. My result in Gpa {}."
print("\n Dynamic String /  Number Addition \n",ASP.format(age,year,gpa))



# Format Method Using In Python.................
# Addition String or Number Use Format Method .................With Order
age0 = 24          # Order ---0
year1 = 2022       # Order ---1
gpa2 = 5.00        # Order ---2
NAME3 = "Prothes"  # Order ---3
SPA = "I am {3} and My result is Gpa {2} .In This Year in {1} , I am {0} years old."
print("\n Dynamic String /  Number Addition \n",SPA.format(year1,age0,gpa2,NAME3))



# Check "free" String is present in the text......Type 1
text = "The best things in life are free !"
print("\n Check Present String = ", "free" in text)


# Check "free" String is present in the text Use if Method..........type 2
text1 = "The best things in life are free !"
if "free" in text1:
    print("\n The Free is Present in text1")



# Check "free" String is not  present in the text......Type 3
text2 = "The best things in life are free !"
print("\n Check Not Present String = ", "you" not in text2)


# Check "free" String is present in the text Use if Method..........type 4
text3 = "The best things in life are free !"
if "you" not in text3:
    print("\n The String Not Present in text1")