import streamlit as st
import os, string
import joblib
import json
import shutil
import config as configUI
import importlib
import sys
import pickle

config = configUI.UI_MetaData()
def get_drive_list():
    available_drives = ['%s:' % d for d in string.ascii_uppercase if not os.path.exists('%s:' % d)]
    return available_drives


def execute_command(environment, drive):
    #need to execute command
    source_path = rf"D:\Version_Controlled\Code_Base\Practice\ML_Self_Prac\stream_lit_tutorial\Report_UI\{environment}_Cloud"
    destination_path = rf"D:\Version_Controlled\Code_Base\Practice\ML_Self_Prac\stream_lit_tutorial\Report_UI\{drive}\{environment}_Cloud"
    shutil.move(source_path, destination_path)



def initiate_local_drive():
    config.USER_INFO["DRIVE_PATH"] = st.session_state.get("DRIVE")
    config.USER_INFO["ENVIRONMENT"] = st.session_state.get("ENVIRONMENT")
    print(config.USER_INFO)
    try:
        with open("LOCAL_USER_CONFIG.json", "r") as file:
            LOCAL_USER_CONFIG = json.load(file)
            print("Loading json file")
            print(LOCAL_USER_CONFIG)
    except Exception as e:
        print(e)
        LOCAL_USER_CONFIG = dict()
    LOCAL_USER_CONFIG["ENVIRONMENT_DETAILS"][config.USER_INFO.get("ENVIRONMENT")] = config.USER_INFO.get("DRIVE_PATH")
    with open("LOCAL_USER_CONFIG.json", "w+") as file:
        json.dump(LOCAL_USER_CONFIG, file)
    


def configure():
    col1, col2 = st.columns([5,1])

    with col1:
        st.header("""**International Internal Reporting Service**""")
        caption_list = [details.get("ENV_ID") for env, details in config.ENVIRONMENT_CONFIGS.items()]
        option = st.radio("# :blue[Select the environment you want to configure]", options=config.ENVIRONMENT_CONFIGS.keys(),horizontal=True, captions=caption_list)
        activation_status = False
        drive_setup = st.selectbox("Choose the drive you want to configure from the following",options=get_drive_list())
        submit_button = st.button("Configure", disabled=activation_status)
        print(drive_setup, option)
        if submit_button:
            st.session_state["ENVIRONMENT"] = option
            st.session_state["DRIVE"] = drive_setup
            initiate_local_drive()
    return

configure()

# with open(r"D:\Version_Controlled\Code_Base\Practice\ML_Self_Prac\stream_lit_tutorial\Report_UI\USER_CONFIG", "rb") as reader:
#     obj = pickle.load(reader)

# print(obj)
