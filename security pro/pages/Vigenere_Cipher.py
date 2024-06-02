import streamlit as st

def vigenere_encrypt(plaintext, keyword):
    if not keyword:
        return "Error: Keyword cannot be empty!"

    plaintext = plaintext.upper()
    keyword = keyword.upper()
    encrypted_text = ''
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)]) - ord('A')
            shifted = (ord(char) + shift - 65) % 26 + 65
            encrypted_text += chr(shifted)
            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text


def vigenere_decrypt(ciphertext, keyword):
    ciphertext = ciphertext.upper()
    keyword = keyword.upper()
    decrypted_text = ''
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(keyword[key_index]) - ord('A')
            shifted = (ord(char) - shift - 65) % 26 + 65
            decrypted_text += chr(shifted)
            key_index = (key_index + 1) % len(keyword)
        else:
            decrypted_text += char

    return decrypted_text

def vigenere_cipher_page():
    st.title("Vigenère Cipher Encryption and Decryption")

    text = st.text_input("Enter your text:")
    keyword = st.text_input("Enter the keyword:",type='password')

    option = st.radio("Choose an option:", ("Encrypt", "Decrypt"))

    result = ""
    if option == "Encrypt":
        result = vigenere_encrypt(text, keyword);
        if st.button("Decryption of encrypted text"):  # Clearer button label
            output = vigenere_decrypt(result, keyword);
            st.success(f"Decrypted Result: {output.lower()}")  # Specify "Decrypted Result"
    elif option == "Decrypt":
        result = vigenere_decrypt(text, keyword);
        if st.button("Encryption of decrypted text"):  # Clearer button label
            output = vigenere_encrypt(result, keyword);
            st.success(f"Decrypted Result: {output.lower()}")  # Specify "Decrypted Result"

    if st.button("Show Result"):
        st.success(f"Result: {result.lower()}");

if __name__=="__main__":
    vigenere_cipher_page();
