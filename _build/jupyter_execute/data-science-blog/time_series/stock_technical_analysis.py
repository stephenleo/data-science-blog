#!/usr/bin/env python
# coding: utf-8

# # 💹 Stock Technical Analysis

# ## 📈 FinTA (Financial Technical Analysis)
# 
# FinTa (Financial Technical Analysis): Easily plot common financial technical indicators!
# - Feed-in your OHLCV (Open, High, Low, Close, Volume) pandas dataframe and plot away!
# - Supports 80 technical indicators! Including various moving averages, MACD, RSI, Bollinger Bands, Buy/Sell pressure, etc.
# - Full list of supported indicators on the Github page.
# 
# 🌟 Github: https://github.com/peerchemist/finta
# 
# Another way to make money with Data Science!🤑
# 
# I regularly post about practical and applied data science. If you like my posts, let's connect here or on Twitter @MarieStephenLeo!
# 
# #datascience #dataanlytics #timeseries #python #finance #technicalanalysis #fire

# In[1]:


# Imports
from finta import TA
import pandas as pd
pd.options.plotting.backend = "plotly"

# Load the data
df = pd.read_csv("data/stock_technical_analysis/aapl.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date").set_index("Date")

print(df.shape)
df.head(2)


# In[2]:


# 7, 50, 100 day moving averages
for num_days in [7, 50, 100]:
    df[f"sma_{num_days}"] = TA.SMA(df, num_days)
    
# bollinger bands
df = df.join(TA.BBANDS(df))

# Plot
cols_to_plot = ["sma_7", "sma_50", "sma_100", 
                "BB_UPPER", "BB_MIDDLE", "BB_LOWER"]
df[cols_to_plot].plot()


# In[ ]:




