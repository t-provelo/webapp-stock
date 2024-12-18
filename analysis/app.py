from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    print("Serving the homepage!")
    # Fetching data from the Financial Modeling Prep API
    print("Fetching data from Financial Modeling Prep API...")
    api_url = "https://financialmodelingprep.com/api/v3/gainers?apikey=cEIQ6q3OnK0zxQCJqnCeRjSLIVGsyEwx"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        top_gainers = data[:20]  # Fetch the top 20 gainers
        print("Top 20 Gainers Data:", top_gainers)
        return render_template("index.html", gainers=top_gainers)
    else:
        print("Error fetching data from API.")
        return "Error fetching data from API", 500

if __name__ == '__main__':
    print("Starting Flask application...")
    app.run(debug=True)













