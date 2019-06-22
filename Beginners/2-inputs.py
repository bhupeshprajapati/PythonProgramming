name= input('what is your name? ')
fav = input('what is your fav color')
print('hi' + name +' fav colr= ' + fav)

#Type conversions

birth_year = input('birth year : ') #input returns a string
#age = 2019 - birth_year #this creates an error of type miss-match
#print(age)
#Every variable in python is a string by default ...we have to convert it into corresponding data types

# int()
# float()
# bool()

#type miss match creates an error for expressions 
age= 2019 -int(birth_year)
print(age)
# to pring data type

print(type(age)) #output : <class 'int'>
