import string

text = input("Enter your statement: ").lower()
alphabet = string.ascii_lowercase

result = True
for letter in alphabet:
    if letter not in text:
        result = False
        break
print(result)