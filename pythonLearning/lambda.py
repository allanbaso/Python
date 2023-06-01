def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(99)

print(mydoubler(11))
print(mytripler(11))