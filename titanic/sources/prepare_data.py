'''
Created on 18 sept. 2013

@author: Y3GDTU
'''
import csv
import numpy as np
import pandas as pd
import json
import os

#nettoyer une column
#si n
def get_fill_df(column, df,type='numeric',verbose=False):
    #numerique on remplace par la moyenne
    if(type=='numeric') :
        df[column].fillna(df.mean()[column],inplace=True)
        if(verbose):
            print("recodage de "+column+" fill with : "+str(df.mean()[column]))
    #catégorie on remplace par la plus présente
    if(type=='categorical'):
        mostFrequentCat=df[column].value_counts().index[0]
        df[column].fillna(mostFrequentCat,inplace=True)
        if(verbose):
            print("recodage de "+column+" fill with : "+str(mostFrequentCat))
    return df

def get_recode_df(column, df,type='numeric',verbose=False):
    if(type=='categorical'):
        modalities =df[column].unique()
        modalities.sort()
        dict={}
        for i,modality in enumerate(modalities) :
            dict[modality]=i
        df=df.replace(to_replace={column: dict})
        if(verbose):
            print("recodage de "+column+" recode with : "+str(dict))
    return df

def drop_column_df(listColumn, df):
    for col in listColumn :
        del df[col]
        print("suppression de la colonne "+str(col))
    return df