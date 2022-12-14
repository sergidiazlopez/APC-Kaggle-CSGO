# Pràctica Kaggle APC UAB 2022-23
### Name: Sergi Diaz Lopez
### DATASET: CS:GO Competitive Matchmaking Data
### URL: [kaggle](https://www.kaggle.com/datasets/skihikingkevin/csgo-matchmaking-damage)

![Counter Strike presentation image](images/library_hero.jpg)
[Versió en Català](README.md)

## Resum

The CS:GO Competitive Matchmaking Data dataset contains information about Counter-Strike: Global Offensive matches in competitive mode. The dataset includes detailed information about each match, such as the date and time it was played, the map, the teams and players who participated, and the result of the match.

It also includes information about kills, deaths, damage dealt, etc. In addition, it also contains information about the weapons and equipment used by players in each match.

This dataset can be useful for analyzing and understanding how different factors affect the outcome of a CS:GO match, and how they are related to each other. It will also be useful for making predictions about the outcome of a match.

We have four files with ESEA match data (kill data, grenade data, dmg data, and meta data) and two with data from the official matchmaking. In the notebook you will find more information about the analysis of these data. Some csv files come in 2 parts.

We have data from all rounds of 377,629 ESEA matches. The two data files that we will use, esea_meta_demos and esea_master_kills_demos, have 9 and 12 attributes respectively.
### Objective
The goal is to predict which of the two sides will win the round, based on the current match data.
## Experiments
In this project I did the following experiments
### Preprocessing
Please check the notebook for more detailed information about the developement.Here is a summary of the data preprocessing I did:

* Encode categorical variables
* Delete data without weight in the prediction (timestamps, player IDs...)
* Delete incomplete data
* Look for correlations between variables
* Try to normalize data but without changes in the final model
### Model
The following models were implemented. For more information, check the notebook, the demo and the next sections of this file.

| Model | Hyperparameters | Precision | Recall | F1 | Time (train) | Time(pred.)
| -- | -- | -- | -- | -- | -- | -- |
| Logistic Regression | 'C': 1, 'fit_intercept': False | 81% | 81% | 81% | 65s | 0.05s
| Decission Tree | 'max_depth': 7, 'max_leaf_nodes': 100 | 82% | 82% | 82% | 45s | 0.15s
| Linear SVC | 'C': 0.1, 'loss': 'hinge' | 78% | 76% | 76% | 18 min | 0.05s
| KNN |'n_neighbors': 3, 'p': 1, 'weights': 'distance'| 84%| 84%| 84% | 181s |17s|
| Random Forest | 'max_depth': 8, 'n_estimators': 100 | 82% | 82% | 82% | 2h 47min | 16s|
| Multi-layer perceptron | 'activation': 'relu', 'hidden_layer_sizes': (10, 20, 10), 'learning_rate': 'constant' | 81% | 81% | 81% | 2h | 0.6s
## Demo
First, clone this repo

``` https://github.com/sergidiazlopez/APC-Kaggle-CSGO ```

``` cd APC-Kaggle-CSGO ```

Make sure to satisfy all the dependencies for this project. You can install them with the following command

``` pip install -r requirements.txt ```

Before executing download the dataset from Kaggle and extract all .csv files into the ``` dataset``` folder

To run the demo, simply run the following command

``` python3 demo/demo.py --input here ```

Note: by default the demo does not train the models, they are loaded from files located in the models folder. You can control this behaviour in config.conf
## Conclusions
Mirant els resultats de l'entrenament i anàlisi dels diferents models que hem implementat obtenim uns incisos:
* More complex models such as Random Forest or Multi-layer perceptron offer performances comparable to more simple models but training takes much more time.
* Linear SVC is the worst performing model.
* KNN is the best performing model (Precision, Recall and F1) but is takes the longest to make predictions.
* More simple models (Log. Reg and Decission Tree) train and predict very quickly and offer a really good performance, at the level of complex models.

For making prediction of matches in real time, the best model to consider is a Decision Tree. It scores high prediction scores (82%) and takes less than a second to execute, making it the best option for an enviroment such as gaming, where GPU and CPU performance is crucial. This way we can do predictions without affecting the game performance

Training times are also fast, so the model could take feedback from new data for improvements

At the end, we could see how complex models are not always the best option. In some enviroments, such as these, a light model is preferred if the scores are still acceptable.

## Ideas for future work

Since this is a video game, where we have all the data in memory and do not need sensors or equipment like in the real world, this repository could be used as a foundation for developing a program that captures the state of a competitive Counter Strike match and predicts the result of the round at all times.

## License
This software is licensed under the terms of the [GPLv3 license](LICENSE.txt).