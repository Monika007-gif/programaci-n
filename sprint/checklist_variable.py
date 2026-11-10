def calc(x, y):
    temp = sum(x) / len(x)  # ¿Qué representa "temp"?
    z = max(x)  # ¿Qué representa "z"?
    w = min(x)  # ¿Qué representa "w"?
    return temp, z, w

#El nombre de la función (calc), es corto y no explica qué datos recibe la función.
#temp no indica qué representa el valor almacenado.
#x, y, z y w son infracciones, no describen. La variable y no indica qué representa y no se utiliza dentro de la función, z no identifica qué valor almacena, al igual que w

#Refactorizado  
def calculate_estatisticas(valores):
    if not valoress:
        raise ValueError("Lista con un elemento como mínimo")
    media = sum(valores) / len(valores)
    maximo = max(valores)
    minimo = min(valores)
    return media, maximo, minimo

PI = 3.14159
#Es una constante matemática, sigue la convención, no es una infracción, pero se podría mejorar
#Refactorizado
PI_VALUE = 3.14159


RED = 1
GREEN = 2
BLUE = 3

#Son constantes que almacenan valores que representan algo concreto, aunque cumple la convención de Python, están en mayúsculas y son descriptivos, podrían mejorar, según los principios del capítulo 11 de Clean Code.


#Refactorizado
COLOR_RED = 1
COLOR_GREEN = 2
COLOR_BLUE = 3

g = [10, 20, 30, 40, 50]
#g representa una lista de números pero no explica qué significan, necesitamos un nombre más descriptivo
#Refactorización
Edades = [10, 20, 30, 40, 50]

# Función con un nombre que no describe su propósito
def doStuff():
    # Uso de nombres de variables booleanas poco claros
    flag = True  # ¿Qué significa "flag"?
    if flag:
        # Uso de nombres de variables que no describen su propósito
        a = calc(g, PI)
        print("Resultados:", a)
#No explica qué hace la función (doStuff), flag es poco descriptivo, calc es abreviado, g es una lista pero no sabemos qué representa, a no explica qué información tiene, PI es una constante matemática, no la necesita esta función.

#Refactorizada
edades = [10, 20, 30, 40, 50]
def calcular_estadisticas(valores):
    media = sum(valores) / len(valores)
    maximo = max(valores)
    minimo = min(valores)
    return media, maximo, minimo
def mostrar_resultados():
    mostrar = True
    if mostrar:
     estadisticas = calcular_estadisticas(edades)
     print("Resultados:", estadisticas)