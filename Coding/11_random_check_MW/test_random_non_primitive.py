import pandas as pd
from random_class import CheckNonPrimitive
from sklearn.model_selection import train_test_split

df = pd.DataFrame({
    "A": [10, 20, 30, 40, 50],
    "B": [1, 2, 3, 4, 5],
    "C": [100, 200, 300, 400, 500]
})


object = CheckNonPrimitive(df, seeds=100)

object.get_stats()
object.add_index()
object.get_stats()

object.init_buckets()

X = object.df
y = object.df[["Index"]]

for i in range(1000):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=i, test_size=0.2)

    X_vals = X_train["Index"].tolist()
    X_test_vals = X_test["Index"].tolist()

    combined = tuple(X_vals + X_test_vals)

    object.buckets[combined].append(i)


for key, value in object.buckets.items():
    if value and (55 in value):
        print("Key: ", key, ", Value: ", value)