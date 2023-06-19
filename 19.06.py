# 1.uzd
def add_mult(a, b, c):
    list = [a, b, c]
    list.sort()
    return (list[0] + list[1]) * list[2]

a = float(input("1.skaitlis: "))
b= float(input("2. skaitlis: "))
c = float(input("3. skaitlis: "))

result = add_mult(a, b, c)

print(result)

# 2.uzd

def format_text(text):
    return text.lower().replace(" ", "")

def is_palindrome(text):
    reverse_text = text[:: -1]
    return format_text(reverse_text) == format_text(text)

text = input("Pārbaudes teksts: ")

result = is_palindrome(text)

print(result)

# 3. uzd

def get_city_year(pO, perc, delta, p):
    if delta <= 0:
        return -1
    else:
        years = 0
        while pO <= p:
            pO = pO + pO * (perc / 100) + delta
            years += 1
        return years
        
result = get_city_year(1000, 2, -50, 5000)
print(result)