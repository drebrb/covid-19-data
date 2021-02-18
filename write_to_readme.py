#!/usr/bin/env python3

import numpy as np
import pandas as pd 

def write_to_readme():
    # Import csv files
    new_cases_csv = np.genfromtxt('/home/nuke/git/covid-19-data/data/us_covid-19_new_cases.csv', dtype='int32')
    new_deaths_csv = np.genfromtxt('/home/nuke/git/covid-19-data/data/us_covid-19_new_deaths.csv', dtype='int32')
    dates_csv = np.genfromtxt('/home/nuke/git/covid-19-data/data/us_covid-19_dates.csv', dtype='datetime64')

    # Build array for new cases and 7-day mean
    cases_array = np.array(new_cases_csv)
    cases_length = len(cases_array)
    cases_today = cases_array[cases_length - 1]
    cases_last_7_days = cases_array[-7:]
    cases_mean = np.mean(cases_last_7_days)

    # Build array for new deaths and 7-day mean
    deaths_array = np.array(new_deaths_csv)
    deaths_length = len(deaths_array)
    deaths_today = deaths_array[deaths_length - 1]
    deaths_last_7_days = deaths_array[-7:]
    deaths_mean = np.mean(deaths_last_7_days)

    # Dates 
    date_array = np.array(dates_csv)
    date_length = len(date_array)
    date_today = date_array[date_length - 1 ]
    date_7_days_ago = date_array[date_length - 7 ]

    # Dataframe for cases and deaths in the last 24 hours
    today = date_today
    index_today = ['New cases', 'New deaths']
    df_today = pd.DataFrame({str(today): [f"{cases_today:,d}", f"{deaths_today:,d}"]}, index=index_today)
    df_today.index.names = ['Date']

    # DataFrame for 7-day average
    index_avg = ['Cases', 'Deaths']
    df_avg = pd.DataFrame({'7-day avg': [f"{int(cases_mean):,d}", f"{int(deaths_mean):,d}"]}, index=index_avg)
    df_avg.index.names = [str(date_7_days_ago) + " - " + str(today)]

    # Write to 'README.md'
    f = open("/home/nuke/git/covid-19-data/README.md", "w")
    f.write("# US COVID-19 [Data](https://github.com/drebrb/covid-19-data/blob/master/data/us_covid-19_data.csv)\n\n###### Reported numbers for " + str(today) + "\n" + df_today.to_markdown() + "\n\n###### 7-day average\n" + df_avg.to_markdown() + """
\n\n## [Total Cases and Deaths](https://github.com/drebrb/covid-19-data/blob/master/data/us_covid-19_total.csv)

### Cases
![Plot](https://github.com/drebrb/covid-19-data/blob/master/plots/US_Total_COVID-19_Cases.png)

### Deaths
![Plot](https://github.com/drebrb/covid-19-data/blob/master/plots/US_Total_COVID-19_Deaths.png)


## [New Cases and Deaths](https://github.com/drebrb/covid-19-data/blob/master/data/us_covid-19_new.csv) 

### Cases
![Plot](https://github.com/drebrb/covid-19-data/blob/master/plots/US_New_COVID-19_Cases.png)

### Deaths
![Plot](https://github.com/drebrb/covid-19-data/blob/master/plots/US_New_COVID-19_Deaths.png)
""")
    f.close()
