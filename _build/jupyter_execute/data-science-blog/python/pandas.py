#!/usr/bin/env python
# coding: utf-8

# # 🐼 Pandas

# # 🧑‍🎓 Learning Pandas
# 
# The best way to learn Pandas (as an Excel practitioner):
# 
# - Pandas is the de-facto standard library for working with tabular data in Python
# - I learnt Pandas by replicating my work from Excel and other spreadsheet-based software (anyone used JMP before?)
# - “Transfer Learning”: Once you know how Excel maps to Pandas, you transfer your wealth of Excel knowledge directly into Pandas. These are transferrable skills!
# - Ensures you’re doing the correct thing by comparing outputs of operations between Excel and Pandas. It boosted my confidence a lot in the initial days!
# - Learn Python while automating your work!
# 
# `pip install pandas`
# 
# 📖 Pandas for Excel practitioners: [https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#compare-with-spreadsheets](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#compare-with-spreadsheets)
# 
# I regularly post about practical and applied data science. If you like my posts, let’s connect here or on Twitter @MarieStephenLeo!
# 
# #datascience #dataanalytics #dataengineering #pandas #python #programming
# 
# ```{image} images/pandas/Tips-learning_pandas.png
# :alt: learning_pandas
# :class: bg-primary mb-1
# :width: 100%
# :align: center
# ```

# In[1]:


import pandas as pd

url = "https://raw.github.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/tips.csv"

tips = pd.read_csv(url)
tips_pivot = tips.pivot_table(
    values="tip", index=["size"], columns=["sex"], aggfunc="mean"
)


# In[ ]:




