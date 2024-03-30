import joblib
class UI_MetaData:
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
                "CONFIG_PATH":"D:\Version_Controlled\Code_Base\Practice\ML_Self_Prac\stream_lit_tutorial\Report_UI\TEST_Cloud\config.py"
            
            },
            

        "PROD":{"REPORT_CONFIG":"path",
                "TEMPLATE_PATH":"path",
                "ENV_ID":"vgi-ics-prod",
                "SETUP_COMMAND":"abc",
                "CONFIG_PATH":"D:\Version_Controlled\Code_Base\Practice\ML_Self_Prac\stream_lit_tutorial\Report_UI\PROD_Cloud\config.py"
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