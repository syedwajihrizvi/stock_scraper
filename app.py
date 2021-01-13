from openpyxl import Workbook
from company import PublicCompany
from excel import ComparitiveSheet
from statements import indicators

company_name = input('Enter the name of the company: ')

excel = ComparitiveSheet(company_name)
excel.changeColumnWidth(35)
excel.create_keys(indicators['general'], 'General')
excel.create_keys(indicators['cashFlow'], 'Cash Flow')
excel.create_keys(indicators['incomeStatement'], 'Income')
excel.create_keys(indicators['balanceSheet'], 'Balance Sheet')
excel.create_keys(indicators['keyStats'], 'Key Stats')
excel.create_keys(indicators['financialData'], 'Financials')
excel.create_keys(indicators['summaryDetail'], 'Summary')

company = PublicCompany(company_name)
competitors = company.get_competitors()
company_data = {
    'general': company.get_general(),
    'cash_flow_statement': company.get_cash_flow_statement(),
    'income_statement': company.get_income_statement(),
    'balance_sheet': company.get_balance_sheet(),
    'key_stats': company.get_key_stats(),
    'fin_data': company.get_fin_data(),
    'sum_detail': company.get_sum_detail()
}

excel.upload_data(company_data['general'], 'General')
excel.upload_data(company_data['cash_flow_statement'], 'Cash Flow')
excel.upload_data(company_data['income_statement'], 'Income')
excel.upload_data(company_data['balance_sheet'], 'Balance Sheet')
excel.upload_data(company_data['key_stats'], 'Key Stats')
excel.upload_data(company_data['fin_data'], 'Financials')
excel.upload_data(company_data['sum_detail'], 'Summary')
excel.save()
