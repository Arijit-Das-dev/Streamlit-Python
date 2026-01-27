import streamlit as st

col1, col2, col3, col4, col5 = st.columns(5)

with col1:

    st.selectbox(
    label="Select below",
    options=["A", "B", "C"],
    help="Select from the options",
    label_visibility="visible",
    index=None,
)

with col2:

    st.multiselect(
    label="Select below",
    options=["A", "B", "C", "D"],
    help="select the options",
    label_visibility="visible",
    
) 

with col3:

    st.radio(

        label="Select the options below",
        options=["A", "B", "C", "D"],
        label_visibility="visible",
        help="Select from the options",
        index=None
)

with col4:

    st.checkbox(
    "Accept Terms & Conditions",
    value=False
)