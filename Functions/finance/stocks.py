from datetime import date
import yfinance as yf
from matplotlib import pyplot as plt
from matplotlib import style

def stock(company):

    obj = yf.Ticker(str(company))
    historyData = obj.history(period='1y', start='1910-01-01', end=str(date.today()))
    todayPrice = obj.history(period='1d', start=str(date.today()), end=str(date.today()))
    todayPrice = todayPrice['Close'][0]
    todayPrice = round(todayPrice, 3)
    plt.style.use('ggplot')
    plt.plot(historyData['Close'])
    plt.title(str(company)+ ' -  $' + str(todayPrice))
    plt.ylabel('Price ($)')
    plt.xlabel('Date')
    plt.savefig(f'historyData.png')
    plt.close()
    
    return f'{str(company)} price is $' + str(todayPrice)