from datetime import date
import yfinance as yf
from matplotlib import pyplot as plt

def stock(company):

    obj = yf.Ticker(str(company))
    #historyData = obj.history(period='1y', start='1910-01-01', end=str(date.today()))

    todayPrice = obj.history(period='1d', start=str(date.today()), end=str(date.today()))

    return str(todayPrice)