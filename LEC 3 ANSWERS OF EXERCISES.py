#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#EXERCISE 1 AND 2 
arr = np.arange(0, 20)
arr1 = arr.reshape((4, 5), order='F')
print(arr1)


# In[3]:


# method 1: with a single for loop

arr2 = np.empty((4, 5), dtype=int)
for i in range(4):
    arr2[i] = np.arange(0+i, 5+i)**2

print(arr2)


# In[4]:


# method 2: tile method

A = np.tile(np.arange(5), (4,1))
B = np.tile(np.arange(4), (5,1)).T
arr2 = (A+B)**2
print(arr2)


# In[5]:


# method 3: with mgrid method

A, B = np.mgrid[0:4, 0:5]
arr2 = (A+B)**2
print(arr2)


# In[6]:


arr = [[0, 1], [1, 0]]

arr3 = np.tile(arr, (3, 3))
print(arr3)


# In[7]:


#EXERCISE 3
print(arr1)


# In[8]:


arr = arr1[[2, 3, 1], :]
arr = arr[:, [1, 4, 2]]
print(arr)


# In[10]:


#EXERCISE 4
print(arr3)


# In[11]:


arr3[arr3 == 0] = -1
print(arr3)


# In[12]:


#EXERCISE 4BIS

arr = np.random.rand(20)
print(arr)
arr[np.argmax(arr)] = -1
arr[np.argmax(arr)] = -2
print(arr)


# In[ ]:




