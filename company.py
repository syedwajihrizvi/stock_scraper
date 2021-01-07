import requests
from bs4 import BeautifulSoup
import rapid_api as API
from utils import get_google_url, get_yahoo_profile_url, exchanges
from statements import generate_statement, generate_value, indicators
import json


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
        self.__set_financial_details()

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
        with open(f'{self.company}_fs.json', 'w') as file:
            json.dump(data, file)

        statements = json.loads(data)
        cashflowStatementHistory = statements.get('cashflowStatementHistory')
        cfs = cashflowStatementHistory.get('cashflowStatements')[0]
        balanceSheetHistory = statements.get('balanceSheetHistory')
        bs = balanceSheetHistory.get('balanceSheetStatements')[0]
        incomeStatementHistory = statements.get('incomeStatementHistory')
        incs = incomeStatementHistory.get('incomeStatementHistory')[0]
        self.balance_sheet = generate_statement(
            indicators['balanceSheet'], bs)
        self.income_statement = generate_statement(
            indicators['incomeStatement'], incs)
        self.cash_flow_statement = generate_statement(
            indicators['cashFlow'], cfs)

    def get_cash_flow_statement(self):
        return self.cash_flow_statement

    def get_income_statement(self):
        return self.income_statement

    def get_balance_sheet(self):
        return self.balance_sheet

    # Financial Details
    def __set_financial_details(self):
        response = API.get_financial_data('AAPL')
        data = response.json()
        with open(f'{self.company}_fd.json', 'w') as file:
            json.dump(data, file)
        financial_data = json.loads(data)
        key_stats = financial_data.get('defaultKeyStatistics')
        self.ks = generate_statement(indicators.get('keyStats'), key_stats)
        fin_data = financial_data.get('financialData')
        self.fd = generate_statement(indicators.get('financialData'), fin_data)
        sum_detail = financial_data.get('summaryDetail')
        self.sd = generate_statement(
            indicators.get('summaryDetail'), sum_detail)

    def get_key_stats(self):
        return self.ks

    def get_fin_data(self):
        return self.fd

    def get_sum_detail(self):
        return self.sd
