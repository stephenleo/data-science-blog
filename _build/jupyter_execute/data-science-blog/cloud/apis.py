#!/usr/bin/env python
# coding: utf-8

# # 📟 Application Programming Interface (API)

# ## 📶 JSON Lines
# 
# The JSON format is one of the most popular ways of transmitting information over any network. Why is this important for a Data Scientist?
# 
# - When you deploy a model as an endpoint, you will probably send and receive data from the deployed model in JSON format.
# 
# There are many ways to construct a JSON string. The best way, in my opinion, is to use the JSON lines format.
# 
# - Directly convert to and from Pandas dataframes!
# - One line is one row of data. No ambiguity about how to split rows!
# - Very readable where each key is the column name, and each value is the value of the row in that column. No ambiguity about which value belongs to which feature!
# - Easy to parallelize (e.g., using Sagemaker Batch Transform) since we can send each line to a different machine for inference.
# 
# While deploying ML models (e.g., in Sagemaker), you need to handle converting to and from the JSON object. So keeping your deployment consistent with JSON lines format will make your life much easier and unambiguous.
# 
# #mlops #datascience #dataanalytics #dataengineering #aws #sagemaker #gcp #azure #python
# 
# ```{image} images/apis/Tips-json_lines.png
# :alt: json lines
# :class: bg-primary mb-1
# :width: 100%
# :align: center
# ```

# In[1]:


import pandas as pd

# Create dummy dataframe
df = pd.DataFrame({"col_a": [1.5, 2.3], "col_b": [200.1, 150.6], "col_c": ["a", "b"]})
print(df)

# Pandas Dataframe to JSON lines string
json_lines_str = df.to_json(orient="records", lines=True)
print(json_lines_str)

# JSON lines string to Pandas Dataframe
df_reconstructed = pd.read_json(json_lines_str, lines=True)
print(df_reconstructed)


# In[ ]:




