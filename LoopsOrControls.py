#WHILE LOOP


a,b=0,1
while a<1000:
    print(a)
    a,b=b,a+b

# print in same line
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

#If statements
#x= int(input("\nPlease enter an integer: "))
x=-2
if x<0:
    print("Negative number")
    print("Number less than 0")
elif x==0:
    print('Number is 0')
else:
    print('Number is positive.')

#for statements
words=['cat', 'batsman', 'matter','Windows']
for w in words:
    print(w, len(w))

#Manipulate a collection
users={'User1':'active', 'User2':'inactive','User3':'active'}

# Strategy:  Iterate over a copy to modify it
for user, status in users.copy().items():
    if status == 'inactive':
        #print(user)
        del users[user]

# Strategy:  Create a new collection by filtering
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

for user in active_users:
    print(user)


#Range
# start with 0
print("\n")
for i in range(10):
    print(i, end=',')

#Start with another number
print("\n")
for i in range(5,10):
    print(i, end=',')

#Start with 0 with increment by 3 and max number is 10
print("\n")
for i in range(0,10,3):
    print(i, end=',')

print("\n")
print(sum(range(11)))

#Break
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

#Continue
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

# For loop with else. If the loop finishes without executing the break, the else clause executes.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

#Pass
#The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action
#while True:
    #pass  # Busy-wait for keyboard interrupt (Ctrl+C)
    #print ("Hello")


#Match similar to switch.
status=416
match status:
    case 400:
        print("Bad request")
    case 404:
        print( "Not found")
    case 418 |415|416:
        print( "I'm a teapot")
    case _: #default
        print( "Something's wrong with the internet")