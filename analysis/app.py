from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Home route showing top 20 gainers
@app.route('/')
def index():
    api_url = "https://financialmodelingprep.com/api/v3/gainers?apikey=cEIQ6q3OnK0zxQCJqnCeRjSLIVGsyEwx"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        gainers = response.json()  # Extract the data from the response
        return render_template('index.html', gainers=gainers)
    else:
        print("Failed to fetch data from API.")
        return render_template('index.html', gainers=[])

# Search route to search for stock by ticker
@app.route('/search', methods=['GET', 'POST'])
def search():
    stock_data = None
    news_data = None
    
    if request.method == 'POST':
        ticker = request.form.get('ticker')  # Get the stock ticker from the form

        # API calls to get stock information
        stock_url = f"https://financialmodelingprep.com/api/v3/quote/{ticker}?apikey=cEIQ6q3OnK0zxQCJqnCeRjSLIVGsyEwx"
        news_url = f"https://financialmodelingprep.com/api/v3/stock_news?tickers={ticker}&limit=5&apikey=cEIQ6q3OnK0zxQCJqnCeRjSLIVGsyEwx"

        stock_response = requests.get(stock_url)
        news_response = requests.get(news_url)

        if stock_response.status_code == 200:
            stock_data = stock_response.json()[0]  # Get the stock information
        if news_response.status_code == 200:
            news_data = news_response.json()  # Get the news articles

    return render_template('search.html', stock_data=stock_data, news_data=news_data)

if __name__ == "__main__":
    app.run(debug=True)



















