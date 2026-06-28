


walid = 1234
walid_string = "walid"

walid_list = ["house","door","window"]

walid_boolTrue = True
walid_boolFalse = False

print(walid)
print(walid_string)
print(walid_list)
print(walid_boolTrue)
print(walid_boolFalse)
print(walid,walid_string,walid_list,walid_boolTrue,walid_boolFalse)
ending= '\n'

print("walid was here or something idk",end=ending)

lyrics = """
i wanna grab by shoulders
and shake baby
arctic monkeys - snap out of it

"""

import math

expension = math.exp(1)

print(expension)
print(expension**3)
print(expension // 2)
print("mod",expension % 2)

## every read number is a float by default
walid_read = input("Enter a number: ")
print(type(walid_read))

print(lyrics.capitalize(),lyrics.upper(),lyrics.lower())
print(lyrics.count("l"))

if(math.exp(1) % 3 != math.exp(1) // 2 ):
    print("exp(1) % 3 is equal to exp(1) // 2",math.exp(1)%3,math.exp(1) // 2)

if(True):
    print("True is true")
else:
    print("never prints this anyways")

list1 = [walid,"walid string"]
print(list1,len(list1))
list1.append("walid list")
print(list1,len(list1))
print(list1.pop(),len(list1))
print(id(list1))

y = list1[:]
print(y,"here is the id",id(y))

for i in y:
    print(i)

##slicer

walid_slicer =[1,2,3,4,5,6,7,8,9]

print(walid_slicer[::-1])