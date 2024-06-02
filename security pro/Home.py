import streamlit as st
from pages import affinecipher, Caesar_Cipher, Rail_Fence_Cipher, Vigenere_Cipher, Playfair_Cipher,Documentation,Hashing;
import streamlit as st
import pandas as pd
import altair as alt

# Hide Streamlit's default menu

st.set_page_config(initial_sidebar_state='collapsed')

selected_option = st.sidebar.selectbox("Search Ciphers", ("Home","affinecipher" ,"Caesar_Cipher","Hashing", "PlayFair_Cipher", "Rail_Fence_Cipher", "Vigenere_Cipher"))

# Display content based on selected option

if selected_option == "Home":
    # Page title with custom styling
    st.markdown(
        """
        <style>
            .title {
                font-size: 36px;
                color: #3366cc;
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


    # Animated title with custom styling and JavaScript
    st.markdown(
        """
        <style>
            @keyframes colorChange {
                0% { color: #ff0000; }
                25% { color: #00ff00; }
                50% { color: #0000ff; }
                75% { color: #ff00ff; }
                100% { color: #ffff00; }
            }

            .animated-title {
                animation: colorChange 5s linear infinite;
                text-align: center;
            }
        </style>
        <script>
            setInterval(function() {
                const title = document.querySelector('.animated-title');
                title.style.animation = 'none';
                title.offsetHeight; /* trigger reflow */
                title.style.animation = null;
            }, 5000);
        </script>
        """,
        unsafe_allow_html=True
    )

    # Display the balloon animation for the title


    # Display the animated title at the top center
    st.markdown('<h1 class="animated-title title">CryptifyHub</h1>', unsafe_allow_html=True)

    # Display the introductory text below the title
    st.markdown(
        """
        <div class="animated-title">
            <p>Welcome to CryptifyHub! </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    selected_cipher = st.session_state.get("selected_cipher", None)

    if selected_cipher is None:  # Show the home page
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            st.header("List of Ciphers:")
            ciphers = ["Caesar Cipher", "Vigenere Cipher", "Affine Cipher","Hashing", "Playfair Cipher", "Rail Fence Cipher",
                       "Documentation"]
            for cipher in ciphers:
                if st.button(cipher, key=cipher):
                    st.session_state.selected_cipher = cipher;
                    st.experimental_rerun();
        with col3:
            st.markdown('<h2>Popularity of Cipher Techniques</h2>', unsafe_allow_html=True)

            cipher_data = pd.DataFrame({
                'Cipher': ["Caesar", "Vigenere", "Affine", "Playfair", "Rail fence","hashing"],
                'Popularity': [30, 25, 20, 15, 27,35]  # Example data (you can replace with actual data)
            })

        bar_chart = alt.Chart(cipher_data).mark_bar().encode(
                x='Cipher:O',
                y='Popularity:Q'
            ).properties(
                width=400,
                height=300
            )

        col3.altair_chart(bar_chart, use_container_width=True);



            # ... (your code for the popularity chart)

    else:  # Show the selected cipher page
        if st.button("Back to Main Menu"):
            st.session_state.selected_cipher = None
            st.experimental_rerun();
        elif selected_cipher == "Caesar Cipher":
            Caesar_Cipher.Caesarcipher_page()
        elif selected_cipher == "Vigenere Cipher":
            Vigenere_Cipher.vigenere_cipher_page()
        elif selected_cipher == "Affine Cipher":
            affinecipher.affinecipher_page()
        elif selected_cipher == "Playfair Cipher":
            Playfair_Cipher.playfair_cipher_page()
        elif selected_cipher == "Documentation":
            Documentation.documentation_page()
        elif selected_cipher == "Rail Fence Cipher":
            Rail_Fence_Cipher.rail_fence_page();
        elif selected_cipher == "Hashing":
            Hashing.hash_page_algo();
        else:
            st.error("Invalid cipher selected.")

elif selected_option == "affinecipher":
    affinecipher.affinecipher_page()
elif selected_option == "Caesar_Cipher":
    Caesar_Cipher.Caesarcipher_page();
elif selected_option == "Vigenere_Cipher":
    Vigenere_Cipher.vigenere_cipher_page();
elif selected_option == "PlayFair_Cipher":
    Playfair_Cipher.playfair_cipher_page();
elif selected_option == "Rail_Fence_Cipher":
    Rail_Fence_Cipher.rail_fence_page();
elif selected_option=="Hashing":
    Hashing.hash_page_algo();
