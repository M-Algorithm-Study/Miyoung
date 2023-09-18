word = input()

converted_word = ''
for char in word:
    if char.isupper():
        converted_word += char.lower()
    else:
        converted_word += char.upper()

print(converted_word)