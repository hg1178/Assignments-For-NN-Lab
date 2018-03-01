
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def image2vector(im):
     return im.reshape(im.shape[0]*im.shape[1]*im.shape[2],1)


# This is a 3 by 3 by 2 array, typically images will be (num_px_x, num_px_y,3) where 3 represents the RGB values

# In[3]:


image = np.array([[[ 0.67826139,  0.29380381],
        [ 0.90714982,  0.52835647],
        [ 0.4215251 ,  0.45017551]],

       [[ 0.92814219,  0.96677647],
        [ 0.85304703,  0.52351845],
        [ 0.19981397,  0.27417313]],

       [[ 0.60659855,  0.00533165],
        [ 0.10820313,  0.49978937],
        [ 0.34144279,  0.94630077]]])


# In[4]:


image2vector(image)

