# Capstone
Ontario broader public sector Emissions and Energy Usage data

Abstract:
Agencies under the broader public sector in Ontario are required to report energy use and greenhouse gas emissions under Ontario Regulation 507/18 made under the electricity Act, 1998. Under this regulation municipalities, their service boards, school boards, post-secondary educational institutions, and public hospitals are all required to report. The reports are summarized to include energy consumption, water, sewage, and greenhouse gas emissions. Reporting agencies are also required on every 5th anniversary of July 1, 2019, to submit and publish plans to the public for energy consumption, forecasted results, results achieved and changes to be made to reach the forecasted results.
	The objective of this project is to look at the data for 6 years and see what this regulation has accomplished in that time. It will look at energy consumption and emissions by sector and agency and see who the major contributors are, then it will look at the changes by sector and agency over the 6-year period. Based on the changes and patterns that may exist visualization models will be created to show what the energy consumption and GHG emissions looks like in the broader public sector of Ontario.
	This project will focus on the data that has been reported for the years 2014 to 2019 available on the Ontario Government data catalogue (https://data.ontario.ca/en/dataset/energy-use-and-greenhouse-gas-emissions-for-the-broader-public-sector). It will look at regression and/or correlation for predicting the consumption and emissions for the year 2020 based on what is observed in the data. The analytics and modelling will be done mainly on python using pandas and other libraries with some visualization done on R. Overall, this work will determine whether there have been any significant changes and if the regulation is on track to accomplishing its goals of reducing the energy consumption and greenhouse gas emissions by agencies under the Ontario broader public sector.

Methodology:
•	Data Preprocessing:
  o	From the 41 columns in each of the 6 datasets extract the columns with sufficient information(Operation, Sector, Operation Type, City, Total indoor space, Unit of measure, GHG     Emissions(KG), Energy Intensity(GJ/m2)
  o	Drop duplicates based on unique column “Operation”, convert indoor space to the same unit Sq.m, drop unit of measure columns
  o	Replace all division by zero errors and nan values to zero in the numeric columns for year 2014 and create a clean dataframe, add Emissions and Energy Intensity columns by         year to clean dataframe with empty values.
  o	Rename columns in all dataframes to match with the year values in clean dataframe, set index to unique value column “Operation” and update clean dataframe with values from         each dataframe.
  o	Clean commas, errors and convert numeric columns to numeric datatype, remove rows containing 0 in the 2014 or 2019 GHG and Energy Intensity Columns.
  o	Create two new columns for GHG results, and Energy Intensity results and fill with zeroes. Compare values in 2014 to 2019 and change value to 1 if they have been succesful in     having less emissions and Energy usage in 2019 respectively.
•	Create a train and test division and complete a decision tree algortihm.
•	Complete a Logistic regression model.
•	Evaluate the performance of the two models.
