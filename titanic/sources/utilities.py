'''
Created on 18 sept. 2013

@author: Y3GDTU
'''
import csv
import numpy as np
import pandas as pd
import json
import os

def get_paths():
    paths = json.loads(open("settings.json").read())
    for key in paths:
        paths[key] = os.path.expandvars(paths[key])
    return paths


def get_train_df():
    train_path = get_paths()["train_data_path"]
    return pd.read_csv(train_path)

def get_test_df():
    test_path = get_paths()["test_data_path"]
    return pd.read_csv(test_path)

if __name__=="__main__":
    print(get_train_df())