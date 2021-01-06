from pathlib import Path
from company import PublicCompany
from statements import generate_statement, generate_value
import requests
import json

# response = requests.request("GET", url, headers=headers, params=querystring)

# data = response.json()
# Read from JSON
with open('results.txt', 'w') as file:
    data = Path('data.json').read_text()
    content = json.loads(data)
    for c in content:
        file.write(f'KEY: {c} \n {content.get(c)} \n \n \n \n')

cash_flow_statement = content.get('cashflowStatementHistory')
cfs = cash_flow_statement.get('cashflowStatements')[0]

cash_flow_indicators = [
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
    {'name': 'capitalExpenditures', 'label': 'Capital Expenditures'}, ]

income_statement = content.get('incomeStatementHistory')
incs = income_statement.get('incomeStatementHistory')[0]

income_statement_indicators = [
    {'name': 'researchDevelopment', 'label': 'RD'},
    {'name': 'incomeBeforeTax', 'label': 'Pretax Income'},
    {'name': 'netIncome', 'label': 'netIncome'},
    {'name': 'grossProfit', 'label': 'Gross Profit'},
    {'name': 'operatingIncome', 'label': 'Operating Income'},
    {'name': 'otherOperatingExpenses', 'label': 'Other Operating Expenses'},
    {'name': 'incomeTaxExpense', 'label': 'Income Tax Expense'},
    {'name': 'totalRevenue', 'label': 'Total Revenue'},
    {'name': 'totalOperatingExpenses', 'label': 'Total Operating expenses'},
    {'name': 'costOfRevenue', 'label': 'Cost of Revenue'},

]

balance_sheet = content.get('balanceSheetHistory')
bs = balance_sheet.get('balanceSheetStatements')[0]

balance_sheet_indicators = [
    {'name': 'intangibleAssets', 'label': 'Intangible Assets'},
    {'name': 'totalLiab', 'label': 'Total Liabilities'},
    {'name': 'totalStockholderEquity', 'label': 'Total Stockholder Equity'},
    {'name': 'deferredLongTermLiab', 'label': 'Deferred Long Term Liabilities'},
    {'name': 'otherCurrentLiab', 'label': 'Other Current Liabilities'},
    {'name': 'totalAssets', 'label': 'Total Assets'},
    {'name': 'commonStock', 'label': 'Common Stock'},
    {'name': 'otherCurrentAssets', 'label': 'Other Current Assets'},
    {'name': 'retainedEarnings', 'label': 'Retained Earnings'},
    {'name': 'otherLiab', 'label': 'Other Liabilities'},
    {'name': 'cash', 'label': 'Cash'},
    {'name': 'totalCurrentLiabilities', 'label': 'Total Current Liabilities'},
    {'name': 'deferredLongTermAssetCharges',
        'label': 'Deferred Long Term Asset Charges'},
    {'name': 'shortLongTermDebt', 'label': 'Short Long Term Debt'},
    {'name': 'otherAssets', 'label': 'Other Assets'},
    {'name': 'totalCurrentAssets', 'label': 'Total Current Assets'},
    {'name': 'longTermInvestments', 'label': 'Long Term Investments'},
    {'name': 'netTangibleAssets', 'label': 'Net Tangible Assets'},
    {'name': 'shortTermInvestments', 'label': 'Short Term Investments'},
    {'name': 'longTermDebt', 'label': 'Long Term Debt'},
    {'name': 'inventory', 'label': 'Inventory'},
    {'name': 'accountsPayable', 'label': 'Accounts Payable'},
]
