def caesar_cipher(message, shift, mode='encrypt'):
    result = ""
    
    for char in message:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char

    return result

# Get user input
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
mode = input("Enter 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()

# Perform encryption or decryption
if mode in ['encrypt', 'decrypt']:
    output = caesar_cipher(message, shift, mode)
    print(f"Result: {output}")
else:
    print("Invalid mode selected. Please enter 'encrypt' or 'decrypt'.")
