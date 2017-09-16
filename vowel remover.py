## This is a program that takes a string from the user,
## removes the vowels from it and returns the new string,
## along with a list of the vowels removed.

input_string = input("Insert a word to remove the vowels from: ")
print("You inserted the word:",input_string)
vowels = ["a", "e", "i", "u", "y", "o", "A", "E", "I", "U", "Y", "O"]
new_string = ''
vowels_removed = ''
for letter in input_string:
    if letter not in vowels:
        new_string+=letter
    else:
        vowels_removed+=letter+' '
print("The new word is: ",new_string, "\nThe vowels removed are: ",vowels_removed)
