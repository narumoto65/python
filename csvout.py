#coding: utf-8
import os
import csv
import openpyxl

def main():
    filepath = os.path.join('/Users','sera','python','param_sample.xlsx')
    book = openpyxl.load_workbook(filepath,read_only=True,keep_vba=False)

    dest_dir = os.path.join('/Users','sera','python','openpyxl_sample')
    os.makedirs(dest_dir,exist_ok=True)

    # for sheet in book.worksheets:
    #     sheet_name = sheet.title
    #     dest_path = os.path.join(dest_dir,sheet_name,+'.csv')

    #     with open(dest_path,'w',encoding='utf-8') as fp:
    #         writer = csv.writer(fp)

    #         for cols in sheet.rows:
    #             writer.writerow([str(col.value or '') for col in cols])
if __name__ == '__main__':
    main()


    
