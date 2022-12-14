import time
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from tqdm import *
from joblib import dump, load
# Module for training machine learning model(s)

def train_model(X_train, X_test, y_train, y_test, model, searchHyperparameters):
    start = time.time()  # Get the current time

    # Select the model
    if searchHyperparameters == True:
        if model == 'logistic':
            lr = LogisticRegression(max_iter=1000, n_jobs=-1, verbose=False)
            parameters = {'fit_intercept':[True,False], 'C': [0.1, 1, 10, 100]}
            clf = GridSearchCV(lr, parameters)
        elif model == 'tree':
            parameters = {'max_depth': [3, 5, 7, 9, 11, 13, 15], "max_leaf_nodes": [20, 50, 80, 90, 100]}
            clf = GridSearchCV(DecisionTreeClassifier(), parameters, verbose=10, n_jobs=-1)
        elif model == 'svc':
            parameters = {'C': [0.1, 1, 10],'loss': ['hinge', 'squared_hinge']}
            svc = LinearSVC(max_iter=1000)
            clf = GridSearchCV(svc, parameters, cv=5, verbose=3, n_jobs=-1)
        elif model == 'knn':
            parameters = {  'n_neighbors': [3,5,7,9,11],
                            'weights': ['uniform', 'distance'],
                            'p': [1,2,3]}
            knn = KNeighborsClassifier()
            clf = GridSearchCV(knn, parameters, verbose=True, n_jobs=-1)
        elif model == 'randomForest':
            parameters = {  'n_estimators' : [100, 300, 500, 800, 1200],
                            'max_depth' : [5, 8, 15, 25, 30]}
            rf = RandomForestClassifier()
            clf = GridSearchCV(rf, parameters, verbose=True, n_jobs=-1)
        elif model == 'perceptron':
            parameters = {  'hidden_layer_sizes': [(10,10,10), (10,20,10), (20,20,20)],
                            'activation': ['tanh', 'relu'],
                            'learning_rate': ['constant','adaptive']}
            mlp = MLPClassifier(max_iter=300)
            clf = GridSearchCV(mlp, parameters, cv=5, verbose=2)
        else:
            print("model not implemented")
    else:   # Dont search for hyperparameters, use provided settings
        if model == 'logistic':
            clf = LogisticRegression(max_iter=1000, C=0.1, fit_intercept=False, n_jobs=-1, verbose=False)
        elif model == 'tree':
            clf = DecisionTreeClassifier(max_depth= 9, max_leaf_nodes=100)
        elif model == 'svc':
            clf = LinearSVC(C=0.1, loss='hinge', max_iter=1000)
        elif model == 'knn':
            clf = KNeighborsClassifier(n_neighbors=3, p=1, weights='distance', n_jobs=-1)
        elif model == 'randomForest':
            clf = RandomForestClassifier(max_depth=8, n_estimators=100, verbose=True, n_jobs=-1)
        elif model == 'perceptron':
            clf = MLPClassifier(activation='relu', hidden_layer_sizes=(10, 20, 10), learning_rate='constant', max_iter=300, verbose=2)
        else:
            print("model not implemented")

    
    clf.fit(X_train, y_train)

    # Calculate the time difference
    time_elapsed = time.time() - start
    print(f"Time elapsed(train): {time_elapsed} seconds")

    if searchHyperparameters == True:
        print('Best score: {}'.format(clf.best_score_))
        print('Best parameters: {}'.format(clf.best_params_))

    start = time.time()  # Get the current time

    y_pred = clf.predict(X_test)

    # Calculate the time difference
    time_elapsed = time.time() - start
    print(f"Time elapsed (predict): {time_elapsed} seconds")

    print(classification_report(y_test, y_pred))

    return clf

