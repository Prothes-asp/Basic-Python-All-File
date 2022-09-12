# Python While Loop................
"""
Python While Loop er 3ta Part ,Firstly Initialization i.e. koto theke suru hbe,
Then Condition i.e. koto projonto cholbe..then increment hobe i.e. Update part....
then Extra Part Then End............
"""
# While Loop Deye 1 theke 10 Projonto Print.....................
i = 1
while i <= 10:
    print(i,end=" ") # akhane  end=" " deye akta row te output dekhano hoy ata \n er reverse kaj kore
    i = i+1


# While Loop Use kore 10 Bar Name Print..........................
j = 0
while j<=10:
    print("India")
    j = j+1



# Python Break Statement use in while loop.......................
print("\nUse Break Statement In While Loop")
k = 0
while k<=6:
    print(k)
    if k==4:
        break
    k = k + 1



# Python Continue Statement use in while loop.......................
print("\nUse Continue Statement In While Loop")
l = 0
while l<10:
    l = l+1
    if l == 5:
        continue
    print(l)


# Python While Loop IF Statement....................
print("\nIF.........Statement")
p = 0
while p <5:
    p = p+1
    if p == 4:
        print("$")
    print(p)


# Python While Loop Else Statement....................
print("\nELse.........Statement")
e = 0
while e<=5:
    print(e)
    e = e + 1
else:
    print("Next Print Longer Than Five")