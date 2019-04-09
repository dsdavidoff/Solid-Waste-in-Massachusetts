# -*- coding: utf-8 -*-
"""
Danielle Davidoff
dsdavidoff@gmail.com
April 8, 2019

Tons of Waste in Solid Waste Facilities Around Massachusetts, by Municipality
downloaded dataset from mass.gov, 'Master List of Solid Waste Facilities in Massachusetts, May 2018

"""
import pandas as pd
import numpy as np

sites = pd.read_csv('sitesnotnull.csv')

sites.dropna(subset=['TPD_Max']) 
#drop null values

sites['TPD_Max'].replace('', np.nan, inplace=True)
#replace blank values with null values\

sites2 = sites.dropna(subset=['TPD_Max'])
#drop newly null values

sitesbycity = sites2.groupby('Muni').agg({'TPD_Max':['sum']})
#group solid waste sites by city, sum total number of tons of trash in landfills in each city

sitesbycity.index.name = 'Muncipality'
#rename index column (formerly 'Muni' in original dataset) as Municipality

sitesbycity.to_clipboard()
#export

