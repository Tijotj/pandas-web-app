import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Financial Analyser")
uploaded_files = st.file_uploader("Choose a CSV or Excel files for comparison", type=['csv','xlsx','xls'], accept_multiple_files= True)
narration_col = "Narration"
debit_col = "Withdrawal Amt."
credit_col = "Deposit Amt."
all_months_dfs = []

if uploaded_files is not None:
	for uploaded_file in uploaded_files:	
		try:
			if uploaded_file.name.endswith(".csv"): 
				month_df = pd.read_csv(uploaded_file)		
			else:
				month_df = pd.read_excel(uploaded_file)
			month_df['Month_source'] = uploaded_file.name	
			all_months_dfs.append(month_df)
			st.toast(f"Loaded: {uploaded_file.name}") 
		except Exception as e:
			st.error(f"Error reading {uploaded_file.name}: {e}") 

	if all_months_dfs:
		df = pd.concat(all_months_dfs,ignore_index=True) 

		for col in [debit_col,credit_col]:	
			if col in df.columns:
				df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)   	

		if debit_col in df.columns and credit_col in df.columns:
			st.header("Month over month comparison") 
			
			comparison_df = df.groupby('Month_source').agg(
				Total_Debits = (debit_col, 'sum'),
				Total_Credits = (credit_col, 'sum'),
				Transaction_Count = (narration_col, 'count')	
			) 

			comparison_df['Net_Cash_Flow'] = comparison_df['Total_Credits'] - comparison_df['Total_Debits'] 
			
			st.dataframe(
				comparison_df.style.format({
					"Total_Debits" : "{:,.2f}INR",
					"Total_Credits" : "{:,.2f}INR",
					"Net_Cash_Flow" : "{:,.2f}INR",
					"Transaction_Count" : "{:,}" 	
				})
			) 	
			
	else:
		st.error(f"Make sure both files contain columns named exactly '{debit_col}' and '{credit_col}'.") 	
	
