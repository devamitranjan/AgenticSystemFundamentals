# Row indexing can be accesssed using either iloc or loc


import pandas as pd

df = pd.read_csv("employees.csv")
print(df.iloc[0:3])


# use loc when u want to access via labels else use iloc
df.index = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(df.iloc[0])