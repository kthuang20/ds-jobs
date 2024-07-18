# import necessary tools
import pandas as pd
import altair as alt
import streamlit as st

# add title to dashboard
st.title("Data Science Salaries in 2023")

""" 
	## Motivation
	There are so many careers that are currently available in the data science field. \
	While I am interested in becoming a data scientist, I thought it would also be interesting see \
	what other kinds of careers are there in the field and how their salaries compare to a data scientist. \
	To answer this question, I have taken a dataset publicly available from \
	[Kaggle](https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023/data) containing \
	the salaries of different data science related jobs in 2023.
"""

# import the dataset
ds_salaries = pd.read_csv("./ds_salaries.csv")

""" #### Q1: What were the median salaries of various jobs in the data science field in 2023? """
def calc_med_salaries():
	# calculate and show the mean salaries of all jobs
	med_salaries = ds_salaries.groupby("job_title")["salary_in_usd"].median().reset_index()
	med_salaries = med_salaries.sort_values(by="salary_in_usd", ascending=False)
	med_salaries.columns = ["Job Title", "Salary (in USD)"]

	# create bar plot showing salaries of jobs sorted from highest to lowest (left to right)
	bar_plot = alt.Chart(med_salaries).mark_bar().encode(
	    x=alt.X("Job Title", sort=None),  # Set sort=None to ensure the sorted order is maintained
	    y="Salary (in USD)"
	)

	return med_salaries, bar_plot

# show the table and bar plot of the mean salaries
with st.container():
	med_salaries, med_saleries_chart = calc_med_salaries()
	col1, col2 = st.columns(2)
	col1.write(med_salaries)
	col2.altair_chart(med_saleries_chart, use_container_width=True)
	
