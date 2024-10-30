'''
Input: Agrofood_co2_emission.csv and gdp.csv
Output: README.md
    ~ Labeled 4-panel plot:
        - Top left (A): Line plot of Year vs Average Temperature. Only plot the data for Mexico, Canada, and the United States. Lines should be colored according to the country and there should be a legend.
        - Top right (B): Scatter plot of year vs total greenhouse gas emissions from various sources (there’s a column for this in the dataset). Only plot the data for Mexico, Canada, and the United States–they should be colored to match the line plots in panel A and include a legend.
        - Bottom left (C): Scatter plot of GPD (from gdp.csv) vs total emissions for those countries colored by year
        - Bottom right (D): An additional figure of your choosing to support your narrative.
    ~ Explaination of plot
    ~ Answer to #4: If you had all the resources imaginable, what extra data and figures would you include in your report to strengthen your argument?

'''

import matplotlib as plt
import pandas as pd
