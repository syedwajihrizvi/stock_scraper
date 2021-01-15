from openpyxl import Workbook
from company import PublicCompany
from excel import ComparitiveSheet
from statements import indicators

company_name = input('Enter the name of the company: ')
company = PublicCompany(company_name, False)
competitors = company.get_competitors()

competitors = list(map(lambda c: PublicCompany(c, True), competitors))
competitors.insert(0, company)

excel = ComparitiveSheet(company_name)

competitors = [c for c in competitors if c.get_ticker_info().get(
    'ticker_symbol') != 'Private']

excel.create_company_names(competitors)
excel.changeColumnWidth(35)
excel.create_keys(indicators['general'], 'General')
excel.create_keys(indicators['cashFlow'], 'Cash Flow')
excel.create_keys(indicators['incomeStatement'], 'Income')
excel.create_keys(indicators['balanceSheet'], 'Balance Sheet')
excel.create_keys(indicators['keyStats'], 'Key Stats')
excel.create_keys(indicators['financialData'], 'Financials')
excel.create_keys(indicators['summaryDetail'], 'Summary')

competitors_data = map(lambda c: c.get_company_data(), competitors)

column = 0
for competitor_data in competitors_data:
    excel.upload_data(competitor_data['general'], column, 'General')
    excel.upload_data(
        competitor_data['cash_flow_statement'], column, 'Cash Flow')
    excel.upload_data(competitor_data['income_statement'], column, 'Income')
    excel.upload_data(
        competitor_data['balance_sheet'], column, 'Balance Sheet')
    excel.upload_data(competitor_data['key_stats'], column, 'Key Stats')
    excel.upload_data(competitor_data['fin_data'], column, 'Financials')
    excel.upload_data(competitor_data['sum_detail'], column, 'Summary')
    column = column+1
excel.save()
