import pandas as pd
import plotly.express as py
with open("file1.csv") as f:
  s = pd.read_csv(f)
g = py.scatter(s,x="date",y="cases",color="country")
g.show()