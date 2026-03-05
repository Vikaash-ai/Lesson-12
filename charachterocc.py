word = input("Please enter your word: ")

char = input("Please enter the charcter to search: ")

i = 0
count = 0

while (i < len(word)):
    
    if (word[i] == char):
        count = count + 1
        
    i = i+1
        
print(f"The number of {char}, in your word is {count}")