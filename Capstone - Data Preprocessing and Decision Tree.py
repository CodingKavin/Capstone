# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 08:49:28 2022

@author: kavin
"""

import pandas as pd
import numpy as np

#read csv files into 6 dataframes
rawdata2014 = pd.read_csv(r'C:\Users\kavin\OneDrive\Desktop\Data Science Projects\Emissions Data Ontario\CSV\bps_2014_report_english.csv')
rawdata2015 = pd.read_csv(r'C:\Users\kavin\OneDrive\Desktop\Data Science Projects\Emissions Data Ontario\CSV\bps_2015_report_english.csv')
rawdata2016 = pd.read_csv(r'C:\Users\kavin\OneDrive\Desktop\Data Science Projects\Emissions Data Ontario\CSV\bps_2016_report_english.csv')
rawdata2017 = pd.read_csv(r'C:\Users\kavin\OneDrive\Desktop\Data Science Projects\Emissions Data Ontario\CSV\2017_energy_consumption.csv')
rawdata2018 = pd.read_csv(r'C:\Users\kavin\OneDrive\Desktop\Data Science Projects\Emissions Data Ontario\CSV\2018_final_data_set.csv')
rawdata2019 = pd.read_csv(r'C:\Users\kavin\OneDrive\Desktop\Data Science Projects\Emissions Data Ontario\CSV\2019_final_data_set.csv')

#Extract the attributes to start with into dataframes by year
df2014 = rawdata2014[["Operation", "Sector", "Operation Type", "City", "Total Indoor Space_x", "Unit of Measure", "GHG Emissions KG", "Energy Intensity GJ_m2", "Weekly Average Hours"]]
df2015 = rawdata2015[["Operation", "Sector", "Operation Type", "City", "Total Indoor Space_x", "Unit of Measure", "GHG Emissions KG", "Energy Intensity GJ_m2"]]
df2016 = rawdata2016[["Operation", "Sector", "Operation Type", "City", "Total Indoor Space_x", "Unit of Measure", "GHG Emissions KG", "Energy Intensity GJ_m2"]]
df2017 = rawdata2017[["Operation", "Sector", "Operation Type", "City", "Total Indoor Space_x", "Unit of Measure", "GHG Emissions KG", "Energy Intensity GJ_m2"]]
df2018 = rawdata2018[["Operation", "Sector", "Operation Type", "City", "Total Indoor Space_x", "Unit of Measure", "GHG Emissions KG", "Energy Intensity GJ_m2"]]
df2019 = rawdata2019[["Operation", "Sector", "Operation Type", "City", "Total Indoor Space_x", "Unit of Measure", "GHG Emissions KG", "Energy Intensity GJ_m2"]]

#drop duplicates in the 2014 dataframe based on unique colum Operation
df2014 = df2014.drop_duplicates('Operation')

print(df2014.dtypes)

#Reset indexes for all dataframes so there is no issue when iterating with for loop
df2014.reset_index(drop=True, inplace=True)
df2015.reset_index(drop=True, inplace=True)
df2016.reset_index(drop=True, inplace=True)
df2017.reset_index(drop=True, inplace=True)
df2018.reset_index(drop=True, inplace=True)
df2019.reset_index(drop=True, inplace=True)

#convert columns to numeric and remove any commas and convvert square feet units to square metres
for a in range(0, len(df2014["Operation"])):
    if df2014["Unit of Measure"][a] == "Square feet":
        df2014["Total Indoor Space_x"][a] = df2014["Total Indoor Space_x"][a] * 0.092903
        
for b in range(0, len(df2015["Operation"])):
    if df2015["Unit of Measure"][b] == "Square feet":
        df2015["Total Indoor Space_x"][b] = df2015["Total Indoor Space_x"][b] * 0.092903

for c in range(0, len(df2016["Operation"])):
    if df2016["Unit of Measure"][c] == "Square feet":
        df2016["Total Indoor Space_x"][c] = df2016["Total Indoor Space_x"][c] * 0.092903

for d in range(0, len(df2017["Operation"])):
    if df2017["Unit of Measure"][d] == "Square feet":
        df2017["Total Indoor Space_x"][d] = df2017["Total Indoor Space_x"][d] * 0.092903

print(df2018.dtypes)
df2018["Total Indoor Space_x"] = df2018["Total Indoor Space_x"].replace(",", "", regex=True)
df2018["Total Indoor Space_x"] = pd.to_numeric(df2018["Total Indoor Space_x"])

for e in range(0, len(df2018["Operation"])):
    if df2018["Unit of Measure"][e] == "Square feet":
        df2018["Total Indoor Space_x"][e] = df2018["Total Indoor Space_x"][e] * 0.092903
        
print(df2019.dtypes)
df2019["Total Indoor Space_x"] = df2019["Total Indoor Space_x"].replace(",", "", regex=True)
df2019["Total Indoor Space_x"] = pd.to_numeric(df2019["Total Indoor Space_x"])

for f in range(0, len(df2019["Operation"])):
    if df2019["Unit of Measure"][f] == "Square feet":
        df2019["Total Indoor Space_x"][f] = df2019["Total Indoor Space_x"][f] * 0.092903

#Rename columns pertaining to Emissions and energy in 2014 dataframe and move it over and start with a clean dataframe
dfclean = df2014.rename(columns={'GHG Emissions KG': '2014 GHG Em(KG)', 'Energy Intensity GJ_m2': '2014 EI(GJ/m2)', 'Total Indoor Space_x': 'Indoor Space(m2)'})
dfclean = dfclean[["Operation", "Sector", "Operation Type", "City", "Indoor Space(m2)", "2014 GHG Em(KG)", "2014 EI(GJ/m2)", "Weekly Average Hours"]]

print(dfclean.dtypes)

#Replace all the division by zero erros and replace with zeros
dfclean["2014 EI(GJ/m2)"] = dfclean["2014 EI(GJ/m2)"].replace("#DIV/0!", "0")
dfclean["2014 EI(GJ/m2)"] = pd.to_numeric(dfclean["2014 EI(GJ/m2)"])

#create empty columns in the clean dataframe for emissions and energy for each year
dfclean["2015 GHG Em(KG)"] = ""
dfclean["2015 EI(GJ/m2)"] = ""
dfclean["2016 GHG Em(KG)"] =""
dfclean["2016 EI(GJ/m2)"] = ""
dfclean["2017 GHG Em(KG)"] = ""
dfclean["2017 EI(GJ/m2)"] = ""
dfclean["2018 GHG Em(KG)"] = ""
dfclean["2018 EI(GJ/m2)"] = ""
dfclean["2019 GHG Em(KG)"] = ""
dfclean["2019 EI(GJ/m2)"] = ""

#replace division by zero errors in all the remaining dataframes and replace with zeros
df2015["Energy Intensity GJ_m2"] = df2015["Energy Intensity GJ_m2"].replace("#DIV/0!", "0")
df2015["Energy Intensity GJ_m2"] = pd.to_numeric(df2015["Energy Intensity GJ_m2"])

df2016["Energy Intensity GJ_m2"] = df2016["Energy Intensity GJ_m2"].replace("#DIV/0!", "0")
df2016["Energy Intensity GJ_m2"] = pd.to_numeric(df2016["Energy Intensity GJ_m2"])

df2017["Energy Intensity GJ_m2"] = df2017["Energy Intensity GJ_m2"].replace("#DIV/0!", "0")
df2017["Energy Intensity GJ_m2"] = pd.to_numeric(df2017["Energy Intensity GJ_m2"])

df2018["Energy Intensity GJ_m2"] = df2018["Energy Intensity GJ_m2"].replace("#DIV/0!", "0")
df2018["Energy Intensity GJ_m2"] = pd.to_numeric(df2018["Energy Intensity GJ_m2"])

df2019["Energy Intensity GJ_m2"] = df2019["Energy Intensity GJ_m2"].replace("#DIV/0!", "0")
df2019["Energy Intensity GJ_m2"] = pd.to_numeric(df2019["Energy Intensity GJ_m2"])

#Drop duplicates for all the other dataframes and rename columns to match the clean dataframe
df2015 = df2015.drop_duplicates('Operation')
df2015 = df2015.rename(columns={'GHG Emissions KG': '2015 GHG Em(KG)', 'Energy Intensity GJ_m2': '2015 EI(GJ/m2)'})

df2016 = df2016.drop_duplicates('Operation')
df2016 = df2016.rename(columns={'GHG Emissions KG': '2016 GHG Em(KG)', 'Energy Intensity GJ_m2': '2016 EI(GJ/m2)'})

df2017 = df2017.drop_duplicates('Operation')
df2017 = df2017.rename(columns={'GHG Emissions KG': '2017 GHG Em(KG)', 'Energy Intensity GJ_m2': '2017 EI(GJ/m2)'})

df2018 = df2018.drop_duplicates('Operation')
df2018 = df2018.rename(columns={'GHG Emissions KG': '2018 GHG Em(KG)', 'Energy Intensity GJ_m2': '2018 EI(GJ/m2)'})

df2019 = df2019.drop_duplicates('Operation')
df2019 = df2019.rename(columns={'GHG Emissions KG': '2019 GHG Em(KG)', 'Energy Intensity GJ_m2': '2019 EI(GJ/m2)'})

#For all dataframes set the index as the unique column "Operation"
dfclean = dfclean.set_index("Operation")
df2015 = df2015.set_index("Operation")
df2016 = df2016.set_index("Operation")
df2017 = df2017.set_index("Operation")
df2018 = df2018.set_index("Operation")
df2019 = df2019.set_index("Operation")

#Update the clean dataframe with the values for each via matching volumn names from the remaining 5 dataframes by year
dfclean.update(df2015)
dfclean.update(df2016)
dfclean.update(df2017) 
dfclean.update(df2018)
dfclean.update(df2019)

#Replace the commas for the new column in the clean dataframe and convert them to numeric
dfclean["2015 GHG Em(KG)"] = dfclean["2015 GHG Em(KG)"].replace(",", "", regex=True)
dfclean["2015 EI(GJ/m2)"] = dfclean["2015 EI(GJ/m2)"].replace(",", "", regex=True)
dfclean["2015 GHG Em(KG)"] = pd.to_numeric(dfclean["2015 GHG Em(KG)"])
dfclean["2015 EI(GJ/m2)"] = pd.to_numeric(dfclean["2015 EI(GJ/m2)"])

dfclean["2016 GHG Em(KG)"] = dfclean["2016 GHG Em(KG)"].replace(",", "", regex=True)
dfclean["2016 EI(GJ/m2)"] = dfclean["2016 EI(GJ/m2)"].replace(",", "", regex=True)
dfclean["2016 GHG Em(KG)"] = pd.to_numeric(dfclean["2016 GHG Em(KG)"])
dfclean["2016 EI(GJ/m2)"] = pd.to_numeric(dfclean["2016 EI(GJ/m2)"])

dfclean["2017 GHG Em(KG)"] = dfclean["2017 GHG Em(KG)"].replace(",", "", regex=True)
dfclean["2017 EI(GJ/m2)"] = dfclean["2017 EI(GJ/m2)"].replace(",", "", regex=True)
dfclean["2017 GHG Em(KG)"] = pd.to_numeric(dfclean["2017 GHG Em(KG)"])
dfclean["2017 EI(GJ/m2)"] = pd.to_numeric(dfclean["2017 EI(GJ/m2)"])

dfclean["2018 GHG Em(KG)"] = dfclean["2018 GHG Em(KG)"].replace(",", "", regex=True)
dfclean["2018 EI(GJ/m2)"] = dfclean["2018 EI(GJ/m2)"].replace(",", "", regex=True)
dfclean["2018 GHG Em(KG)"] = pd.to_numeric(dfclean["2018 GHG Em(KG)"])
dfclean["2018 EI(GJ/m2)"] = pd.to_numeric(dfclean["2018 EI(GJ/m2)"])

dfclean["2019 GHG Em(KG)"] = dfclean["2019 GHG Em(KG)"].replace(",", "", regex=True)
dfclean["2019 EI(GJ/m2)"] = dfclean["2019 EI(GJ/m2)"].replace(",", "", regex=True)
dfclean["2019 GHG Em(KG)"] = pd.to_numeric(dfclean["2019 GHG Em(KG)"])
dfclean["2019 EI(GJ/m2)"] = pd.to_numeric(dfclean["2019 EI(GJ/m2)"])

print(dfclean.dtypes)

#Fill nan values with zero
dfclean = dfclean.fillna(0)

#create a new clean dataframe check to see if any of the 2014 or 2019 columns for energy and emissions have zero
#since we will not be able to populate reults columns if either are zero check by multiplying to see if theres a zero
#keep only non zero values in the new dataframe
dfclean1 = dfclean.loc[dfclean["2014 GHG Em(KG)"] * dfclean["2019 GHG Em(KG)"] != 0]
dfclean1 = dfclean1.loc[dfclean1["2014 EI(GJ/m2)"] * dfclean1["2019 EI(GJ/m2)"] != 0]

#Create two empty columns for results for energy intensity and GHG emissions and fill with zeros
dfclean1["Result GHG"] = 0
dfclean1["Result EI"] = 0

print(dfclean1.dtypes)

#If the energy intensity and emissions is lower in 2019 than 2014 then they have succesfully reduced each respectively
#fill value of 1 for those that have been successful in reducing emissions and energy consumption
for i in range(0, len(dfclean1["Sector"])):
    if (dfclean1["2019 GHG Em(KG)"][i] - dfclean1["2014 GHG Em(KG)"][i]) < 0:
        dfclean1["Result GHG"][i] = 1
    if (dfclean1["2019 EI(GJ/m2)"][i] - dfclean1["2014 EI(GJ/m2)"][i]) < 0:
        dfclean1["Result EI"][i] = 1

#Trying to keep more attributes from the original dataframe to improve model accuracy. take in 5 more columns including "Operation"
altdf = rawdata2014.drop_duplicates('Operation')
altdf = altdf[["Operation", "Sub Sector", "Organization", "Swimming Pool", "Number of Portables"]]

print(altdf.dtypes)

#reset index to avoid errors during for loop iteration with an alternate dataframe
altdf.reset_index(drop=True, inplace=True)

#convert swimming pool from yes no to 1 and 0
for j in range(0, len(altdf["Operation"])):
    if altdf["Swimming Pool"][j] == "Yes":
        altdf["Swimming Pool"][j] = 1
    else:
        altdf["Swimming Pool"][j] = 0
        
altdf["Swimming Pool"] = pd.to_numeric(altdf["Swimming Pool"])

#set index in alt df to unique column "Operation"
altdf = altdf.set_index("Operation")

#Create empty values for each of these new values in the new clean dataframe
dfclean1["Sub Sector"] = ""
dfclean1["Organization"] = ""
dfclean1["Swimming Pool"] = 0
dfclean1["Number of Portables"] = 0

#Update values from alternate dataframe to the clean dataframe for respective columns
dfclean1.update(altdf)

#Keep only rows containing values less than or equal to 168 in weekly average hours as you cannot have more than 168 hours in a week
dfclean1 = dfclean1[dfclean1["Weekly Average Hours"] <= 168]

#Replace nan values with 0 again
dfclean1.fillna(0)

#Repeat the above process for more attributes from the original dataframe for heating types
altdf1 = rawdata2014.drop_duplicates('Operation')
altdf1 = altdf1[["Operation", "FuelOil12_Quantity", "FuelOil46_Quantity", "Propane_Quantity", "Coal_Quantity", "Wood_Quantity"]]

altdf1.reset_index(drop=True, inplace=True)

altdf1["FuelOil12_Quantity"] = pd.to_numeric(altdf1["FuelOil12_Quantity"])
altdf1["FuelOil46_Quantity"] = pd.to_numeric(altdf1["FuelOil46_Quantity"])
altdf1["Propane_Quantity"] = pd.to_numeric(altdf1["Propane_Quantity"])
altdf1["Coal_Quantity"] = pd.to_numeric(altdf1["Coal_Quantity"])
altdf1["Wood_Quantity"] = pd.to_numeric(altdf1["Wood_Quantity"])

altdf1.fillna(0)

#for all the non zero values in this column replace with 1. We are just keeping the information of whether each operation
#uses this type of heating or not and keeping it a simple binary column. The values are reflected in the EI and emissions columns
for k in range(0,len(altdf1["Operation"])):
    if altdf1["FuelOil12_Quantity"][k] != 0:
        altdf1["FuelOil12_Quantity"][k] = 1

for l in range(0,len(altdf1["Operation"])):
    if altdf1["FuelOil46_Quantity"][l] != 0:
        altdf1["FuelOil46_Quantity"][l] = 1

for m in range(0,len(altdf1["Operation"])):
    if altdf1["Propane_Quantity"][m] != 0:
        altdf1["Propane_Quantity"][m] = 1

for n in range(0,len(altdf1["Operation"])):
    if altdf1["Coal_Quantity"][n] != 0:
        altdf1["Coal_Quantity"][n] = 1

for p in range(0,len(altdf1["Operation"])):
    if altdf1["Wood_Quantity"][p] != 0:
        altdf1["Wood_Quantity"][p] = 1

#Set index to operation, rename columns to match, create empty columns in clean df and update values as before        
altdf1 = altdf1.set_index("Operation")

altdf1 = altdf1.rename(columns={'FuelOil12_Quantity': 'Oil12', 'FuelOil46_Quantity': 'Oil46', 'Propane_Quantity': 'Propane', 'Coal_Quantity': 'Coal', 'Wood_Quantity': 'Wood'})

dfclean1["Oil12"] = 0
dfclean1["Oil46"] = 0
dfclean1["Propane"] = 0
dfclean1["Coal"] = 0
dfclean1["Wood"] = 0

dfclean1.update(altdf1)

dfclean1.to_csv(r"C:\Users\kavin\OneDrive\Desktop\Data Science Projects\Emissions Data Ontario\CSV\clean_df.csv")

#One Hot Encoding
#Since decision tree from sklearn only takes numeric inputs we need to transform the categorical data
#pandas get_dummies creates new columns for each category in the these columns and fills with 1 or 0 for yes and no
#this drastically increases number of columns to over 1800
transdata = pd.get_dummies(data = dfclean1, columns = ['Sector', 'Operation Type', 'City', 'Sub Sector', 'Organization'])

#importing train test split and decision tree classifier and the tree from sklearn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree


#set up X and Y for the classifier create two Y's for Energy intensity and GHG emissions
#For the X values drop the result columns and the 2014 and 2019 columns as the result was derived from these
#without dropping the 2014 and 2019 columns all the decision tree branches will simply belong to these two columns
#X = transdata.drop(["Result GHG", "Result EI"], axis = 1)
X = transdata.drop(["Result GHG", "Result EI", "2014 GHG Em(KG)", "2019 GHG Em(KG)", "2014 EI(GJ/m2)", "2019 EI(GJ/m2)"], axis = 1)
Y1 = transdata[["Result GHG"]]
Y2 = transdata[["Result EI"]]

#First Emissions

#Complete the decision tree process and obtain the tree and confusion matrix, max leaf nodes of 10 used because increasing
#the leaf nodes does not improve the performance of the model beyond this point
X_train, X_test, Y1_train, Y1_test = train_test_split(X, Y1, test_size = 0.3, random_state = 1)

clf1 = DecisionTreeClassifier(max_leaf_nodes=10, random_state=0)
clf1.fit(X_train, Y1_train)

tree.plot_tree(clf1)

pred1 = clf1.predict(X_test)
score1 = clf1.score(X_test, Y1_test)

from sklearn.metrics import confusion_matrix
cfm = confusion_matrix(Y1_test, pred1)

#Second Energy Intensity

#complete the same process above for the energy intensity result
X2_train, X2_test, Y2_train, Y2_test = train_test_split(X, Y2, test_size = 0.3, random_state = 2)

clf2 = DecisionTreeClassifier(max_leaf_nodes=10, random_state=3)
clf2.fit(X2_train, Y2_train)

tree.plot_tree(clf2)

pred2 = clf2.predict(X2_test)
score2 = clf2.score(X2_test, Y2_test)

cfm2 = confusion_matrix(Y2_test, pred2)

#Run the below codes to see total unmber of operations that have been successful in reducing emission and energy usage
#print(sum(dfclean1["Result GHG"]))
#print(sum(dfclean1["Result EI"]))

#For the decision tree we can run below statement to check what each column value refers to by changing the index
#print(transdata.columns[43])
