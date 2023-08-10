'''[set comprehension] Given a list of numbers, create a set using set
comprehension that contains only unique even numbers.'''

x = [1,2,3,4,12,14,14,5,6,6,7,8,8]
y = {s for s in x if s % 2 == 0}
print(y)


'''[set comprehension] Given a list of words, write a Python program to create a set
using set comprehension that contains all the unique characters present in the
words. '''

words = ["Nepal", "India", "China"]
final = {char for word in words for char in word}
print(final)

'''[set comprehension] Given two strings, write a Python program to create a set
using set comprehension that contains all the characters that are common in both
strings.''' 

string1 = "welcome"
string2 = "home"

common_characters_set = {char for char in string1 if char in string2}
print(common_characters_set)