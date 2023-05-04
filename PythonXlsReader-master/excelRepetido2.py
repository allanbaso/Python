import xlrd
book = xlrd.open_workbook("Book3.xls")
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))

sh = book.sheet_by_index(0)
print("{0} rows {1} columns {2}".format(sh.name, sh.nrows, sh.ncols))

listaRepetida=[]
numLinea=[]
def BuscarRepetido(pfila,indice):
    global sum
    sum=0
    for i in range(indice,sh.nrows):
        row=sh.row_values(i)
        new_list2 = [word2.strip() for word2 in row]
 
        if pfila==new_list2:
            sum=indice
            return True
    return False
    

for rx in range(sh.nrows):
    fila = sh.row_values(rx)
    new_list = [word.strip() for word in fila]#se le quita los espacios y caracteres demas
    if (BuscarRepetido(new_list,rx+1)):
        listaRepetida.append(new_list)
        numLinea.append(sum)
print("La fila "+str(numLinea)+" repetida de la hoja de excel es: "+str(listaRepetida))
