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


# ## 🚲 Efficient Metrics Calculation
# Typically when you want to calculate multiple metrics for a machine learning model, you’d import and run them one by one. 
# 
# Instead, using the get_scorer function, you can refactor your code to calculate multiple metrics with a single get_scorer method, as shown in the image.
# 
# You could move metrics_list to a config.yml so that we can change the metrics calculated without changing any code!
# 
# #datascience #dataanalytics #dataengineering #machinelearning #python
# 
# ```{image} images/classification/Repos-get_scorer.png
# :alt: get_scorer method
# :class: bg-primary mb-1
# :width: 100%
# :align: center
# ```

# In[5]:


from pprint import pprint

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Create dummy classification data and model
X, y = make_classification(n_samples=10_000, random_state=1)
X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LogisticRegression().fit(X_train, y_train)


# In[6]:


# Normal way to calculate multiple metrics 😮‍💨
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)

y_pred = model.predict(X_test)

metrics = {}
metrics["accuracy"] = accuracy_score(y_test, y_pred)
metrics["precision"] = precision_score(y_test, y_pred)
metrics["recall"] = recall_score(y_test, y_pred)
metrics["f1"] = f1_score(y_test, y_pred)
metrics["roc_auc"] = roc_auc_score(y_test, y_pred)

pprint(metrics)


# In[7]:


# Better way to calculate multiple metrics 🤓
from sklearn.metrics import get_scorer

metrics_list = ["accuracy", "precision", "recall", "f1", "roc_auc"]
metrics = {metric: get_scorer(metric)(model, X_test, y_test) for metric in metrics_list}

pprint(metrics)


# In[ ]:




