text = input("Enter a word: ")
char = input("Enter a character: ")

count = 0

for letter in text:
    if letter == char:
        count = count + 1

print("Character occurs", count, "times.")