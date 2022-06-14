# :earth_africa:Climate Change: Project Overview
* Created a [report](https://github.com/ayanoyamamoto0/assignments_2021-2022/blob/main/data_wrangling_2/data_wrangling_2_presentation.pdf) on climate change using data from 6 different souces from APIs, HTML, and CSV files
* Demonstrated use of pycountry and geopandas to assign ISO 3166-1 alpha-3 codes to each dataset for ease of merging
* Inspected and imputated data
* Visualised results using geopandas and seaborn
* Demonstrated storing data in CSV, Excel, JSON, SQLite, and MongoDB

## Code and Resources Used
* **Python Version**: 3.8.8
* **Packages**: pandas, numpy, matplotlib, seaborn, pandas_datareader, pycountry, geopandas, oauth2, twython, json, sklearn, sqlite3, pymongo, certifi
* **Data Sources**
  * World Bank: [Renewable energy consumption (% of total final energy consumption)](https://data.worldbank.org/indicator/EG.FEC.RNEW.ZS?view=chart)
  * Twitter: 100 most recent tweets mentioning "COP26"
  * Twitter: 100 most recent tweets mentioning "electric cars"
  * Wikipedia: [List of countries by carbon dioxide emissions](https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions)
  * Wikipedia: [List of countries by renewable electricity production](https://en.wikipedia.org/wiki/List_of_countries_by_renewable_electricity_production)
  * Kaggle: [Average Temperature per country per year](https://www.kaggle.com/code/akshaychavan/average-temperature-per-country-per-year/data?select=matYearCountry.csv)

## Requirements
When running [data_wrangling_2.ipynb](https://github.com/ayanoyamamoto0/assignments_2021-2022/blob/main/data_wrangling_2/data_wrangling_2.ipynb) please insert your Twitter API key and and API secret in
```
API_KEY = 'PLEASE_INSERT_YOUR_API_KEY'
API_SECRET = 'PLEASE_INSERT_YOUR_API_SECRET'
```
