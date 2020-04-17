import numpy as np
import matplotlib.pyplot as plt

def set_histogram():
    fig, axs = plt.subplots(nrows = 2, ncols = 2, sharex = True, sharey = True)
    fig.suptitle('Lightning Histogram')
    
    
    axs[0, 0].set_title('Dagupan')
    axs[0, 1].set_title('Legazpi')
    axs[1, 0].set_title('Palawan')
    axs[1, 1].set_title('UPLB')
    
    return axs
    
def count_elements(time) -> dict:
    count = {}
    for i in time:
        count[i] = count.get(i, 0) + 1
        
    return count

def plot_histogram(ax, station_count):
    bins = [i for i in range(0,61,1)]
    ax.hist(station_count, bins, histtype = 'bar', rwidth = 0.8)