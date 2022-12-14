import numpy as np

def predict(model):
    print("-----------")
    print("All set. Now you will input some data from the match and the model will predict the winner side")
    #print("This could be automated to extract data directly from the game, but I lack the knowledge to do so. Coming soon?")
    print("You can exit the demo by typing -1 at any time")

    variables = ['ct_alive','t_alive','is_bomb_planted','ct_eq_val','t_eq_val']
    while(1):
        x = []

        for v in variables:
            i = input("input data for " + v + ":     ")
            if (i == '-1'):
                return
            x.append(int(i))

        # Prediction
        x = np.array(x).reshape(1, -1)
        y = model.predict(x)
        if (y[0] == 0):
            print("TERRORISTS WIN")
        else:
            print("COUNTER-TERRORISTS WIN")