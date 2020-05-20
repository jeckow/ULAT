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
        self.dp['TPS'] = self.dp['TPS'].map(lambda x: x.lstrip('TPS') if x != None else 0000)
        self.dp['TPN'] = self.dp['TPN'].map(lambda x: x.lstrip('TPN') if x != None else 0000)
        self.dp['TPS'] = self.dp.TPS.astype(float)
        self.dp['TPN'] = self.dp.TPN.astype(float)
        
        return (self.dp.loc[:, 'TPS']-self.dp.loc[:, 'TPN'])*(0.000001)
    
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
        self.data['tps'] = self.data['tps'].map(lambda x: x.lstrip('TPS') if x != None else 0000)
        self.data['tpp'] = self.data['tpp'].map(lambda x: x.lstrip('TPP') if x != None else 0000)
        self.data['tpz'] = self.data['tpz'].map(lambda x: x.lstrip('TPZ') if x != None else 0000)
        self.data['tpn'] = self.data['tpn'].map(lambda x: x.lstrip('TPN') if x != None else 0000)
        self.data['app'] = self.data['app'].map(lambda x: x.lstrip('APP') if x != None else 0000)
        self.data['apn'] = self.data['apn'].map(lambda x: x.lstrip('APN') if x != None else 0000)
        
        self.data = self.data.astype(float)
        self.data['tps'] = self.data['tps']*0.000001
        self.data['tpp'] = self.data['tpp']*0.000001
        self.data['tpz'] = self.data['tpz']*0.000001
        self.data['tpn'] = self.data['tpn']*0.000001
        self.data['app'] = self.data['app']*0.001
        self.data['apn'] = self.data['apn']*0.001
        dataset = pd.DataFrame(self.data).sort_values(by = 'time', ascending = 1)
        
        return dataset
      
    def fix_headers(self, dataframe):
        self.dataframe = dataframe
        self.dataframe = self.dataframe.rename(columns = {
            0: 'station_id', 1: 'date(UTC)', 2: 'RAF', 3: 'RA1', 4: 'RI1', 
            5: 'ERA', 6: 'CRA', 7: 'AT1', 8: 'RH1', 9: 'PRS', 10: 'SLP', 
            11: 'WD1', 12: 'WDM', 13: 'WS1', 14: 'WSM', 15: 'WND', 16: 'WNS', 
            17: 'SOL', 18: 'WET', 19: 'WBG', 20: 'WEA'})
        
        self.dataframe['RAF'] = self.dataframe['RAF'].map(lambda x: x.lstrip('RAF') if x != None else 0000)
        self.dataframe['RA1'] = self.dataframe['RA1'].map(lambda x: x.lstrip('RA1') if x != None else 0000)
        self.dataframe['RI1'] = self.dataframe['RI1'].map(lambda x: x.lstrip('RI1') if x != None else 0000)
        self.dataframe['ERA'] = self.dataframe['ERA'].map(lambda x: x.lstrip('ERA') if x != None else 0000)
        self.dataframe['CRA'] = self.dataframe['CRA'].map(lambda x: x.lstrip('CRA') if x != None else 0000)
        self.dataframe['AT1'] = self.dataframe['AT1'].map(lambda x: x.lstrip('AT1') if x != None else 0000)
        self.dataframe['RH1'] = self.dataframe['RH1'].map(lambda x: x.lstrip('RH1') if x != None else 0000)
        self.dataframe['PRS'] = self.dataframe['PRS'].map(lambda x: x.lstrip('PRS') if x != None else 0000)
        self.dataframe['SLP'] = self.dataframe['SLP'].map(lambda x: x.lstrip('SLP') if x != None else 0000)
        self.dataframe['WD1'] = self.dataframe['WD1'].map(lambda x: x.lstrip('WD1') if x != None else 0000)
        self.dataframe['WDM'] = self.dataframe['WDM'].map(lambda x: x.lstrip('WDM') if x != None else 0000)
        self.dataframe['WS1'] = self.dataframe['WS1'].map(lambda x: x.lstrip('WS1') if x != None else 0000)
        self.dataframe['WSM'] = self.dataframe['WSM'].map(lambda x: x.lstrip('WSM') if x != None else 0000)
        self.dataframe['WND'] = self.dataframe['WND'].map(lambda x: x.lstrip('WND') if x != None else 0000)
        self.dataframe['WNS'] = self.dataframe['WNS'].map(lambda x: x.lstrip('WNS') if x != None else 0000)
        self.dataframe['SOL'] = self.dataframe['SOL'].map(lambda x: x.lstrip('SOL') if x != None else 0000)
        self.dataframe['WET'] = self.dataframe['WET'].map(lambda x: x.lstrip('WET') if x != None else 0000)
        self.dataframe['WBG'] = self.dataframe['WBG'].map(lambda x: x.lstrip('WBG') if x != None else 0000)
        self.dataframe['WEA'] = self.dataframe['WEA'].map(lambda x: x.lstrip('WEA') if x != None else 0000)
        
        return self.dataframe
                  
    def assign_points(self, raw):
        self.raw = raw
        tps_0 = np.transpose(np.array([self.raw[:,0] + self.raw[:,1], np.zeros(len(self.raw))]))
        tpp_app = np.transpose(np.array([self.raw[:,0] + self.raw[:,2], self.raw[:,5]]))
        tpz_0 = np.transpose(np.array([self.raw[:,0] + self.raw[:,3], np.zeros(len(self.raw))]))
        tpn_apn = np.transpose(np.array([self.raw[:,0] + self.raw[:,4], self.raw[:,6]]))
        
        matrix = np.array([[tps_0[i], tpp_app[i], tpz_0[i], tpn_apn[i]] for i in range(len(tps_0))])
        return matrix