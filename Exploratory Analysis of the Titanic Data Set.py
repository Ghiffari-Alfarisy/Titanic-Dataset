#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd


# In[10]:


pwd


# In[11]:


data = pd.read_csv('D:/Data D/Data E/My Data\Modern/My Folder/Kurikulum Pribadi/Data Science/Project/Titanic Disaster/train.csv')


# In[13]:


data


# In[14]:


data.head()


# In[15]:


len(data)


# In[16]:


data.count()


# In[18]:


data['Age'].min(), data['Age'].max()


# In[19]:


data.describe()


# In[20]:


data.info()


# In[21]:


data['Survived'].value_counts()


# In[22]:


data['Survived'].value_counts()* 100 / len(data)


# In[24]:


data['Sex'].value_counts()


# In[25]:


data['Pclass'].value_counts()


# In[26]:


get_ipython().run_line_magic('matplotlib', 'inline')

alpha_color = 0.5

data['Survived'].value_counts().plot(kind='bar')


# In[29]:


data['Sex'].value_counts().plot(kind='bar',
                                color=['b','r'],
                                  alpha=alpha_color)
                            


# In[34]:


data['Pclass'].value_counts().sort_index().plot(kind='bar',
                                             alpha=alpha_color)


# In[35]:


data.plot(kind='scatter', x='Survived', y='Age')


# In[38]:


data[data['Survived']==1]['Age'].value_counts().sort_index().plot(kind='bar')


# In[39]:


bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]

data['AgeBin']=pd.cut(data['Age'],bins)


# In[40]:


data[data['Survived']==1]['AgeBin'].value_counts().sort_index().plot(kind='bar')


# In[43]:


data[data['Survived']==0]['AgeBin'].value_counts().sort_index().plot(kind='bar')


# In[44]:


data['AgeBin'].value_counts().sort_index().plot(kind='bar')


# In[45]:


data[data['Pclass']==1]['Survived'].value_counts().plot(kind='bar')


# In[46]:


data[data['Pclass']==3]['Survived'].value_counts().plot(kind='bar')


# In[48]:


data[data['Sex']=='male']['Survived'].value_counts().plot(kind='bar')


# In[49]:


data[data['Sex']=='female']['Survived'].value_counts().plot(kind='bar')


# In[52]:


data[(data['Sex']=='male') & (data['Pclass']==1)]['Survived'].value_counts().plot(kind='bar')


# In[53]:


data[(data['Sex']=='male') & (data['Pclass']==3)]['Survived'].value_counts().plot(kind='bar')


# In[54]:


data[(data['Sex']=='female') & (data['Pclass']==1)]['Survived'].value_counts().plot(kind='bar')


# In[55]:


data[(data['Sex']=='female') & (data['Pclass']==3)]['Survived'].value_counts().plot(kind='bar')


# In[ ]:




