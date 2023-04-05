import sys
import pandas as pd
from sklearn.linear_model import LogisticRegression
'''
A simple script for predicting survivability on a sinking ship based on 
class, gender, and age.

To run the script, open a terminal from the project's root directory and type 

    python3 predict.py <class> <female or male> <age>
    
Doing so should print the probability of survival.
'''
# dicts for human-readable input
map_gender = {
    "female": 0,
    "male": 1
}
map_class = {
    "upper": 1,
    "middle": 2,
    "lower": 3
}
def predict(input):
    # read data and drop Nans
    df = pd.read_csv("./train.csv")
    df = df.dropna()

    # maps "Female" to 0, "Male" to 1
    df['Sex'] = df['Sex'].astype('category').cat.codes

    # features and target
    X = df[['Pclass', 'Sex', 'Age']]
    y = df[['Survived']]

    # not evaluating model performance, no train-test split
    model = LogisticRegression()
    model.fit(X, y)

    # map input to their numerical values
    mapped_input = [map_class[input[1]], map_gender[input[2]], int(input[3])]

    # predict
    prediction = model.predict_proba([mapped_input])

    chance_of_survival = prediction[0][1] * 100

    # output
    print("Chance of survival:", "{}%".format(str(round(chance_of_survival, 2))))

if __name__ == '__main__':
    predict(sys.argv)
