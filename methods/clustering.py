import numpy as np
import matplotlib.pyplot as plt

def set_line():
    plt.figure()
    ax = plt.gca()
    ax.set_xlim([0,60])
    ax.set_ylim([-1,1])
    plt.axhline(y = 0, color = 'k', lw = 0.8, ls = '--')
    plt.xlabel('Time (s)')
    plt.title('Time plots of lightning occurences')
    plt.grid(ls = ':')
    
    return ax


def plot_time(ax, time):
    y = np.zeros(len(time))
    ax.scatter(time,y)
    

def cluster_algo(ax, time):
    np.random.seed(200)
    k = 3 #set number of clusters
    
    for i in range 
    
    