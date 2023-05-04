def manual_incrementing_matrix(d):
  rows = [] 
  x = 0
  for y in range(d + x):
    y += x
    row = [] 
    for z in range(d):
      z += x 
      row.append(z)

    x += 1 
    rows.append(row)
    print(row)
    
  return rows 




    
  
print(manual_incrementing_matrix(4))
