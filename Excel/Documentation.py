import os
import xlrd

def parse_excel():

    file_name = os.path.join(os.getcwd(), 'TestData.xlsx')
    work_book = xlrd.open_workbook(file_name)
    work_sheet = work_book.sheet_by_index(0)

    total_rows = work_sheet.nrows

    data_list = []

    key_list = None

    for i in range(total_rows):
        row_data = work_sheet.row_values(i)

        if i == 0:
            key_list = row_data

        else:

            data_dict = dict()

            for index, cel_data in enumerate(row_data):

                key = key_list[index]

                data_dict[key] = cel_data

            data_list.append(data_dict)

    for data in data_list:
        print(data)


if __name__ == 'main':
    parse_excel()
