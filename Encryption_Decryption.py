
print("A.S Muhammad")
print('***CAESAR CIPHER PROGRAM FOR ENCRPTION AND DECRYPTION***')
print()
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) + shift -65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text
def main():
    while True:
        print("Caesar Cipher: Encrypt and Decrypt Text")
        choice = input("Do you want to encrypt or decrypt a message? (e/d): ").lower()
        if choice == 'e' or choice == 'd':
            message = input("Enter your message: ")
            shift = int(input("Enter the shift value: "))

            if choice == 'e':
                encrypted_message = encrypt(message, shift)
                print(f"Encrypted Message: {encrypted_message}")
            else:
                decrypted_message = decrypt(message, shift)
                print(f"Decrypted Message: {decrypted_message}")
        else:
            print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
        again = input("Do you want to process another message? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()



