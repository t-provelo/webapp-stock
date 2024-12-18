from flask import Flask, render_template
import requests

app = Flask(__name__)

# Replace with your actual API key
API_KEY = "cEIQ6q3OnK0zxQCJqnCeRjSLIVGsyEwx"
BASE_URL = f"https://financialmodelingprep.com/api/v3/gainers?apikey={API_KEY}"

@app.route("/")
def home():
    # Debug message to confirm this route is called
    print("Serving the homepage!")

    # Make API call to get top gainers
    try:
        print("Fetching data from Financial Modeling Prep API...")
        response = requests.get(BASE_URL)
        data = response.json()

        # Limit to the top 5 gainers
        top_5_gainers = data[:5]
        print(f"Top 5 Gainers Data: {top_5_gainers}")

        return render_template("index.html", gainers=top_5_gainers)

    except Exception as e:
        # Print any errors that occur while fetching data
        print(f"Error fetching data: {e}")
        return "Error fetching stock data. Please try again later."

if __name__ == "__main__":
    # Debug message to confirm app is running
    print("Starting Flask application...")
    app.run(debug=True)












