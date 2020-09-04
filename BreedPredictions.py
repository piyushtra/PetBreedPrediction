#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
from sklearn.model_selection import train_test_split


# In[12]:


train_df = pd.read_csv("dataSet/a01c26dcd27711ea/Dataset/train.csv")
test_df = pd.read_csv("dataSet/a01c26dcd27711ea/Dataset/test.csv")


# In[13]:



colorType_df = pd.get_dummies(train_df.color_type, prefix='color_type')
train_df


# In[8]:


X = train_df.drop(['breed_category', 'pet_category'], axis=1)
y_breedcateory = train_df['breed_category']
y_petcateory = train_df['pet_category']


# In[9]:


X_train, X_test, y_train, y_test = train_test_split(X, y_breedcateory, test_size=0.33, random_state=42)


# In[10]:


X_train


# In[ ]:




