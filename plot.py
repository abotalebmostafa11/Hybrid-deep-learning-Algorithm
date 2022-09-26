#%%
import pandas as pd
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
df = pd.read_csv('Russia death.csv')
df.head()

# %%
by_date = pd.Series(df['Date']).value_counts().sort_index()
by_date.index = pd.DatetimeIndex(by_date.index)
df_date = by_date.rename_axis('Date').reset_index(name='Cases')
df_date
# %%
plt.style.use('fivethirtyeight')
from pandas import read_csv
from matplotlib import pyplot
df.plot(color='red')
plt.title('Daily SARS-CoV 2 deaths cases in Russian federation',backgroundcolor='white', color='black',fontsize=15)
plt.ylabel('Daily SARS-CoV 2 deaths ',fontsize=15)
plt.xlabel('Days',fontsize=15)
plt.legend(['deaths cases'], loc='upper left',fontsize=15)
plt.grid()
plt.show()
pyplot.show()
# %%