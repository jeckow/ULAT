"""2nd method: Linear least squares but on a hyperbolic equation"""
import numpy as np
import pandas as pd
import sympy as sp
from itertools import combinations

def tdoa2(parameters):
    co = 299.792458 #in meters per microseconds
    df = pd.DataFrame(parameters[:,1:])
    locs  = np.array(df, dtype = np.float32)
    latitudes = np.array(locs[:,2])
    longitudes = np.array(locs[:,1])

#calculating delta parameters:   
    #▲t
    times = np.array(locs[:,0])
    t1, t2 = zip(*list(combinations(times, 2)))
    time_diff = abs(np.array(t1)-np.array(t2))

    #▲x
    comb_lat1, comb_lat2 = zip(*list(combinations(latitudes,2)))
    lat_pairs = np.array(np.transpose([comb_lat1, comb_lat2]))
    lat_diff = lat_pairs[:,0] - lat_pairs[:,1]
    
    #▲y
    comb_long1, comb_long2 = zip(*list(combinations(longitudes,2)))
    long_pairs = np.array(np.transpose([comb_long1, comb_long2]))
    long_diff = long_pairs[:,0] - long_pairs[:,1]

    #[▲x ▲y -(c^2)▲t]
    A = np.transpose(np.array([lat_diff, long_diff, time_diff*co**2]))
    
#calculating K paramemters:
    ri2 = np.transpose([lat_pairs[:,0]**2 + long_pairs[:,0]**2])
    rj2 = np.transpose([lat_pairs[:,1]**2 + long_pairs[:,1]**2])
    tdiff_sqr = np.transpose(np.array([np.array(t1)**2 - np.array(t2)**2]))
    K = 0.5*(ri2 - rj2 - (co**2) * tdiff_sqr )
    
#least squares solution
    ans = np.dot(np.linalg.inv(np.dot(np.transpose(A),A)), np.dot(np.transpose(A),K))
    return ans[0,0], ans[1,0], ans[2,0]