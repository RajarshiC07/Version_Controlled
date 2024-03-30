import streamlit as st
import joblib
import json

def initiation():
    col1, col2 = st.columns([8,1])
    with open(r"D:\Version_Controlled\Code_Base\Practice\ML_Self_Prac\stream_lit_tutorial\CONFIG.json") as file:
        config = json.load(file)


    with col1:
        st.title(config.get("PROJECT_NAME"))
        st.image(image=r"Report_UI\download.png", caption="Vanguard", use_column_width=True)
        


initiation()