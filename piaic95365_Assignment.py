#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# # Numpy_Assignment_2::

# # Question  : 1

# # Convert a 1D array to a 2D array with 2 rows?

# In[2]:


import numpy as np
arr = np.arange(1,13)
print(arr)
arr.reshape(6,2)


# # Question : 2

# # How to stack two array vertically?

# In[3]:


arr1 = np.arange(10).reshape(2,5)
arr2 = np.ones(10, dtype=int).reshape(2,5)
np.vstack((arr1,arr2))


# In[6]:


import numpy as np


# # Question : 2

# # Extract those numbers from given Array. Those are must exist in 5,7 Table

# In[8]:


#task3
def function3():
    #extract those numbers from given array. those are must exist in 5,7 Table
    #example [35,70,105,..]
    a = np.arange(1, 100*10+1).reshape((100,10))
    x = a[(a%5 == 0) & (a%7 == 0)]
    return x
    """
    Expected Output:
     [35,  70, 105, 140, 175, 210, 245, 280, 315, 350, 385, 420, 455,
       490, 525, 560, 595, 630, 665, 700, 735, 770, 805, 840, 875, 910,
       945, 980]
    """
function3()  


# # Question : 4

# # Swap columns 1 and 2 in the array arr

# In[12]:


#task4
def function4():
    #Swap columns 1 and 2 in the array arr.
   
    arr = np.arange(9).reshape(3,3)
    arr[:,[0,1]] = arr[:,[1,0]]
    return arr
    """
    Expected Output:
          array([[1, 0, 2],
                [4, 3, 5],
                [7, 6, 8]])
    """
function4()    


# # Question : 5

# # Create a null vector of size 20 with 4 rows and 5 columns with numpy function

# In[10]:


#task5
def function5():
    #Create a null vector of size 20 with 4 rows and 5 columns with numpy function
   
    z = np.zeros(20).reshape(4,5)
  
    return z
    """
    Expected Output:
          array([[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]])
    """
function5()    


# # Question : 6

# # Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively

# In[13]:


#task6
def function6():
    # Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively
   
    arr = np.zeros(10 , dtype = int)
    arr[4] = 10
    arr[7] = 20
    return arr
  
function6()


# # Question : 7

# # Create an array of zeros with the same shape and type as X. Dont use reshape method

# In[15]:


#task7
def function7():
    #  Create an array of zeros with the same shape and type as X. Dont use reshape method
    x = np.arange(4, dtype=np.int64)
  
    return x*0

    """
    Expected Output:
          array([0, 0, 0, 0], dtype=int64)
    """
function7()   


# In[18]:


import numpy as np


# # Question : 8

# # Create a new array of 2x5 uints, filled with 6

# In[21]:


#task8
def function8():
    # Create a new array of 2x5 uints, filled with 6.
    
    x = np.ones(10 , dtype = np.int32).reshape(2,5)*6
  
    return x

    """
     Expected Output:
              array([[6, 6, 6, 6, 6],
                     [6, 6, 6, 6, 6]], dtype=uint32)
    """
function8()    


# # Question : 9

# # Create an array of 2, 4, 6, 8, ..., 100

# In[24]:


#task9
def function9():
    # Create an array of 2, 4, 6, 8, ..., 100.
    
    a =  np.arange(1,101)
    a =  a[(a%2 == 0)]
    return a

    """
     Expected Output:
              array([  2,   4,   6,   8,  10,  12,  14,  16,  18,  20,  22,  24,  26,
                    28,  30,  32,  34,  36,  38,  40,  42,  44,  46,  48,  50,  52,
                    54,  56,  58,  60,  62,  64,  66,  68,  70,  72,  74,  76,  78,
                    80,  82,  84,  86,  88,  90,  92,  94,  96,  98, 100])
    """
function9()    


# # Question : 10

# # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr

# In[27]:


import numpy as np


# In[29]:


#task10
def function10():
    # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.
    
    arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
    brr = np.array([1,2,3])
    subt = arr-np.vstack(brr) 
  
    return subt

    """
     Expected Output:
               array([[2 2 2]
                      [2 2 2]
                      [2 2 2]])
    """
