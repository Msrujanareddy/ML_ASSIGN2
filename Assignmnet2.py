#!/usr/bin/env python
# coding: utf-8

# In[38]:


import numpy as np
arr=np.random.randint(1,20,(1,15))
print("array\n",arr)

arr=np.reshape(arr,(3,5))
print("new array\n",arr)
print("Shape of array:",arr.shape)

for i in arr:
    i[np.where(i==i.max())]=0
print("max val replaced by 0\n",arr)


# In[18]:


import matplotlib.pyplot as plt
import numpy as np

y = np.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])
mylang = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
myval = [0.2, 0, 0, 0,0,0]
plt.pie(y,labels=mylang, explode = myval,autopct='%1.1f%%')
plt.show()


# In[53]:


import pandas as p
df = p.read_csv('C:\\Users\\makut\\Downloads\\data.csv')
print(df.head(20))


# In[40]:


df.isnull().any()


# In[41]:


column_means = df. mean()
print(column_means)
df = df. fillna(column_means)
print(df.head(20))


# In[42]:


result = df.agg({'Maxpulse': ['mean', 'min','max', 'count'],'Pulse': ['mean', 'min', 'max', 'count']})
print(result)


# In[56]:


filter_df1=df[(df['Calories'] > 500) & (df['Calories'] < 1000)]
print(filter_df1)
filter_df2=df[(df['Calories'] > 500) & (df['Pulse'] < 100)]
print(filter_df2)


# In[46]:


df_modified = df.loc[:, df.columns != 'Maxpulse']
print(df_modified)


# In[54]:


df.drop('Maxpulse', inplace=True, axis=1)
print(df.dtypes)


# In[48]:


df["Calories"] = df["Calories"].astype(float).astype(int)
print(df.dtypes)


# In[50]:


a1 = df.plot.scatter(x='Duration',y='Calories')
print(a1)


# In[ ]:




