def EncontrarMayor(a,b,c):
    if (a>b and a>c):
        msj= 'el numero '+str(a)+' ,variable a es mayor a los demas'
    elif (b>c):
        msj= 'el numero '+str(b)+' ,variable b es mayor a los demas'
    else: msj= 'el numero '+str(c)+' ,variable c es mayor a los demas'    
    return msj    
print(EncontrarMayor(10,600,100))
