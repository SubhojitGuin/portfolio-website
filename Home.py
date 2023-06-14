import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo(2).png")

with col2:
    st.title("Subhojit Guin")
    content = """
    Hi, I am Subhojit Guin! I am a Python programmer who is highly 
    motivated and dedicated to the field of study I am interested in. As a 
    student at the Institute of Engineering & Management, Kolkata, I am pursuing
     a Bachelor of Technology in Computer Science and Engineering to apply  my 
     skills and knowledge in a dynamic and challenging environment. I am eager 
     to contribute to innovative projects, gain practical experience, and 
     positively impact technology. My passion for programming and dedication 
     to my work makes me an asset to any team. I am confident that I can use 
     my enthusiasm and expertise to help build successful projects that will 
     have a lasting impact. I am open to learning new skills and am always 
     looking for ways to improve my knowledge. In addition, I am committed to 
     working collaboratively with colleagues to achieve the team's goals. 
     """
    st.info(content)

content2 = """
Below, you will find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, rows in df[:10].iterrows():
        st.header(rows["title"])
        st.write(rows["description"])
        st.image(f"images/{rows['image']}")
        st.write(f"[Source Code]({rows['url']})")

with col4:
    for index, rows in df[10:].iterrows():
        st.header(rows["title"])
        st.write(rows["description"])
        st.image(f"images/{rows['image']}")
        st.write(f"[Source Code]({rows['url']})")
