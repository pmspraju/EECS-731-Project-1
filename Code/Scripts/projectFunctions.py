# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 00:20:49 2017

@author: Madhu
"""
import os
import pandas as pd
import numpy  as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from matplotlib import pyplot as plt
import seaborn as sns; sns.set()

pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', -1)  # or 199

#Function to load the data
def loadData(path,filename,sepr):
    try:
             files = os.listdir(path)
             for f in files:
                 if f == filename:
                     data = pd.read_csv(os.path.join(path,f),sep=sepr)
                     return data
            
    except Exception as ex:
           print "-----------------------------------------------------------------------"
           template = "An exception of type {0} occurred. Arguments:\n{1!r}"
           message = template.format(type(ex).__name__, ex.args)
           print message

#Function to explore the data
def exploreData(data):
    try:
           #Total number of records                                  
           rows = data.shape[0]
           cols = data.shape[1]    
           
           #separate features and target
           drop_col = ['target']
           features = data.drop(drop_col, axis = 1)
           target = data[drop_col]
          
           # Print the results
           print "-----------------------------------------------------------------------"
           print "Total number of records: {}".format(rows)
           print "Total number of features: {}".format(cols)
           print "-----------------------------------------------------------------------"
           
           #print histograms of columns
           #drawCorr(data)
           
           #draw correlation
#           plt.figure(figsize=(13,13))
#           sns.heatmap(data.corr(),
#           vmin=-1,
#           cmap='coolwarm',
#           annot=True);
           
           return features,target
           
    except Exception as ex:
           print "-----------------------------------------------------------------------"
           template = "An exception of type {0} occurred. Arguments:\n{1!r}"
           message = template.format(type(ex).__name__, ex.args)
           print message

def missingValues(data):
    try:
           # Total missing values
           mis_val = data.isnull().sum()
         
           # Percentage of missing values
           mis_val_percent = 100 * mis_val / len(data)
           
           # Make a table with the results
           mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
           
           # Rename the columns
           mis_val_table_ren_columns = mis_val_table.rename(
           columns = {0 : 'Missing Values', 1 : '% of Total Values'})
           mis_val_table_ren_columns.head(4 )
           # Sort the table by percentage of missing descending
           misVal = mis_val_table_ren_columns[
            mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
                   '% of Total Values', ascending=False).round(1)
                     
           return misVal, mis_val_table_ren_columns

    except Exception as ex:
           print "-----------------------------------------------------------------------"
           template = "An exception of type {0} occurred. Arguments:\n{1!r}"
           message = template.format(type(ex).__name__, ex.args)
           print message

def catCount(feature,target,data): 
    try:
        d_f = data.loc[data[target] == False]
        d_t = data.loc[data[target] == True]
        
        d_f[feature].fillna(value='missing',inplace=True)
        d_t[feature].fillna(value='missing',inplace=True)
         
        f, axes = plt.subplots(1, 2, figsize=(8, 8), sharex=True)
        sns.countplot(x=feature, data=d_f,ax=axes[0])
        axes[0].set_title('churn=False')
        sns.countplot(x=feature, data=d_t,ax=axes[1])
        axes[1].set_title('churn=True')    
        for ax in axes:
            ax.set_xticklabels(ax.get_xticklabels(), rotation=65, horizontalalignment='right')                
        plt.show()
    except Exception as ex:
        print "-----------------------------------------------------------------------"
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print message  

def numCount(feature,target,data):
    try:
        d_f = data.loc[data[target] == False]
        d_t = data.loc[data[target] == True]
         
        plt.figure(figsize = (12, 6))
        sns.kdeplot(d_f[feature], label='churn=false')
        sns.kdeplot(d_t[feature], label='churn=true')
        plt.title(feature)
        plt.legend();
    except Exception as ex:
        print "-----------------------------------------------------------------------"
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print message

def transformData(features,target):
    try:
        
#        skewed = ['rain']
#        features_log_transformed = pd.DataFrame(data = features)
#        features_log_transformed[skewed] = features[skewed].apply(lambda x: np.log(x + 1))
        
        scaler = MinMaxScaler() # default=(0, 1)
        numerical = ['FFMC','DMC','DC','ISI','temp','RH','wind']
        features_log_minmax_transform = pd.DataFrame(data = features)
        features_log_minmax_transform[numerical] = scaler.fit_transform(features[numerical])
                
        # TODO: One-hot encode the 'features_log_minmax_transform' data using pandas.get_dummies()
        #features_final = pd.get_dummies(features_log_minmax_transform)
        enc = LabelEncoder()
        features_log_minmax_transform['month'] = enc.fit_transform(features_log_minmax_transform['month'])
        features_log_minmax_transform['day'] = enc.fit_transform(features_log_minmax_transform['day'])
        features_final = features_log_minmax_transform
        # Print the number of features after one-hot encoding
        #encoded = list(features_final.columns)
        #print "{} total features after one-hot encoding.".format(len(encoded))
        
        target_reg = target
        ind = np.where((target>0) & (target<=200))
        target.iloc[ind] = 1    
        ind = np.where((target>200) & (target<=400))
        target.iloc[ind] = 2
        ind = np.where((target>400) & (target<=800))
        target.iloc[ind] = 3
        ind = np.where((target>800))
        target.iloc[ind] = 4
         
        return features_final, target, target_reg
        
    except Exception as ex:
           print "-----------------------------------------------------------------------"
           template = "An exception of type {0} occurred. Arguments:\n{1!r}"
           message = template.format(type(ex).__name__, ex.args)
           print message
           
def drawCorr(df):
    try:
        #df.hist(column='X',bins=70)   
        fig = plt.figure()
        ax1 = plt.subplot(3,4,1)
        df['X'].value_counts().plot(kind='bar')
        ax1.set_title('X')
        
        ax2 = plt.subplot(3,4,2)
        df['Y'].value_counts().plot(kind='bar')
        ax2.set_title('Y')
        
        ax3 = plt.subplot(3,4,3)
        df['month'].value_counts().plot(kind='bar')
        ax3.set_title('month')
        
        ax4 = plt.subplot(3,4,4)
        df['day'].value_counts().plot(kind='bar')
        ax4.set_title('day')
        
        ax5 = plt.subplot(3,4,5)
        df['FFMC'].plot()
        ax5.set_title('FFMC')
        
        ax6 = plt.subplot(3,4,6)
        df['DMC'].plot()
        ax6.set_title('DMC')
        
        ax7 = plt.subplot(3,4,7)
        df['DC'].plot()
        ax7.set_title('DC')
        
        ax8 = plt.subplot(3,4,8)
        df['ISI'].plot()
        ax8.set_title('ISI')
        
        ax9 = plt.subplot(3,4,9)
        df['temp'].plot()
        ax9.set_title('temp')
        
        ax10 = plt.subplot(3,4,10)
        df['RH'].plot()
        ax10.set_title('RH')
        
        ax11 = plt.subplot(3,4,11)
        df['wind'].plot()
        ax11.set_title('wind')
        
        ax12 = plt.subplot(3,4,12)
        df['rain'].plot()
        ax12.set_title('rain')
        
        plt.show()
             
    except Exception as ex:
        print "-----------------------------------------------------------------------"
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print message        
        
#split the data in to train and test data
def splitData(features,target,testsize):
    try:
        # Split the 'features' and 'income' data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(features,
                                                    target, 
                                                    test_size = testsize, 
                                                    random_state = 1)

        # Show the results of the split
        print "Training set has {} samples.".format(X_train.shape[0])
        print "Testing set has {} samples.".format(X_test.shape[0])
        print "-----------------------------------------------------------------------"
        return X_train, X_test, y_train, y_test
    except Exception as ex:
           print "-----------------------------------------------------------------------"
           template = "An exception of type {0} occurred. Arguments:\n{1!r}"
           message = template.format(type(ex).__name__, ex.args)
           print message