function10()    


# # Question : 11

# # Replace all odd numbers in arr with -1 without changing arr

# In[31]:


#task11
def function11():
    # Replace all odd numbers in arr with -1 without changing arr.
    
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    arr[1::2] = -1
    ans = arr 
  
    return ans

    """
     Expected Output:
              array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])
    """
function11()    


# # Question : 12

# # Create the following pattern without hardcoding. Use only numpy functions and the below input array arr

# In[4]:


import numpy as np


# In[5]:


#task12
def function12():
    # Create the following pattern without hardcoding. Use only numpy functions and the below input array arr.
    # HINT: use stacking concept
    
    arr = np.array([1,2,3])
    ans = np.hstack((np.repeat(arr,3),arr,arr,arr)) 
  
    return ans

    """
     Expected Output:
              array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
    """
function12()    


# # Question : 13

# # Set a condition which gets all items between 5 and 10 from arr

# In[6]:


#task13
def function13():
    # Set a condition which gets all items between 5 and 10 from arr.
    
    
    arr = np.array([2, 6, 1, 9, 10, 3, 27])
    ans = arr[(arr>5)&(arr<10)] 
  
    return ans

    """
     Expected Output:
              array([6, 9])
    """
function13()    


# # Question : 14

# # Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays

# In[7]:


#task14
def function14():
    # Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.
    # Hint use split method
    
    
    arr = np.arange(10, 34, 1) .reshape(8,3)
    ans = np.split(arr,4) 
  
    return ans

    """
     Expected Output:
       [array([[10, 11, 12],[13, 14, 15]]), 
        array([[16, 17, 18],[19, 20, 21]]), 
        array([[22, 23, 24],[25, 26, 27]]), 
        array([[28, 29, 30],[31, 32, 33]])]
    """
function14()    


# # Question : 15 

# # Sort following NumPy array by the second column

# In[8]:


#task15
def function15():
    #Sort following NumPy array by the second column
    
    
    arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])
    arr[:3,1:2] = np.sort(arr[:3,1:2] , axis = 0)
    ans = arr 
  
    return ans

    """
     Expected Output:
           array([[-4,  1,  7],
                   [ 8,  2, -2],
                   [ 6,  3,  9]])
    """
function15()    


# # Question : 16

# # Write a NumPy program to join a sequence of arrays along depth

# In[9]:


#task16
def function16():
    #Write a NumPy program to join a sequence of arrays along depth.
    
    
    x = np.array([[1], [2], [3]])
    y = np.array([[2], [3], [4]])
    ans = np.hstack([x,y]) 
  
    return ans

    """
     Expected Output:
                [[[1 2]]
                 [[2 3]]
                 [[3 4]]]
    """
function16()    


# # Question : 17

# # replace numbers with "YES" if it divided by 3 and 5. Otherwise it will be replaced with "NO"

# In[10]:


#Task17
def function17():
    # replace numbers with "YES" if it divided by 3 and 5
    # otherwise it will be replaced with "NO"
    # Hint: np.where
    arr = np.arange(1,10*10+1).reshape((10,10))
    return np.where((arr%3 == 0)&(arr%5 == 0),"YES","NO")

#Excpected Out
"""
array([['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO']],
      dtype='<U3')
"""
function17()


# # Question : 18

# # count values of "students" are exist in "piaic"

# In[11]:


#Task18
def function18():
    # count values of "students" are exist in "piaic"
    piaic = np.arange(100)
    students = np.array([5,20,50,200,301,7001])
    x = len(set(piaic)&set(students))
    return x

    #Expected output: 3
function18()    


# # Question : 20

# # apply fuction "abc" on each value of Array "X"

# In[13]:


#Task20
def function20():
    #apply fuction "abc" on each value of Array "X"
    x = np.arange(1,11)
    def xyz(x):
        return x*2+3-2

    return xyz(x)
#Expected Output: array([ 3,  5,  7,  9, 11, 13, 15, 17, 19, 21])

function20()


# In[ ]:




