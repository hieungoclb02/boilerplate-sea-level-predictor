import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
    slope, intercept, rvalue, pvalue, stderr= linregress(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])

    x= np.array([i for i in range(1880,2051)])
    y= intercept+slope*x

    # Create first line of best fit
    plt.plot(x,y,'r')
   

    # Create second line of best fit
    df_new=df[df.Year>=2000]
    slope, intercept, rvalue, pvalue, stderr= linregress(x=df_new['Year'],y=df_new['CSIRO Adjusted Sea Level'])
    x = np.array([i for i in range(2000,2051)])
    y= intercept+slope*x
    plt.plot(x,y,'r');
    plt.ylabel('Sea Level (inches)')
    plt.xlabel('Year')
    plt.title('Rise in Sea Level')

    
    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()
