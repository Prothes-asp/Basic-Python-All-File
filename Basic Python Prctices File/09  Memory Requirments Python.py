"""
Memory er Size Dekhar Jonno i.e. Kono Item er Value Memory te Koto tuku Size Akare Ase
Seta Check Korar Jonno  Firstly Amader import Korte Hobe sys then getsizeof() method deye kon
item memory te koto tuku jayga nece ta dekha jabe......lets go............
"""

import sys
Tuple = (1,2,3,4,5,6,7,8,9)
List = [1,2,3,4,5,6,7,8,9]
Sets = {1,2,3,4,5,6,7,8,9}
Dict = {
    "Name":"Prothes",
    "Age" :24,
    "Year":2022
}

a = 10
b = 10
Addition = a + b + 10
Multiplication = a * b * 2000000


print("\nTuple Memory Size =",sys.getsizeof(Tuple))
print("List Memory Size =",sys.getsizeof(List))
print("Sets Memory Size =",sys.getsizeof(Sets))
print("Dict Memory Size =",sys.getsizeof(Dict))
print("a Memory Size =",sys.getsizeof(a))
print("b Memory Size =",sys.getsizeof(b))
print("Addition Memory Size =",sys.getsizeof(Addition))
print("Multiplication Memory Size =",sys.getsizeof(Multiplication))
