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
            data = dict(
                type = 'choropleth',
                locations = failed_states,
                locationmode = 'USA-states',
                colorscale = 'Viridis',
                z = listx)
            lyt = dict(geo=dict(scope='usa'))
            map = go.Figure(data=[data], layout=lyt)
            py.offline.plot(map)
            print(listx)
        else:
            continue


#data = dict(
    #type = 'choropleth',
    #locations = failed_states,
    #locationmode = 'USA-states',
    #colorscale = 'Viridis',
    #z = listx)
#lyt = dict(geo=dict(scope='usa'))
#map = go.Figure(data=[data], layout=lyt)
#py.offline.plot(map)

#select rows ending with '00' for the year 2000
#failed_00 = failed[failed['Closing Date'].str.endswith('00')]

#loop to find the number of failures per state for year
#listx = []
#for i in failed_states:
        #gets the sum of boolean values for 'true' for any state and appends to empty list
#        x = len(failed_00[failed_00['ST'].str.contains(i)])
  #      listx.append(x)
 #       print(listx)

#data = dict (
    #type = 'choropleth',
    #locations = failed_states,
    #locationmode = 'USA-states',
    #colorscale = 'Viridis',
    #z = listx)

#lyt = dict(geo=dict(scope='usa'))
#map = go.Figure(data=[data], layout = lyt)
#py.offline.plot(map)
