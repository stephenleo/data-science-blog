#!/usr/bin/env python
# coding: utf-8

# # 🔀 Named Entity Resolution

# ## Named Entity Linking - 🥔 Spacy OpenTapioca
# 
# - Named Entity Linking is the task of detecting mentions of entities from a knowledge base in free text
# - OpenTapioca is a simple and fast Named Entity Linking system for Wikidata
# - Wikidata is a free knowledge base that contains a variety of information about real world entities.
# - For example, if you want to know who's Linkedin's parent company, wikidata is the knowledge base to programatically get this information.
# 
# 🌟 Spacy OpenTapioca Github: https://github.com/UB-Mannheim/spacyopentapioca
# 
# 🌟 Pywikibot Github: https://github.com/wikimedia/pywikibot

# In[1]:


import spacy
from pywikibot.data.sparql import SparqlQuery

# Add Spacy OpenTapioca Pipeline to identify the entities
nlp = spacy.blank("en")
nlp.add_pipe("opentapioca")

# Wikidata Sparql to query properties of the entity
query = SparqlQuery()

property_to_query = "P749"  # https://www.wikidata.org/wiki/Wikidata:List_of_properties

sparql_query = """
SELECT ?name ?nameLabel 
WHERE {{
  wd:{wikidata_id} wdt:{property_to_query} ?name.
  SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}
}}
"""


# In[2]:


# Run the entity linking analysis
doc = nlp("LinkedIn Premium is offered in four tiers")

for span in doc.ents:
    print(f"Entity: {span.text}")

    # From OpenTapioca
    wikidata_id = span.kb_id_
    print(f"    Wikidata ID: {wikidata_id}")
    print(f"    Desc: {span._.description}")

    # From WikiData
    for item in query.select(
        sparql_query.format(
            wikidata_id=wikidata_id, property_to_query=property_to_query
        )
    ):
        print(f"    Parent Org: {item['nameLabel']}")

    print("\n--------------------------------------------------\n")


# In[ ]:




