def caesar_encrypt(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            shift_amount = (ord(char) - ord('A') + shift )
            encrypted_char = chr(ord('A') + shift_amount)
            cipher_text +=encrypted_char
        else:
            cipher_text += char
    return cipher_text
plain_text = "hello"
shift = 3
cipher_text = caesar_encrypt(plain_text, shift)
print("cipher_text:", cipher_text)
