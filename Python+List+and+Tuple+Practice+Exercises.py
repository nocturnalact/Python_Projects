#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Q1 Create myTuple tuple with the follwoing values ("NPower","JDA","Tuesday",30,3,2021)
myTuple = ("NPower","JDA","Tuesday",30,3,2021)


# In[4]:


#Q2 What is the type of myTuple
type(myTuple)


# In[5]:


#Q3 What is the length of myTuple
len(myTuple)


# In[6]:


#Q4 print the values in each index #Use regular indexing 
print(myTuple[0])
print(myTuple[1])
print(myTuple[2])
print(myTuple[3])
print(myTuple[4])
print(myTuple[5])


# In[7]:


#Q5 print the values in each index #Use negative indexing 
print(myTuple[-1])
print(myTuple[-2])
print(myTuple[-3])
print(myTuple[-4])
print(myTuple[-5])
print(myTuple[-6])


# In[8]:


#Q6 what is the type of each value
print(type(myTuple[0]),type(myTuple[1]),type(myTuple[2]),type(myTuple[3]),type(myTuple[4]),type(myTuple[5]))


# In[9]:


#Q7 unpack myTuple in the follwoeing variables name,program,dayName,month,day,year accordingly 
# print the variables 
name,program,dayName,month,day,year = myTuple
print(name)
print(program)
print(dayName)
print(month)
print(day)
print(year)


# In[14]:


#Q8 unpack myTuple2 in the following variablesname,program,dayName.
# What will happen to variables (name,program,dayName) and (month,day,year)
#myTuple2 = myTuple
name,program, dayName = myTuple2


# In[10]:


# Note the following
Tuple1=("Jerry",2,89) #This is a tuple with 3 elements 
Tuple2=("Ulan")#This is a tuple with 1 element
test="Leul" #This is a VARIABLE with string value

a,b,c=Tuple1
print("Type a",type(a))
print(a,b,c)

d=Tuple2
print(type(d))
print(d)

e=test
print(e)


# In[16]:


#Tuples are immutable
#we can always make the testTuple variable reference a new tuple in the memory 
#and holding different information

testTuple=(1,2,3)
print(testTuple)

testTuple=(4,5,6)
print(testTuple)

#But we can't change or edit a value for the existing tuple

testTuple[0]=6 #ERROR 'tuple' object does not support item assignment


# In[12]:


#Q9 Reverse myTuple, output should looks like ("NPower","JDA","Tuesday",30,3,2021)
tuple(reversed(myTuple))


# In[13]:


#Q10 Create nestedTuple=(("Coursera","course",6),("week",(2,"Lists","Tuple")))
nestedTuple=(("Coursera","course",6),("week",(2,"Lists","Tuple")))


# In[14]:


#Q11 What is the output of nestedTuple[1:2]
nestedTuple[1:2]


# In[57]:


#Q12 print each element in the nestedTuple
print(nestedTuple[0][0],nestedTuple[0][1],nestedTuple[0][2],nestedTuple[1][0],nestedTuple[1][1][0],nestedTuple[1][1][1],nestedTuple[1][1][2])




# In[22]:


#Q13 Access (2,"Lists","Tuple") from nestedTuple
print(nestedTuple[1][1])


# In[20]:


#Q14 Access "Lists" from nestedTuple
print(nestedTuple[1][1][1])


# In[21]:


#Q15 Access "Tuple" from nestedTuple
print(nestedTuple[1][1][2])


# In[27]:


#Q16 Access "course" from nestedTuple
print(nestedTuple[0][1])


# In[42]:


#Q17 Concatenate myTuple with nestedTuple
myTuple = myTuple + nestedTuple


# In[43]:


#Q18 add your name to the tuple
myTuple = myTuple + ('Dami',)
print(myTuple)


# In[44]:


#Q19 check whether Coursera exists within a myTuple

# NOTE in doesn't work properly with nested tuples # Wrong output
'Coursera' in myTuple


# In[37]:


#Q20 check whether an element exists within a testTuple
4 in testTuple


# In[55]:


#Q21 Find the index of JDA in myTuple

myTuple.index('JDA')
# Find the index of 'Coursera' in myTuple
myTuple[6].index('Coursera')
# NOTE index doesn't work properly with nested tuples # Wrong output


# In[46]:


#Q22 print index 8 from myTuple
print(myTuple[8])


# In[48]:


#Q23 Get the 4th element and 4th element from last of a myTuple
print(myTuple[3],myTuple[-4])


# In[49]:


#Q24 Find how many times 27 appeared in the tuple [Hint: Use method count()]
myTuple.count(27)


# In[ ]:




