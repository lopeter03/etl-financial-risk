import streamlit as st
import sqlite3
import pandas as pd

st.title("Basel III Risk Dashboard")

conn = sqlite3.connect("../basel_demo.db")  # parent folder

balance = pd.read_sql("SELECT * FROM balance_sheet", conn)
rwa = pd.read_sql("SELECT * FROM rwa", conn)
revexp = pd.read_sql("SELECT * FROM revenue_expense", conn)

st.subheader("Balance Sheet")
st.write(balance)

st.subheader("RWA")
st.write(rwa)

st.subheader("Revenue/Expense")
st.write(revexp)

conn.close()
