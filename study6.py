#read excel file using python
import xlrd

loc=('C:\\users\\khushbu gupts\\excel task 1.xlsx') #valid loc
wb= xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)  #sheet 1st
print(sheet.cell_value(13,10))   #to get value at a particular cell
print(sheet.ncols)   #no. of columns
print(sheet.nrows)  #no. of rows
for i in range(sheet.ncols):
    print(sheet.cell_value(0,i))
for i in range(sheet.ncols):
        print(sheet.cell_value(0, i))