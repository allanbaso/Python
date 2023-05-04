d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
d['Allan'] = 34
for x,k in d.items():
    if ((k % 2) == 0):
        print ("Los valores pares son :" ,x)
    else:
        print ("Los valores impares son :" ,x)