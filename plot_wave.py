import methods.waveform_analysis as wp
import methods.histogram as hg
import database.data_pipeline as dp
import methods.clustering as cl

#EXTRACTING THE DATA FROM THE DOWNLOADED CSVs
wave = dp.vis_data()

dagupan = wave.extract('C:/Users/Jeckow236/Desktop/Taal Lightning Data/Dagupan/Dagupan 6-7pm/vlf_00181310_202001121015.csv')
dagupan_stack = wave.assign_points(dagupan.to_numpy())

legazpi = wave.extract('C:/Users/Jeckow236/Desktop/Taal Lightning Data/Legazpi/Legazpi 6-7pm/vlf_00181305_202001121015.csv')
legazpi_stack = wave.assign_points(legazpi.to_numpy())

palawan = wave.extract('C:/Users/Jeckow236/Desktop/Taal Lightning Data/Palawan/Palawan 6-7pm/vlf_00174736_202001121015.csv')
palawan_stack = wave.assign_points(palawan.to_numpy())

uplb = wave.extract('C:/Users/Jeckow236/Desktop/Taal Lightning Data/UPLB/UPLB 6-7pm/vlf_00173478_202001121015.csv')
uplb_stack = wave.assign_points(uplb.to_numpy())


'''
This is a centralized codebase dedicated for the data visualization of the downloaded 
data. Comment out the specific functions below if a certain visualization is 
not needed all.
'''


#(1) PLOTTING THE WAVEFORMS
# ax1, ax2, ax3, ax4 = wp.cartesian()

# col = 'blue'
# wp.plot_data(dagupan_stack, ax1, col)
# col = 'red'
# wp.plot_data(legazpi_stack, ax2, col)
# col = 'purple'
# wp.plot_data(palawan_stack, ax3, col)
# col = 'green'
# wp.plot_data(uplb_stack, ax4, col)


#(2) GENERATING HISTOGRAM DISTRIBUTIONS OF LIGHTNING STRIKES
# hgs = hg.set_histogram()

# dagupan_count = dagupan['time'].to_numpy()
# legazpi_count = legazpi['time'].to_numpy()
# palawan_count = palawan['time'].to_numpy()
uplb_count = uplb['time'].to_numpy()

   
# hg.plot_histogram(hgs[0,0], dagupan_count)
# hg.plot_histogram(hgs[0,1], legazpi_count)
# hg.plot_histogram(hgs[1,0], palawan_count)
# hg.plot_histogram(hgs[1,1], uplb_count)

#(3) TIME CLUSTERING OF REGISTERED LIGHTNING EVENTS
ax = cl.set_line()
time = cl.plot_time(ax, uplb_count)