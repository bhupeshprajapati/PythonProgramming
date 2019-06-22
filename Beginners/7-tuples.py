#tuples are similar to list, but they are immutabel i.e. we connot append or edit existing elements
coordinates =(11,22,44) # (...) are used instead of [...] used in lists while declareing
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print(x,y,z)
#only two funtions are availabe for tuples ---index() and count() {although more advanced functions are also prisent} 
#lines 3-5 can also be written as follows using UNPACKING facility in python
print('\n using Unpacking:')
m,n,o=coordinates # index based ordered assignment of the variables in lhs
print(m,n,o)