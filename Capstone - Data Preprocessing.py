# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 08:49:28 2022

@author: kavin
"""

import pandas as pd
import numpy as np
import matplotlib

rawdata2014 = pd.read_csv(r'C:\Users\kavin\OneDrive\Desktop\Data Science Projects\Emissions Data Ontario\CSV\bps_2014_report_english.csv')
rawdata2015 = pd.read_csv(r'C:\Users\kavin\OneDrive\Desktop\Data Science Projects\Emissions Data Ontario\CSV\bps_2015_report_english.csv')
rawdata2016 = pd.read_csv(r'C:\Users\kavin\OneDrive\Desktop\Data Science Projects\Emissions Data Ontario\CSV\bps_2016_report_english.csv')
rawdata2017 = pd.read_csv(r'C:\Users\kavin\OneDrive\Desktop\Data Science Projects\Emissions Data Ontario\CSV\2017_energy_consumption.csv')
rawdata2018 = pd.read_csv(r'C:\Users\kavin\OneDrive\Desktop\Data Science Projects\Emissions Data Ontario\CSV\2018_final_data_set.csv')
rawdata2019 = pd.read_csv(r'C:\Users\kavin\OneDrive\Desktop\Data Science Projects\Emissions Data Ontario\CSV\2019_final_data_set.csv')

df2014 = rawdata2014[["Operation", "Sector", "Operation Type", "City", "Total Indoor Space_x", "Unit of Measure", "GHG Emissions KG", "Energy Intensity GJ_m2", "Weekly Average Hours"]]
df2015 = rawdata2015[["Operation", "Sector", "Operation Type", "City", "Total Indoor Space_x", "Unit of Measure", "GHG Emissions KG", "Energy Intensity GJ_m2"]]
df2016 = rawdata2016[["Operation", "Sector", "Operation Type", "City", "Total Indoor Space_x", "Unit of Measure", "GHG Emissions KG", "Energy Intensity GJ_m2"]]
df2017 = rawdata2017[["Operation", "Sector", "Operation Type", "City", "Total Indoor Space_x", "Unit of Measure", "GHG Emissions KG", "Energy Intensity GJ_m2"]]
df2018 = rawdata2018[["Operation", "Sector", "Operation Type", "City", "Total Indoor Space_x", "Unit of Measure", "GHG Emissions KG", "Energy Intensity GJ_m2"]]
df2019 = rawdata2019[["Operation", "Sector", "Operation Type", "City", "Total Indoor Space_x", "Unit of Measure", "GHG Emissions KG", "Energy Intensity GJ_m2"]]

df2014 = df2014.drop_duplicates('Operation')

print(df2014.dtypes)

df2014.reset_index(drop=True, inplace=True)
df2015.reset_index(drop=True, inplace=True)
df2016.reset_index(drop=True, inplace=True)
df2017.reset_index(drop=True, inplace=True)
df2018.reset_index(drop=True, inplace=True)
df2019.reset_index(drop=True, inplace=True)

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

dfclean = df2014.rename(columns={'GHG Emissions KG': '2014 GHG Em(KG)', 'Energy Intensity GJ_m2': '2014 EI(GJ/m2)', 'Total Indoor Space_x': 'Indoor Space(m2)'})
dfclean = dfclean[["Operation", "Sector", "Operation Type", "City", "Indoor Space(m2)", "2014 GHG Em(KG)", "2014 EI(GJ/m2)", "Weekly Average Hours"]]

print(dfclean.dtypes)

dfclean["2014 EI(GJ/m2)"] = dfclean["2014 EI(GJ/m2)"].replace("#DIV/0!", "0")
dfclean["2014 EI(GJ/m2)"] = pd.to_numeric(dfclean["2014 EI(GJ/m2)"])

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

dfclean = dfclean.set_index("Operation")
df2015 = df2015.set_index("Operation")
df2016 = df2016.set_index("Operation")
df2017 = df2017.set_index("Operation")
df2018 = df2018.set_index("Operation")
df2019 = df2019.set_index("Operation")

dfclean.update(df2015)
dfclean.update(df2016)
dfclean.update(df2017) 
dfclean.update(df2018)
dfclean.update(df2019)

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

dfclean = dfclean.fillna(0)

dfclean1 = dfclean.loc[dfclean["2014 GHG Em(KG)"] * dfclean["2019 GHG Em(KG)"] != 0]
dfclean1 = dfclean1.loc[dfclean1["2014 EI(GJ/m2)"] * dfclean1["2019 EI(GJ/m2)"] != 0]

dfclean1["Result GHG"] = 0
dfclean1["Result EI"] = 0

print(dfclean1.dtypes)

for i in range(0, len(dfclean1["Sector"])):
    if (dfclean1["2019 GHG Em(KG)"][i] - dfclean1["2014 GHG Em(KG)"][i]) < 0:
        dfclean1["Result GHG"][i] = 1
    if (dfclean1["2019 EI(GJ/m2)"][i] - dfclean1["2014 EI(GJ/m2)"][i]) < 0:
        dfclean1["Result EI"][i] = 1

# dfclean.to_csv(r"C:\Users\kavin\OneDrive\Desktop\Data Science Projects\Emissions Data Ontario\CSV\clean_df.csv")

altdf = rawdata2014.drop_duplicates('Operation')
altdf = altdf[["Operation", "Sub Sector", "Organization", "Swimming Pool", "Number of Portables"]]

print(altdf.dtypes)

altdf.reset_index(drop=True, inplace=True)

for j in range(0, len(altdf["Operation"])):
    if altdf["Swimming Pool"][j] == "Yes":
        altdf["Swimming Pool"][j] = 1
    else:
        altdf["Swimming Pool"][j] = 0
        
altdf["Swimming Pool"] = pd.to_numeric(altdf["Swimming Pool"])

altdf = altdf.set_index("Operation")

dfclean1["Sub Sector"] = ""
dfclean1["Organization"] = ""
dfclean1["Swimming Pool"] = 0
dfclean1["Number of Portables"] = 0

dfclean1.update(altdf)

dfclean1 = dfclean1[dfclean1["Weekly Average Hours"] <= 168]

dfclean1.fillna(-1)

#One Hot Encoding
transdata = pd.get_dummies(data = dfclean1, columns = ['Sector', 'Operation Type', 'City', 'Sub Sector', 'Organization'])

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

X = transdata.drop(["Result GHG", "Result EI"], axis = 1)
Y1 = transdata[["Result GHG"]]
Y2 = transdata[["Result EI"]]

#First Emissions

X_train, X_test, Y1_train, Y1_test = train_test_split(X, Y1, test_size = 0.3, random_state = 1)

clf1 = DecisionTreeClassifier(max_leaf_nodes=20, random_state=0)
clf1.fit(X_train, Y1_train)

tree.plot_tree(clf1)

pred1 = clf1.predict(X_test)
score1 = clf1.score(X_test, Y1_test)

from sklearn.metrics import confusion_matrix
cfm = confusion_matrix(Y1_test, pred1)