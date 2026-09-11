import pandas as pd
import streamlit as st

st.title("My CSV / Excel Processor")
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv","xlsx"])

if uploaded_file is not None:
	if uploaded_file.name.endswith(".csv"):
		df = pd.read_csv(uploaded_file) 
	else:
		df = pd.read_excel(uploaded_file)
	st.write("### Original Data ")
	st.dataframe(df)

	st.write("### Processed Data ")
	dep_amt = df[df['Deposit Amt.'].notna()] 
	st.write(dep_amt.head())
 
