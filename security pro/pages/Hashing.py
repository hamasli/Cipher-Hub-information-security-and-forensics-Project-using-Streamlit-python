import hashlib;
import streamlit as st;

def generate_hash(text, algorithm="sha256"):
    # Choose the hash algorithm (default is SHA-256)
    hash_algorithm = hashlib.new(algorithm)

    # Update the hash object with the bytes-like object (UTF-8 encoding)
    hash_algorithm.update(text.encode("utf-8"))

    # Get the hexadecimal representation of the hash
    hashed_text = hash_algorithm.hexdigest()

    return hashed_text


def hash_page_algo():
    st.title("Hashing")
    text = st.text_input("Enter your text:")
    result = ""
    hashed_value = generate_hash(text);
    if st.button("Show Result"):
        st.success(f"Result: {hashed_value}")

if __name__ == "__main__":
    hash_page_algo();


