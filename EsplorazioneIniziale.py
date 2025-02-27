import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
                names=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])

print("Informazioni sul dataset:")
print(df.info())
print("\nPrime 5 righe del dataset:")
print(df.head())

print("\nStatistica descrittiva:")
print(df.describe())

print("\nConteggio delle specie:")
print(df["species"].value_counts())