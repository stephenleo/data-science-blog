#!/usr/bin/env python
# coding: utf-8

# # 💠 Classification

# ## 🏏 Multi-label Classification Stratified Split
# 
# Iterative Stratification: Easily stratify the train test split for multi-label classification problems
# 
# - In machine learning classification problems, when your input data has imbalanced classes, it's necessary to stratify the train-test split so that we maintain the proportion of the minority class in both the train and test splits.
# - Unfortunately, sklearn's train_test_split only allows stratified splits for single-label classification and does not support multiple labels.
# 
# Enter iterative-stratification:
# 
# - Stratify the train test split across multiple labels concurrently
# - With K-Fold cross-validation!
# - Compatible with sklearn
# 
# `pip install iterative-stratification`
# 
# 🌟 Github: https://github.com/trent-b/iterative-stratification
# 
# #datascience #dataanalytics #machinelearning #python
# 
# ```{image} images/classification/Repos-iterative-stratification.png
# :alt: multi-label stratified split
# :class: bg-primary mb-1
# :width: 100%
# :align: center
# ```

# In[1]:


import pandas as pd
from iterstrat.ml_stratifiers import MultilabelStratifiedKFold
from sklearn.datasets import make_multilabel_classification


def y_proportions(y):
    df = pd.DataFrame(y)
    return df.apply(pd.value_counts)


# Create dummy multi-label data
X, y = make_multilabel_classification(n_samples=10_000, random_state=1)

# Stratified K-Fold split
mskf = MultilabelStratifiedKFold(n_splits=3, shuffle=True)

for train_index, test_index in mskf.split(X, y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # TODO: Fit and score model


# In[2]:


# Overall
print(y_proportions(y))


# In[3]:


# Train
print(y_proportions(y_train))


# In[4]:


# Test
print(y_proportions(y_test))


# In[ ]:




