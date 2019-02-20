
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:
#changes made by Chhavi

import matplotlib.pyplot as plt


# In[3]:


get_ipython().magic('matplotlib inline')


# In[4]:


existing_df = pd.read_csv("C:/Users/chavi/downloads/trans_us.csv", index_col = 0, thousands = ',')


# In[5]:


existing_df.index.names = ['stations']


# In[6]:


existing_df.columns.names = ['months']


# In[7]:


existing_df = existing_df.fillna(15)


# In[8]:


existing_df.head()


# In[9]:


from sklearn.decomposition import PCA


# In[10]:


pca = PCA(n_components=2)


# In[11]:


pca.fit(existing_df)


# In[13]:


existing_2d = pca.transform(existing_df)


# In[14]:


existing_df_2d = pd.DataFrame(existing_2d)


# In[15]:


existing_df_2d.index = existing_df.index


# In[16]:


existing_df_2d.columns = ['PC1','PC2']


# In[17]:


existing_df_2d.head()


# In[18]:


print(pca.explained_variance_ratio_)

