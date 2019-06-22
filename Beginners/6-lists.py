
#Basics of lists
names =['bhupesh','ragini','rajeshwar','devesh','garvit','mihir','triyasa']
print(names[0]) #first index is 0, only bhupesh is printed
print(names[-2]) # accessing items from the end of the list
print(names[0:4]) # list items at 0 through 3 index are printed ; 4 is the end index but it is not included !
print(names[2:-2]) # starting index is 2 i.e. 'rajeshwar' and offset is set from the end of the list , last two elements are excluded



#Program to find the largest number in the list
numbers = [1,45,3,78,3,6,9,33,0,-3,-44] 
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print(f'The largest number in the list {numbers} is : {largest}')

# 2-D Lists

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][1]) #prints 2
#Travesing a 2-D matrix
for row in matrix:
    for item in row:
        print(item)

#List Methods
numbers = [2,5,7,1,8,9,5]
numbers.append(20) #addes an element at the end or the list
print(f'append 20 : {numbers}')
numbers.pop()#removes last element from the list
print(f'pop (20 popped): {numbers}')
numbers.insert(1,10) #insert(index,object) - object can be a string also
print(f'insert 10 at index 1:  {numbers}')
print(f'occurances of 5:{numbers.count(5)}') #counts the no. of occurances of 5 in the list
numbers.remove(2) 
print(f'remove 2: {numbers}')
print(50 in numbers) #we are using in operator it returns a boolean value -- true is object is present in the list and false otherwise
print(5 in numbers)
print(numbers.index(5))# if the element is present then it returns the index of its first occurance , but an error if it is not present
#  print(numbers.index(50)) this statement gives an error "valueError: 50 is not in list" therefore using in operator is a better option

#Sorting
print(numbers.sort()) #this returns an object None which denotes nothing is returned by the function
print(numbers) # the list is sorted by the above statement ... we are just printing the list here
numbers2= numbers.copy() #number2 gets becomes a copy of numbers...any changes in numbers2 won't affect the numbers list
numbers2.reverse() #it reverses the list
print(numbers2)
numbers.clear()
print(f'all elements cleared {numbers}')

#Program to remove duplicates from a string
numbers =[2,3,5,7,2,5,9,1,1]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(f'original list : {numbers}')
print(f'duplicates removed : {uniques}')




#these methods alter the list in the memory and the changes are used by preceeding statements


