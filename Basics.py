# First program
msg='hello world'
print (msg)
print(msg.lower())

helloMessage =False

if helloMessage:
    print("message printed.")

# classic division
print(17/3) 

# floor division discards the fractional part
print(17//3)

# % gives remainder
print(17%3) 

# 17 multiplied by 3
print(17*3) 

# 2 to the power 3
print(2**3) 

print('doesn\'t')  # use \' to escape the single quote...

print ("doesn't")  # ...or use double quotes instead

print('First line.\nSecond line.')  # \n means newline

print(r'C:\some\name')  # note the r before the quote for raw string

# Multi-line strings.
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 3 times 'un', followed by 'ium'
print(3 * 'un' + 'ium')  #'unununium'

#Automatic concatenation
print('Py' 'thon')

word = 'Python'
print(word[0])  # character in position 0 'P'

print(word[-1])  # last character

print(word[0:2])  # characters from position 0 (included) to 2 (excluded)

print(word[:2])   # character from the beginning to position 2 (excluded) 'Py'
print(word[4:])   # characters from position 4 (included) to the end 'on'
print(word[-2:])  # characters from the second-last (included) to the end 'on'

#Input from user
x = str(input("\nEnter your name: "))
print ("Welcome "+x)