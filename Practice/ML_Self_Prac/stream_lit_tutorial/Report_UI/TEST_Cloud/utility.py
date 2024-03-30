import shutil
import json
from UserConfig.config import UI_MetaData
def reset():
    pass
    # session_object = 
    #         shutil.move()

def transfer(page_name: str, source_path: str, destination_path:str,  *args, **kaargs):
    try:
        print(f"{source_path}\{page_name} \n {destination_path} \n {page_name}")
        shutil.move(f"{source_path}\{page_name}", f"{destination_path}")
    except Exception:
        print("File not found")


def path_allotment(include = True, exclude = False):
    if include:
        return "EXCLUDE_PATH", "INCLUDE_PATH"
    if exclude:
        return "INCLUDE_PATH", "EXCLUDE_PATH"


def transfer_process(specific_page = None, include = True, exclude = False, *args, **kaargs):
    config_object =  UI_MetaData().PAGES
    source_path, destination_path = path_allotment(include, exclude)
    if not specific_page:
        transfer(specific_page, source_path=config_object.get(specific_page).get(source_path),destination_path=config_object.get(specific_page).get(destination_path))
    else:
        for page, paths in config_object.items():
            transfer(page, source_path=paths.get(source_path),destination_path=paths.get( destination_path))
    return f"Transferred"


def include_page(specific_page = None, *args, **kaargs):
    return transfer_process(specific_page=specific_page, include=True, exclude=False)


def exclude_page(specific_page = None, *args, **kaargs):
    return transfer_process(specific_page=specific_page, include=False, exclude=True)



# exclude_page(f"report_selection.py")





