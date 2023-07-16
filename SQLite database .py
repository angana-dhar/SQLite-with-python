#!/usr/bin/env python
# coding: utf-8

# In[1]:


#create database using SQLite
import sqlite3


# In[2]:


#connecting to sqlite
#connection object
conn= sqlite3.connect('INSTRUCTOR.db')


# In[3]:


#cursor object
cursor_obj = conn.cursor()


# In[4]:


# Drop the table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")


# In[5]:


table="create table IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL,FNAME VARCHAR(20),LNAME VARCHAR(20),CITY VARCHAR(10),CCODE CHAR(2))"
cursor_obj.execute(table)
print("Table is Ready")


# In[18]:


cursor_obj.execute('''insert into INSTRUCTOR values (9, 'Rav', 'Ahuja', 'TORONTO', 'CA')''')


# In[19]:


cursor_obj.execute('''insert into INSTRUCTOR values(2,'Megha','Dhar','Mumbai','IN'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')''')


# In[22]:


table


# In[23]:


#In this step we will retrieve data we inserted into the INSTRUCTOR table.
statement = '''SELECT*FROM INSTRUCTOR'''
cursor_obj.execute(statement)
print('All the values')
output_all = cursor_obj.fetchall()
for row_all in output_all:
    print(row_all)


# In[26]:


## Fetch few rows from the table
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
  
print("All the data")
# If you want to fetch few rows from the table we use fetchmany(numberofrows) and mention the number how many rows you want to fetch
output_many = cursor_obj.fetchmany(2) 
for row_many in output_many:
  print(row_many)


# In[27]:


# Fetch only FNAME from the table
statement = '''SELECT FNAME FROM INSTRUCTOR'''
cursor_obj.execute(statement)
  
print("All the data")
output_column = cursor_obj.fetchall()
for fetch in output_column:
  print(fetch)


# In[28]:


query_update='''update INSTRUCTOR set CITY='MOOSETOWN' where FNAME="Rav"'''
cursor_obj.execute(query_update)


# In[29]:


statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
  
print("All the data")
output1 = cursor_obj.fetchmany(2)
for row in output1:
  print(row)


# In[30]:


#Retrieve data into Pandas
import pandas as pd
#retrieve the query results into a pandas dataframe
df = pd.read_sql_query("select * from instructor;", conn)

#print the dataframe
df


# In[31]:


#print just the LNAME for first row in the pandas data frame
df.LNAME[0]


# In[32]:


df.shape


# In[33]:


# Close the connection
conn.close()


# In[ ]:




