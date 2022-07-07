import streamlit as st
from shillelagh.backends.apsw.db import connect

conn = connect(
    ":memory:",
    adapter_kwargs={
        "gsheetaspi": {
            "service_account_info": {
                
            },
        },
    },
)

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["private_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
for row in rows:
    st.write(f"{row.name} has a :{row.pet}:")