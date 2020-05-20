import methods.waveform_analysis as wp
import methods.histogram as hg
import database.data_pipeline as dp
import methods.clustering as cl
import glob2
import numpy as np
import matplotlib.pyplot as plt


#--------------------listing all data directories---------------
# access_csvs = glob2.glob("C:/Users/Jeckow236/Desktop/Taal Lightning Data/Dagupan/0112/*.csv")
# dagupan_filenames = [i.replace('\\','/') for i in access_csvs]

# access_csvs = glob2.glob("C:/Users/Jeckow236/Desktop/Taal Lightning Data/Legazpi/0112/*.csv")
# legazpi_filenames = np.array([i.replace('\\','/') for i in access_csvs])

# access_csvs = glob2.glob("C:/Users/Jeckow236/Desktop/Taal Lightning Data/Palawan/0112/*.csv")
# palawan_filenames = np.array([i.replace('\\','/') for i in access_csvs])

# access_csvs = glob2.glob("C:/Users/Jeckow236/Desktop/Taal Lightning Data/UPLB/0112/*.csv")
# uplb_filenames = np.array([i.replace('\\','/') for i in access_csvs])

 
#-------------EXTRACTING THE DATA FROM THE DOWNLOADED CSVs------------
wave = dp.vis_data()

dagupan = wave.extract('C:/Users/Jeckow236/Desktop/Taal Lightning Data/Dagupan/Dagupan 6-7pm/vlf_00181310_202001121002.csv')
dagupan_stack = wave.assign_points(dagupan.to_numpy())

legazpi = wave.extract('C:/Users/Jeckow236/Desktop/Taal Lightning Data/Legazpi/Legazpi 6-7pm/vlf_00181305_202001121002.csv')
legazpi_stack = wave.assign_points(legazpi.to_numpy())

palawan = wave.extract('C:/Users/Jeckow236/Desktop/Taal Lightning Data/Palawan/Palawan 6-7pm/vlf_00174736_202001121002.csv')
palawan_stack = wave.assign_points(palawan.to_numpy())

uplb = wave.extract('C:/Users/Jeckow236/Desktop/Taal Lightning Data/UPLB/UPLB 6-7pm/vlf_00173478_202001121002.csv')
uplb_stack = wave.assign_points(uplb.to_numpy())

'''
This is a centralized codebase dedicated for the data visualization of the downloaded 
data. Comment out the specific functions below if a certain visualization is 
not needed all.
'''

#--------------------(1) PLOTTING THE WAVEFORMS------------------
ax1, ax2, ax3, ax4 = wp.cartesian()

col = 'blue'
wp.plot_data(dagupan_stack, ax1, col)
col = 'red'
wp.plot_data(legazpi_stack, ax2, col)
col = 'purple'
wp.plot_data(palawan_stack, ax3, col)
col = 'green'
wp.plot_data(uplb_stack, ax4, col)


#-------(2) GENERATING HISTOGRAM DISTRIBUTIONS OF LIGHTNING STRIKES----------
#-----------------------subplot histograms------------------
# hgs = hg.subplot_histograms()

dagupan_count = dagupan['time'].to_numpy()
legazpi_count = legazpi['time'].to_numpy()
palawan_count = palawan['time'].to_numpy()
uplb_count = uplb['time'].to_numpy()

# hg.plot_histogram(hgs[0,0], dagupan_count, None)
# hg.plot_histogram(hgs[0,1], legazpi_count, None)
# hg.plot_histogram(hgs[1,0], palawan_count, None)
# hg.plot_histogram(hgs[1,1], uplb_count, None)

#------------------------Daily histogram----------------------
# ax = hg.hourly_histogram()
# dagupan_hours = np.array([])
# for i in dagupan_filenames:
#     dagupan_hours = np.append(dagupan_hours, float(i[-8:-6]) + (float(i[-6:-4]) + dagupan['time'].to_numpy(dtype = float)/60)/60)
# hg.plot_histogram(ax, dagupan_hours, 'January 12 Dagupan')
    
