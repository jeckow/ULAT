import numpy as np
import matplotlib.pyplot as plt

def set_line():
    plt.figure()
    ax = plt.gca()
    ax.set_xlim([0,60])
    ax.set_ylim([-1,1])
    plt.axhline(y = 0, color = 'k', lw = 0.8, ls = '--')
    plt.xlabel('Time (s)')
    plt.grid(ls = ':')
    
    return ax


def plot_time(ax, points, key, name):
    if key == 0:
        y = np.zeros(len(points))
        ax.scatter(points, y, color = "#FF1654", alpha = 0.8)
        
    elif key == 1:
        y = np.zeros(len(points))
        palette = ['#247BA0', '#70C1B3', '#B2DBBF']
        ax.scatter(points, y, color = palette, alpha = 0.2, s = 200)
        u1 = ax.axvline(x = points[0], color = palette[0])
        u2 = ax.axvline(x = points[1], color = palette[1])
        u3 = ax.axvline(x = points[2], color = palette[2])
        plt.title(name)
        plt.legend([u1, u2, u3], ['µ1', 'µ2', 'µ3'])
        ax.set_facecolor('#F1F1F1')
        
       
    elif key == 2:
        y = np.zeros(len(points[0]))
        ax.scatter(points[0], y, color = '#247BA0', alpha = 0.8)

        y = np.zeros(len(points[1]))
        ax.scatter(points[1], y, color = '#70C1B3', alpha = 0.8)

        y = np.zeros(len(points[2]))
        ax.scatter(points[2], y, color = '#B2DBBF', alpha = 0.8)
        
    return ax
    

def cluster_algo(time):
    # k = 3 #set number of clusters
    centroids = np.array([10, 30, 50])
    # centroids = np.random.randint(low = 1, high = 60, size = k)

    for i in range(15):
        l2_dist = [[np.linalg.norm(i-j) for j in centroids] for i in time]
        bin0, bin1, bin2 = np.array([]), np.array([]), np.array([])
        
        for i in range(len(time)):
            if l2_dist[i].index(min(l2_dist[i])) == 0:
                bin0 = np.append(bin0, time[i])
                
            if l2_dist[i].index(min(l2_dist[i])) == 1:
                bin1 = np.append(bin1, time[i])
                
            if l2_dist[i].index(min(l2_dist[i])) == 2:
                bin2 = np.append(bin2, time[i])    
        
        # print('\n')
        # print(len(bin0))
        # print(len(bin1))
        # print(len(bin2))
        
        c0 = sum(bin0)/len(bin0) if len(bin0) != 0 else 0
        c1 = sum(bin1)/len(bin1) if len(bin1) != 0 else 0
        c2 = sum(bin2)/len(bin2) if len(bin2) != 0 else 0
        
        centroids = np.array([c0, c1, c2])

    centroids[centroids == 0] = None
    clusters = np.array([bin0, bin1, bin2])
    print(centroids)
    return centroids, clusters
    