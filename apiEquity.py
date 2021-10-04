#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 14:07:40 2021

@author: William
"""

import requests
import pandas as pd 


##Will be utilzing real time intraday equity data from Alpha Vantage 
##Adjusted API link to pull data for ticker "SPY" with 5 minute intervals 

apikey = 'INSERTHERE'
endpoint = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SPY&interval=5min&apikey=INSERTHERE'
r = requests.get(endpoint)
r.status_code

spyInfo = r.json()
spyInfodf = pd.DataFrame(spyInfo['Time Series (5min)'])
spyInfodf
