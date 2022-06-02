#!/usr/bin/env python
# coding: utf-8

# # 🗂️ Weak Supervision
# 
# - Weak Supervision is the Data Centric AI technique to 
# > Reduce the efforts of manual labeling while unlocking the vast knowledge of domain subject matter experts (SMEs) by leveraging a diversity of weaker, often programmatic supervision sources.
# 
# ![](images/weak_supervision/drake_meme.png)

# ## 🎤 No Training Data? No Problem! Weak Supervision to the Rescue! 
# 
# - Presentation at Quantum Black Meetup at Singapore on May 19, 2022: [Link to slides](https://www.slideshare.net/StephenLeo7/weak-supervisionpdf)
# - The topics I covered are,
#     - ML's insatiable need for large datasets
#     - Contemporary ML leaving out domain knowledge from Subject Matter Experts
#     - How Weak Supervision, an approach of Data-Centric AI, solves both the problems simultaneously by encoding domain subject matter expertise into programmatic labeling functions.
#     - The WRENCH benchmark to compare various weak supervision algorithms on several standard datasets.
#     - Snorkel to combine the various labeling functions.
#     - COSINE to fine-tune a final transformer based model that overcomes the noise in weak labels
#     - Future Directions and Resources
# 
# - The slides have several links to all the necessary resources if you're interested to read more.
# 
# - Feel free to use the slides but please remember to credit me with a link back to this repository or my Linkedin profile!
# 
# #datascience #machinelearning #artificialintelligence #nlp #algorithms
# 
# [![](images/weak_supervision/quantum_black_meetup_talk.png)](https://www.slideshare.net/StephenLeo7/weak-supervisionpdf)

# ## 🦦 WeaSEL: Weakly Supervised End-to-end Learning
# 
# An interesting paper/code for those of us working on problems that have low/no labels but high SME domain knowledge. **WeaSEL: Weakly Supervised End-to-end Learning**.
# 
# Train your favorite neural network for weakly-supervised classification:
# 
# ✅ With only labeling functions (LFs), i.e. without any labeled training data!
# 
# ✅ In an end-to-end manner, i.e. directly train and evaluate your neural net, there's no need to train a separate label model anymore as in Snorkel
# 
# ✅ With a better test set performance and enhanced robustness against correlated or inaccurate LFs than prior methods like Snorkel
# 
# 🌟 Github: [https://github.com/autonlab/weasel](https://github.com/autonlab/weasel)
# 
# 📖 Paper: [https://arxiv.org/abs/2107.02233](https://arxiv.org/abs/2107.02233)
# 
# Have you used any other weak supervision library? Please share in the comments!
# 
# #nlp #machinelearning #datascience #researchpaper #github #dataprogramming #weaksupervision
# 
# ![](images/weak_supervision/weasel_performance.png)

# In[ ]:




