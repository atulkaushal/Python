#Set represented by {}.
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

a=set('abracadabra')
b=set('alacazam')
print(a)
print(b)
print(a-b)

#Dictionary
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel['sape'])

del tel['sape']
print(tel)

print(list(tel))
print(sorted(tel))
print('guido' in tel)

#Init Dictonary
dic=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dic)

#print key:value of dictionary
for k, v in dic.items():
    print(k, v)