
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def sigmoid(x):
    return(1/(1+np.exp(-x)))


# In[3]:


def sigmoid_gradient(x):
    s = sigmoid(x)
    return s*(1-s)


# In[4]:


sigmoid(5)


# In[5]:


arr=np.array([1,2,3])


# In[6]:


sigmoid(arr)


# In[7]:


sigmoid_gradient(5)


# In[8]:


sigmoid_gradient(arr)


# In[9]:


sigmoid(0)


# In[10]:


sigmoid_gradient(0)

