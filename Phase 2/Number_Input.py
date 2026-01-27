import streamlit as st

st.number_input(

    label="Age",
    min_value=19,
    max_value=100,
    help="Age must contain withing 19 to 100",
    disabled=False,
    step=1,
    icon="🔞"
)

st.slider(

    label="Enter range",
    min_value=1,
    step=1,
    max_value=100
)
