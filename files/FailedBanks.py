import pandas as pd
import numpy as np
import geopandas as gpd
import plotly.figure_factory as ff

#import excel file
failed = pd.read_csv('banklist.csv')

fips = ['06021', '06023', '06027',
        '06029', '06033', '06059',
        '06047', '06049', '06051',
        '06055', '06061']
values = range(len(fips))

fig = ff.create_choropleth(fips=fips, values=values)
fig.layout.template = None
fig.show()