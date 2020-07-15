import plotly.express as px
import pandas as pd

failed = pd.read_csv('banklist.csv')
#create year column by taking last two strings in original column of the data which represent the year
fdf_yr = pd.DataFrame(failed['Closing Date'].str.strip().str[-2:])
#add 20-- to begining of new column
fdf_yr['Closing Date'] = '20' + fdf_yr['Closing Date'].astype(str)
#create state code column
fdf_state = pd.DataFrame(failed['ST'])
#create indicator column
fdf_yes = pd.DataFrame([1]*len(failed))

#merge into a new dataframe
fdf = pd.concat([fdf_state,fdf_yr,fdf_yes], axis=1)
#change column names
fdf.rename(columns={'ST':'State','Closing Date':'Year', 0:'Fail'}, inplace=True)

#to get total number of fails per state per year, use groupby function (we have to reset index to get it back to dataframe)
fdf = fdf.groupby(['State','Year'])['Fail'].sum().reset_index()

#sort values by year
fdf = fdf.sort_values(by=['Year'])

fdf_ani = px.choropleth(fdf,
                        locations='State',
                        color='Fail',
                        animation_frame='Year',
                        color_continuous_scale="Inferno",
                        locationmode='USA-states',
                        scope="usa",
                        range_color=(0, 30),
                        title='Bank Failures United States since 2000',
                        height=600
                        )
fdf_ani.show()

