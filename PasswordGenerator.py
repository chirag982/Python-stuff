import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
         'r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','&','*','^','?']

print("Welcome to the PyPassword Generator!")
nr_letters=int(input("How many letters would you like in your password?\n"))
nr_symbols=int(input("How many symbols would you like in your password?\n"))
nr_numbers=int(input("How many numbers would you like in your password?\n"))

if nr_letters==0 or nr_symbols==0 or nr_numbers==0:
    print("Sorry but input can't be this!")

password=""
for char in range(1,nr_letters + 1):
    random_char = random.choice(letters)
    password = password + random_char
for char in range(1,nr_symbols+1):
    random_symb = random.choice(symbols)
    password = password + random_symb
for char in range(1,nr_numbers+1):
    random_numb = random.choice(numbers)
    password = password + random_numb

print("The password generated is:")
print(''.join(random.sample(password,len(password))))                
                    

