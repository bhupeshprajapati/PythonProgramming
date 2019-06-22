try:
    value = int(input("enter a no.: "))
    print(value)
    income = 2000
    risk = income/ value
    print(risk)
except ValueError: # to handle non int() value
    print("Invalid value")
except ZeroDivisionError: # Handling multiple errors of exceptions whith same try block
    print("Value cannot be 0.")

     