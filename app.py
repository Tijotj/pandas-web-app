import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns



st.title("My CSV / Excel Processor")
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv","xlsx"])

if uploaded_file is not None:
	if uploaded_file.name.endswith(".csv"):
		df = pd.read_csv(uploaded_file) 
	else:
		df = pd.read_excel(uploaded_file)
	st.write("### Original Data ")
	st.dataframe(df)

	st.write("### Deposit Data ")
	dep_amt = df['Deposit Amt.'].sum() 
	st.write(f"Total Credited Amount in August: {dep_amt}")

	st.write("### Swiggy Income ")
	swiggy_income = df[df['Narration'].str.contains('Swiggy', na=False, case=False)]
	total_swiggy_income = swiggy_income['Deposit Amt.'].sum()
	st.write(f"Total Swiggy Income: {total_swiggy_income}")  

	comparison_data = pd.DataFrame({
		'Category': ['Swiggy','Total Income'],
		'Total Amount': [total_swiggy_income, dep_amt]  
	})


	# Plotting the bar chart
	fig = plt.figure(figsize=(10, 6))
	sns.barplot(x='Category', y='Total Amount', data=comparison_data, palette='viridis')
	plt.title('Comparison of Total Amounts: Swiggy, Total Amount')
	plt.ylabel('Total Amount (₹)')
	plt.xlabel('Category')
	plt.xticks(rotation=45, ha='right')
	plt.tight_layout()
	plt.show() 
