'''
Variable Assignment
'''

# # add 'alfred' to the variable 'name'
# name = "Alfred"''
# print(name)

#=================

# assign same value to multiple variables on the same line
# a = b = c= 'cat'
# print(a)
# print(b)
# print(c)

#=================

# reuse  variable names, the last assignment is printed
#colour = 'Red'
#colour = 'Blue'

#print (colour)

#=================

#Legal names
#These are all valid names that you can use for variables
#firstname = "John"
#first_name = "John"
#_firs_tname = "John"
#firstname2 = "John"
#FIRSTNAME = "John"


#illegal variable names
#no numbers to start with, no dash and no spaces otherwise they are illegal like below
#2firstname = "John"
#first-name = "John"
#first name = "John"

#=================

'''
Reserved Keywords
'''

#help("Keywords")
#To run shell, run script help("keywords")

#from = "London"
#print(from)
#Example above, if you run that then you get a syntax error as that is a reserved keyword

#=================

#variable types
#var = "Hello world"
#print(type(var))
#string saved inside the var

#var = 23
#print(type(var))
#Integer

'''
Object identity
'''
#score = 400
#identity = id (score)
#print(identity)

#=================

#score variable is saved into the pb by reference

#score = 400
#pb = score
#print(id(score))
#print(id(pb))

''' Object reference
'''

#===============

#pb ------------------>int 20
# score ----------------> int 100
#score = 20
#pb = 100

#print(type(score))
#print(type(pb))
#print(score)
#print(pb)


#===============
#pb ----------->int 20
# score -------------->str "completed"
#--------------------->int 100
#This process is known as garbage collection
pb = 20
score = 100
score = "Completed"

print(type(score))
print(type(pb))
print(score)
print(pb)

#==========================