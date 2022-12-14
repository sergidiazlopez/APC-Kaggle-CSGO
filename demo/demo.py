import sys
sys.path.append( 'src/' )

from ingest_data import *
from generate_features import *
from train_model import *

from configparser import ConfigParser

from tqdm import *

from os.path import exists, join, dirname

from joblib import dump, load

print("CS:GO Competitive Round Predictor (DEMO)")
print("Author: Sergi Diaz Lopez")
print("Aprenentatge Computacional - Machine Learning")
print("Universitat Autònoma de Barcelona")

sys.stdout.write('\rInitializing... Please wait...')

# Import config files
conf = ConfigParser()
conf.read('config/config.conf')

# Read and process dataset
data = ingest_data()
X_train, X_test, y_train, y_test = generate_features(data)

sys.stdout.write('\rDone                        \n')

# Train model

search_hyperparameters = conf.get('train', 'searchHyperparameters')
models = []
if conf.get('train', 'skip') == "False":
    if conf.get('train', 'logistic') == "True":
        models.append('logistic')
    if conf.get('train', 'tree') == "True":
        models.append('tree')
    if conf.get('train', 'svc') == "True":
        models.append('svc')
    if conf.get('train', 'knn') == "True":
        models.append('knn')
    if conf.get('train', 'randomForest') == "True":
        models.append('randomForest')
    if conf.get('train', 'perceptron') == "True":
        models.append('perceptron')

trained_models = []
save_param = conf.get('train', 'saveModelToFile')
load_param = conf.get('train', 'loadModelFromFile')
searchHyperparameters = conf.get('train', 'searchHyperparameters')
print(load_param)
for i, model in enumerate(models):
    print('[' + str(i+1) + '/' + str(len(models)) +'] Training model ' + model)
    file_path = join('models', 'CSGO-model-' + model + '.sav')
    if exists(file_path) and load_param == "True":
        print ("Found trained model in file" + file_path + "Loading instead of training. You can change this behaviour in config.conf")
        clf = load(file_path)
    else:
        clf = train_model(X_train, X_test, y_train, y_test, model, searchHyperparameters)
        if save_param == "True":
            print('Saving model to ' + file_path)
            dump(clf, file_path) 

    



# Use model to predict more data
model_selected = conf.get('prediction', 'modelToUse')
print("Model to use: " + model_selected)