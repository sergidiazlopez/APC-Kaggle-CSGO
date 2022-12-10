import sys
sys.path.append( 'src/' )

from ingest_data import *
from generate_features import *
from train_model import *

from configparser import ConfigParser

print("CS:GO Competitive Round Predictor (DEMO)")
print("Author: Sergi Diaz Lopez")
print("Aprenentatge Computacional - Machine Learning")
print("Universitat Autònoma de Barcelona")

# Import config files
conf = ConfigParser()
conf.read('config/config.conf')

# Read and process dataset
print("Reading data...")
data = ingest_data()
X_train, X_test, y_train, y_test = generate_features(data)

# Train model
save = conf.get('train', 'saveToFile')
search_hyperparameters = conf.get('train', 'searchHyperparameters')

if conf.get('train', 'skip'):
    if conf.get('train', 'logistic'):
        train_logistic(save)
    if conf.get('train', 'tree'):
        train_logistic(save)
    if conf.get('train', 'svc'):
        train_logistic(save)
    if conf.get('train', 'knn'):
        train_logistic(save)
    if conf.get('train', 'randomForest'):
        train_logistic(save)
    if conf.get('train', 'perceptron'):
        train_logistic(save)

# Use model to predict more data
#TODO