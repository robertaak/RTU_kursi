# 1.uzdevums

word = input("Ievadi vārdu: ")
reverse_word = word[:: -1].title()
first_letter = word[0].upper()

print(f"{reverse_word}, pamatīgs juceklis vai ne {first_letter}?")

# 2.uzdevums
text = input("Ievadi tekstu: ")
symbol = "*"
output = ""

for char in text:
    if char.isalnum():
        output = output + symbol
    else:
        output = output + char

print(output)

new_output = ""
guess = input("Ievadi simbolu:")
for char in text:
    if char == guess:
        new_output = new_output + guess
    else:
        new_output = new_output + symbol

print(new_output)

# 3.uzdevums - NAV PABEIGTS :(

input = input("Ievadi tekstu!")

replaceable_word1 = "nav"
replaceable_word2 = "slikts"

new_word1 = "ir"
new_word2 = "labs"

output = ""

if replaceable_word1 in input and replaceable_word2 in input:
    print("to be replaced")
