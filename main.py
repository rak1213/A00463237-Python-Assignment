import streamlit as st
from streamlit_apps.coin_detail import show_app_crypto_detail
from streamlit_apps.coin_comparison import show_app_crypto_comparison
from streamlit_apps.digit_classifier import show_app_digit_classifier


# Navigation
app_selection = st.sidebar.radio("Go to", ['Crypto App', 'Digit Classifier'])

if app_selection == 'Crypto App':
    tab1, tab2 = st.tabs(["Coin Detail", "Coin Comparison"])
    with tab1:
        show_app_crypto_detail()

    with tab2:
        show_app_crypto_comparison()
elif app_selection == 'Digit Classifier':
    show_app_digit_classifier()


