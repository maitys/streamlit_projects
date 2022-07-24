# # Contents of ~/my_app/main_page.py
# import streamlit as st
# import pandas as pd
# from st_aggrid import AgGrid, JsCode
# from st_aggrid.grid_options_builder import GridOptionsBuilder

# st.set_page_config(page_title="Ag Grid Testing", page_icon="🔍", layout="wide", initial_sidebar_state="expanded")
# st.markdown("# Main page 🎈")
# st.sidebar.title("Testing")

# df_ad_table1 = pd.read_csv("ad_table1.csv")
# df_ad_table1["Date"] = pd.to_datetime(df_ad_table1["Date"])
# # st.title("Streamlit Dataframe")
# # st.dataframe(df_ad_table1)

# st.title("Ag Grid Dataframe")

# # Set customizations
# gd = GridOptionsBuilder.from_dataframe(df_ad_table1)
# gd.configure_pagination(enabled=True, paginationAutoPageSize=True, paginationPageSize=10)
# gd.configure_default_column(min_column_width=100, resizable=True)

# # format Site Pred to whole number with commas

# # format to comma separated numbers
# # gd.configure_column("Site Pred", type=["customNumericFormat"], precision=2, )



# gridoptions = gd.build()

# # cellstyle_jscode = JsCode(

# # available_themes = ["streamlit", "light", "dark", "blue", "fresh", "material"]
# AgGrid(df_ad_table1, gridOptions=gridoptions, theme="dark", fit_columns_on_grid_load=True, height=350,allow_unsafe_jscode=True)


#         # filter1 = df_ad_fc["site_flag"]=="yes_negative"       
#         # df_ad_table1 = df_ad_fc[filter1][["date", "site_actual", "site_pred", "site_lower", "site_upper", "site_importance", "cohort_actual", "cohort_pred", "cohort_flag"]].sort_values(by=["date"], ascending=False).head(10)               
#         # df_ad_table1 = df_ad_table1.rename(columns={"site_importance": "anomaly_importance"})
#         # df_ad_table1.columns = [x.replace("_", " ") for x in df_ad_table1.columns]
#         # df_ad_table1.columns = df_ad_table1.columns.str.title()
        
        
#         # gd = GridOptionsBuilder.from_dataframe(df_ad_table1)
#         # gd.configure_pagination(enabled=True, paginationAutoPageSize=True, paginationPageSize=10)
#         # #gd.configure_default_column(min_column_width=100, resizable=True)
        
#         # gridoptions = gd.build()
        
#         # # available_themes = ["streamlit", "light", "dark", "blue", "fresh", "material"]
#         # AgGrid(df_ad_table1, gridOptions=gridoptions, theme="fresh", fit_columns_on_grid_load=True


import streamlit as st
from datetime import datetime

if "default_checkbox_value" not in st.session_state:
    st.session_state["default_checkbox_value"] = False
    st.session_state["form_key"] = f"data_approval{str(datetime.now())}"

if st.button("Select All"):
    st.session_state["default_checkbox_value"] = True
    st.session_state["form_key"] = f"data_approval{str(datetime.now())}"
if st.button("Deselect All"):
    st.session_state["default_checkbox_value"] = False
    st.session_state["form_key"] = f"data_approval{str(datetime.now())}"

checkbox_statusses = []
with st.form(key=st.session_state["form_key"]):

    checkbox_statusses.extend(
        st.checkbox(
            "select",
            key=str(i),
            value=st.session_state["default_checkbox_value"],
        )
        for i in range(5)
    )

    approve_button = st.form_submit_button(label="Do Something")


if approve_button:
    if any(checkbox_statusses):
        st.header("You selected some checkboxes!")
    else:
        st.warning("No selectboxes selected!")