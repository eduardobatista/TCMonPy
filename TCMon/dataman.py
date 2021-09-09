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
            self.TData.append(np.zeros(self.totpoints))
            self.TTime.append(np.zeros(self.totpoints))
            self.ctsample.append(0)
        self.globalctreadings = 0
            

    def resetData(self,tsampling=1):
        self.totpoints = int(self.maxtime*60/tsampling)
        for k in range(8):
            self.TData[k] = np.zeros(self.totpoints)
            self.TTime[k] = np.zeros(self.totpoints)
            self.ctsample[k] = 0
        self.globalctreadings = 0
    
    def appendTData(self,idx,time,val):
        self.TData[idx][self.ctsample] = val
        self.TTime[idx][self.ctsample] = val
        self.ctsample[idx] += 1 
        self.globalctreadings = self.ctsample[idx]

