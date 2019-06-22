course = "python's course for beginners"
# double quotes and single quotes can be nested alternatively

#multiple line strings
course='''
hello this is a very big string

hello this is insane
'''
print(course)

#to get a character in a string
hello="this is an index test string"
print(hello[0])
print(hello[-2])

print(hello[0:3]) #output : all characters from index 0 to 3 excluding 3...ie... 0 1 2 
print(hello[:7]) # 0 is assumed at empty places
print(hello[:])
print(hello[2:]) # exclude first 2 characters <string name>[<start index> : <string length>]

# imp

name = 'jennifer'
print(name[1:-1]) #guess the output (hint: '-' means starting from the end)

# FORMATED STRINGS
first ='bhupesh'
last = 'prajapati'
message = first + ' [' + last + '] is a code' # not good for comprehension
msg = f'{first} [{last}] is a coder' # THIS IS A GOOD WAY OF DOING IT- use f before a stirng {} is place holders for variables

print(message)
print(msg)

#STRING FUNCTIONS
course = 'python for heros'
print(len(course))

print(course.upper()) # upper case
print(course.lower()) #lower case
print(course.title())

print(course.find('ho')) #finds the starting index of the sequence of characters
print(course.replace('python', 'PYTHON')) # replace - case sensitive

print('python' in course) # returns a boolean value - whether this sequence of strigs is present or not
print('Python' in course) # flase because P is capital