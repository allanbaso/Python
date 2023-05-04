import xlrd
#import sys, datetime
#from tabulate import tabulate

book = xlrd.open_workbook("Book2.xls")
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))

sh = book.sheet_by_index(0)
print("{0} rows {1} columns {2}".format(sh.name, sh.nrows, sh.ncols))

for col in range(sh.ncols):
    for rx in range(sh.nrows):
        fila = sh.row_values(rx)
        new_list = [word.strip() for word in fila]#se le quita los espacios y caracteres demas
        print("El nombre del elmento #"+str(rx+1)+" de la lista es : "+str(new_list))
