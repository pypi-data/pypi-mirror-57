# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:41:30 2019
python test_deploy.py --a=test_deploy.csv #run in terminal, input is the raw data 640 *3 with serial number and messageid 
pyinstaller test_deploy.py will generate test_deply.spec
modify test_deploy.spec first 2 lines as 
import sys
sys.setrecursionlimit(5000)
then 

pyinstaller --clean --onefile test_deploy.spec will  creat dist\test_deploy\test_deploy.exe
put input test_deploy.csv and model file xgboost_jupyeroutput in the same folder as test_deploy.exe

run 
tests_deploy.exe --a=test_deply.csv


make sure hook-xgboost is in the folder /media/c/Users/qli/AppData/local/conda/conda/envs/py36/lib/site-packages/PyInstaller/hooks
content is 
from PyInstaller.utils.hooks import collect_all

datas, binaries, hiddenimports = collect_all("xgboost")



@author: QLi
"""
#from PyInstaller.utils.hooks import collect_all
#datas, binaries, hiddenimports = collect_all("xgboost")
#import xgboost
import argparse
import numpy as np
from scipy import signal
import scipy
from os import getcwd, listdir, path,chdir
#import matplotlib.pyplot as plt
import sys
import os
import re
#import seaborn as sns
from numpy import exp,log
import pickle
import dill
import pandas as pd
#import pywt
#import pyodbc
#pd.set_option('display.max_rows', 500)
#pd.set_option('display.max_columns', 500)
#pd.set_option('display.width', 1000)

forcethreshold =700 #above this value will be categorized as high impact high risk


def filtersd(x,fc,fss=12500):
    #fss=12500.0#sampling freq at 640Hz
    order=200
    #fc=50#low pass at 50hz
    FIR = signal.firwin(order+1, np.clip((2.*fc)/fss, 0.001, 0.999), nyq=1.0) #
    return(signal.filtfilt(FIR, 1,x))#dff is a dataframe  
#mean error for the predicted value and actual value 
def mae(preds,actual):
    return(np.mean(np.abs((preds-actual)/actual)))
#err percentage for each data point
def errf(preds,actual):
    return(((preds-actual)/actual))
#pickle save object to a file
def picklesave(obj,filename):
    filehandler = open(filename, 'wb') 
    dill.dump(obj, filehandler) 
    
def pickleload(filename):
    filehandler = open(filename, 'rb') 
    return(pickle.load(filehandler)) 


def filterfinal(finaldf,bandf):
    longf = finaldf.melt(id_vars=['SerialNumber','newlabel','SequenceNumber'],value_vars=['XValue','YValue','ZValue']) #crucial diff from matlab, multi-d array to df notes
    longff = longf.groupby(['SerialNumber','newlabel','variable']).apply(lambda x: filtersd(x.sort_values('SequenceNumber').value,bandf,640)) #has to follow this apply format to do the filtering for the grouped data
    rawlong = longf.groupby(['SerialNumber','newlabel','variable']).apply(lambda x: x.sort_values('SequenceNumber'))#raw values before filtering
    lpg = longff.reset_index()# now grouped variable(multiindex) become columns
    lpg['key'] = lpg.index #add join key, lpg is best for correlation 

    widef = pd.DataFrame(lpg.iloc[:,3].tolist()) #list to dataframe transformation, now have 640 columns whith 0 as the initial sequence number,but sequence number strat from 1.

    fullf = pd.concat([lpg,widef],axis=1) #get the full expanded df
    #fullf.drop(0,axis=1).unstack()
    wf = widef.unstack().reset_index() #level_0 is sequencey number and level_1 is , wide to 1 column long format 

    #now change lpg list to vertical series
    #.value.apply(lambda x: filtersd(x.sort_values('SequenceNumber'),10,640))
    #plt.plot(lpg.iloc[1,3].tolist())
    ff = pd.merge(lpg,wf,how='left',left_on='key',right_on='level_1').drop(['key','level_1'],axis=1)
    ff = ff.rename(columns = {'level_0':'sequence','0_y':'acc'})
    #ff.info()
    return([lpg,ff,rawlong,wf,widef])


def getunits_data(finalgood,bandf):    
#bandf = 20    
    allun_raw_fil = filterfinal(finalgood,bandf)
    raws = allun_raw_fil[2][['value','SequenceNumber']].reset_index().drop('level_3',axis=1).rename(columns = {"value": "raws",'SequenceNumber':  'sequence'})
    raws.sequence = raws.sequence-1 #have to count the inital of sequence from 1 or from 0
    ppl = pd.merge(allun_raw_fil[1],raws,how='left',on= ['SerialNumber','newlabel','variable','sequence'],indicator=True)
    return(ppl)


def main():
    parser = argparse.ArgumentParser(description='input file name!')
    parser.add_argument("--a")
    args = parser.parse_args() #use argpase package to parse argument of command line  
    filename = args.a
    tryband=2 #final filtering settings, 1st filterfinal, low pass each unit acc direction, then get the magnitude, 1 sec whole recording filer by 2hz
    finalgood = pd.read_csv(filename,sep='|') #need to change to the path
    ppl = getunits_data(finalgood,tryband) #filtering at 2hz
    ppl['acc_mag'] = ppl.groupby(['SerialNumber','newlabel','sequence']).acc.transform(lambda x: sum((x*x))**(0.5)) #get acc_magnitude
    pplpost = ppl.groupby(['SerialNumber','newlabel']).apply(lambda x: x.loc[np.arange(pd.Series.idxmax(x.acc_mag),pd.Series.idxmax(x.acc_mag)+320)]).droplevel([0,1])#get peak to peak+320 timeseries
    pplpost['peaktime'] = pplpost.groupby(['SerialNumber','newlabel']).cumcount() 
    dfg=pd.pivot_table(index=['SerialNumber','newlabel'], columns='peaktime', values='acc_mag',data = pplpost).reset_index() #320points dataframe
    model = pickleload("xgboost_jupyeroutput")
    
    dfg.columns = ["acc_"+str(i) if str(i).isdigit() else i for i in list(dfg.columns) ]
    predictedt = model.predict(dfg.iloc[:,2:162])#only 160 points needed for model 
    predicted = exp(predictedt) * dfg.acc_0# recover the correct scaling
    risk = predicted.copy().astype('object')
    risk[predicted >= forcethreshold] = 'high'
    risk[predicted < forcethreshold] ='low'
    dfg['predicted'] = predicted
    dfg['risk'] = risk

 #   dfgf = pd.merge(dfg,finalgood[['SerialNumber','newlabel','EventDateET']]    
    do1 = dfg[['SerialNumber','newlabel','predicted', 'risk']] #number of records with force 
    do2 = pd.merge(do1,finalgood[['SerialNumber','newlabel','EventDateET','MessageID']].drop_duplicates())
   #finaloutput = dfgf[['SerialNumber','newlabel','EventDateET','predicted','risk']].sort_values('EventDateET',ascending=True)
    #message_event = finalgood[['SerialNumber','MessageID','EventDateET']].drop_duplicates()
    #aos = pd.merge(finaloutput,message_event, how='inner')
    do2.reset_index(drop=True).drop('newlabel',axis=1).to_csv('test_deploy_out.csv',sep='|')

if __name__== "__main__":
    main()