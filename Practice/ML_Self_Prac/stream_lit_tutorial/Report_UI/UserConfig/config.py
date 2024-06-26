
class UI_MetaData:
    LOCAL_PATH = r"D:\Version_Controlled\Code_Base\Practice\ML_Self_Prac\stream_lit_tutorial\Report_UI\UserConfig\config.py"
    PROJECT_NAME = "International Reporting Service"
    USER_INFO = {
                    "DRIVE_PATH":"",
                    "ENVIRONMENT":""
                }
    ENVIRONMENT_CONFIGS = {
        "TEST":{"REPORT_CONFIG":"path",
                "TEMPLATE_PATH":"path",
                "ENV_ID":"vgi-ics-test",
                "SETUP_COMMAND":"xyz",
                "REMOTE_CONFIG_PATH":"D:\Version_Controlled\Code_Base\Practice\ML_Self_Prac\stream_lit_tutorial\Report_UI\TEST_Cloud"
            
            },
            

        "PROD":{"REPORT_CONFIG":"path",
                "TEMPLATE_PATH":"path",
                "ENV_ID":"vgi-ics-prod",
                "SETUP_COMMAND":"abc",
                "REMOTE_CONFIG_PATH":"D:\Version_Controlled\Code_Base\Practice\ML_Self_Prac\stream_lit_tutorial\Report_UI\PROD_Cloud"
            }
        }
    # PAGES = {
    #     "report_selection.py":{
    #         "INCLUDE_PATH":f"""D:\Version_Controlled\Code_Base\Practice\ML_Self_Prac\stream_lit_tutorial\Report_UI\{DRIVE_PATH}\Cloud\App_Files\pages""",
    #         "EXCLUDE_PATH":f"D:\Version_Controlled\Code_Base\Practice\ML_Self_Prac\stream_lit_tutorial\Report_UI\{DRIVE_PATH}\Cloud"
    #     }
    # }

    def __init__(self) -> None:
        self.local_env = ""