import requests
from bs4 import BeautifulSoup
import rapid_api as API
from utils import get_google_url, get_yahoo_profile_url, exchanges
from statements import generate_statement, generate_value
import json

statement_indicators = {
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
    ]}


class PublicCompany:

    def __init__(self, company):
        self.company = company
        self.__generate_google_soup()
        self.__set_ticker_info()
        self.__set_general_info()
        self.__set_competitors()
        self.__set_year_founded()
        self.__set_ceo()
        self.__generate_yahoo_profile_soup()
        self.__set_number_of_employees()
        self.__set_statements()

    # General soups for various scrapers
    def __generate_google_soup(self):
        url = get_google_url(self.company)
        response = requests.get(url)
        self.__google_soup = BeautifulSoup(response.text, 'html.parser')

    def __generate_yahoo_profile_soup(self):
        url = get_yahoo_profile_url(self.ticker_symbol)
        response = requests.get(url)
        self.__yahoo_profile_soup = BeautifulSoup(response.text, 'html.parser')

    # ticker info
    def __set_ticker_info(self):
        stock_price = self.__google_soup.find_all(
            'div', class_='BNeawe tAd8D AP7Wnd')
        if not stock_price:
            return False
        stock_price = list(filter(lambda parent: len(
            parent.find_all('div', class_='BNeawe tAd8D AP7Wnd')) > 0, stock_price)).pop()

        spans = stock_price.find_all('span', class_='r0bn4c rQMQod')
        ticker_span = [span for span in spans if any(
            ele in span.get_text() for ele in exchanges)]
        if not ticker_span:
            return False
        ticker_span = ticker_span.pop().get_text()
        bracket_index = ticker_span.find('(')
        self.ticker_symbol = ticker_span[0:bracket_index]
        self.stock_exchange = ticker_span[bracket_index+1:len(ticker_span)-1]

    def get_ticker_info(self):
        return {
            'company': self.company,
            'ticker_symbol': self.ticker_symbol,
            'stock_exchange': self.stock_exchange
        }

    # competitors
    def __set_competitors(self):
        competitors = []

        company_info_headlines = self.__google_soup.find_all('span', 'punez')
        people_also_search_for = [headline for headline in company_info_headlines if headline.find(
            'div').get_text() == 'People also search for'].pop()

        competitors_urls = people_also_search_for.find_parent(
            'div').find_parent('div').select('.BVG0Nb')

        for url in competitors_urls:
            competitors.append(url.get_text())

        self.competitor_names = list(filter(lambda c: c != False, competitors))

    def get_competitors(self):
        return self.competitor_names

    # general info
    def __set_general_info(self):
        founded = self.__google_soup.find('div', class_="vbShOe kCrYT")
        spans = founded.select('div.AVsepf span.AP7Wnd')
        self.__general_info = [span.get_text().lower() for span in spans]

    def get_general_info(self):
        pass

    # year founded
    def __set_year_founded(self):
        founded_index = self.__general_info.index('founded')
        self.founded_year = self.__general_info[founded_index+1]

    def get_year_founded(self):
        return self.founded_year

    # CEO
    def __set_ceo(self):
        ceo_index = self.__general_info.index('ceo')
        self.ceo = self.__general_info[ceo_index+1]

    def get_ceo(self):
        return self.ceo

    # Number of Employees
    def __set_number_of_employees(self):
        asset_profile = self.__yahoo_profile_soup.find(
            'div', class_='asset-profile-container')
        profile_info = asset_profile.find_all('span')
        profile_info = [span.get_text().lower().replace(" ", "")
                        for span in profile_info]
        index_of_employees = profile_info.index('fulltimeemployees')
        self.number_of_employees = profile_info[index_of_employees+1]

    def get_number_of_employees(self):
        return self.number_of_employees

    # Financial Statements
    def __set_statements(self):
        response = API.get_statements(self.ticker_symbol)
        data = response.json()
        # Write JSON to company file
        with open(f'{self.company}.json', 'w') as file:
            json.dump(data, file)

        statements = json.loads(data)
        cashflowStatementHistory = statements.get('cashflowStatementHistory')
        cfs = cashflowStatementHistory.get('cashflowStatements')[0]
        balanceSheetHistory = statements.get('balanceSheetHistory')
        bs = balanceSheetHistory.get('balanceSheetStatements')[0]
        incomeStatementHistory = statements.get('incomeStatementHistory')
        incs = incomeStatementHistory.get('incomeStatementHistory')[0]
        self.balance_sheet = generate_statement(
            statement_indicators['balanceSheet'], bs)
        self.income_statement = generate_statement(
            statement_indicators['incomeStatement'], incs)
        self.cash_flow_statement = generate_statement(
            statement_indicators['cashFlow'], cfs)

    def get_cash_flow_statement(self):
        return self.cash_flow_statement

    def get_income_statement(self):
        return self.income_statement

    def get_balance_sheet(self):
        return self.balance_sheet
