import numpy as np
import matplotlib.pyplot as plt

def subplot_histograms():
    fig, axs = plt.subplots(nrows = 2, ncols = 2, sharex = True, sharey = True)
    fig.suptitle('Lightning Histogram')
    axs[0, 0].set_title('Dagupan')
    axs[0, 1].set_title('Legazpi')
    axs[1, 0].set_title('Palawan')
    axs[1, 1].set_title('UPLB')
    
    return axs


def hourly_histogram():
    plt.figure()
    ax = plt.gca()
    ax.set_xlim([0, 24])
    ax.set_xlabel('time (H)')
    ax.set_ylabel('Number of strikes')
    plt.grid(ls = ':')
            
    return ax
    

# def count_elements(time) -> dict:
#     count = {}
#     for i in time:
#         count[i] = count.get(i, 0) + 1
#     print(count)
#     return count


def plot_histogram(ax, station_count, title):
    plt.title(title)
    n, bins, patches = ax.hist(station_count, bins = np.linspace(0,24,49),\
            histtype = 'bar', facecolor='#2ab0ff',\
            edgecolor='#e0e0e0', linewidth=0.5, alpha=0.7)
    n = n.astype('int')
    
    for i in range(len(patches)):
        patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))