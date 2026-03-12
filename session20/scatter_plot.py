import plotly.express as px #simple interface for creating charts
import pandas as pd


df_scatter = pd.DataFrame({
    "users": [100, 150, 200, 250, 300, 350],
    "purchases": [20, 25, 45, 55, 70, 80]
})

fig = px.scatter(
    df_scatter,
    x="users",
    y="purchases",
    title="Users vs Purchases Relationship"
)

fig.show()