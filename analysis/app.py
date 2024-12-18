from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # Default to showing top gainers
    filter_type = request.form.get('filter_type', 'gainers')  # Default is gainers
    
    # Determine which API URL to use based on the filter
    if filter_type == 'gainers':
        api_url = "https://financialmodelingprep.com/api/v3/gainers?apikey=cEIQ6q3OnK0zxQCJqnCeRjSLIVGsyEwx"
    else:  # 'losers' filter
        api_url = "https://financialmodelingprep.com/api/v3/losers?apikey=cEIQ6q3OnK0zxQCJqnCeRjSLIVGsyEwx"
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        market_data = response.json()
        top_20_stocks = market_data[:20]  # Only take the first 20
    else:
        top_20_stocks = []
    
    return render_template('stock.html', stocks=top_20_stocks, filter_type=filter_type)


@app.route('/search', methods=['POST'])
def search():
    stock_symbol = request.form['stock_symbol']
    
    # Fetch stock data
    stock_api_url = f"https://financialmodelingprep.com/api/v3/quote/{stock_symbol}?apikey=cEIQ6q3OnK0zxQCJqnCeRjSLIVGsyEwx"
    stock_response = requests.get(stock_api_url)
    
    if stock_response.status_code == 200:
        stock_data = stock_response.json()[0]
        current_price = stock_data['price']
        open_price = stock_data['dayLow']  # Using dayLow as placeholder for open price
        close_price = stock_data['dayHigh']  # Using dayHigh as placeholder for close price
    else:
        stock_data = {}
        current_price = open_price = close_price = "N/A"
    
    # Fetch trending news articles
    news_api_url = f"https://financialmodelingprep.com/api/v3/stock_news?symbol={stock_symbol}&limit=5&apikey=cEIQ6q3OnK0zxQCJqnCeRjSLIVGsyEwx"
    news_response = requests.get(news_api_url)
    
    if news_response.status_code == 200:
        news_data = news_response.json()
    else:
        news_data = []
    
    return render_template('stock.html', 
                           stock_data=stock_data, 
                           current_price=current_price, 
                           open_price=open_price, 
                           close_price=close_price, 
                           news_data=news_data)


if __name__ == "__main__":
    app.run(debug=True)





















