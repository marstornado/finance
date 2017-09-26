import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12, 31)

df = web.DataReader('AMZN', "yahoo", start, end)

print(df.head())

df.to_csv('AMZN.csv')

df = pd.read_csv('AMZN.csv', parse_dates=True, index_col=0)

df.plot()
plt.show()

df['Adj Close'].plot()
plt.show()

df[['High','Low']]

