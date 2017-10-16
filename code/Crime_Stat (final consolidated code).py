
# coding: utf-8

# In[1]:

import pandas as pd
import Demographics as dm
import crime_plot as cs
import random_f as rf
import heatmap as ch
get_ipython().magic(u'matplotlib inline')


# In[2]:


class MainScreen:
    
    def __init__(self):
         self.Badgeinput=1
         self.Passwordinput=1
         self.dfpopo = pd.read_csv("Police.csv",index_col='Badge')
        
    def empty(df):
        return df.empty
        
    def plogin(self,Badgeinput,Passwordinput):
        verified=False
        verqry=self.dfpopo.index[self.dfpopo.index==(Badgeinput)]        
        # use the true/false array self.dfpopo.index==(Badgeinput) to 
        # index into the dataframe. if this is empty, the badge number 
        # doesn't exist
        ver2qry=self.dfpopo[self.dfpopo.index==Badgeinput]['Password'].get_values()
        # if verqry does exist, index into the Password column to retrieve 
        # the password

        if (len(verqry.tolist()) == 0 | ver2qry != Passwordinput):
            verified==False
            print("\nPlease enter a valid Badge# and Password\n")
            a.LoginMenu()
        else:
            print("\nVerified User...\n")
            verified = True
            a.getName(Badgeinput) 
            a.getPDdist(Badgeinput)
            selection = self.Menu1()
            
        return verified 
    def LoginMenu(self):
        Badgeinput=int(input("Badge#:\n"))
        Passwordinput=int(input("Password#:\n"))
        a.plogin(Badgeinput,Passwordinput)
        
                
    def listToStringWithoutBrackets(self,list1):
        return str(list1).replace('[','').replace(']','')
        
    def getName(self,Badgeinput):
        Qname=self.dfpopo[self.dfpopo.index==Badgeinput]['LastName'].get_values()        
        LName=Qname.tolist()
        fName=a.listToStringWithoutBrackets(LName)
        fName=fName.replace("'","") # for cleanup. still not really sure why this is needed.....
        print "\nWelcome Officer " + fName +"\n"
                                            
        return fName
        
    def getPDdist(self,Badgeinput):
        QPDdist=self.dfpopo[self.dfpopo.index==Badgeinput]['PD District'].get_values()        
        LPDdist=QPDdist.tolist()
        fPDdist=a.listToStringWithoutBrackets(LPDdist)
        fPDdist=fPDdist.replace("'","")
        print "District: "+fPDdist+"\n"
        return fPDdist
        
    def Menu1(self):
             
        print "\nMenu\n******\n"
        print "1. Demographics\n"
        print "2. Crime Stats\n"
        print "3. Crime Predictions\n"
        print "4. Heatmaps\n"
        print "5. Exit\n"
        menu1input=int(input("Please enter Menu# (1,2,3,4,5):\n"))
        
        if menu1input==1:
            #b.Crosstab(a.Badgeinput)#UNSURE OF CALL LOGIC/SYNTAX
            #b.BarChart()            
            #b.ByPd()#Prints object location instead of values??
            b.PdDemo()
            a.Menu1()
        
            
        elif  menu1input==2:
            c.visualisation()
            a.Menu1()
            
        elif  menu1input==3:
            d.Random()
            a.Menu1()
       
        elif  menu1input==4:
            get_ipython().magic(u'matplotlib inline')
            e.crime_heatmap()
            #a.Menu1()
            
        else:
            exit()
        


# In[3]:

a = MainScreen()
a.Badgeinput
a.dfpopo


# In[4]:

b = dm.Demographics()
print("San Francisco PD\nLogin\n")
c = cs.Crime_Stats()
d = rf.Predictions()
e = ch.heatmap()


# In[ ]:

a.LoginMenu()


# In[ ]:



