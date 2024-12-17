import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = "cEIQ6q3OnK0zxQCJqnCeRjSLIVGsyEwx"
GAINERS_URL = f"https://financialmodelingprep.com/api/v3/gainers?apikey={API_KEY}"

@app.route("/")
def home():
    try:
        # Fetch top 20 biggest gainers
        response = requests.get(GAINERS_URL)
        response.raise_for_status()  # Raise an error for failed requests
        gainers = response.json()

        return render_template("index.html", gainers=gainers[:20])  # Limit to 20 gainers
    except Exception as e:
        return f"Error fetching gainers: {e}"


@app.route("/search", methods=["GET"])
def search_stock():
    try:
        # Get the stock symbol from the search bar
        symbol = request.args.get("symbol").upper()

        # Fetch news for the searched stock
        NEWS_URL = f"https://financialmodelingprep.com/api/v3/stock_news?tickers={symbol}&limit=5&apikey={API_KEY}"
        response = requests.get(NEWS_URL)
        response.raise_for_status()
        news = response.json()

        return render_template("stock.html", symbol=symbol, news=news)
    except Exception as e:
        return f"Error fetching news for {symbol}: {e}"


if __name__ == "__main__":
    app.run(debug=True)










