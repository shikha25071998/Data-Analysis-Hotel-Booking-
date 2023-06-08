#!/usr/bin/env python
# coding: utf-8

# ## Importing Libraries

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# ## Loading the dataset

# In[2]:


df = pd.read_csv('hotel_bookings 2.csv')


# ## Exploratory Data Analysis and Data Cleaning

# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


df.columns


# In[7]:


df.info()


# In[8]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])


# In[9]:


df.info()


# In[10]:


df.describe(include = 'object')


# In[11]:


for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[12]:


df.isnull().sum()


# In[13]:


df.drop(['company','agent'], axis =1, inplace = True)
df.dropna(inplace = True)


# In[14]:


df.isnull().sum()


# In[15]:


df.describe()


# In[16]:


df['adr'].plot(kind = 'box')


# In[17]:


df = df[df['adr']<5000]


# ## Data Analysis and Visualization

# In[18]:


cancelled_perc = df['is_canceled'].value_counts(normalize = True)
print(cancelled_perc)

plt.figure(figsize = (5,4))
plt.title ('Reservation status count')
plt.bar(['Not canceled','canceled'],df['is_canceled'].value_counts(),edgecolor = 'k',width = 0.7)
plt.show


# In[19]:


plt.figure(figsize =(8,4))
ax1 = sns.countplot(x = 'hotel', hue = 'is_canceled',data = df,palette ='Blues')
legend_labels,_ = ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title('Reservation status in different hotels', size =20)
plt.xlable('hotel')
plt.ylable('number of reservations')
plt.legend(['not canceld', 'canceled'])
plt.show()


# In[ ]:





# In[ ]:




