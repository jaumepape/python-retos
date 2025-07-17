for numero in range(1, 101):
    if numero % 3 != 0 and numero % 5 != 0:
        print ("frizzbuzz")
    elif numero % 5 != 0:
        print ("buzz")
    elif numero % 3 != 0:
        print ("firzz")
    else:
        print (numero)
