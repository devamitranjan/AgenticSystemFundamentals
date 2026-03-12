import plotly.express as px #simple interface for creating charts
import pandas as pd


df = pd.DataFrame({
    "epoch": range(1, 11), #training iteration number
    "loss": [0.9, 0.8, 0.75, 0.7, 0.65, 0.6, 0.58, 0.55, 0.52, 0.5] #model error value
})


fig = px.line(
    df, #data source
    x="epoch", # column used for horizontal axis
    y="loss", # column used for vertical axis
    title="Training loss over Time" # chart title
)

fig.show()

