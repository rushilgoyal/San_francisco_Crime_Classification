# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 00:26:27 2016

@author: dahenriq
"""

import pandas as pd
import Demographics as dm

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
        print "4. Exit\n"
        menu1input=int(input("Please enter Menu# (1,2,3,4):\n"))
        
        if menu1input==1:
            #b.Crosstab(a.Badgeinput)#UNSURE OF CALL LOGIC/SYNTAX
            #b.BarChart()            
            #b.ByPd()#Prints object location instead of values??
            b.PdDemo()
            a.Menu1()
        else:
            exit()
    
    
#       Will Need - CrimeStats Class, and a Crime Predictions class.  
#       based on what the user inputs, you would instantiate the given class and do stuff with it. 
#       Ex.
#       if(menu1input == 1):
#          a = Demographics()
#          ((No sub menu)show summary stats for logged in officers district grouped by zip-#Crimes,Pop 2013, Pop Density, unemployment rate etc.
#           Provide option to print stats to csv)
#
        #elif(menu1input == 2):
#          a = CrimeStats
#           (Sub menu - options )
#
        #elif(menu1input == 3):
#          a = CrimePredictions
#           (Sub menu - options)
#       
#        return menu1input
#      
#       
#       Using subclasses for the submenu items ex.  item 2 submenu  will be 
#       a class that inherits from the item 2 class. This should satisy "inheritance" as per grading rubric
#
#       So with this proposed structure we will have four files: one for each menu item class and then this one.
#       we will have three additional import statements that might be 
#       import Demographcs() Danielle coded
#       import CrimeStats() Siddhant??- I provided suggested menu choices please feel free to edit
#       import CrimePredictions() Rushil?? -Please let me know what you would like for your menu options 



            
        
        
#TestMain


a=MainScreen()
b=dm.Demographics()
print("San Francisco PD\nLogin\n")

a.LoginMenu()