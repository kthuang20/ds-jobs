# import necessary tools
import pandas as pd
import plotly.express as px
import streamlit as st

### components of the sidebar of dashboard
with st.sidebar:
	""" 
		# Motivation
		There are so many careers that are currently available in the data science field. \
		While I am interested in becoming a data scientist, I thought it would also be interesting see \
		what other kinds of careers are there in the field and how their salaries compare to a data scientist. \
		To answer this question, I have taken a dataset publicly available from \
		[Kaggle](https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023/data) containing \
		the salaries of different data science related jobs in 2023.
	"""

	# import the dataset
	ds_salaries = pd.read_csv("./ds_salaries.csv")

	# ask the user to input the job they're interested in learning about
	job = st.selectbox("Enter the job title of interest:",
						ds_salaries["job_title"].unique())

	# select only the data for that job of interest
	job_data = ds_salaries[ds_salaries["job_title"] == job]

### add title
st.title(f"Exploring The Salaries of {job}s in 2023")

### function to calculate statistics about the salary of the job
def calc_salary_info(job_data):
	with st.container():
		col1, col2 = st.columns(2)
		## calculate the summary statistics of the salary
		sum_stats = job_data["salary_in_usd"].describe()

		# show the statistics
		col1.write("In 2023, the:")
		col1.write(f"* highest salary was ${sum_stats['max']:,.2f}")
		col1.write(f"* lowest salary was ${sum_stats['min']:,.2f}")
		col1.write(f"* median salary was ${sum_stats['50%']:,.2f}")
		col1.write(f"* mean salary was ${sum_stats['mean']:,.2f}")

		## create a box plot showing the summary statistics
		fig = px.box(job_data, 
					 y="salary_in_usd")
		## add labels
		fig.update_layout(title = f"Overall Salaries of {job}s",
						  yaxis_title = "Salary",
						  xaxis_title = job)
		## show box plot
		col2.plotly_chart(fig)
	
### show the table and bar plot of the mean salaries
calc_salary_info(job_data)

### 

### add title of dashboard
# st.header(f"How does the salary of a {job} vary based on different factors \
# 	like experience level, employment type, remote work ratio, and company size?")

job_data

