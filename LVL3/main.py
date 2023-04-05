from fastapi import FastAPI
import pandas as pd
from sklearn.linear_model import LogisticRegression
from enum import auto
from fastapi_utils.enums import StrEnum


### --- SETUP --- ###

# Defining values for each feature
class Gender(StrEnum):
    female = auto()
    male = auto()

class Status(StrEnum):
    upper = auto()
    middle = auto()
    lower = auto()

# Mapping each value to a number
map_gender = {
    Gender.female: 0,
    Gender.male: 1
}
map_status = {
    Status.upper: 1,
    Status.middle: 2,
    Status.lower: 3
}

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


### --- API STUFF --- ###

# create an instance of our API
app = FastAPI()

@app.get("/")
def read_root():
    return "Smoke test succeeded. Go to /docs to figure out how this API works."


@app.get("/predict/")
async def predict(status: Status, gender: Gender, age: int):
    # map input to their numerical values
    mapped_input = [map_status[status], map_gender[gender], age]

    # predict
    prediction = model.predict_proba([mapped_input])

    chance_of_survival = prediction[0][1] * 100

    # output
    return "Chance of survival: {}%".format(str(round(chance_of_survival, 2)))
