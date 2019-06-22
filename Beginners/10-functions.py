def greet_user(): #def stands for definition
    print("\nI am inside a function")
    print("hi there")
                                        #Best practices : leave atleast 2 lines after a function definition

print("start")
greet_user()
print("\nend")

# Using Parameters
def greet_users(name,surname="prajapati"): #If a function has a parameter we are obliged to pass a value to the parameter, Otherwise there is an error
    # in the above definition surname is the keyword argument
    print("\nI am inside a function")
    print(f"hi {name} {surname}")
                                        #Best practices : leave atleast 2 lines after a function definition

print("start")
greet_users("Bhupesh") # positional argument sent = bhupesh , no surname => default key argument will be used
greet_users("Rakesh","Ramashray") # positional argument sent = rakesh , surname is sent as Ramashray here
print("\nend\n")
    #for most part use positional arguments
    #keyword argumnets improves the readability of a funtin parameter list (specially if they are numbers)
    #keyword arguments must always be places AFTER positional parameters

# Return Statements
def square(number):
   return number*number


print(square(4))
# By default all functions return a None 
# None is an object in python that means nothing ... similar to NULL in C/C++
    

