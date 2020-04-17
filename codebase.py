'''
Algorithm #1: Based on IEEE paper DOI 10.1109/MSP.2005.1458275
Algorithm #2: Based on Alex's sent paper

Comment out the linear least squares alogirthm for if not needed to be simulated
'''
import methods.lls as lls
import database.data_pipeline as dp
import numpy as np
import pandas as pd

'''
FOR FUNCTIONAL TESTING
v_poteka = np.array([['Dagupan',0.0003,120.352008,16.086819],
                      ['Legazpi',0.0019,123.728444,13.150769],
                      ['Puerto Princessa',0.0008,118.758694,9.740128],
                      ['UPLB',0.0003,121.250111,14.164922]]
                    )

print(lls2.tdoa2(v_poteka))
'''

#input CSVs links here
dagupan = dp.data()
dagupan = abs(dagupan.extract('C:/Users/Jeckow236/Desktop/Taal Lightning Data/Dagupan/Dagupan 6-7pm/vlf_00181310_202001121021.csv'))

legazpi = dp.data()
legazpi = abs(legazpi.extract('C:/Users/Jeckow236/Desktop/Taal Lightning Data/Legazpi/Legazpi 6-7pm/vlf_00181305_202001121021.csv'))

palawan = dp.data()
palawan = abs(palawan.extract('C:/Users/Jeckow236/Desktop/Taal Lightning Data/Palawan/Palawan 6-7pm/vlf_00174736_202001121021.csv'))

uplb = dp.data()
uplb = abs(uplb.extract('C:/Users/Jeckow236/Desktop/Taal Lightning Data/UPLB/UPLB 6-7pm/vlf_00173478_202001121021.csv'))

#brute force linear least squares algorithm 1
move_strikes = dp.data()
for i in dagupan:
    for j in legazpi:
        for k in palawan:
            for l in uplb:
                v_poteka = np.array([['Dagupan',i,120.352008,16.086819],
                      ['Legazpi',j,123.728444,13.150769],
                      ['Puerto Princessa',k,118.758694,9.740128],
                      ['UPLB',l,121.250111,14.164922]]
                    )
                
                lat, long = lls.tdoa1(v_poteka)
                print(lat, long)
                geolocation_points = move_strikes.put(lat, long)
        

#brute force linear least squares algorithm 2
move_strikes = dp.data()
for i in dagupan:
    for j in legazpi:
        for k in palawan:
            for l in uplb:
                v_poteka = np.array([['Dagupan',i,120.352008,16.086819],
                      ['Legazpi',j,123.728444,13.150769],
                      ['Puerto Princessa',k,118.758694,9.740128],
                      ['UPLB',l,121.250111,14.164922]]
                    )
                
                lat, long, t = lls.tdoa2(v_poteka)
                print(lat, long, t)
                geolocation_points = move_strikes.put(lat, long)
        
# store to csv   
geolocation_points.to_csv('C:/Users/Jeckow236/Desktop/Taal Lightning Data/gelocation2_621.csv')