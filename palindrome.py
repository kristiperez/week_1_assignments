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

