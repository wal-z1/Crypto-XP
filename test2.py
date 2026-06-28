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