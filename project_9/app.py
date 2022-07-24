################
#### TEST 1 ####
################
# from tkinter.font import families
# import streamlit as st
# from streamlit_option_menu import option_menu

# with st.sidebar:
#     choose = option_menu(menu_title="Select Page", 
#                          options=["Topline", "Device", "Media Type", "Device & Media Type", "Traffic Source", "Country", "Browser"],
#                          icons=['bookmark-fill']*7,
#                          menu_icon="app-indicator", default_index=0,
#                          styles={"container": {"padding": "5!important", "background-color": "silver"},
#                                  "icon": {"color": "black", "font-size": "14px"},
#                                  "nav-link": {"font-size": "17px", "text-align": "left", "margin": "0px", "--hover-color": "olive"},
#                                  "nav-link-selected": {"background-color": "forestgreen"},
#                                  "seperator": {"border-top": "1px solid #02ab21", "margin": "0px", "padding": "0px"}})

# name = "Siddharth"

# if choose == "Topline":
#     st.title("Topline: {}".format(name))

# elif choose == "Device":
#     st.title("Device: {}".format(name))
    
# elif choose == "Media Type":
#     st.title("Media Type: {}".format(name))
    
# elif choose == "Device & Media Type":
#     st.title("Device & Media Type: {}".format(name))
    
# elif choose == "Traffic Source":
#     st.title("Traffic Source: {}".format(name))
    
# elif choose == "Country":
#     st.title("Country: {}".format(name))
    
# elif choose == "Browser":
#     st.title("Browser: {}".format(name))

################
#### TEST 2 ####
################
# import streamlit as st
# with st.sidebar.form("Input"):
#     queryText = st.text_area("Site to Run:", height=3, max_chars=None)
#     btnResult = st.form_submit_button('Run')

# if btnResult:
#     st.sidebar.text('Button pushed')

#     # run query
#     st.write("Running query for: {}".format(queryText))

################
#### TEST 3 ####
################
import streamlit as st
form = st.form("my_form")
cols = form.columns((1,1,1))
x = cols[0].slider("x")
y = cols[1].slider("y")
z = cols[2].slider("z")

# Now add a submit button to the form:
form.form_submit_button("Submit")

st.write(x)
st.write(y)
st.write(z)