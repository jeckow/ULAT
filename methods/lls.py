import numpy as np
import pandas as pd
import sympy as sp
from itertools import combinations

"""1st method: Linear least squares via circle equations"""
#Sorting the stations based on time of arrival
def tdoa1(parameters):
    co = 299.792458 #in meters per microseconds
    df = pd.DataFrame(parameters[:,1:])
    locs = np.array(df.sort_values(by = 0, ascending = 1), dtype = np.float32)
    times = np.transpose(np.array([locs[:,0]]))
    
#shift coordinates to the origin
    Hs = np.array(locs[1:,1:] - locs[0,1:])

#TDOA w.r.t the 1st station
    ri1 = np.transpose(np.array([co*(times[1:,0]-times[0,0])]))
    
#calculating other parameters for least squares
    c = -ri1
    r1 = np.array([locs[0,1]**2 + locs[0,2]**2])
    Ksq = np.transpose(np.array([Hs[:,0]**2 + Hs[:,1]**2]))
    d = 0.5*np.array(Ksq-ri1**2)

#calculating the intermediate least squares solution
    Hs_trn = np.transpose(Hs)
    Hs_inv = np.linalg.inv(Hs_trn.dot(Hs))
    xint = np.array(Hs_inv.dot(Hs_trn).dot([c,d])).reshape(2,2)
    
#calculating the final least squares solution
    x1, y1, ri = sp.symbols('x y r')  
    x1 = ri*xint[0,0] + xint[0,1]
    y1 = ri*xint[1,0] + xint[1,1]
    roots = sp.Eq(x1**2 + y1**2 - ri**2,0)
    sol = sp.solve(roots, ri)
    r = np.array([i for i in sol if i> 0 ])
    shifted = np.array([r*xint[0,0] + xint[0,1], r*xint[1,0] + xint[1,1]])
    source = np.transpose(shifted) + locs[0,1:] + 0.9944
    
    return source[0,1], source[0,0]

"""2nd method: Linear least squares via hyperbolic equations"""
def tdoa2(parameters):
    co = 299.792458 #in meters per microseconds
    df = pd.DataFrame(parameters[:,1:])
    locs  = np.array(df, dtype = np.float32)
    latitudes = np.array(locs[:,2])
    longitudes = np.array(locs[:,1])
    print(df)
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