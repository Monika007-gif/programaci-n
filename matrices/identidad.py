def esMatrizCuadrada(matrix):

    numeroFilas = len(matrix)

    for i in range (numeroFilas):
      columnas = len(matrix[i])
      if numeroFilas != columnas:
            return False

    return True



# Casos test:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]

print (esMatrizCuadrada(matrix1))
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print (esMatrizCuadrada(matrix2))
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print (esMatrizCuadrada(matrix3))
#>>>False

matrix6 = [[1,0,0,0],  
           [0,1,0,2],  
           [0,0,1,0],  
           [0,0,0,1]]

print (esMatrizCuadrada(matrix6))
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print (esMatrizCuadrada(matrix7))
#>>>False           


# casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert):

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print (esMatrizCuadrada(matrix4))
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print (esMatrizCuadrada(matrix5))
#>>>False           