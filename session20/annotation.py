import plotly.express as px #simple interface for creating charts
import pandas as pd

df = pd.DataFrame({
    "epoch": range(1, 11), #training iteration number
    "loss": [0.9, 0.8, 0.75, 0.7, 0.65, 0.6, 0.58, 0.55, 0.52, 0.5] #model error value
})


fig = px.line(
    df,
    x="epoch",
    y="loss",
    title = "Training loss with annotation"
)

fig.add_annotation(
    x=5, # x axis
    y=0.65, # y axis
    text= "Training Plateau", # what text u want to add
    showarrow=True, # true
    arrowhead=6 # shape of arrow head

)

fig.show()