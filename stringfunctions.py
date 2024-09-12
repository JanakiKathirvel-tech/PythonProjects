#Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])

#Loop through the letters in the word "banana":
for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

# Slicing strings
#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

#Slice from start
print(b[:5])

#Slice to the end
print(b[5:])

#Negative indexing
b = "Hello, World!"
print(b[-5:-2])

# removes white space
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"