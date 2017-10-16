
import pandas as pd
import numpy as np


class Demographics():
    
    def __init__(self):
         #self.dfpopo = pd.read_csv("Police.csv",index_col='Badge')
         self.dfdemodata=pd.read_csv("Demographics.csv")
         
    
        
    def PdDemo(self):
     
                
        print(self.dfdemodata)
        ts=self.dfdemodata.transpose()        
        print(ts)
        pf=raw_input("Print to file? Y/N:  ")
        
        if pf=="y" or pf=="Y":
            f = open('PdDistrictDemographics.csv','w') 
            print >>f, ts
            f.close()
            return self.dfdemodata
        else:
            return self.dfdemodata
                #if(raw_input("Would you like to print to file? [y/n]").lower() == 'y'):
