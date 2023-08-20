def caesar_cipher_decrypt(encrypted_text, distance):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isprintable():
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                decrypted_char = chr((ord(char) - base - distance) % 26 + base)
            else:
                decrypted_char = chr((ord(char) - 32 - distance) % 94 + 32)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

if __name__ == "__main__":
    try:
        encrypted_text = input("Enter the encrypted text: ")
        distance = int(input("Enter the distance value: "))

        plaintext = caesar_cipher_decrypt(encrypted_text, distance)
        print("Decrypted text:", plaintext)

    except ValueError:
        print("Invalid input. Distance value should be an integer.")
