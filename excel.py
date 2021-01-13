from openpyxl import Workbook
from statements import indicators


class ComparitiveSheet:
    def __init__(self, company):
        self.company = company
        self.__wb = Workbook()
        self.general_worksheet = self.__wb.create_sheet('General')
        self.cfs_worksheet = self.__wb.create_sheet('Cash Flow')
        self.income_worksheet = self.__wb.create_sheet('Income')
        self.balance_worksheet = self.__wb.create_sheet('Balance Sheet')
        self.key_stats_worksheet = self.__wb.create_sheet('Key Stats')
        self.fin_data_worksheet = self.__wb.create_sheet('Financials')
        self.sum_detail_worksheet = self.__wb.create_sheet('Summary')

    def changeColumnWidth(self, width):
        for sheet in self.__wb:
            sheet.column_dimensions['A'].width = width
            sheet.column_dimensions['B'].width = width

    def create_keys(self, keys, sheet_name):
        cell_number = 1
        sheet = self.__wb[sheet_name]
        sheet['A1'] = 'Key'
        sheet['B1'] = self.company
        for key in keys:
            cell_number = cell_number + 1
            sheet[f'A{cell_number}'] = key['label']

    def save(self):
        self.__wb.save("/Users/wajihrizvi/Desktop/python-projects/test.xlsx")

    def upload_data(self, data, sheet_name):
        cell_number = 1
        sheet = self.__wb[sheet_name]
        for key in data:
            cell_number = cell_number + 1
            sheet[f'B{cell_number}'] = data[key].get('value')
