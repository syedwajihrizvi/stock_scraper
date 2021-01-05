def get_google_url(company):
    return f'https://www.google.com/search?client=safari&rls=en&q={company}+stock&ie=UTF-8&oe=UTF-8'


def get_yahoo_profile_url(ticker_symbol):
    return f'https://ca.finance.yahoo.com/quote/{ticker_symbol}/profile?p={ticker_symbol}'


def get_trading_view_profile(company, exchange):
    return f'https://www.tradingview.com/symbols/{exchange.upper()}-{company.upper()}/'


exchanges = ['NYSE', 'NASDAQ', 'TSE']
