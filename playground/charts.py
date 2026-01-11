import streamlit as st
import pandas as pd
import numpy as np

st.title("this is for charts")

st.write("Visulization of data charts in streamlit")

all_users = ["Alex", "Bob", "Charlie", "David"]

with st.container(border=True):
    users = st.multiselect("Select users", all_users, default=all_users)
    #st.write("You selected:", users)


    tg = st.toggle("Moving Average", value=True)
    win = st.slider("Window Size", min_value=1, max_value=20, value=5)

np.random.seed(42)
data = pd.DataFrame(np.random.rand(100, len(users)), columns=users)


if tg:
    data = data.rolling(window=win).mean()

tab1 , tab2 = st.tabs(["Line Chart", "Area Chart"])
with tab1:
    st.line_chart(data)
with tab2:
    st.area_chart(data)


# learning outcomes
# -- add dataframe
# -- add visualization (line chart, area chart)
# -- add container with border
# -- add multiselect