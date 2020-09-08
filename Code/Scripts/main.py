# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 00:14:26 2017

@author: Madhu
"""
# Import libraries necessary for this project
import sklearn
import numpy  as np
import pandas as pd
from pandas import compat
compat.PY3 = True
print "-----------------------------------------------------------------------"
print('The scikit-learn version is {}.'.format(sklearn.__version__))

#load functions from 
from projectFunctions import loadData, exploreData, missingValues, catCount, numCount

path = r'C:\Users\pmspr\Documents\HS\MS\Sem 3\EECS 731\Week 2\HW\Data exploration\Data\CVD'
filename = "cardio_train.csv"
#col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
data1 = loadData(path,filename,';')
data1.rename(columns={'cardio':'target'},inplace=True)
drop_col = ['id']
data1 = data1.drop(drop_col, axis = 1)
data1 = data1.sort_index(axis=1)
print ("----------------------Cardio Vascular data-----------------------------")
features1, target1 = exploreData(data1)
misVal, mis_val_table_ren_columns = missingValues(data1)
 # Print some summary information
print ("Columns that have missing values:" + str(misVal.shape[0]))
print "-----------------------------------------------------------------------"
print(mis_val_table_ren_columns.head(20))

path = r'C:\Users\pmspr\Documents\HS\MS\Sem 3\EECS 731\Week 2\HW\Data exploration\Data\UCI1'
filename = "heart.csv"
#col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
data2 = loadData(path,filename,',')
data2.rename(columns={'sex':'gender','chol':'cholesterol'},inplace=True)
data2 = data2.sort_index(axis=1)
print ("----------------------Heart Disease UCI--------------------------------")
features2, target2 = exploreData(data2)
misVal, mis_val_table_ren_columns = missingValues(data2)
 # Print some summary information
print ("Columns that have missing values:" + str(misVal.shape[0]))
print "-----------------------------------------------------------------------"
print(mis_val_table_ren_columns.head(20))

path = r'C:\Users\pmspr\Documents\HS\MS\Sem 3\EECS 731\Week 2\HW\Data exploration\Data\UCI2'
filename = "echocardiogram.csv"
#col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
data3 = loadData(path,filename,',')
data3.rename(columns={'alive':'target'},inplace=True)
data3 = data3.sort_index(axis=1)
print ("-------------------------echocardiogram--------------------------------")
features3, target3 = exploreData(data3)
misVal, mis_val_table_ren_columns = missingValues(data3)
# Print some summary information
print ("Columns that have missing values:" + str(misVal.shape[0]))
print "-----------------------------------------------------------------------"
print(mis_val_table_ren_columns.head(20))

#Remove rows with missing values in age and target
d_f = data3
col = ['target','age']
for i in col:
    d_f[i].fillna(value='missing',inplace=True)
    d_f = d_f.loc[d_f[i] != 'missing']

#Replace with zeroes for columns having less number of missing values
col = ['survival','pericardialeffusion','wallmotion-score','wallmotion-index','mult','name']
for i in col:
    d_f[i].fillna(value=0,inplace=True)

#Find the max probable values by target value 
#catCount('fractionalshortening','target',data3)
#numCount('fractionalshortening','target',data3)
mp_true = 0.24
mp_false = 0.171
d_f['fractionalshortening'].fillna(value='missing',inplace=True)
ind = np.where((d_f['fractionalshortening'] == 'missing') & (d_f['target'] == 0))
d_f['fractionalshortening'].iloc[ind] = mp_false
ind = np.where((d_f['fractionalshortening'] == 'missing') & (d_f['target'] == 1))
d_f['fractionalshortening'].iloc[ind] = mp_true

#catCount('epss','target',data3)
#numCount('epss','target',data3)
mp_true = 12.3
mp_false = 8.3
d_f['epss'].fillna(value='missing',inplace=True)
ind = np.where((d_f['epss'] == 'missing') & (d_f['target'] == 0))
d_f['epss'].iloc[ind] = mp_false
ind = np.where((d_f['epss'] == 'missing') & (d_f['target'] == 1))
d_f['epss'].iloc[ind] = mp_true


#catCount('lvdd','target',data3)
#numCount('lvdd','target',data3)
mp_true = 5.02
mp_false = 4.4
d_f['lvdd'].fillna(value='missing',inplace=True)
ind = np.where((d_f['lvdd'] == 'missing') & (d_f['target'] == 0))
d_f['lvdd'].iloc[ind] = mp_false
ind = np.where((d_f['lvdd'] == 'missing') & (d_f['target'] == 1))
d_f['lvdd'].iloc[ind] = mp_true

#catCount('group','target',data3)
#numCount('group','target',data3)
mp_true = 2
mp_false =2
d_f['group'].fillna(value='missing',inplace=True)
ind = np.where((d_f['group'] == 'missing') & (d_f['target'] == 0))
d_f['group'].iloc[ind] = mp_false
ind = np.where((d_f['group'] == 'missing') & (d_f['target'] == 1))
d_f['group'].iloc[ind] = mp_true

#Drop the features having more missing values
drop_col = ['aliveat1']
d_f = d_f.drop(drop_col, axis = 1)

print ("-------------------------echocardiogram--------------------------------")
misVal, mis_val_table_ren_columns = missingValues(d_f)
# Print some summary information
print ("Columns that have missing values:" + str(misVal.shape[0]))
print "-----------------------------------------------------------------------"
print(mis_val_table_ren_columns.head(20))

#Add columns to data frames to make columns common across
col1 = list(data1.columns)
col2 = list(data2.columns)
col3 = list(d_f.columns)
tot_col = col1 + col2 + col3
tot_col = list(dict.fromkeys(tot_col))
c1 = list(set(tot_col) - set(col1))
c2 = list(set(tot_col) - set(col2))
c3 = list(set(tot_col) - set(col3))
print(c3)
for i in c1:
    data1[i] = 0

for i in c2:
    data2[i] = 0

for i in c3:
    d_f[i] = 0
    
data = pd.concat([data1,data2,d_f], axis=0)

print ("------------------------Combined Heart dataset-------------------------------")
misVal, mis_val_table_ren_columns = missingValues(data)
# Print some summary information
print ("Columns that have missing values:" + str(misVal.shape[0]))
print ("-----------------------------------------------------------------------")
print(mis_val_table_ren_columns.head(20))

data.to_csv('test.csv')