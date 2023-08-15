#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_excel('sales.xlsx',skiprows=range(4), header=1)
df.head(10)


# In[2]:


# Display the first few rows of the DataFrame before removing the rows
print("Before removing rows:")
print(df.head())

# Drop the first two rows from the DataFrame using the iloc method
df = df.iloc[2:]

# Reset the index of the DataFrame after dropping the rows
df = df.reset_index(drop=True)

# Display the first few rows of the DataFrame after removing the rows
print("After removing rows:")
df.head()


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.info()


# # changing the dtype of the column into  

# In[6]:


# Function to check if a string can be converted to a float
def is_float(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

# Loop through each column in the DataFrame (except 'Time Period')
for column in df.columns:
    if column != 'Time Period':
        # Check if the column is of object data type and if all values can be converted to float
        if df[column].dtype == 'object' and df[column].apply(is_float).all():
            # Convert the column to float
            df[column] = df[column].astype(float)

# Now, the numeric columns (except 'Time Period') in the DataFrame should be of float data type


# In[7]:


df.info()


# In[8]:


df.isnull().sum()


# # Checking dataset is normally distributed or not concerning that which values are reliable to fill the null values 

# In[9]:


import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt



# Create a list of numeric columns (excluding 'Time Period')
numeric_columns = [col for col in df.columns if col != 'Time Period' and np.issubdtype(df[col].dtype, np.number)]

# Perform normality tests and plot histograms and QQ plots
for column in numeric_columns:
    data = df[column].dropna()
    # Shapiro-Wilk test
    shapiro_test = stats.shapiro(data)
    # Anderson-Darling test
    anderson_test = stats.anderson(data)
    # D'Agostino and Pearson's test
    dagostino_test = stats.normaltest(data)
    
    print(f"Column: {column}")
    print(f"Shapiro-Wilk Test - p-value: {shapiro_test.pvalue}")
    print(f"Anderson-Darling Test - Statistic: {anderson_test.statistic}, Critical Values: {anderson_test.critical_values}")
    print(f"D'Agostino and Pearson's Test - p-value: {dagostino_test.pvalue}")
    
    # Histogram
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.hist(data, bins='auto', density=True)
    plt.title('Histogram')
    
    # QQ Plot
    plt.subplot(1, 2, 2)
    stats.probplot(data, dist='norm', plot=plt)
    plt.title('QQ Plot')
    
    plt.show()


# In[ ]:




