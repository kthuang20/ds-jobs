### import necessary functions
import pandas as pd
import plotly.express as px
import streamlit as st

### function to calculate statistics about the salary of the job
def calc_salary_info(job_data, job):
	## create container
	with st.container():
		# create two columns inside container
		col1, col2 = st.columns(2)
		## calculate the summary statistics of the salary
		sum_stats = job_data["salary_in_usd"].describe()

		# show the statistics
		col1.write("In 2023, the:")
		col1.write(f"* highest salary was ${sum_stats['max']:,.2f}")
		col1.write(f"* lowest salary was ${sum_stats['min']:,.2f}")
		col1.write(f"* median salary was ${sum_stats['50%']:,.2f}")
		col1.write(f"* mean salary was ${sum_stats['mean']:,.2f}")

		# create a box plot showing the summary statistics
		fig = px.box(job_data, y = "salary_in_usd")
		# add labels
		fig.update_layout(title = f"Overall Salaries of {job}s",
						  title_x = 0.25,
						  yaxis_title = "Salary",
						  xaxis_title = job)
		# show box plot
		col2.plotly_chart(fig)


### generate figures describing the type of employment
def show_job_type(job_data, job):
	## add a bar chart showing the number of employees at each country
	with st.container():
		# count the number of data scientists in each country
		job_counts = job_data["employee_residence"].value_counts().reset_index()
		# create bar chart show
		fig = px.bar(job_counts, x="employee_residence", y="count", title=f"Geographical Distribution of {job}s")
		# format labels
		fig.update_layout(title_x = 0.35,
						  xaxis_title = "Country",
						  yaxis_title = f"# of {job}s")
		# show bar chart
		st.plotly_chart(fig)

	## create 3 pie charts
	with st.container():
		# create three columns
		col1, col2, col3 = st.columns(3)
		
		# add a column containing the labels for the numbers representing remote ratios
		fig1_labels = {0:"Onsite", 50: "Hybrid", 100:"Fully Remote"}
		job_data["remote_labels"] = job_data["remote_ratio"].map(fig1_labels)
		# show a pie chart of % of all remote jobs in first column
		fig1 = px.pie(job_data, names="remote_labels", title="% Remote")
		col1.plotly_chart(fig1)

		# replace employment type labels with full descriptions
		fig2_labels = {"FT": "Full Time", "PT": "Part Time", "CT": "Contract Worker"}
		job_data["employment_type"] = job_data["employment_type"].map(fig2_labels)
		# show a pie chart showing employment type in second column
		fig2 = px.pie(job_data, names="employment_type", title="Employment Type")
		col2.plotly_chart(fig2)

		# replace company size labels with full description
		fig3_labels = {"M": "Medium", "L": "Large", "S": "Small"}
		job_data["company_size"] = job_data["company_size"].map(fig3_labels)
		# show a pie chart showing size the companies that employees worked at in third column
		fig3 = px.pie(job_data, names="company_size", title="Company Size Distribution")
		col3.plotly_chart(fig3)