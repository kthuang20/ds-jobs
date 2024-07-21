# import necessary tools
import pandas as pd
import plotly.express as px
import streamlit as st
import gen_figs

### components of the sidebar of dashboard
with st.sidebar:
	""" 
		# Motivation
		This dashboard that allows students who are interested in pursuing a career in the data science field to \
		understnad the current state of their profession of interest. This dashboard allows the student to select \
		or type in their profession of interest. It then generates numerous visualizations, providing \
		insight into the salary expectation, geographical distribution, work environment preferences, and employment type. 
		
		The data used to generate these visualizations containing \
		the salaries of different data science related jobs in 2023. It is publicly available at \
		[Kaggle](https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023/data) .
	"""

	## import the dataset
	ds_salaries = pd.read_csv("./ds_salaries.csv")
	## select only jobs that have more than 50 recorded people
	job_counts = ds_salaries.groupby("job_title").size()
	most_recorded_jobs = job_counts.index[job_counts > 50].tolist()
	## keep only the data with the top most recorded job titles
	ds_salaries = ds_salaries[ds_salaries["job_title"].isin(most_recorded_jobs)]

	## ask the user to input the job they're interested in learning about
	job = st.selectbox("Enter the job title of interest:",
						ds_salaries["job_title"].unique())

	## select only the data for that job of interest
	job_data = ds_salaries[ds_salaries["job_title"] == job]

### add section title about salaries
st.title(f"Exploring The Salaries of {job}s in 2023")
### show the table and bar plot of the mean salaries
gen_figs.calc_salary_info(job_data, job)

### add title for next section describing employment
st.title("Employment Details")
### show figures describing the job type
gen_figs.show_job_type(job_data, job)
