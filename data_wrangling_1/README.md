# :briefcase: Employee Reviews: Project Overview
* Created a [report](https://github.com/ayanoyamamoto0/assignments_2021-2022/blob/main/data_wrangling_1/data_wrangling_1_assignment_report.pdf) on the best companies to work for using Kaggle’s dataset `employees_reviews.csv`
* Merged additional data from Wikipedia (last run date 2022-06-14) and the companies' diversity reports

## Code and Resources Used
* **Python Version**: 3.8.8
* **Employee Reviews Dataset**: https://www.kaggle.com/saqlainrehan/employeesreviews-dataset

## Data Cleaning
* Removed duplicate rows
* Replaced 'none' with `np.nan`
* Converted strings to date and numerical formats where appropriate
* Imputated missing values in star rating columns with median values for each company per star rating
* For Best Reviewed Locations, filtered the dataframe to only consider locations with above-mean number of reviews to exclude those with one 5-star ratings
