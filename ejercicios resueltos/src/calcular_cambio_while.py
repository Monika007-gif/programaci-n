def calcular_cambio(pago):

    assert isinstance(pago, int), "Error: El pago debe ser un número entero."

    numeroDeMonedas = [0, 0, 0]
    
    if pago <= 0:
        return numeroDeMonedas
    
    tiposDeMonedas = [5, 2, 1]

    monedaIndex = 0

    while pago > 0 and monedaIndex < len(tiposDeMonedas):
       moneda = tiposDeMonedas[monedaIndex]
       numeroDeMonedas[monedaIndex] = pago // moneda
       pago = pago % moneda
       if pago == 0:
          break
       else:
           monedaIndex += 1
           assert monedaIndex < len(tiposDeMonedas), "Error: No hay más tipos de monedas disponibles"
    assert pago == 0, "Error: No se pudo calcular el cambio correctamente."
    return numeroDeMonedas   
print(calcular_cambio(8))       
print(calcular_cambio(13))
print(calcular_cambio(4))
print(calcular_cambio(0))




#print(euros(8))
assert calcular_cambio(8) == [1, 1, 1]
#>>> (1, 1, 1)  # una de 5 cénts, una de 2 cénts y una de 1 cént.

# print(euros(5))
assert calcular_cambio(5) == [1, 0, 0]
#>>> (1, 0, 0)  # una 5 cénts, ninguna de 2 cénts y ninguna de 1 cént.

assert calcular_cambio(2) == [0, 1, 0]

assert calcular_cambio(1) == [0, 0, 1]

assert calcular_cambio(29) == [5, 2, 0]
#print(euros(29))
#>>> (5, 2, 0)  # cinco de 5 cénts, dos de 2 cénts y ninguna de 1 cént.

assert calcular_cambio(235) == [47, 0, 0]

# print(calcular_cambio(0))
assert calcular_cambio(0) == [0, 0, 0]
#>>> [0, 0, 0] # ninguna de 5 cénts, ninguna de 2 cénts y 1 de cénts.
assert calcular_cambio(-1) == [0, 0, 0]