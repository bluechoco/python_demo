!git clone https://github.com/koreal6803/crypto_backtrader.git
%cd crypto_backtrader

!pip install python-binance
!pip install bitmex
!pip install Backtesting
!pip install backtrader

from finlab import crypto
from backtesting import Backtest
from backtesting.lib import SignalStrategy
import pandas as pd

df = crypto.get_all_binance('BTCUSDT', '4h')

class Strategy(SignalStrategy):
    
    def init(self):
        super().init()
        
        # Precompute the two moving averages
        close = pd.Series(self.data.Close)
        sma1 = close.rolling(20).mean()
        sma2 = close.rolling(60).mean()
        
        # Precompute signal
        signal_long = (sma1 > sma2) & (sma1.shift() < sma2.shift())
        signal_short = (sma1 < sma2) & (sma1.shift() > sma2.shift())
        
        signal = signal_long
        signal[signal_short] = -1
        
        self.set_signal(signal)
        
        
    def next(self):
        super().next()

bt = Backtest(df, Strategy)
bt.run()
bt.plot()
