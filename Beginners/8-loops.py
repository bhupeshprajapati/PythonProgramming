#while loop
#guess the number ----- input 9 to bypass
i=1
no=9
guesses=3
while i<=guesses:
    guess_no = int(input("Guess : "))
    if guess_no==no:
        print("You Won")
        break
    i= i+1


#car driving game using while loop ----- input quit to bypass

started= False
while True:
    command = input("Command: ").lower()
    if command =='start':
        if started ==True:
            print("Car is already started!")
        else:
            started =True
            print("The car is started")
    elif command =='stop':
        if started == False:
            print("The car is already Stopped!")
        else:
            started = False
            print("The car is stopped")
    elif command =='help':
        print('''
            start: start the car
            stop: stop the car
            quit: end the program        
        ''')
    elif command =='quit':
        print('Thank you for driving, see you soon')
        break
    else:
        print('sorry, enter a correct command -- enter "help" for command list ')
        break

#FOR LOOP

for item in 'python': # item is repeatd on each character of the list of characters 'python'
    print(item)

for item in ['bhupesh', 'rajeshwar' ,'devesh']:
    print(item)

for item in range(10): #10 is not included in the output i.e. 0 is the lower bound of range() by default
    print(item)


#Table of 3
print('Table of 3')
for item in range(3,31,3): #range(<starting index>,<ending index (excluded)>,<steps>) here it is taking steps of 3 till 31 is reached 
    print(item)            #(if we write 30 there then 30 will be excluded and output will be till 27)



#Neated loops ---Printing coordinates
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
                         
#printing a pattern using list
print('printing a pattern')
for i in [5,6,2,2,1]:
    print('x'*i)

    #using a nested loop
print('using nested loop')
for i in [5,6,2,2,1]:
    output =''
    for j in range(i):
        output += 'x'
    print(output)
