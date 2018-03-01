
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def normalize_Ma_Row(x):
    x_norm = np.linalg.norm(x, axis = 1, keepdims = True)
    return x / x_norm


# In[5]:


x = np.array([[1,2],[3,4]])


# In[6]:


normalize_Ma_Row(x)

