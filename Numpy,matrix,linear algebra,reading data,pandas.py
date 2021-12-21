# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 20:13:28 2021

@author: shivani arade
"""
#numerical python
import numpy as np
x=np.array([2,3,4,5])
print(type(x))
print(x)

x=np.array([2,3,'n',5])
print(x)

#generate arrays using linspace
#np.linspace(start,stop,num,dtype,retstep) retstep-return the samples,step value
b=np.linspace(1,5,10,retstep=False,endpoint=True)
print(b)
c=np.linspace(1,5,10,retstep=False,endpoint=False)
print(c)

#generate arrays using arange
#np.arange(start,stop,step)
d=np.arange(1,10,2)

#generate arrays using ones
#np.ones(shape,dtype) dtype:default float
e=np.ones((3,4))

#generate arrays using zeroes
#np.zeros(shape,dtype)
f=np.zeros((3,4))

#generate arrays using random.rand
#np.random.rand(shape)
np.random.rand(5)
np.random.rand(3,2)

#generate arrays using logspace
#np.logspace(start,stop,num,endpoint,base,dtype) num default 50 base(base of log space) default 10
g=np.logspace(1,10,5,endpoint=True,base=10.0)

x=range(1000)
timeit sum(x)

y=np.array(x)
timeit np.sum(y)
#arrays work faster than lists

import sys
sys.getsizeof(1)*len(x)

y.itemsize * y.size
#storage space arrays less

'''matrix'''
a=np.matrix("1,2,3,4;4,5,6,7;7,8,9,10")
print(a)
a.shape
shape[0] #rows
shape[1] #columns
a.size

#modify matrix using insert
#np.insert(matrix,obj,values,axis) axis 0 rows 1 columns obj:index position
col_new=np.matrix("2,3,4")
a=np.insert(a,0,col_new,axis=1)
print(a)

row_new=np.matrix("4,5,6,7,9")
a=np.insert(a,0,row_new,axis=0)
print(a)

#modify matrix using index
a[1,1]=-3

#access elements using index
print(a[1,:])

#matrix addition
A=np.matrix(np.arange(0,20)).reshape(5,4)
print(A)
B=np.matrix(np.arange(20,40)).reshape(5,4)
print(B)
np.add(A,B)
np.subtract(A,B)
#for matrix multiplication no.ofrows in A should be equal to no. of columns in B
B=np.transpose(B)
np.dot(A,B)
np.multiply(A,B)
np.divide(A,B)

'''linear algebra'''

#det of matrix
x=np.matrix("4,5,6,4;8,9,7,5;8,4,5,1;7,8,9,6")
print(x)
np.linalg.det(x)

#rank of mtrix
np.linalg.matrix_rank(x)

#inverse of matrix
np.linalg.inv(x)
#det 0 inverse does not exist

#system of linear equations
A=np.matrix("3,1,2;3,2,5;6,7,8")
b=np.matrix("2,-1,3").transpose()
print(b)
print(A)
np.linalg.solve(A,b)

#reading data
import os
os.chdir("D:\Python")
import pandas as pd
csv_data=pd.read_csv('Iris_data_sample.csv',index_col=0,na_values=['###','??'])
excel=pd.read_excel("Iris_data_sample.xlsx",sheet_name='Iris_data')
text=pd.read_table('Iris_data_sample.txt',sep=" ")                  #use read_csv

cars_data=pd.read_csv('Toyota.csv',index_col=0)

#shallow copy(changes to copy also reflect in original)
samp=cars_data.copy(deep=False)
samp=cars_data

#deep copy((changes to copy not reflect in original))
samp1=cars_data.copy(deep=True)

#attributes
cars_data.index  #row labels
cars_data.columns
cars_data.size
cars_data.shape
cars_data.memory_usage()
cars_data.ndim
cars_data.dtypes
cars_data.describe()
cars_data.info()

#indexing and selecting data
cars_data.head(6)
cars_data.tail(5)
cars_data.at[4,'Fuel_Type']     #single indexing based accessing
cars_data.iat[5,6]              #integer based accessing
cars_data.loc[:,['Fuel_Type','Model']]    #indexing based accessing

#character types
#category and object(if cols has nan calls-datatype=object)  
import pandas as pd
cars_data.get_dtype_counts()
cars_data.select_dtypes(exclude=[object])
np.unique(cars_data['Fuel_Type'])
cars_data['Fuel_Type'].unique()
cars_data['Fuel_Type'].nbytes
cars_data.isnull().sum()
cars_data.isna().sum()

#to convert datatype:astype
#to replace:dataframe.replace([to_replace,value])

#subsetting the rows that have 1 or more missing value
#missing=cars_data[cars_data.isnull().any(axis=1)]

#imputation high deviation between mean and median:median otherwise mean
cars_data['Age_08_04'].mean()
cars_data['Age_08_04'].fillna(cars_data['Age_08_04'].mean(),inplace=True)

cars_data['Fuel_Type'].value_counts()
cars_data['Fuel_Type'].value_counts().index[0]
cars_data['Fuel_Type'].fillna(cars_data['Fuel_Type'].value_counts().index[0],inplace=True)

#to fill na values in both numerical and categorical variable at one stretch
cars_data3=cars_data3.apply(lambda x:x.fillna(x.mean()) if x.dtype=='float' else x.fillna(x.value_counts().index[0]))










     




















