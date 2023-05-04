import xlrd

book = xlrd.open_workbook("Book4.xls")
conSH=0
contLib2=0
contLib1=0
contnulo=0

sh = book.sheet_by_index(0)
for col in range(sh.ncols):
    for rx in range(sh.nrows):
        fila = sh.row_values(rx)
        new_list = [word.strip() for word in fila]#se le quita los espacios y caracteres demas
        if "HOLDPROD" in new_list:
            #print("El nombre del elmento #"+str(rx+1)+" de la lista es : "+str(new_list))
            if "H" in new_list:
                conSH+=1/sh.ncols
            else:
                contLib2+=1/sh.ncols
        if "PROD" in new_list:
            if "H" in new_list:
                contnulo+=1/sh.ncols
            else:
                contLib1+=1/sh.ncols

print('Se encontraron {0} de elementos para borrar con stage H libman2'.format(round(conSH)))
print('Se encontraron {0} de elementos para borrar libman2'.format(round(contLib2)))
print('Se encontraron {0} de elementos para borrar libman1'.format(round(contLib1)))
print('Se encontraron {0} de elementos que coinciden con el sistema y stage'.format(round(contnulo)))    