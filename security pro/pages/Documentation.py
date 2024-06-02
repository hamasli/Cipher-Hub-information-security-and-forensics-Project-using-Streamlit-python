
import streamlit as st


def show_caesar_cipher_docs():
    st.title("Caesar Cipher Documentation")
    st.write("""
    The Caesar cipher is a type of substitution cipher in which each letter 
    in the plaintext is shifted a certain number of places down or up the alphabet.

    ### Encryption:
    - Each letter in the plaintext is shifted a fixed number of places down the alphabet.
    - Example: With a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so on.

    ### Decryption:
    - Each letter in the ciphertext is shifted back a fixed number of places to reveal the plaintext.
    """)


def show_rail_fence_cipher_docs():
    st.title("Rail Fence Cipher Documentation")
    st.write("""
    The Rail Fence cipher is a form of transposition cipher that writes the plaintext in a zigzag pattern.

    ### Encryption:
    - The plaintext is written in a zigzag pattern across a specified number of rails (rows).
    - Example: With 3 rails, 'HELLO' becomes 'HOLEL'.

    ### Decryption:
    - The ciphertext is read in a zigzag pattern to reveal the plaintext.
    """)


def show_affine_cipher_docs():
    st.title("Affine Cipher Documentation")
    st.write("""
    The Affine cipher is a type of substitution cipher in which each letter in the plaintext 
    is mapped to its numeric equivalent, encrypted, and converted back to a letter.

    ### Encryption:
    - Each letter is transformed using a mathematical formula (ax + b) % 26.

    ### Decryption:
    - The formula (a^-1)(x - b) % 26 is used to reverse the encryption process.
    """)


def show_vigenere_cipher_docs():
    st.title("Vigenere Cipher Documentation")
    st.write("""
    The Vigenère cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution.

    ### Encryption:
    - It uses a keyword to shift each letter of the plaintext multiple times based on the keyword.

    ### Decryption:
    - It reverses the process by using the same keyword to shift each letter back to reveal the plaintext.
    """)


def show_playfair_cipher_docs():
    st.title("Playfair Cipher Documentation")
    st.write("""
    The Playfair cipher is a digraph substitution cipher that encrypts pairs of letters (digraphs).

    ### Encryption:
    - It uses a 5x5 grid of letters to encrypt digraphs based on their positions in the grid.

    ### Decryption:
    - It reverses the process using the same grid to reveal the plaintext.
    """)


def documentation_page():
    # Streamlit app for cipher documentation
    st.title("Cipher Documentation")

    cipher_choice = st.selectbox("Select a cipher:", (
        "Caesar Cipher", "Rail Fence Cipher", "Affine Cipher", "Vigenere Cipher", "Playfair Cipher"))

    if cipher_choice == "Caesar Cipher":
        show_caesar_cipher_docs()
    elif cipher_choice == "Rail Fence Cipher":
        show_rail_fence_cipher_docs()
    elif cipher_choice == "Affine Cipher":
        show_affine_cipher_docs()
    elif cipher_choice == "Vigenere Cipher":
        show_vigenere_cipher_docs()
    elif cipher_choice == "Playfair Cipher":
        show_playfair_cipher_docs();

if __name__=="__main__":
    documentation_page();
