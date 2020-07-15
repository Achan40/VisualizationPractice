import pandas as pd
import plotly as py
import plotly.graph_objs as go

#import excel file
failed = pd.read_csv('banklist.csv')
#list of states(unique)
failed_states = list(set(failed['ST']))
#list of years(unique). had to strip last 2 characters of column to get the year then sort the list
failed_years = sorted(list(set(failed['Closing Date'].str.strip().str[-2:])))

#create dictionary for each year
d = {year: pd.DataFrame for year in failed_years}
#select rows for each year and assign to dictionary
for key in d.keys():
    d[key] = failed[failed['Closing Date'].str.endswith(key)]

#nested loop so I can count the number of bank failures for each year by state
for key in d.keys():
    #totals by state go in this list
    listx = []
    for i in failed_states:
        x = len(d[key][d[key]['ST'].str.contains(i)])
        listx.append(x)
        #loop until total data for each year acheived
        if len(listx) == len(failed_states):
            #uses each loop to output a graph of a choropleth map for bank failures per year in the US for all keys in the dictionary
            data = dict(
                type = 'choropleth',
                locations = failed_states,
                locationmode = 'USA-states',
                colorscale = 'Viridis',
                z = listx,
                zmin = 0,
                zmax = 30,
                title='test')
            lyt = dict(geo=dict(scope='usa'))
            map = go.Figure(data=[data], layout=lyt)
            py.offline.plot(map)
        else:
            continue