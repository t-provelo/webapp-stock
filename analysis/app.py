from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    api_url = "https://financialmodelingprep.com/api/v3/gainers?apikey=cEIQ6q3OnK0zxQCJqnCeRjSLIVGsyEwx"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        gainers = response.json()  # Extract the data from the response
        print(f"Number of gainers fetched: {len(gainers)}")  # Check how many gainers were fetched
        # Return the HTML page, passing the gainers data to the template
        return render_template('index.html', gainers=gainers)
    else:
        print("Failed to fetch data from API.")
        return render_template('index.html', gainers=[])

if __name__ == "__main__":
    app.run(debug=True)


















