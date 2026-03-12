import plotly.express as px #simple interface for creating charts
import pandas as pd
import numpy as np

df_cluster = pd.DataFrame({
    "x": np.random.randn(100), #generated 100 random numbers
    "y": np.random.randn(100),
    "group": np.random.choice(["A", "B", "C"], 100) # randomly assiedn each point to group A , group b or grpou c
})
## Create a dataset with 100 rows , randomly assign each row with a group either A or B

#print(df_cluster)

fig = px.scatter(
    df_cluster,
    x="x",
    y="y",
    color="group", #color each point based on the group value
    title="Cluster visualization",
    color_discrete_sequence=["#1f77b4", "#ff7f0e"] #
)

fig.show()