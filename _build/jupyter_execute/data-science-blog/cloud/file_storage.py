#!/usr/bin/env python
# coding: utf-8

# # 🗄️ File Storage (S3, GCS, etc)

# ## 📭 Smart Open
# Smart Open: Easiest way to read and write files from storage such as S3, GCS, Azure Blob Storage, HDFS, local filesystem, etc. 
# 
# - Drop-in replacement from python’s open()
# - On-the-fly decompression for a variety of different formats (.gz, .bz2)
# - Easily iterate over S3 bucket contents with iter_bucket()
# - Skip the boilerplate!
# 
# `pip install smart-open`
# 
# 🌟 Github: https://github.com/RaRe-Technologies/smart_open
# 
# 📖 More examples: https://github.com/RaRe-Technologies/smart_open/blob/develop/howto.md
# 
# 
# #datascience #dataanalytics #dataengineering #aws #gcp #azure #python
# 
# 
# ```{image} images/file_storage/Repos-smart_open.png
# :alt: smart_open
# :class: bg-primary mb-1
# :width: 100%
# :align: center
# ```

# In[1]:


# Imports
import boto3
from smart_open import open

file_to_read = "s3://commoncrawl/robots.txt"

# With Boto3 - 🥴
print("-----Reading with Boto3-----")
s3 = boto3.resource("s3")
split_filename = file_to_read.split("/")
obj = s3.Object(split_filename[2], "/".join(split_filename[3:]))
body = obj.get()["Body"].read()
print(body.decode())

# With Smart Open! - 😎
print("\n-----Reading with Smart Open-----")
with open(file_to_read) as f:
    print(f.read())


# In[ ]:




