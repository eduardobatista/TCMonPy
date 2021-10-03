import numpy as np
import pandas as pd


class dataman:


    def __init__(self,maxtime=360,tsampling=1):
        self.maxtime = maxtime
        self.totpoints = int(maxtime*60/tsampling)
        self.TData = []
        self.TTime = [] 
        self.ctsample = []       
        for k in range(8):
            self.TData.append(np.empty(self.totpoints))
            self.TData[-1].fill(np.nan)
            self.TTime.append(np.zeros(self.totpoints))
            self.ctsample.append(0)
        self.globalctreadings = 0
        self.setpoint = None


    def resetData(self,tsampling=1):
        self.totpoints = int(self.maxtime*60/tsampling)
        for k in range(8):
            self.TData.append(np.empty(self.totpoints))
            self.TData[-1].fill(np.nan)
            self.TTime[k] = np.zeros(self.totpoints)
            self.ctsample[k] = 0
        self.globalctreadings = 0

    
    def appendTData(self,idx,time,val):
        self.TData[idx][self.ctsample[idx]] = val
        self.TTime[idx][self.ctsample[idx]] = time
        self.ctsample[idx] += 1


    def appendEmptyData(self,idx,time):
        # self.TData[idx][self.ctsample[idx]] = np.nan
        self.TTime[idx][self.ctsample[idx]] = time
        self.ctsample[idx] += 1

    
    def incrementCtReadings(self):
        self.globalctreadings += 1