# ax = hg.hourly_histogram()
# legazpi_hours = np.array([])
# for i in legazpi_filenames:
#     legazpi_hours = np.append(legazpi_hours, float(i[-8:-6]) + (float(i[-6:-4]) + legazpi['time'].to_numpy(dtype = float)/60)/60)
# hg.plot_histogram(ax, legazpi_hours, 'January 12 Legazpi')

# ax = hg.hourly_histogram()
# palawan_hours = np.array([])
# for i in palawan_filenames:
#     palawan_hours = np.append(palawan_hours, float(i[-8:-6]) + (float(i[-6:-4]) + palawan['time'].to_numpy(dtype = float)/60)/60)
# hg.plot_histogram(ax, palawan_hours, 'January 12 Palawan')

# ax = hg.hourly_histogram()
# uplb_hours = np.array([])
# for i in uplb_filenames:
#     uplb_hours = np.append(uplb_hours, float(i[-8:-6]) + (float(i[-6:-4]) + uplb['time'].to_numpy(dtype = float)/60)/60)
# hg.plot_histogram(ax, uplb_hours, 'January 12 UPLB')

#----------(3) TIME CLUSTERING OF REGISTERED LIGHTNING EVENTS--------------
ax1 = cl.set_line()
centroids, clusters = cl.cluster_algo(dagupan_count)
cl.plot_time(ax1, centroids, 1, 'Dagupan Cluster')
cl.plot_time(ax1, clusters, 2, None)

ax2 = cl.set_line()
centroids, clusters = cl.cluster_algo(legazpi_count)
cl.plot_time(ax2, centroids, 1, 'Legazpi Cluster')
cl.plot_time(ax2, clusters, 2, None)

ax3 = cl.set_line()
centroids, clusters = cl.cluster_algo(palawan_count)
cl.plot_time(ax3, centroids, 1, 'Palawan Cluster')
cl.plot_time(ax3, clusters, 2, None)

ax4 = cl.set_line()
centroids, clusters = cl.cluster_algo(uplb_count)
cl.plot_time(ax4, centroids, 1, 'UPLB Cluster')
cl.plot_time(ax4, clusters, 2, None)

#------------(4) BOX PLOTS FOR CHECKNG TIME OUTLIERS----------------
# fig, ax = plt.subplots()
# outliers = dict(markerfacecolor = '#B2DBBF', marker = 'o', alpha = 0.8)
# whiskers = dict(ls = '--', color = 'green')
# medianprops = dict(linestyle='-.', linewidth=2.5, color='#70C1B3')
# boxes = dict(facecolor = '#F1F1F1', color = 'black')
# meanpoint = dict(marker='D', markeredgecolor='black', markerfacecolor='#247BA0')
# data = [dagupan_hours, legazpi_hours, palawan_hours, uplb_hours]

# ax.set_title('January 12 Lightning Distribution Data')
# ax.boxplot(data, labels = ['Dagupan', 'Legazpi', 'Palawan', 'UPLB'], 
#            notch = True, flierprops = outliers, showmeans = True,
#            medianprops = medianprops, meanprops = meanpoint,
#            whis = [5, 95], whiskerprops = whiskers,
#            boxprops = boxes, patch_artist = True, positions = [1, 1.5, 2, 2.5],
#            widths = [0.3, 0.3, 0.3, 0.3])
# plt.grid(ls = ':', alpha = 0.5)
# ax.set_ylabel('Time (H)')

# print('Means:')
# print(sum(dagupan_hours)/len(dagupan_hours))
# print(sum(legazpi_hours)/len(legazpi_hours))
# print(sum(palawan_hours)/len(palawan_hours))
# print(sum(uplb_hours)/len(uplb_hours))

# print('\nMedians:')
# print(np.median(dagupan_hours))
# print(np.median(legazpi_hours))
# print(np.median(palawan_hours))
# print(np.median(uplb_hours))