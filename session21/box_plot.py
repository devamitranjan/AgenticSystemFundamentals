import pandas as pd
import plotly.express as px

df = pd.read_csv("titanic.csv")

fig = px.box(
    df,
    x="Sex",
    y="Fare",
    title="Passenger Fare Distribution",
)

fig.show()