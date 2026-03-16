import pandas as pd
import plotly.express as px

df = pd.read_csv("titanic.csv")


corr = df[["Fare", "Survived"]].corr(numeric_only=True)

fig = px.imshow(
    corr,
    text_auto=True,
    title="Correlation Heatmap of Titanic Dataset"
)

fig.show()