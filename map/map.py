import geopandas as gpd
import matplotlib.pyplot as plt
import psycopg2
import numpy as np
import pandas as pd
from shapely.geometry import Point
from scipy import interpolate
from mpl_toolkits.basemap import Basemap

#START SESSION
db_connect = psycopg2.connect(
    dbname = 'philsensor',
    user = 'jerico_orejudos',
    password = 'R5Lxgwf6TZhVMrHy',
    host = '202.90.158.249',
    port = '5433')

cur = db_connect.cursor()    

#-----QUERY FOR STATION NAMES
query = 'SELECT {0} FROM ulat.tbl_station WHERE province = {1}'.format('location','\'METRO MANILA\'')
cur.execute(query)
stations = np.array(cur.fetchall())
for name in stations:
    name = str(name).strip('(\'\'),')

ids = []
for row in stations:
    ids.append(row[0])
#try np.ravel() ???

#-----QUERY FOR LATITUDES
query = 'SELECT {0} FROM ulat.tbl_station WHERE province = {1}'.format('latitude','\'METRO MANILA\'')
cur.execute(query)
latitudes = cur.fetchall()

lat = []
for row in latitudes:
    lat.append(row[0])
 
    
#-----QUERY FOR LONGITUDES
query = 'SELECT {0} FROM ulat.tbl_station WHERE province = {1}'.format('longitude','\'METRO MANILA\'')
cur.execute(query)
longitudes = cur.fetchall()

long = []
for row in longitudes:
    long.append(row[0])

#----RANDOM TEMPERATURES FOR TESTING
temp = np.random.uniform(35,37,len(long))
    
d = {'id': ids, 'lat': lat, 'long': long, 'temp': temp}
df = pd.DataFrame(data = d)
df = df.dropna()
print(df)
#TEMPORARY REPLACEMENT OF COORDINATES DUE TO DATABASE ERROR
#[14.6706, 120.9552])
df = df.replace(to_replace = [df.lat[0], df.long[0]], value = [14.6706, 120.9552])
df = df.replace(to_replace = [df.lat[1], df.long[1]], value = [14.4384, 121.0097])
df = df.replace(to_replace = [df.lat[2], df.long[2]], value = [14.4778, 120.9799])
df = df.replace(to_replace = [df.lat[3], df.long[3]], value = [14.604, 121.0406])
df = df.replace(to_replace = [df.lat[5], df.long[5]], value = [14.4385, 121.0097])
df = df.replace(to_replace = [df.lat[6], df.long[6]], value = [14.5769, 121.0335])
df = df.replace(to_replace = [df.lat[7], df.long[7]], value = [14.6297, 120.9687])
df = df.replace(to_replace = [df.lat[9], df.long[9]], value = [14.7134,	121.0009])
df = df.replace(to_replace = [df.lat[11], df.long[11]], value = [14.4119, 121.0522])
df = df.replace(to_replace = [df.lat[13], df.long[13]], value = [14.6509, 120.9475])
df = df.replace(to_replace = [df.lat[14], df.long[14]], value = [14.4575, 121.0513])
df = df.replace(to_replace = [df.lat[15], df.long[15]], value = [14.5354, 121.0412])
df = df.replace(to_replace = [df.lat[16], df.long[16]], value = [14.5107, 121.0358])
df = df.replace(to_replace = [df.lat[17], df.long[17]], value = [14.3836, 121.0337])
df = df.replace(to_replace = [df.lat[18], df.long[18]], value = [14.6450, 121.0443])
df = df.replace(to_replace = [df.lat[19], df.long[19]], value = [14.4728, 121.0185])
df = df.replace(to_replace = [df.lat[20], df.long[20]], value = [14.6588, 121.0298])
df = df.replace(to_replace = [df.lat[23], df.long[23]], value = [14.5141, 121.0045])
df = df.replace(to_replace = [df.lat[24], df.long[24]], value = [14.5837, 121.0062])
df = df.replace(to_replace = [df.lat[25], df.long[25]], value = [14.4896, 121.0521])
df = df.replace(to_replace = [df.lat[26], df.long[26]], value = [14.6705, 120.9973])
df = df.replace(to_replace = [df.lat[27], df.long[27]], value = [14.7409, 120.9899])
df = df.replace(to_replace = [df.lat[28], df.long[28]], value = [14.694, 121.0086])
df = df.replace(to_replace = [df.lat[29], df.long[29]], value = [14.6934, 120.9683])
df = df.replace(to_replace = [df.lat[30], df.long[30]], value = [14.5729, 121.0974])
df = df.replace(to_replace = [df.lat[31], df.long[31]], value = [14.5702,121.0818])
df = df.drop(['id'], axis = 1)
# print(df)

#CLOSE SESSION
cur.close()    
db_connect.close()


#TRUNCATE COORDINATES
lat_truncate = [float('%.2f'%(row)) for row in df.lat]
long_truncate = [float('%.2f'%(row)) for row in df.long]
# new_temp = df.temp.to_numpy(dtype = float)
truncated_coordinates = np.transpose([lat_truncate, long_truncate])

#PIECEWISE FUNCTION 
x, y = np.mgrid[0:14.8:0.01, 0:121.15:0.01]
z = np.empty(x.shape)

for i in range(len(truncated_coordinates)):
    lat_index = int(truncated_coordinates[i][0]/0.01)
    long_index = int(truncated_coordinates[i][1]/0.01)
    z[lat_index][long_index] =  temp[i]


# geometry = [Point(xy) for xy in zip(df.long, df.lat)]
# df = df.drop(['long', 'lat'], axis = 1)
# crs = {'init': 'epsg 4326'}
# stations_gdf = gpd.GeoDataFrame(df, crs = crs, geometry = geometry)
# # print(stations_gdf)

# #GENERATE MAP
# gdf = gpd.read_file('Metropolitan Manila.shp')
# # gdf_webmerc = gdf.to_crs(epsg = 3857) 
# # gdf_webmerc.plot(cmap = 'gray', figsize = (100,50))
# # metro = gdf.plot(cmap = 'gray', figsize = (100,50))
# # gdf_webmerc.plot(ax = ax)

# base = gdf.plot(cmap = 'bone', figsize = (100,50))
# ax = stations_gdf.plot(ax = base, color = 'firebrick', markersize = 300, figsize = (100,50))