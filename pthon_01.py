#@title
!git clone https://github.com/koreal6803/crypto_backtrader.git
%cd crypto_backtrader

!pip install python-binance
!pip install bitmex
!pip install Backtesting
!pip install backtrader

from finlab import crypto
df = crypto.get_all_binance('BTCUSDT', '4h')
df.head()

df.Close

sma1 = df.Close.rolling(20).mean()
sma2 = df.Close.rolling(60).mean()

df.Close.plot()
sma1.plot()
sma2.plot()

df.Close['2021'].plot()
sma1['2021'].plot()
sma2['2021'].plot()



condition = sma1 > sma2
condition

print(df.Close)
print(df.Close.shift(1))

signal_long = (sma1 > sma2) & (sma1.shift() < sma2.shift())
signal_short = (sma1 < sma2) & (sma1.shift() > sma2.shift())

signal_long.astype(int).plot()
(-signal_short.astype(int)).plot()
