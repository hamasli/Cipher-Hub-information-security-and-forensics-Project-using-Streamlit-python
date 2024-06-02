import streamlit as st

def caesar_encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def Caesarcipher_page():
    st.title("Caesar Cipher Encryption and Decryption")

    text = st.text_input("Enter your text:")
    shift = st.text_input("Enter the shift value: ", type='password')  # Use type='number' for numeric input

    option = st.radio("Choose an option:", ("Encrypt", "Decrypt"))

    result = ""
    output = ""

    if option == "Encrypt":
        shift_value = int(shift) if shift else 0
        result = caesar_encrypt(text, shift_value)

        if st.button("Decryption of encrypted text"):  # Clearer button label
            output = caesar_decrypt(result, shift_value)
            st.success(f"Decrypted Result: {output}")  # Specify "Decrypted Result"

    elif option == "Decrypt":
        shift_value = int(shift) if shift else 0
        result = caesar_decrypt(text, shift_value)

        if st.button("Encryption of decrypted text"):  # Clearer button label
            output = caesar_encrypt(result, shift_value)
            st.success(f"Encrypted Result: {output}")  # Specify "Encrypted Result"

    if st.button("Show Result"):
        st.success(f"Result: {result}")

if __name__ == "__main__":
    Caesarcipher_page()
