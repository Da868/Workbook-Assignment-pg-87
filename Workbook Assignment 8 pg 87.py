#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
dataframe = pd.DataFrame({'Col':
            np.random.normal(size=200)})
plt.scatter(dataframe.index, dataframe['Col'])


# In[1]:


import matplotlib.pyplot as plt
import pandas as pd 


# In[13]:


df = pd.read_csv('datasets/gradedata.csv', delimiter=',', nrows=20)


# In[14]:


df


# In[15]:


y = df['hours'];
x = df['grade']


# In[16]:


plt.xlabel('grade'); plt.ylabel('hours')
plt.scatter(x,y)


# In[ ]:




