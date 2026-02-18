import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

from numpy.random import default_rng as rng
from dotenv import load_dotenv
from pull_annual_transit_data import pull_sheet_data
from graphs import annual_transit_bar
load_dotenv()

## Default data sheet info
SPREADSHEET_NAME = "Copy of 24-25 shuttle ridership" 
WORKSHEET_NAME = "24-25 Totals" 
CREDENTIALS_FILE = "../ucsc-transit-dashboard-credentials.json"
limited_1 = "Science Hill Limited (ER)"
limited_2 = "Science Hill Limited (WR)"
limited_total = "Science Hill Limited Total"

    
st.set_page_config(page_title="UCSC TAPS Transportation Dashboard", page_icon=":bar_chart:", layout="wide")

st.title(" :bar_chart: UCSC TAPS Transportation Dashboard", width="stretch", text_alignment="left")
st.markdown('<style>div.block-container{padding-top:2rem;}</style>',unsafe_allow_html=True)

# st.header("Live operational metrics", divider="gray", width="stretch", text_alignment="left")
st.subheader("UC Santa Cruz - Operational metrics", divider="gray", width="stretch", text_alignment="left")
st.markdown('''Transportation and Parking Services (TAPS) supports the University’s mission by providing access to UC Santa Cruz,  
                acting as fiscal stewards, and managing the sustainable planning, design, and operation of safe and equitable  
                bicycle/pedestrian programs, transit services, parking, and other transportation-related needs.  ''')
st.markdown(''' This dashboard displays the current and historical ridership numbers across all Transit services.''')


# st.markdown("*Streamlit* is **really** ***cool***.")
# st.markdown('''
#     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
#     :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
# st.markdown("Here's a bouquet &mdash;\
#             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# multi = '''If you end a line with two spaces,
# a soft return is used for the next line.

# Two (or more) newline characters in a row will result in a hard return.
# '''
# st.markdown(multi)

st.divider()

with st.container():
    # st.write("This is inside the container")

    option = st.selectbox(
        "Transit Year",
        ["24-25 Totals", "25-26 Totals"],
        index=None,
        placeholder="24-25 Totals",
        accept_new_options=False)

    if option == "24-25 Totals":
        print(option)

    elif option == "25-26 Totals":
        print(option)
        SPREADSHEET_NAME = "Copy of 25-26 shuttle ridership" 
        WORKSHEET_NAME = "25-26 Totals"
        limited_1 = "Upper Campus Limited 1"
        limited_2 = "Upper Campus Limited 2"
        limited_total = "Upper Campus Limited Total"


# transit_totals_full_df = pull_sheet_data(SPREADSHEET_NAME, WORKSHEET_NAME, CREDENTIALS_FILE)
fig2, fig_pie = annual_transit_bar(SPREADSHEET_NAME, WORKSHEET_NAME, CREDENTIALS_FILE, limited_1, limited_2, limited_total)

col1, col2 = st.columns([0.35, 0.65], gap="small", vertical_alignment="top", border=False, width="stretch")

with col1:
    st.header("Overall Ridership split")
    st.plotly_chart(fig_pie, use_container_width=True)
    st.caption("This is a string that explains something above.")
    

with col2:
    st.header("Monthly Transit Ridership")   
    # # Display the chart in Streamlit
    st.plotly_chart(fig2, width='stretch')
    st.caption("This is a string that explains something above.")






