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
load_dotenv()

## Default data sheet info
SPREADSHEET_NAME = "Copy of 24-25 shuttle ridership" 
WORKSHEET_NAME = "24-25 Totals" 
CREDENTIALS_FILE = "ucsc-transit-dashboard-credentials.json"

    # print(transit_24_25_totals_full_df)
    # custom_order = ['July 2024', 'August 2024', 'September 2024','October 2024', 'November 2024','December 2024', 'January 2025', 'February 2025', 'March 2025', 'April 2025', 'May 2025', 'June 2025']
    # transit_24_25_totals_full_df['Date'] = pd.Categorical(transit_24_25_totals_full_df['Date'], categories=custom_order, ordered=True)
    # transit_24_25_totals_full_df = transit_24_25_totals_full_df.sort_values('Date')






st.set_page_config(page_title="UCSC Transit Dashboard", page_icon=":bar_chart:", layout="wide")

st.title(" :bar_chart: UCSC Transit Dashboard", width="stretch", text_alignment="left")
st.markdown('<style>div.block-container{padding-top:2rem;}</style>',unsafe_allow_html=True)

st.header("This is a header with a divider", divider="gray", width="stretch", text_alignment="left")
st.subheader("This is a subheader with a divider", divider="gray", width="stretch", text_alignment="left")
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

st.divider()


# df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

col1, col2 = st.columns([0.2, 0.8], gap="small", vertical_alignment="top", border=False, width="stretch")

with col1:
    st.header("A cat")

    st.caption("This is a string that explains something above.")
    

with col2:
    st.header("Annual Transit passenger numbers")
    with st.container():
        # st.write("This is inside the container")
        colors = px.colors.qualitative.Plotly 

        option = st.selectbox(
            "Transit Year",
            ["24-25 Totals", "25-26 Totals"],
            index=None,
            placeholder="24-25 Totals",
            accept_new_options=False)

        if option == "24-25 Totals":
            print(option)
        elif option == "25-26 Totals":
            SPREADSHEET_NAME = "Copy of 25-26 shuttle ridership" 
            WORKSHEET_NAME = "25-26 Totals"
                
        if __name__ == "__main__":
            transit_totals_df = pull_sheet_data(SPREADSHEET_NAME, WORKSHEET_NAME, CREDENTIALS_FILE)

            # 2. Create the figure and add the trace
            fig2 = go.Figure(data=[
                go.Bar(name="EG_Total",x=transit_totals_df["Date"], y=transit_totals_df['EG_Total'], marker_color=colors[0]),
                go.Bar(name="BT_Total",x=transit_totals_df["Date"], y=transit_totals_df['BT_Total'], marker_color=colors[1]),
                go.Bar(name="Night Total",x=transit_totals_df["Date"], y=transit_totals_df['Night Total'], marker_color=colors[2]),
                go.Bar(name="UC Total",x=transit_totals_df["Date"], y=transit_totals_df['UC Total'], marker_color=colors[3]),
                go.Bar(name="Upper Campus Limited (ER)",x=transit_totals_df["Date"], y=transit_totals_df['Upper Campus Limited (ER)'], marker_color=colors[4]),
                go.Bar(name="Upper Campus Limited (WR)",x=transit_totals_df["Date"], y=transit_totals_df['Upper Campus Limited (WR)'], marker_color=colors[5]),
                go.Bar(name="Bike Shuttle Total",x=transit_totals_df["Date"], y=transit_totals_df['Bike Shuttle Total'], marker_color=colors[6]),
                go.Bar(name="SVC Shuttle",x=transit_totals_df["Date"], y=transit_totals_df['SVC Shuttle'], marker_color=colors[7]),
                go.Bar(name="BT_Total",x=transit_totals_df["Date"], y=transit_totals_df['WSC Shuttle'], marker_color=colors[8]),
                
                ])
            fig2.update_layout(barmode='stack', title='Stacked Bar Chart')


        # # Display the chart in Streamlit
        st.plotly_chart(fig2, use_container_width=True)
        st.caption("This is a string that explains something above.")






