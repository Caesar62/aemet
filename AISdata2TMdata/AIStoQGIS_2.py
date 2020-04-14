#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pandas as pd
import glob
import easygui as eg
import os
  
extension = ["*.csv"]
mycsv = eg.fileopenbox(msg="Abrir archivo",
                         title="Control: fileopenbox",
                         default='*.csv',
                         filetypes=extension)
print(mycsv)
#eg.msgbox(mycsv, "fileopenbox", ok_button="Continuar")

mycsv1 = os.path.split(mycsv)
mycsv2 = mycsv1[0]
mycsv3 = mycsv1[1]

df = pd.read_csv(mycsv,sep=";",decimal=",",encoding="windows-1252",parse_dates=["Timestamp"])
#print(df)
mycsv4 = df.to_csv("TIME_MANAGER_"+ mycsv3)
#print(mycsv2)
mycsv4 = "TIME_MANAGER_{}   ".format(mycsv3)
mycsv5 = "PROCESADO  FILE {} => TIME_MANAGER_{}   ".format(mycsv3,mycsv3)

eg.msgbox(mycsv5, "filesavebox", ok_button="Continuar")
