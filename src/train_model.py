import time
# Module for training machine learning model(s)

def train_logistic(save):
    start = time.time()  # Get the current time

    # Logistic Regression using GridSearchCV
    lr = LogisticRegression(max_iter=1000, verbose=1)
    parameters = {'fit_intercept':[True,False], 'C': [0.1, 1, 10, 100]}
    clf = GridSearchCV(lr, parameters)
    clf.fit(X_train, y_train)
    # Calculate the time difference
    time_elapsed = time.time() - start
    print(f"Time elapsed(train): {time_elapsed} seconds")

    print('Best score: {}'.format(clf.best_score_))
    print('Best parameters: {}'.format(clf.best_params_))

    start = time.time()  # Get the current time

    y_pred = clf.predict(X_test)

    # Calculate the time difference
    time_elapsed = time.time() - start
    print(f"Time elapsed (predict): {time_elapsed} seconds")

    if save:
        print("Saving model...")

def train_tree(save):
    print("TODO")

    
def train_svc(save):
    print("TODO")

    
def train_knn(save):
    print("TODO")


def train_random_forest(save):
    print("TODO")

def train_perceptron(save):
    print("TODO")