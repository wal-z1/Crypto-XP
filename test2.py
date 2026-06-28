#I'll test sets here :

x = {1, 32,2, 3, 4, 5,5}
print(x)

y = {'key1':'4'}
print(y['key1'])

y['key2']= "hacking to the gate"
print(y)

h = tuple ([ i for i in range(10) if i % 2 == 0]) ## contains even numbers from 0 to 9
print(h)

def walid_func():
    print("walid function was called")
    return 1,2 ## returns a tuple

print(walid_func())

try:
    print(1/0)
except ZeroDivisionError as e:
    print("error occured",e.__cause__)
finally:
    print("this will always run")

lambda_func = lambda g: g**2

print(lambda_func(4))

numbers = [1,2,3,4,5,6,7,8,9]

updated_numbers =list(filter(lambda x: x % 2 == 0,numbers))

print(updated_numbers, type(updated_numbers))
print(f'{updated_numbers} is a list of even numbers from {numbers}')