import pandas as pd
import streamlit as st
st.set_page_config(layout='wide')
import streamlit as st
import json
# st.cache_data
def get_layout(options, report_list):
    if options:
        tabs = list(st.tabs(options))
        command = dict()
        print(tabs)
        for tab, option in zip(tabs, options):
            with tab:
                # for option in options:
                    
                data_set = report_list.get(option)
                primary_data = dict()
                selected = dict()
                date_chosen = dict()
                for key, value in data_set.items():
                    primary_data[key] = []
                    date_chosen = {}
                    if "DATE" in key.upper():
                        date_chosen[key] = st.date_input("Enter the date", key=f"{option}-{key}")
                        # st.write(date_chosen[key])

                    else:
                        st.write(key)
                        selected = {}
                        for fields in value:
                            selected[fields] = st.checkbox(fields, disabled=False, key=f"{option}-{key}-{fields}")
                command[option] = st.button("Filter", key=option)
                if command:
                    print(selected)
                    print(date_chosen)
                    tabs.pop(tabs.index(tab))
                    options.pop(option.index(option))
                    continue



with open(r"D:\python projects\ML_Self_Prac\stream_lit_tutorial\Report_UI\config.json","r") as file:
    report_list = json.load(file)

col1, col2 = st.columns([5,2])


report_names = list(report_list.keys())
option = st.sidebar.multiselect(
   "Report Name",
   report_names,
   placeholder="Select Report...",
)
report_chosen = st.sidebar.button("Proceed")
# st.write('You selected:', option)

with col1:
    st.markdown('''
        # :blue[International Report Service ]
        ## :yellow[Report Selection Window]
    ''')
    if report_chosen:
            get_layout(option, report_list)




