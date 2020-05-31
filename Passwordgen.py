import random
Max_length = 12

digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

low_char = ['a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

upper_char = ['A', 'B', 'C', 'D', 'E', 'F',
              'G', 'H', 'I', 'J', 'K', 'M',
              'N', 'O', 'p', 'Q', 'z']

Symbol = ['@', '#', '$', '%', '=', ':', '?',
          '.', '/', '|', '~', '>', '*', '(', ')']

combined_list = digit + low_char + upper_char + Symbol

r_degit = random.choice(digit)
r_low = random.choice(low_char)
r_upper = random.choice(upper_char)
r_symbol = random.choice(Symbol)

temp_pass = r_degit + r_low + r_upper + r_symbol

for x in range(Max_length-4):
    temp_pass = temp_pass + random.choice(combined_list)

password = ""
for x in temp_pass:
    password = password + x
print("Strong password=   ", password)



