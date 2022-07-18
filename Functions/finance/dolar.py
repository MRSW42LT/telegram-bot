from datetime import date
import yfinance as yf
from matplotlib import pyplot as plt
from matplotlib import style

def cotar_dolar():

    obj = yf.Ticker(str('USDBRL=X'))
    historyData = obj.history(period='1y', start='2022-01-01', end=str(date.today()))
    todayPrice = obj.history(period='7d', start='2022-01-01', end=str(date.today()))
    todayPrice = todayPrice['Close'].iloc[-1]
    todayPrice = round(todayPrice, 3)
    plt.style.use('seaborn')
    plt.plot(historyData['Close'])
    plt.title('Dólar hoje: R$' + str(todayPrice))
    plt.ylabel('Preço (R$)')
    plt.xlabel('Data')
    plt.savefig(f'dolarHistoryData.png')
    plt.close()
    
    return f'Dólar hoje: R$' + str(todayPrice)