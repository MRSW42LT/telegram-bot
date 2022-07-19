from datetime import date
import yfinance as yf
from matplotlib import pyplot as plt
from matplotlib import style

def stock(company):

    obj = yf.Ticker(str(company))
    historyData = obj.history(period='1y', start='1910-01-01', end=str(date.today()))
    todayPrice = obj.history(period='7d', start='2022-01-01', end=str(date.today()))
    todayPrice = todayPrice['Close'].iloc[-1]
    todayPrice = round(todayPrice, 3)
    plt.style.use('seaborn')
    plt.plot(historyData['Close'])
    plt.title(str(company)+ ' -  $' + str(todayPrice))
    plt.ylabel('Price ($)')
    plt.xlabel('Date')
    plt.savefig(f'historyData.png')
    plt.close()
    
    return f'{str(company)} price is $' + str(todayPrice)