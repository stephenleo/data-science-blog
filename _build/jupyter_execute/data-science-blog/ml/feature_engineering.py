#!/usr/bin/env python
# coding: utf-8

# # 🛠️ Feature Engineering

# ## 😼 Dirty Cat
# 
# Dirty Cat: Never use one-hot encoding again!
# 
# - Most ML models can only work with numeric data. So it’s common practice to one-hot encode categorical data before feeding them into an ML model.
# - However, one-hot encoding creates a new column for each unique category in your column. E.g., If you have 300 unique job titles in your company, one hot encoding this job_title column will convert that one column to 300 (or 299 if you drop first) new columns.
# - Adding so many columns to your dataset could result in the curse of dimensionality and cause model accuracy to suffer.
# 
# How to solve this problem?
# 
# - You could use CatBoost: 🌟Github: https://github.com/catboost/catboost, which supports categorical features natively.
# - However, if you want to use any other scikit-learn algorithm, then you can either use the various options available in the category encoders library: 🌟 Github: https://github.com/scikit-learn-contrib/category_encoders
# - Or you can use dirty_cat: 🌟 Github: https://github.com/dirty-cat/dirty_cat
# 
# `pip install dirty_cat`
# 
# I particularly like dirt_cat because
# 
# - Simple implementation in just one line!
# - Automatically selects the best encoder to use for each categorical column.
# - Automatically passes through continuous columns without the need for column transformers.
# - Provides NLP N-gram similarity and topic modeling-based encoders for string categories. E.g., the classes”Firefighter/Rescuer III” and “Fire/Rescue Lieutenant” belong to the same topic “firefighter, rescuer, rescue.”
# - Excellent results in head-to-head comparisons.
# 
# 🌟 Github: https://github.com/dirty-cat/dirty_cat
# 
# 📖 Docs: [https://dirty-cat.github.io/stable/index.html](https://dirty-cat.github.io/stable/index.html)
# 
# 📒 Sample notebook:
# 
# ```{image} images/feature_engineering/Repos-dirty_cat.png
# :alt: kmodes
# :class: bg-primary mb-1
# :width: 100%
# :align: center
# ```

# In[1]:


# Imports
import warnings

import pandas as pd
import plotly.express as px
from dirty_cat import SuperVectorizer
from dirty_cat.datasets import fetch_employee_salaries
from sklearn.compose import make_column_transformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder

warnings.filterwarnings("ignore", category=FutureWarning)

# Load some high cardinal feature data
employee_salaries = fetch_employee_salaries()
X = employee_salaries.X
y = employee_salaries.y

# Pre-processing
mask = X.isna()["gender"]
X.dropna(subset=["gender"], inplace=True)
y = y[~mask]
X = X[
    [
        "gender",
        "department_name",
        "assignment_category",
        "employee_position_title",
        "year_first_hired",
    ]
]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.15, random_state=42
)

# Print original data stats
print(f"Num cols before categorical encoding: {X_train.shape[1]}")
print(f"Num unique values in each col: \n{X_train.nunique()}")


# In[2]:


# Group the cols
cat_cols = [
    "gender",
    "department_name",
    "assignment_category",
    "employee_position_title",
]
cont_cols = ["year_first_hired"]


# In[3]:


def plot_feature_importance(pipeline, features):
    importances = pipeline[1].feature_importances_
    feature_importance_df = (
        pd.DataFrame({"feature": features, "importances": importances})
        .sort_values("importances")
        .tail(10)
    )
    fig = px.bar(
        feature_importance_df, x="importances", y="feature", title="Feature Importance"
    )
    fig.show()


def pipeline_model(encoder, X_train, y_train, X_test, y_test):
    ## Pipeline Model
    pipeline = make_pipeline(encoder, RandomForestRegressor())

    ## Fit and evaluate model
    pipeline.fit(X_train, y_train)
    train_score = pipeline.score(X_train, y_train)
    test_score = pipeline.score(X_test, y_test)
    print(f"Train score: {train_score:.3f}, Test score: {test_score:.3f}")

    # Check the features
    features = pipeline[0].get_feature_names_out()
    print(f"Num cols after encoding: {len(features)}")
    print(f"Encoded columns: ...{features[-5:]}")

    # Plot Feature Importance
    plot_feature_importance(pipeline, features)
    return pipeline, features


# In[4]:


# One Hot encoding - 🪢 Complex!
oh_encoder = make_column_transformer(
    (OneHotEncoder(handle_unknown="ignore", drop="first"), cat_cols),
    ("passthrough", cont_cols),
)

# Create and fit the pipeline model
pipeline, features = pipeline_model(oh_encoder, X_train, y_train, X_test, y_test)


# In[5]:


# Dirty Cat SuperVectorizer - 🧵 Simple!
super_encoder = SuperVectorizer()

# Create and fit the pipeline model
pipeline, features = pipeline_model(super_encoder, X_train, y_train, X_test, y_test)


# In[ ]:




