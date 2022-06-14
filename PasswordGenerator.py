
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['~','!','@','#','$','%','&','*','(',')',]



num_letter = int(input("How many letters would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password?: "))
num_symbols = int(input("How many symbols you like in your password?: "))

password = ""

for let in range(0,num_letter ):
    password+=random.choice(letters)

for num in range(0,num_numbers):
    password += random.choice(numbers)

for sym in range(0,num_symbols):
    password += random.choice(symbols)

print(f"Your Password is {password}")

password_list = []
for let in range(0,num_numbers):
    password_list.append(random.choice(letters))

for num in range(0,num_numbers):
    password_list.append(random.choice(numbers))

for sym in range(0,num_symbols):
    password_list.append(random.choice(symbols))

#print(password_list)

random.shuffle(password_list)

passcode= ""
for char in password_list:
    passcode += char

print(f"Your Secured Password is {passcode}")
