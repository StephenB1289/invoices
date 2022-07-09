from numpy import NaN
import streamlit as st
from google.oauth2 import service_account
import pygsheets

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)

client = pygsheets.authorize(custom_credentials = credentials)

sheet = client.open_by_url(st.secrets['sheet_url'])

data = sheet.sheet1.get_as_df(empty_value = 0)

