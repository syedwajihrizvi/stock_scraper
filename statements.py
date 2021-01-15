indicators = {
    'general': [
        {'name': 'ticker', 'label': 'Ticker'},
        {'name': 'stock_exchange', 'label': 'Exchange'},
        {'name': 'Year Founded', 'label': 'Year Founded'},
        {'name': 'ceo', 'label': 'CEO'},
        {'name': 'num_employees', 'label': 'Number of Employees'},
    ],
    'cashFlow': [
        {'name': 'netIncome', 'label': 'Net Income'},
        {'name': 'investments', 'label': 'Investments'},
        {'name': 'changeInCash', 'label': 'Change in Cash'},
        {'name': 'changeToLiabilities', 'label': 'Change in Liabilities'},
        {'name': 'changeToNetincome', 'label': 'Change to Net Income'},
        {'name': 'totalCashflowsFromInvestingActivities',
         'label': 'Cash Flow from Investing Activities'},
        {'name': 'netBorrowings', 'label': 'Net Borrowings'},
        {'name': 'totalCashFromFinancingActivities',
         'label': 'Total Cash from Financing Activites'},
        {'name': 'repurchaseOfStock', 'label': 'Repurchase of Stock'},
        {'name': 'totalCashFromOperatingActivities',
         'label': 'Total Cash from Operating Activities'},
        {'name': 'dividendsPaid', 'label': 'Dividends Paid'},
        {'name': 'otherCashflowsFromFinancingActivities',
         'label': 'Other Cash Flow from Financing Activites'},
        {'name': 'capitalExpenditures', 'label': 'Capital Expenditures'}, ],
    'incomeStatement': [
        {'name': 'researchDevelopment', 'label': 'RD'},
        {'name': 'incomeBeforeTax', 'label': 'Pretax Income'},
        {'name': 'netIncome', 'label': 'netIncome'},
        {'name': 'grossProfit', 'label': 'Gross Profit'},
        {'name': 'operatingIncome', 'label': 'Operating Income'},
        {'name': 'otherOperatingExpenses', 'label': 'Other Operating Expenses'},
        {'name': 'incomeTaxExpense', 'label': 'Income Tax Expense'},
        {'name': 'totalRevenue', 'label': 'Total Revenue'},
        {'name': 'totalOperatingExpenses', 'label': 'Total Operating expenses'},
        {'name': 'costOfRevenue', 'label': 'Cost of Revenue'}, ],
    'balanceSheet': [
        {'name': 'totalLiab', 'label': 'Total Liabilities'},
        {'name': 'totalStockholderEquity', 'label': 'Total Stockholder Equity'},
        {'name': 'otherCurrentLiab', 'label': 'Other Current Liabilities'},
        {'name': 'totalAssets', 'label': 'Total Assets'},
        {'name': 'commonStock', 'label': 'Common Stock'},
        {'name': 'otherCurrentAssets', 'label': 'Other Current Assets'},
        {'name': 'retainedEarnings', 'label': 'Retained Earnings'},
        {'name': 'otherLiab', 'label': 'Other Liabilities'},
        {'name': 'cash', 'label': 'Cash'},
        {'name': 'totalCurrentLiabilities', 'label': 'Total Current Liabilities'},
        {'name': 'shortLongTermDebt', 'label': 'Short Long Term Debt'},
        {'name': 'otherAssets', 'label': 'Other Assets'},
        {'name': 'totalCurrentAssets', 'label': 'Total Current Assets'},
        {'name': 'longTermInvestments', 'label': 'Long Term Investments'},
        {'name': 'netTangibleAssets', 'label': 'Net Tangible Assets'},
        {'name': 'shortTermInvestments', 'label': 'Short Term Investments'},
        {'name': 'longTermDebt', 'label': 'Long Term Debt'},
        {'name': 'inventory', 'label': 'Inventory'},
        {'name': 'accountsPayable', 'label': 'Accounts Payable'},
    ],
    'keyStats': [
        {'name': 'enterpriseValue', 'label': 'Enterprise Value'},
        {'name': 'enterpriseToRevenue', 'label': 'Enterprise To Revenue'},
        {'name': 'profitMargins', 'label': 'Profit Margins'},
        {'name': 'enterpriseToEbitda', 'label': 'Enterprise To EBITDA'},
        {'name': '52WeekChange', 'label': '52 Week Change'},
        {'name': 'sharesOutstanding', 'label': 'Shares Outstanding'},
        {'name': 'bookValue', 'label': 'Book Value'},
        {'name': 'trailingEps', 'label': 'Trailing EPS'},
        {'name': 'priceToBook', 'label': 'Price to Book'},
        {'name': 'pegRatio', 'label': 'Price/Earnings Growth'},
        {'name': 'forwardPE', 'label': 'Forward Price to Earnings'},
        {'name': 'priceToBook', 'label': 'Price to Book'}
    ],
    'financialData': [
        {'name': 'ebitdaMargins', 'label': 'EBITDA Margins'},
        {'name': 'profitMargins', 'label': 'Profit Margins'},
        {'name': 'grossMargins', 'label': 'Gross Margins'},
        {'name': 'operatingCashflow', 'label': 'Operating Cash Flow'},
        {'name': 'revenueGrowth', 'label': 'Revenue Growth'},
        {'name': 'operatingMargins', 'label': 'Operating Margins'},
        {'name': 'ebitda', 'label': 'EBITDA'},
        {'name': 'grossProfits', 'label': 'Gross Profits'},
        {'name': 'freeCashflow', 'label': 'Free Cash Flow'},
        {'name': 'currentPrice', 'label': 'Current Price'},
        {'name': 'earningsGrowth', 'label': 'Earnings Growth'},
        {'name': 'currentRatio', 'label': 'Current Ratio'},
        {'name': 'returnOnAssets', 'label': 'Return on Assets'},
        {'name': 'debtToEquity', 'label': 'Debt to Equity'},
        {'name': 'returnOnEquity', 'label': 'Return on Equity'},
        {'name': 'totalCash', 'label': 'Total Cash'},
        {'name': 'totalDebt', 'label': 'Total Debt'},
        {'name': 'totalRevenue', 'label': 'Total Revenue'},
        {'name': 'totalCashPerShare', 'label': 'Total Cash Per Share'}
    ],
    'summaryDetail': [
        {'name': 'twoHundredDayAverage', 'label': '200 Day Average'},
        {'name': 'trailingAnnualDividendYield',
            'label': 'Trailing Annual Dividend Yield'},
        {'name': 'fiftyDayAverage', 'label': '50 Day Average'},
        {'name': 'fiftyTwoWeekHigh', 'label': '52 Week High'},
        {'name': 'fiftyTwoWeekLow', 'label': '50 Week Low'},
        {'name': 'trailingPE', 'label': 'Trailing PE'},
        {'name': 'forwardPE', 'label': 'Forward PE'},
        {'name': 'marketCap', 'label': 'Market Cap'}
    ]
}


def generate_value(label, value):
    return {
        'label': label,
        'value': value
    }


def generate_statement(indicators, data):
    statement = {}
    for indicator in indicators:
        value = data.get(indicator.get('name'), None)
        if value != None:
            value = value.get('fmt')
        statement[indicator.get('name')] = generate_value(
            label=indicator.get('label'), value=value)
    return statement
