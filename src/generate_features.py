import numpy as np
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split, GridSearchCV
# Module for cleaning and transforming data and generating features used for use in training and scoring

def generate_features(m):
    # Codificar variables categóriques
    m["winner_side"].replace({'Terrorist': 0, 'CounterTerrorist' : 1, 'None' : 1, np.NaN:1}, inplace=True)

    m["att_side"].replace({'Terrorist': 0, 'CounterTerrorist' : 1, 'None' : -1}, inplace=True)
    m["vic_side"].replace({'Terrorist': 0, 'CounterTerrorist' : 1, 'None' : -1}, inplace=True)
    m["is_bomb_planted"].replace({False:0, True: 1}, inplace=True)

    y = m['winner_side']
    X = m[['ct_alive','t_alive','is_bomb_planted','ct_eq_val','t_eq_val']]

    # Dividir dades entre test i train
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7)
    return X_train, X_test, y_train, y_test