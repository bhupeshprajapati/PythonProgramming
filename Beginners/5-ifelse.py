is_hot=True
is_cold=True

if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
elif is_cold:
    print("It's a cold day")
    print('wear warm cloths')
else:
    print("It's a lovely day")

# LOGICAL OPERATORS
price=10000
has_good_credit = True
has_good_income =False
if has_good_credit and has_good_income:
    print("and")
elif has_good_credit or has_good_income:
    print ("or")
if has_good_credit and not has_good_income:
    print("and not")

# and , or , not, 

temp =30
if temp >= 30:  # these comparison opertors are same a c-language
    print("It is a hot day")


