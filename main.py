import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo(2).png")

with col2:
    st.title("Subhojit Guin")
    content = """Hi, I am Subhojit Guin! 
    I am a Python programmer. Highly motivated and dedicated student pursuing a B.Tech in Computer Science and Engineering, seeking an opportunity to apply my skills and knowledge in a dynamic and challenging environment. Eager to contribute to innovative projects, gain practical experience, and make a positive impact in the field of technology. """

    st.info(content)

content2 = """
Below, you will find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)
