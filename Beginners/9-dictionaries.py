#Dictionaries are very important and are used in many places in real world

#used when the data is key value pairs like --- Name:bhupesh , Age:20 , gender: male, etc
customer = {
    "name":"Bhupesh",
    "id":"123456789",
    "is_verified":True
}
print(customer["name"])# this gives an error if the key is not present in the dictionary, so we use get() method 
print(customer.get('name')) #it returns a None object if the key is not found
customer["name"]='rakesh' #changing the value for name key
print(customer.get("date","7 Dec 1998")) #default date is used (and printed) when the date key is not present in the dictionary
customer["DOB"]= "19 jan 1966"
print(customer.get('DOB'))

