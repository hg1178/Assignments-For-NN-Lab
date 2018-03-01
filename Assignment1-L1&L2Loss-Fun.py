
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def L1(x, y):
    return sum(abs(y-x))


# In[3]:


x = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])


# In[4]:


L1(x,y)


# In[7]:


def L2(x, y):
   
   return sum((y-x)**2)



# In[13]:


x = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])


# In[14]:


L2(x,y)

