#imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_histogram_with_stats(df, columns, yscale=False):
    """
    Plots a histogram with mean and median lines for the given data series.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    columns (list): List of column names for which to generate the histogram.
    yscale (bool): If True, set y-scale to log.

    Returns:
    None
    """
    for i in columns:
        sns.histplot(df[i])
        plt.axvline(df[i].mean(), color='r', linestyle='--')
        plt.axvline(df[i].median(), color='g', linestyle='-')
        plt.title('Histogram for ' + str(i))
        
        plt.legend({'Mean': df[i].mean(), 'Median': df[i].median()})
        
        if yscale:
            plt.yscale('log')
            
        plt.show()
