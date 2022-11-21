#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import *


# In[ ]:





# In[2]:


x = Symbol('x')


# In[3]:


fx = x**3 - 50*x
gx = -x**4 + 88*x**2 - 241


# In[4]:


inters = solve (fx - gx, x)


# In[5]:


inters_x = []


# In[6]:


for i in inters:
    z = round(i.n(10), 2)
    inters_x.append(z)


# In[7]:


inters_x


# In[8]:


inters_y = []


# In[9]:


for i in inters_x:
    y1 = fx.subs(x, i)
    inters_y.append(y1)


# In[10]:


inters_y


# In[11]:


for i, (x, y) in enumerate(zip(inters_x, inters_y), start = 1):
    print(f"точка пересечения {i} : ({x}, {y})")


# In[12]:


plot(fx - gx)


# In[13]:


plot(fx, gx)


# In[ ]:




