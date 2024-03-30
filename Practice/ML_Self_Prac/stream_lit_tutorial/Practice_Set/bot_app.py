import streamlit as st
import pandas as pd
# st.header("Welcome to RadCorp")

st.header("""Welcome to **RAD**.""")
st.markdown('''
    # :blue[Enter the path you want to traverse]
   ''')

value = st.text_area(label = "Enter your text here",placeholder="Capg to Accen")
# path = "digraph{"+f"""{value.replace("to"," -> ")}"""+"}"
# st.graphviz_chart(path)

city = pd.DataFrame({
    "Lovers" : ["Mani", "Jaleel", "Arun"],
    "lat" : [13.212323, 13.312313, 4.562323],
    "lon" :[80.123242, 80.234341, 11.834576]
})

st.map(city, color = "#FFC0CB")