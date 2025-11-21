# simulate wearable stream data for testing
import time
import random
import pandas as pd


def generate_sample():
    # returns a dict of simulated metrics
    hr = random.randint(55, 120)
    spo2 = random.randint(88, 100)
    activity = random.choice(["low", "moderate", "high"])
    return {"heart_rate": hr, "blood_oxygen": spo2, "activity_level": activity}


def generate_dataframe(n=500):
    # create a dataframe to seed model training
    data = [generate_sample() for _ in range(n)]
    df = pd.DataFrame(data)
    return df


if __name__ == "__main__":
    df = generate_dataframe(200)
    print(df.head())
