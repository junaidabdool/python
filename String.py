phrase = "hello mr junaid"
print("length of the Phrase " + str(phrase.__len__()))
print("The Phrase in lower Case: "+phrase.lower())
print("The Phrase in Upper Case: "+phrase.upper())
print("First character of the string:\n"+phrase[0])     # Prints first character of the string
print("characters starting from 3rd to 5th:\n"+phrase[2:5])  # Prints characters starting from 3rd to 5th
print("string starting from 6th character:\n"+phrase[6:])  # Prints string starting from 3rd character
# index function
print("Index of j:\n"+str(phrase.index("j")))
# replace function
print("Replace junaid with Abdool:\n"+phrase.replace("junaid","Abdool"))
print("Reverse the String\n"+phrase[::-1]) # Reverse String

print("My name is %s and weight is %d kg!" % ('Cehl', 25))