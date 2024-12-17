from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Your API key
API_KEY = '6KTR8DTNQ69W9ZF5'
BASE_URL = 'https://www.alphavantage.co/query'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    stock_symbol = request.form['stock_symbol']
    if stock_symbol:
        response = get_stock_data(stock_symbol)
        if response:
            return render_template('stock.html', data=response, stock_symbol=stock_symbol)
        else:
            return render_template('stock.html', error="Stock not found!", stock_symbol=stock_symbol)
    return render_template('index.html', error="Please enter a stock symbol.")

def get_stock_data(symbol):
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if 'Time Series (Daily)' in data:
            timeseries = data['Time Series (Daily)']
            dates = list(timeseries.keys())
            latest_date = dates[0]
            latest_data = timeseries[latest_date]
            return {
                'symbol': symbol,
                'latest_date': latest_date,
                'latest_close': latest_data['4. close'],
                'latest_open': latest_data['1. open'],
            }
    return None

if __name__ == "__main__":
    app.run(debug=True)




