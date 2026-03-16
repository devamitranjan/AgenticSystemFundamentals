import pandas as pd
import plotly.express as px


df = pd.read_csv("titanic.csv")

print(df.info())

# Agre, Cabin, embarked

fig = px.histogram(
    df,
    x="Age",
    nbins=30,
    title="Passenger Age distribution"
)

fig.show()



