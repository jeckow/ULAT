import pandas as pd
import numpy as np

class data():
    def __init__(self):
        self.column_names = ['Latitude', 'Longitude']
        self.strikes = pd.DataFrame(columns = self.column_names)
    
    def extract(self, path):
        self.path = path
        self.dp = pd.read_csv(self.path,
                          usecols = [6,9],
                          names = ["TPS", "TPN"],
                        )        
        self.dp['TPS'] = self.dp['TPS'].map(lambda x: x.lstrip('TPS'))
        self.dp['TPN'] = self.dp['TPN'].map(lambda x: x.lstrip('TPN'))
        self.dp['TPS'] = self.dp.TPS.astype(float)
        self.dp['TPN'] = self.dp.TPN.astype(float)
        
        return (self.dp.loc[:, 'TPS']-self.dp.loc[:, 'TPN'])*(0.0001)
    
    def put(self, lat, long):
        self.lat = lat
        self.long = long
        self.strikes = self.strikes.append({'Latitude': self.lat,
                                            'Longitude': self.long},
                                           ignore_index =True)
        return self.strikes
        
    
class vis_data():
    def extract(self, path):
        self.path = path
        self.data = pd.read_csv(self.path,
                                usecols = [3,6,7,8,9,10,11],
                                names = ['time','tps','tpp','tpz','tpn','app','apn']
                                )
        
        self.data = self.data.astype(str)
        self.data['time'] = self.data['time'].str.slice(12,14)
        self.data['tps'] = self.data['tps'].map(lambda x: x.lstrip('TPS'))
        self.data['tpp'] = self.data['tpp'].map(lambda x: x.lstrip('TPP'))
        self.data['tpz'] = self.data['tpz'].map(lambda x: x.lstrip('TPZ'))
        self.data['tpn'] = self.data['tpn'].map(lambda x: x.lstrip('TPN'))
        self.data['app'] = self.data['app'].map(lambda x: x.lstrip('APP'))
        self.data['apn'] = self.data['apn'].map(lambda x: x.lstrip('APN'))
        
        self.data = self.data.astype(float)
        self.data['tps'] = self.data['tps']*0.000001
        self.data['tpp'] = self.data['tpp']*0.000001
        self.data['tpz'] = self.data['tpz']*0.000001
        self.data['tpn'] = self.data['tpn']*0.000001
        self.data['app'] = self.data['app']*0.001
        self.data['apn'] = self.data['apn']*0.001
        dataset = pd.DataFrame(self.data).sort_values(by = 'time', ascending = 1)
        
        return dataset
                        
    def assign_points(self, raw):
        self.raw = raw
        tps_0 = np.transpose(np.array([self.raw[:,0] + self.raw[:,1], np.zeros(len(self.raw))]))
        tpp_app = np.transpose(np.array([self.raw[:,0] + self.raw[:,2], self.raw[:,5]]))
        tpz_0 = np.transpose(np.array([self.raw[:,0] + self.raw[:,3], np.zeros(len(self.raw))]))
        tpn_apn = np.transpose(np.array([self.raw[:,0] + self.raw[:,4], self.raw[:,6]]))
        
        matrix = np.array([[tps_0[i], tpp_app[i], tpz_0[i], tpn_apn[i]] for i in range(len(tps_0))])
        return matrix