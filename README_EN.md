# Pràctica Kaggle APC UAB 2022-23
### Name: Sergi Diaz Lopez
### DATASET: CS:GO Competitive Matchmaking Data
### URL: [kaggle](https://www.kaggle.com/datasets/skihikingkevin/csgo-matchmaking-damage)

![Counter Strike presentation image](images/library_hero.jpg)

### Work in progress...

## Resum

The CS:GO Competitive Matchmaking Data dataset contains information about Counter-Strike: Global Offensive matches in competitive mode. The dataset includes detailed information about each match, such as the date and time it was played, the map, the teams and players who participated, and the result of the match.

It also includes information about kills, deaths, damage dealt, etc. In addition, it also contains information about the weapons and equipment used by players in each match.

This dataset can be useful for analyzing and understanding how different factors affect the outcome of a CS:GO match, and how they are related to each other. It will also be useful for making predictions about the outcome of a match.

We have four files with ESEA match data (kill data, grenade data, dmg data, and meta data) and two with data from the official matchmaking. In the notebook you will find more information about the analysis of these data. Some csv files come in 2 parts.

We have data from all rounds of 377,629 ESEA matches. The two data files that we will use, esea_meta_demos and esea_master_kills_demos, have 9 and 12 attributes respectively.
### Objective
The goal is to predict which of the two sides will win the round, based on the current match data.

## Demo
First, clone this repo

``` https://github.com/sergidiazlopez/APC-Kaggle-CSGO ```

``` cd APC-Kaggle-CSGO ```

Make sure to satisfy all the dependencies for this project. You can install them with the following command

``` pip install -r requirements.txt ```

Before executing download the dataset from Kaggle and extract all .csv files into the ``` dataset``` folder

To run the demo, simply run the following command

``` python3 demo/demo.py --input here ```

## Idees per treballar en un futur

Since this is a video game, where we have all the data in memory and do not need sensors or equipment like in the real world, this repository could be used as a foundation for developing a program that captures the state of a competitive Counter Strike match and predicts the result of the round at all times.