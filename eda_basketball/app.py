import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64

"# NBA Player Stats Explorer"

"""
This app performs simple webscraping of NBA player stats data!

- **Data source:** [Basketball-reference.com](https://www.basketball-reference.com)
"""

st.sidebar.header("User Input Features")
selected_year = st.sidebar.selectbox("Year", list(range(2023, 1949, -1)))


@st.cache_data
def load_data(year):
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html"
    html = pd.read_html(url, header=0)
    df = html[0]
    df.set_index("Rk", inplace=True)
    df.drop(df.index[df.index == "Rk"], inplace=True)
    df.fillna(0, inplace=True)
    return df


df = load_data(selected_year)

# Using sorted returns a list compared to .sort() which returns a series
sorted_teams = sorted(df.Tm.unique())
selected_teams = st.sidebar.multiselect("Team", sorted_teams, sorted_teams)


sorted_pos = sorted(df.Pos.unique())
selected_pos = st.sidebar.multiselect("Positions", sorted_pos, sorted_pos)

players = df[(df.Tm.isin(selected_teams)) & (df.Pos.isin(selected_pos))]


def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href


players

st.markdown(filedownload(players), unsafe_allow_html=True)
button = st.button("Intercorrelation Heatmap")
if button:
    "# Intercorrelation Matrix Heatmap"
    corr = df.corr(numeric_only=True)
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    st.pyplot(sns.heatmap(corr, mask=mask, vmax=1, square=True))
