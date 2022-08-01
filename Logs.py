import streamlit as st
from google.oauth2 import service_account
import pygsheets
from datetime import date
import pandas as pd
import numpy as np

def get_num(prev):
    today = date.today()

    start = f'Inv{today.year}{today.month:02d}'

    if prev[:9] == start:
        num = 1 + int(prev[10:])
    else:
        num = 1

    number = start + f'_{num:02d}'

    return number

def insert(details, charges):

    credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
    )

    client = pygsheets.authorize(custom_credentials = credentials)

    sheet = client.open_by_url(st.secrets['sheet_url'])

    data = sheet.sheet1.get_as_df(empty_value = 0)

    if np.any(data['Invoice'].values):
        last_num = data['Invoice'].values[-1]
    else:
        last_num = ''

    number = get_num(last_num)

    values = {
        'Invoice': number,
        'Name': details[0],
        'Date': date.today(),
        'Lab': details[1],
        'Account #': details[2]}

    mat_cost, print_cost, core_cost = 0, 0, 0

    for charge in charges:
        values[charge[0]] = charge[2]

        if charge[0] in ['Labor', 'Consulting', 'Post-Processing']:
            core_cost += charge[3]
        elif charge[0] == 'Print Time':
            print_cost = charge[3]
        else:
            mat_cost += charge[3]


    values['Material Cost'] = mat_cost
    values['Printer Cost'] = print_cost
    values['Core Cost'] = core_cost
    values['Total Cost'] = mat_cost + print_cost + core_cost

    data = pd.concat([data, pd.DataFrame([values])], ignore_index = True)

    sheet.sheet1.set_dataframe(data.replace(np.NaN, 0), 'A1')
    
    return number
