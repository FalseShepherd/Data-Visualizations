import pandas as pd
import plotly.express as px
from plotly import offline
df = pd.read_csv('removedNulls.csv')
df = df [:1000]
fig = px.parallel_categories(df, dimensions=['age', 'income'])

fig.update_layout(title='Age/Income Parallel Plot')

offline.plot(fig)