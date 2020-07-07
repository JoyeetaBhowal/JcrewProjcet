#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas
import csv
import json 
import os
import numpy as np


# In[24]:


def get_column_name_file(filename,delimiter,prefix):
    headerColumns = open(filename).readline().split(delimiter)
    finalCol = []
    for col in headerColumns:
        finalCol.append(prefix +"_" + col.replace("\n","") )
    return finalCol

def get_convertor_string(columnNames):
    headerColumns = columnNames
    finalCol = {}
    for col in headerColumns:
        #u'fieldname':str
        prefix='fieldname'
        finalCol.update( "{u'" + "col"  + "':str}" )
    return finalCol

def get_all_vali_values_for_a_column(filename,delimiter,colname):
    fileDataFrame = pandas.read_csv(filename,sep=delimiter,header =0,quotechar="\"")
    finalArray = fileDataFrame[colname].unique()
    return finalArray


## Sample Data - read for operating system 
dataSourceDir="C:\\Users\\jaita\\OneDrive\\Documents\\NEU\\ALY6980Capstone\\"


# In[25]:


#Raw Files
censuesData="JCREW_CENCUS.csv"
ProjectData="TeamprojectData.csv"



# In[26]:


censuesData_col = get_column_name_file(dataSourceDir+censuesData,",","censD")
ProjectData_col = get_column_name_file(dataSourceDir+ProjectData,",","ProjD")


# In[27]:


# Read all the data from account tables 
censuesData_df = pandas.read_csv(dataSourceDir+censuesData,sep=",",skiprows =1,quotechar="\"",names = censuesData_col,dtype=np.str)
ProjectData_df = pandas.read_csv(dataSourceDir+ProjectData,sep=",",skiprows =1,quotechar="\"",names = ProjectData_col,dtype=np.str)


# In[28]:


ProjectData_df.head()


# In[33]:


### Join All the Tables with one to one
mergedData = pandas.merge(censuesData_df,ProjectData_df,how="left",left_on=['censD_STATE'],right_on=['ProjD_STORE_STATE'])


# In[35]:


#Write Final CSV

mergedData.to_csv(dataSourceDir + mergedData_output_csv , sep=",",index=False,quoting=csv.QUOTE_MINIMAL,escapechar="\\")


# In[36]:


#OutPut
mergedData_output_csv="JCFinalData.csv"


# In[ ]:




