# Defining functions
def doSomething(id):
    print("my id is ",id)

doSomething(25)

#Function assignment to a variable and calling that variable.
f=doSomething
f(40)

#function with Default argument values
def printName(name="Foo"):
    print("my name is ",name)

printName()

#Keyword arguments

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

#Lambdas

def make_incrementor(n):
    return lambda x: x + n

f=make_incrementor(10)

print(f(0))
print(f(2))

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')