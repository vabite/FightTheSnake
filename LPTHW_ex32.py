
# coding: utf-8

# #For loops and lists

# In[1]:

the_count = [1, 2, 3, 4, 5]


# In[2]:

fruits = ['apples', 'oranges', 'pears', 'apricots']


# In[3]:

change = [1, 'pennies', 2, 'dimes', 3, 'quarters']


# In[ ]:




# this first kind of for-loop goes through a list

# In[4]:

for number in the_count:
    print "This is count %d" % number


# In[ ]:




# same as above

# In[5]:

for fruit in fruits:
    print "A fruit of type: %s" % fruit


# In[ ]:




# also we can go through mixed lists too

# notice we have to use %r since we don't know what's in it

# In[6]:

for i in change:
    print "I got %r" % i


# In[ ]:




# we can also build lists, first start with an empy one

# In[7]:

elements = []


# then use the range function to do 0 to 5 counts

# In[8]:

for i in range(0, 6):
    print "Adding %d to the list." %i
    #append is a function thet lists undestand
    elements.append(i)


# now we can print them out too

# In[9]:

for i in elements:
    print "Element was: %d" % i

