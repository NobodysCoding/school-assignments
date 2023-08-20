def caesar_cipher_encrypt(plaintext, distance):
    encrypted_text = ""
    for char in plaintext:
        if char.isprintable():
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                encrypted_char = chr((ord(char) - base + distance) % 26 + base)
            else:
                encrypted_char = chr((ord(char) - 32 + distance) % 94 + 32)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

if __name__ == "__main__":
    try:
        plaintext = input("Enter the plaintext: ")
        distance = int(input("Enter the distance value: "))

        encrypted_text = caesar_cipher_encrypt(plaintext, distance)
        print("Encrypted text:", encrypted_text)

    except ValueError:
        print("Invalid input. Distance value should be an integer.")
