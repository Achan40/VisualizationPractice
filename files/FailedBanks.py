import pandas as pd
import plotly as py
import plotly.graph_objs as go

#import excel file
failed = pd.read_csv('banklist.csv')
#list of states(unique)
failed_states = list(set(failed['ST']))

#loop to find the number of failures per state
listx = []
for i in failed_states:
        #gets the sum of boolean values for 'true' for any state and appends to empty list
        x = len(failed[failed['ST'].str.contains(i)])
        listx.append(x)

data = dict (
    type = 'choropleth',
    locations = failed_states,
    locationmode = 'USA-states',
    colorscale = 'Viridis',
    z = listx)

lyt = dict(geo=dict(scope='usa'))
map = go.Figure(data=[data], layout = lyt)
py.offline.plot(map)
