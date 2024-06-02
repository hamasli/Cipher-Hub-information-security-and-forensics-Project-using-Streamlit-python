import streamlit as st


# Function to generate the Playfair cipher matrix
def generate_playfair_matrix(key):
    key = key.replace("J", "I")  # Replacing 'J' with 'I'
    key += "".join(filter(lambda x: x not in key, "ABCDEFGHIKLMNOPQRSTUVWXYZ"))
    matrix = [key[i:i + 5] for i in range(0, 25, 5)]
    return matrix

# Function to perform Playfair cipher encryption
def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = plaintext.upper().replace("J", "I")  # Replacing 'J' with 'I'
    plaintext = "".join(filter(str.isalpha, plaintext))
    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    digraphs = [plaintext[i:i + 2] for i in range(0, len(plaintext), 2)]

    encrypted_text = ""
    for digraph in digraphs:
        a, b = digraph[0], digraph[1]

        # Find positions of characters 'a' and 'b' in the matrix
        try:
            a_pos = [(i, row.index(a)) for i, row in enumerate(matrix) if a in row][0]
            b_pos = [(i, row.index(b)) for i, row in enumerate(matrix) if b in row][0]
        except IndexError:
            # If a character is not found in the matrix, handle the exception
            encrypted_text += digraph
            continue

        a_row, a_col = a_pos[0], a_pos[1]
        b_row, b_col = b_pos[0], b_pos[1]

        if a_row == b_row:
            encrypted_text += matrix[a_row][(a_col + 1) % 5] + matrix[b_row][(b_col + 1) % 5]
        elif a_col == b_col:
            encrypted_text += matrix[(a_row + 1) % 5][a_col] + matrix[(b_row + 1) % 5][b_col]
        else:
            encrypted_text += matrix[a_row][b_col] + matrix[b_row][a_col]

    return encrypted_text




# Function to perform Playfair cipher decryption
def playfair_decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    ciphertext = ciphertext.upper().replace("J", "I")  # Replacing 'J' with 'I'
    ciphertext = "".join(filter(str.isalpha, ciphertext))
    if len(ciphertext) % 2 != 0:
        ciphertext += 'X'

    digraphs = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]

    decrypted_text = ""
    for digraph in digraphs:
        a, b = digraph[0], digraph[1]

        # Find positions of characters 'a' and 'b' in the matrix
        try:
            a_pos = [(i, row.index(a)) for i, row in enumerate(matrix) if a in row][0]
            b_pos = [(i, row.index(b)) for i, row in enumerate(matrix) if b in row][0]
        except IndexError:
            # If a character is not found in the matrix, handle the exception
            decrypted_text += digraph
            continue

        a_row, a_col = a_pos[0], a_pos[1]
        b_row, b_col = b_pos[0], b_pos[1]

        if a_row == b_row:
            decrypted_text += matrix[a_row][(a_col - 1) % 5] + matrix[b_row][(b_col - 1) % 5]
        elif a_col == b_col:
            decrypted_text += matrix[(a_row - 1) % 5][a_col] + matrix[(b_row - 1) % 5][b_col]
        else:
            decrypted_text += matrix[a_row][b_col] + matrix[b_row][a_col]

    return decrypted_text


def playfair_cipher_page():
    # Streamlit app
    st.title("Playfair Cipher Encryption and Decryption")

    text = st.text_input("Enter your text:")
    # key = st.text_input("Enter the keyword:").upper()
    key = st.text_input("Enter the keyword:", type='password').upper()
    option = st.radio("Choose an option:", ("Encrypt", "Decrypt"))

    result = ""
    if option == "Encrypt":
        result = playfair_encrypt(text, key);
        if st.button("Decryption of encrypted text"):  # Clearer button label
            output = playfair_decrypt(result,key);
            st.success(f"Decrypted Result: {output.lower()}")  # Specify "Decrypted Result"
    elif option == "Decrypt":
        result = playfair_decrypt(text, key);
        if st.button("Encryption of decrypted text"):  # Clearer button label
            output = playfair_encrypt(result,key)
            st.success(f"Decrypted Result: {output.lower()}")  # S

    if st.button("Show Result"):
        st.success(f"Result: {result.lower()}");

if __name__=="__main__":
    playfair_cipher_page();
