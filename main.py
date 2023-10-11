alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#User input
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted_text = " "
    for letter in text:
        shifted_letter = (alphabet.index(letter) + shift) % len(alphabet) #Find the index of letter in alphabet, add shift to that number. Use % to wrap around alphabet is shift higher than 25
        encrypted_text += alphabet[shifted_letter] # Adding shifted letter to encrypted text variable
    print(f"The encoded text is {encrypted_text.strip()}")

def decode(text, shift):
  decrypted_text = " "

  for letter in text:
    shifted_letter = (alphabet.index(letter) - shift) % len(alphabet)
    decrypted_text += alphabet[shifted_letter]
  print(f"The decoded text is {decrypted_text.strip()}")

if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  decode(text, shift)
else:
  print("Invalid input.")