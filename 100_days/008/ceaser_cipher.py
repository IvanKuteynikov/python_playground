import string

alphabet = list(string.ascii_lowercase)

want_to_cipher = True

def cipher(text, shift, direction):
    ciphered = []
    if direction == 'decode':
        shift *= -1
    for letter in text:
        try:
            p = alphabet.index(letter) + shift
            p %= len(alphabet)
            ciphered.append(alphabet[p])
        except ValueError:
            ciphered.append(letter)
            continue
    print("".join(ciphered))
    user = input("\nType 'Yes' to continue, or 'No' to exit\n").lower()
    if user == 'no':
        want_to_cipher == False
        print("Thanks and bye!")

while want_to_cipher:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher(text, shift, direction)