import requests

headers = {
    'x-rapidapi-key': "1ecf9f88d4msh40a78a6c5f89f74p1dfc3cjsn1b9a26cc7e5e",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}


def get_statements(symbol):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-balance-sheet"
    querystring = {"symbol": symbol, "region": "US"}
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    return response
