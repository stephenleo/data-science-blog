#!/usr/bin/env python
# coding: utf-8

# # 🗄️ Datasets

# ## 📥 Download datasets for Machine Learning projects
# 
# Top 5 ways to find datasets for your next Machine Learning project! 
# 
# Super convenient for those looking to build up a project portfolio to showcase to prospective hiring managers.
# 
# 1. Kaggle: [https://www.kaggle.com/datasets](https://www.kaggle.com/datasets)
# 2. Papers with code: [https://paperswithcode.com/datasets](https://paperswithcode.com/datasets). 
# 3. UCI machine learning repository: [http://archive.ics.uci.edu/ml/datasets.php](http://archive.ics.uci.edu/ml/datasets.php)
# 4. Huggingface datasets library: [https://huggingface.co/datasets](https://huggingface.co/datasets). The most convenient with a standard interface. `pip install datasets`. See image.
# 5. Google dataset search: [https://datasetsearch.research.google.com/](https://datasetsearch.research.google.com/). Search for any kind of dataset across the entire internet.
# 
# Of course, for the closest experience into what real-world Data Science would look like, you should scrape the data by yourself from the internet, but hey, it's fun to play with a clean dataset!
# 
# Do you know any other good sources of datasets? Pls, let me know in the comments!
# 
# I regularly post about practical and applied data science. If you like my posts, let's connect here or on Twitter @MarieStephenLeo!
# 
# #datascience #dataanalytics #machinelearning #python #learning #career
# 
# ```{image} images/datasets/Repos-datasets.png
# :alt: datasets
# :class: bg-primary mb-1
# :width: 100%
# :align: center
# ```

# In[1]:


# Import
import pandas as pd
from datasets import load_dataset

# Download the data
dataset = load_dataset("ag_news")

# Convert to dataframe
train_df = pd.DataFrame(dataset["train"])
test_df = pd.DataFrame(dataset["test"])

train_df.head()


# In[ ]:




