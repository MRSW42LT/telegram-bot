from datetime import date
import yfinance as yf
from matplotlib import pyplot as plt
from matplotlib import style

def cotar_dolar():

    obj = yf.Ticker(str('USDBRL=X'))
    historyData = obj.history(period='1y', start='1910-01-01', end=str(date.today()))
    todayPrice = obj.history(period='1d', start=str(date.today()), end=str(date.today()))
    todayPrice = todayPrice['Close'][0]
    todayPrice = round(todayPrice, 3)
    plt.style.use('ggplot')
    plt.plot(historyData['Close'])
    plt.title('Dólar hoje: R$' + str(todayPrice))
    plt.ylabel('Preço (R$)')
    plt.xlabel('Data')
    plt.savefig(f'dolarHistoryData.png')
    plt.close()
    
    return 'O preço atual de $1 em R$ é de: R$' + str(todayPrice)