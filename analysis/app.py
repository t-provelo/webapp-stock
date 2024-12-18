import requests

api_url = "https://financialmodelingprep.com/api/v3/gainers?apikey=cEIQ6q3OnK0zxQCJqnCeRjSLIVGsyEwx"
response = requests.get(api_url)

# Add detailed debugging
print(f"Request URL: {api_url}")
print(f"Response Status Code: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    print(f"Number of gainers fetched: {len(data)}")
    for gainer in data[:20]:  # Print the first 20 gainers
        print(gainer)
else:
    print("Failed to fetch data from API. Response:", response.text)














