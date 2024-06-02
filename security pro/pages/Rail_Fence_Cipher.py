import streamlit as st

def rail_fence_encrypt(text, rails):
    text = text.replace(" ", "").upper()

    if not rails:  # Handle empty rails input
        st.error("Please enter a valid number of rails.")
        return ""

    fence = [''] * int(rails)
    direction = -1
    row = 0

    for char in text:
        fence[row] += char
        if row == 0 or row == int(rails) - 1:
            direction *= -1
        row += direction

    encrypted_text = ''.join(fence)
    return encrypted_text

def rail_fence_decrypt(text, rails):
    text = text.replace(" ", "").upper()

    if not rails:  # Handle empty rails input
        st.error("Please enter a valid number of rails.")
        return ""

    fence = [''] * int(rails)
    direction = -1
    row = 0
    index = 0

    for char in text:
        fence[row] += '*'
        if row == 0 or row == int(rails) - 1:
            direction *= -1
        row += direction

    for i in range(int(rails)):
        for j in range(len(fence[i])):
            if index < len(text) and fence[i][j] == '*':
                fence[i] = fence[i][:j] + text[index] + fence[i][j+1:]
                index += 1

    direction = -1
    row = 0
    decrypted_text = ''
    for _ in range(len(text)):
        decrypted_text += fence[row][0]
        fence[row] = fence[row][1:]
        if row == 0 or row == int(rails) - 1:
            direction *= -1
        row += direction

    return decrypted_text

def rail_fence_page():
    st.title("Rail Fence Cipher Encryption and Decryption")

    text = st.text_input("Enter your text:")
    rails = st.text_input("Enter the number of rails:", type='password')

    # Convert rails to int only if it's not empty
    rails = int(rails) if rails else 0

    option = st.radio("Choose an option:", ("Encrypt", "Decrypt"))

    result = ""
    if option == "Encrypt":
        result = rail_fence_encrypt(text, rails);
        if st.button("Decryption of encrypted text"):  # Clearer button label
            output = rail_fence_decrypt(result,rails);
            st.success(f"Decrypted Result: {output.lower()}")  # Specify "Decrypted Result"
    elif option == "Decrypt":
        result = rail_fence_decrypt(text, rails);
        if st.button("Encryption of decrypted text"):  # Clearer button label
            output = rail_fence_encrypt(result,rails);
            st.success(f"Decrypted Result: {output.lower()}") ;

    if st.button("Show Result"):
        st.success(f"Result: {result.lower()}")

if __name__=="__main__":
    rail_fence_page();
