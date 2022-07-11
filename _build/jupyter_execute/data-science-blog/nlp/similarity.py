#!/usr/bin/env python
# coding: utf-8

# # ♻️ Similarity

# ## 🌫️ Fuzzy String Matching

# In[1]:


# Generate random texts
from faker import Faker

fake = Faker()
fake.seed_instance(0)
fake_text = fake.text(max_nb_chars=200_000).split("\n")
print(fake_text[:3])


# In[2]:


# Imports
from rapidfuzz import process as rapidfuzz_process
from thefuzz import process as thefuzz_process


# In[3]:


get_ipython().run_cell_magic('time', '', 'thefuzz_process.extract("stock ball organization", choices=fake_text)\n')


# In[4]:


get_ipython().run_cell_magic('time', '', 'rapidfuzz_process.extract("stock ball organization", choices=fake_text)\n')


# In[ ]:




