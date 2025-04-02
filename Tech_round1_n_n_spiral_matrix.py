#!/usr/bin/env python
# coding: utf-8

# create matrix n*n size (4), return as a 2D list 
# 
# techround_1 n*n spiral matrix

# In[1]:


import numpy as np


# In[10]:


def spiral_matrix(n):
    matrix=[[0] * n for i in range(n)]
    left,right,top,bottom=0,n-1,0,n-1 # set boundaries
    n=1 # start filling with 1
    
    while left<=right and top<=bottom:
        for i in range(left,right+1): # moving from left to right 
            matrix[top][i]=n
            n+=1
            
        top+=1
        
        
        for i in range(top,bottom+1):
            matrix[i][right]=n
            n+=1
            
        right-=1
        
        
        if top<=bottom:
            for i in range(right,left-1,-1):
                matrix[bottom][i]=n
                n+=1
                
            bottom-=1
            
        if left<=right:
            for i in range(bottom,top-1,-1):
                matrix[i][left]=n
                n+=1
            left+=1
            
    return matrix

N= 6
mat_spiral=spiral_matrix(N)

for i in mat_spiral:
    print(i)

                       
    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[2]:


x_mat=np.random.randint(0,10,size=(3,3))
x_mat


# In[ ]:





# In[ ]:





# In[ ]:




