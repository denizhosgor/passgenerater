import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters = input("How many letters would you like in your password?\n")
nr_symbols = input("How many symbols would you like?\n")
nr_numbers = input("How many numbers would you like?\n")

if not nr_letters.isdigit() or not nr_symbols.isdigit() or not nr_numbers.isdigit():
    print("You can write only digit character\n")
    exit()

keypass = ''
passwd = []
for chooseLet in range(0, int(nr_letters)):
    passwd.append(random.choice(letters))

for chooseNum in range(0, int(nr_numbers)):
    passwd.append(random.choice(numbers))

for chooseSym in range(0, int(nr_symbols)):
    passwd.append(random.choice(symbols))

#print(passwd)
random.shuffle(passwd)
for x in range(len(passwd)):
    keypass = keypass + str(passwd[x])
print(f"\nPassword Generated\n{keypass}")
