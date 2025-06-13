import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    headers = {
        "Authorization": "Bearer 32c7c7916043c994f27dde9f5bb8c9bef6706638b0593ab734c7e68688a1d024"
    }
    url = "https://rest.coincap.io/v3/assets/bitcoin"
    response = requests.get(url, headers=headers)

    data = response.json()
    price = float(data["data"]["priceUsd"])

    total_cost = amount * price
    print(f"${total_cost:,.4f}")

except requests.RequestException:
    sys.exit("API request failed")
