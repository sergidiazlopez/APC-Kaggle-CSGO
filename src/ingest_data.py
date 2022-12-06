import pandas as pd

# Funcions per a llegir dades en format csv
def load_dataset(path):
    dataset = pd.read_csv(path, header=0, delimiter=',')
    return dataset

# La majoria de les dades estan separades en multiples fitxers. Funcio util per a llegir totes les parts
def load_split_dataset(path, parts):
    dataset = pd.concat([pd.read_csv(path + ".part%d.csv" % x, header=0, delimiter=',') for x in range(1,parts+1)])
    return dataset


meta_data = load_split_dataset('../dataset/esea_meta_demos', 2)

kills_data = load_split_dataset('../dataset/esea_master_kills_demos', 2)
kills_data = kills_data.drop(columns=['tick','att_team','vic_team'])

m = pd.merge(kills_data, meta_data)
