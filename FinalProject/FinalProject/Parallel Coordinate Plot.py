import pandas as pd
import plotly.express as px
from plotly import offline
df = pd.read_csv('removedNulls.csv')

fig = px.parallel_categories(df, dimensions=['occupation', 'sex', 'income'])

fig.update_layout(title='Occupation/Sex/Income Parallel Plot')

offline.plot(fig)