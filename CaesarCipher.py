alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("Welcome to the CaesarCipher Generator!")
def caesar(direction, text, shift):
    if shift>=26:
        shift = shift%26
    end_text=''
    if direction == 'decode':
        shift *= -1 
    for letter in text:
            if letter in alphabet:               
                position = alphabet.index(letter)
                new_position = position + shift
                end_text += alphabet[new_position]
            else:
                end_text += letter
    print(f"The {direction}d message is : {end_text}")

should_continue = True
while should_continue:
    cipher_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    cipher_text = input("Type Your message:\n").lower()
    shift_amount = int(input("Type the shift numbers:\n"))

    caesar(direction = cipher_direction, text = cipher_text, shift = shift_amount)
    result = input("Type 'yes' if you want to go again. Otherwise typw 'no'.\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye")
