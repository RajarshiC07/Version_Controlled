import sys
from streamlit.web import cli as stcli
import streamlit as st
import joblib
import os

class Setup:
    LOCAL_CONFIG_PATH = r""
    DRIVE_SETUP_PATH = r""
    def __init__(self) -> None:
        pass

    def check_local_config_exists(self):
        try:
            config_file = joblib.load(r"D:\Version_Controlled\Code_Base\Practice\ML_Self_Prac\stream_lit_tutorial\Report_UI\UserConfig\user_config.joblib")
        except Exception as e:
            print(e)
            raise

    def check_drive_path_exists(self):
        return os.path.exists(self.DRIVE_SETUP_PATH)
        

    def initiate_local_config(self):
        pass


def fetch_local_config():
    path = r"D:\Version_Controlled\Code_Base\Practice\ML_Self_Prac\stream_lit_tutorial\Report_UI\UserConfig\UserConfig"
    obj = None
    try:
        obj = joblib.load(path)
    except Exception:
        print(f"Not found")
        return obj


if __name__ == '__main__':
    
    # config_obj = fetch_local_config()
    # if not config_obj:
    #     pass
    sys.argv = ["streamlit", "run", r"D:\Version_Controlled\Code_Base\Practice\ML_Self_Prac\stream_lit_tutorial\Report_UI\UserConfig\configuration.py"]
    sys.exit(stcli.main())