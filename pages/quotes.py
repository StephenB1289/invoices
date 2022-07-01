import streamlit as st
from pdf_templates import quote
import pricing

st.title('Quotes')

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    col1, col2, col3 = st.columns(3)

    with col1:
        name = st.text_input('Customer Name:')
        labor = st.number_input('Labor:', min_value = 0, max_value = 1, step = 1, value = 0)
        hours = st.number_input('Print hours:', min_value = 0, step = 1, value = 0)

    with col2:
        lab = st.text_input('Customer Lab:')
        minutes = st.number_input('Print minutes:', min_value = 0, max_value = 60, step = 1, value = 0)

    with col3:
        consulting = st.number_input('Consulting:', min_value= 0.0, step = 0.5, value = 0.0)
        processing = st.number_input('Post-Processing:', min_value = 0.0, step = 0.5, value = 0.0)

    materials = st.multiselect('Materials used:', pricing.materials.keys())

    col4, col5, col6 = st.columns(3)

    for i, resin in enumerate(materials):
        if i % 3 == 0:
            with col4:
                st.number_input(resin, min_value = 0, step = 1, value = 0, key = resin)
        elif i % 3 == 1:
            with col5:
                st.number_input(resin, min_value = 0, step = 1, value = 0, key = resin)
        else:
            with col6:
                st.number_input(resin, min_value = 0, step = 1, value = 0, key = resin)

    run = st.button('Generate Quote')

    if run:
        details = (name, lab)

        charges = [
            ['Labor', pricing.core['Labor'], labor, labor*pricing.core['Labor']],
            ['Consulting', pricing.core['Consulting'], consulting, consulting*pricing.core['Consulting']],
            ['Post-processing', pricing.core['Processing'], processing, processing*pricing.core['Processing']],
            ['Print time', pricing.core['Printing'], (hours + minutes/60), (hours + minutes/60)*pricing.core['Printing']]
        ]

        for resin in materials:
            charges.append([resin, pricing.materials[resin], st.session_state[resin], st.session_state[resin]*pricing.materials[resin]])

        pdf = quote()
        pdf.generate_quote(details, charges)

        st.success('Great success!')
        st.balloons()

        with open(f'{name}_quote.pdf', 'rb') as file:
            st.download_button('Download PDF', data = file, file_name = f'{name}_quote.pdf')