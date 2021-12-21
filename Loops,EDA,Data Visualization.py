# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 22:22:58 2021

@author: shivani arade
"""

import os
os.chdir("D:\Python")
import pandas as pd
cars_data=pd.read_csv('Toyota.csv',index_col=0)

cars_data2=cars_data.copy()

#frequency tables
pd.crosstab(index=cars_data2['Fuel_Type'],columns='count',dropna=True)
#two way tables
pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['Fuel_Type'],dropna=True)
#two way tables-joint prob
pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['Fuel_Type'],normalize=True,dropna=True)
#two way tables-marginal prob
pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['Fuel_Type'],margins=True,normalize=True,dropna=True)
#two way tables-conditional prob
pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['Fuel_Type'],margins=True,normalize='index',dropna=True)
pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['Fuel_Type'],margins=True,normalize='columns',dropna=True)

#correlation
numerical_data=cars_data2.select_dtypes(exclude=[object])
corr_matrix=numerical_data.corr()

import numpy as np
import matplotlib.pyplot as plt
cars_data.dropna(axis=0,inplace=True)
#scatter plot
plt.scatter(cars_data['Age_08_04'],cars_data['Price'],c='red')
plt.title("scatter plot of price vs age")
plt.xlabel("Age")
plt.ylabel("months")
plt.show()
#histogram
plt.hist(cars_data['KM'],color='green',edgecolor='white',bins=5)
#barplot for categorical variable
counts=[979,120,12]
fuelType=('Petrol','Diesel','CNG')
index=np.arange(len(fuelType))
plt.bar(index,counts,color=['red','orange','blue'])

import seaborn as sns
#scatter plot
sns.set(style="darkgrid")
sns.regplot(x=cars_data['Age_08_04'],y=cars_data['Price'])
sns.regplot(x=cars_data['Age_08_04'],y=cars_data['Price'],fit_reg=False)
sns.lmplot(x='Age_08_04',y='Price',data=cars_data,fit_reg=False,hue='Fuel_Type',
           legend=True,palette="Set1")
#hist
sns.distplot(cars_data['Age_08_04'])
sns.distplot(cars_data['Age_08_04'],kde=False,bins=5)
#barplot
sns.countplot(x="Fuel_Type",data=cars_data)
#grouped barplot
sns.countplot(x="Fuel_Type",data=cars_data,hue="Automatic")
#boxplot
sns.boxplot(y=cars_data['Price'])
sns.boxplot(x=cars_data["Fuel_Type"],y=cars_data['Price'])
#grouped boxplot
sns.boxplot(x="Fuel_Type",y=cars_data['Price'],data=cars_data,hue="Automatic")
#boxplot and hist on same window
f,(ax_box,ax_hist)=plt.subplots(2,gridspec_kw={"height_ratios":(.15,.85)})
sns.boxplot(y=cars_data['Price'],ax=ax_box)
sns.distplot(cars_data['Price'],ax=ax_hist,kde=False)
#pairwise plots
sns.pairplot(cars_data,kind="scatter",hue="Fuel_Type")
plt.show()


#if else for loops
cars_data2.insert(10,"Price_Class","")

for i in range(0,len(cars_data2["Price"]),1):
    if (cars_data2["Price"][i]<=8450):
        cars_data2["Price_Class"][i]="Low"
    elif ((cars_data2["Price"][i]>=11950)):
        cars_data2["Price_Class"][i]="High" 
    else:cars_data2["Price_Class"][i]="Medium"
    i=i+1

i=0
while i < len(cars_data2["Price"]):
    if (cars_data2["Price"][i]<=8450):
        cars_data2["Price_Class"][i]="Low"
    elif ((cars_data2["Price"][i]>=11950)):
        cars_data2["Price_Class"][i]="High" 
    else:
        cars_data2["Price_Class"][i]="Medium"
    i=i+1











