# VisualizationPractice
Visualization of Bank Failures by State over time

Using data gathered from: https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/index.html

This project was written in Python and uses the pandas and plotly packages.

FailedBanks.py:
Organizes the failed banks by year into a dictionary for each year. From there, we interate through the dictionary using two loops. Outer loop uses the dictionary keys for the year, inner loop uses the state code to count how many banks failed per state per year. Then using data gathered by state by year, outputs a choropleth graph for country.
18 graphs in total, some years had no data.

FailedBanksAnimation.py:
Instead of writing loops to create graphs for each year, plotly express has an animation function so that we can animate our data. There was a good amount of data wrangling in order to retrieve the data that we wanted, but after that, we could just use the choropleth function to create an animated map.

