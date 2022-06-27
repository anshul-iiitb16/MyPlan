#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
cdr_df = pd.DataFrame({})
udr_df = pd.DataFrame({})

df = pd.read_csv("Call Details-Data.csv")
cdr_df = cdr_df.append(df)

udr = pd.read_csv("UDR.csv")
udr_df = udr_df.append(udr)

cdr_df["Phone Number"] = cdr_df["Phone Number"].astype(str) 
udr_df["Phone Number"] = udr_df["Phone Number"].astype(str) 


df_merge = pd.merge(udr_df,cdr_df, on = "Phone Number")
df_merge.head()

