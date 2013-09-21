import json
import os
import pandas as pd
import pickle

def get_paths():
    paths = json.loads(open("../SETTINGS.json").read())
    for key in paths:
        paths[key] = os.path.expandvars(paths[key])
    return paths

def get_train_df():
    train_path = get_paths()["train_data_path"]
    return pd.read_csv(train_path,)

def save_model(model):
    out_path = get_paths()["model_path"]
    pickle.dump(model, open(out_path, "w"))

def load_model():
    in_path = get_paths()["model_path"]
    return pickle.load(open(in_path))

if __name__ == '__main__':
    print(get_paths())
    print(get_train_df())