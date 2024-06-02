import streamlit as st

# Function to find modular multiplicative inverse
def mod_inverse(a, m):
    for i in range(26):
        if (a * i) % m == 1:
            return i
    return None;


def affine_encrypt(plaintext, key_a, key_b):
    encrypted_text = ''
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                shifted = ((ord(char) - ord('a')) * key_a + key_b) % 26
                encrypted_text += chr(shifted + ord('a'))
            elif char.isupper():
                shifted = ((ord(char) - ord('A')) * key_a + key_b) % 26
                encrypted_text += chr(shifted + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def affine_decrypt(ciphertext, key_a, key_b):
    decrypted_text = ''
    inverse = mod_inverse(key_a, 26)
    if inverse is None:
        return "Error: Key 'a' is not valid."

    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                shifted = (inverse * (ord(char) - ord('a') - key_b)) % 26
                decrypted_text += chr(shifted + ord('a'))
            elif char.isupper():
                shifted = (inverse * (ord(char) - ord('A') - key_b)) % 26
                decrypted_text += chr(shifted + ord('A'))
        else:
            decrypted_text += char;
    return decrypted_text

def affinecipher_page():
    # Streamlit app
    st.title("Affine Cipher Encryption and Decryption")

    text = st.text_input("Enter your text:")
    key_a = st.text_input("Enter the key 'a' value:",type='password')
    key_b = st.text_input("Enter the key 'b' value:",type='password')
    option = st.radio("Choose an option:", ("Encrypt", "Decrypt"));
    key_a = int(key_a) if key_a else 0
    key_b = int(key_b) if key_b else 0
    result = ""
    if option == "Encrypt":
        result = affine_encrypt(text, key_a, key_b)
        if st.button("Decrypt Encrypted Text"):
            output = affine_decrypt(result, key_a, key_b)
            st.success(f"Decrypted Result: {output}")
    elif option == "Decrypt":
        result = affine_decrypt(text, key_a, key_b)
        if st.button("Encrypt Decrypted Text"):
            output = affine_encrypt(result, key_a, key_b)
            st.success(f"Encrypted Result: {output}")

    if st.button("Show Result"):
        st.success(f"Result: {result}")

if __name__=="__main__":
    affinecipher_page();