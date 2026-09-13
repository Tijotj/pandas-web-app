import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Financial Analyser")
uploaded_file1 = st.file_uploader("Choose a CSV or Excel file of last month", type=['csv','xlsx']")

if uploaded_file1 is not None:
	if uploaded_file1.name.endswith(".csv"): 
		df = pd.read_csv(uploaded_file1)		
	else:
		df = pd.read_excel(uploaded_file1)	
	st.write("### Original Data")
	st.dataframe(df)	

	st.write("### Total Credits")
	total_credited = df['Deposited Amt.'].sum()
	st.write(f"Total Amount Credited last month {total_credited}") 

	st.write("### Total Debits")
	total_debits = df['Withdrawal Amt.'].sum()
	st.write(f"Total Amount Debited last month {total_debits}")  

	st.write("### High 5 transactions")
	
	narration_col = "Narration"	
	amount_col = "Withdrawal Amt."
	
	if narration_col in df.columns and amount_col in df.columns:
		df[amount_col] = pd.to_numeric(df[amount_col], errors='coerce').fillna(0)   	
		st.subheader("Top 5 spending categories(By Narration)") 

		grouped_df = df.groupby(narration_col)[amount_col].sum().reset_index()   

		top_5_grouped = grouped_df.nlargest(5, amount_col)  

		top_5_grouped.columns = ["Transaction Description","Total Amount"] 
		st.dataframe(top_5_grouped.style.format({"Total Amount":"${:,.2f}"})) 
 
	else:
		st.error(f"Make sure both '{narration_col}' and '{amount_col}' columns exist in your file.") 	
	
