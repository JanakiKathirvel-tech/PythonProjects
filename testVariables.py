# Check-the-type-of-Variable

#Check the data type of variable

print("Helow", "world")

a=12
b="janaki"
c=5.6
d=[1,2,3]
e=(1,2,3)
f={1,2,3}
g={"name":"janaki","age":25}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

#Camel Case
#Each word, except the first, starts with a capital letter:
myVariableName = "John"

#Pascal Case
#Each word starts with a capital letter:
MyVariableName = "John"

#Snake Case
#Each word is separated by an underscore character:

my_variable_name = "John"

# Check-the-Id-of-variable

a=25
'''Id of Variables 
                    The id() method also returns the identity of a variable or object, as shown below.
                    The identity of the two same values is the same,as shown below.
                    In the above example,
                    the id of 10 and variable num are the same because both have the same literal value.'''
b=25
c=50                #The id function is differented by the variable's value.
d=a+b               #The id is refers the memory location of the Variable's Value.
print(id(a))
print(id(c))
print(id(d))