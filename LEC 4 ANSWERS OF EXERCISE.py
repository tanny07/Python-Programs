#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# In[4]:


#EXERCISE1

fig1, ax1 = plt.subplots(figsize=(8, 4))

x = np.linspace(0.1, 8, 200)
y1 = np.log(x)
y2 = np.sin(x)
ax1.plot(x, y1, color="red", label="log")
ax1.plot(x, y2, color="green", label="sin")
ax1.set_title("sine curve and logarithmic curve")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.legend()
ax1.fill_between(x, y1, y2, color="steelblue", alpha=0.8);


# In[5]:


#EXERCISE2

fig2, ax2 = plt.subplots(figsize=(8, 4))

# code for plotting the circle
theta = np.linspace(0, 2*np.pi, 100)
r = np.sqrt(1.0)
x1 = r*np.cos(theta)
x2 = r*np.sin(theta)
ax2.plot(x1, x2)
ax2.set_title("circle & random points")
ax2.set_aspect(1);

# code for generating scatter points
n = 500
x = 2 * np.random.rand(n) - 1
y = 2 * np.random.rand(n) - 1

# code for the color of each point
colors = np.array(["green"]*n)
colors[x**2 + y**2 > 1] = "red"

# code for plotting scatter points
ax2.scatter(x, y, c=colors, marker="+");


# In[6]:


#EXERCISE3

fig3, ax3 = plt.subplots(1, 2, figsize=(16, 4))

# first plot: from ax1
x = np.linspace(0.1, 8, 200)
y1 = np.log(x)
y2 = np.sin(x)
ax3[0].plot(x, y1, color="red", label="log")
ax3[0].plot(x, y2, color="green", label="sin")
ax3[0].set_title("sine curve and logarithmic curve")
ax3[0].set_xlabel("x")
ax3[0].set_ylabel("y")
ax3[0].legend()
ax3[0].fill_between(x, y1, y2, color="steelblue", alpha=0.8)

# second plot
theta = np.linspace(0, 2*np.pi, 100)
r = np.sqrt(1.0)
x1 = r*np.cos(theta)
x2 = r*np.sin(theta)
ax3[1].plot(x1, x2)
ax3[1].set_title("circle & random points")
ax3[1].set_aspect(1);

n = 500
x = 2 * np.random.rand(n) - 1
y = 2 * np.random.rand(n) - 1

colors = np.array(["green"]*n)
colors[x**2 + y**2 > 1] = "red"

ax3[1].scatter(x, y, c=colors, marker="+");


# In[7]:


#EXERCISE4

# alternatively: not shorter but useful
fig3, ax3 = plt.subplots(1, 2, figsize=(16, 4))

# first plot: from ax1
lines1 = ax1.lines[0]
lines2 = ax1.lines[1]
x, y1 = lines1.get_data()
x, y2 = lines2.get_data()
ax3[0].plot(x, y1, color=lines1.get_color(), label=lines1.get_label())
ax3[0].plot(x, y2, color=lines2.get_color(), label=lines2.get_label())
ax3[0].set_title(ax1.get_title())
ax3[0].set_xlabel(ax1.get_xlabel())
ax3[0].set_ylabel(ax1.get_ylabel())
ax3[0].legend()
ax3[0].fill_between(x, y1, y2, color="steelblue", alpha=0.8);

# second plot: from ax2
x, y = ax2.collections[0].get_offsets().data.T
colors = ax2.collections[0].get_facecolors()
ax3[1].scatter(x, y, c = colors, marker="+")

x, y = ax2.lines[0].get_data()
ax3[1].plot(x, y)
ax3[1].set_title(ax2.get_title())
ax3[1].set_aspect(1);


# In[ ]:




