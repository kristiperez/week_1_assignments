#get input word 
enter_word = input("Enter a word: ")
#create variable and initialize to blank
reversed_word = ""

#for each letter in the word entered return it in reverse and add that to the initial value of reversed_word
for letter in enter_word[::-1]:
    reversed_word += letter
print(reversed_word)    
    
if reversed_word == enter_word:
    print("Palendrome")
else:
    print("NOT")

#breaking down steps of palindrome
#Take user input
#print out individual letters in order
#for  index in range(0,len(word)):
#   print(word[index])
#print out individual letters in reverse order
#for index in range(len(word)-1, -1, -1):
#append letters to form a reverse string
#   reversed_word = reversed_word + word[index]
#
#compare reverse word with original word for palindrome