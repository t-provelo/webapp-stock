from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Your API Key
API_KEY = "cEIQ6q3OnK0zxQCJqnCeRjSLIVGsyEwx"

# Home Route - Fetch Top 20 Biggest Gainers
@app.route("/")
def home():
    gainers_url = f"https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey={API_KEY}"
    response = requests.get(gainers_url)
    
    if response.status_code == 200:
        gainers = response.json()[:20]  # Top 20 gainers
    else:
        gainers = []
    
    return render_template("index.html", gainers=gainers)

# Search Route - Fetch News for a Specific Stock
@app.route("/search", methods=["POST"])
def search():
    stock = request.form.get("stock")  # Get stock input from search bar
    
    # Fetch news for the entered stock
    news_url = f"https://financialmodelingprep.com/api/v3/stock_news?tickers={stock}&limit=10&apikey={API_KEY}"
    response = requests.get(news_url)
    
    if response.status_code == 200:
        news = response.json()  # Get top 10 news articles
    else:
        news = []
    
    return render_template("stock.html", stock=stock.upper(), news=news)

if __name__ == "__main__":
    app.run(debug=True)








