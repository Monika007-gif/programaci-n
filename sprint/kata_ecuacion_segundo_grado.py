def raiz_ecuacion_segundo_grado(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
       return None
    raiz = discriminante **0.5
    x1 = (-b + raiz) / (2 * a)
    x2 = (-b - raiz) / (2 * a)
    return (x1, x2)
if __name__ == "__main__":
    print(raiz_ecuacion_segundo_grado(1, -7, 12))
    assert raiz_ecuacion_segundo_grado(1, -7, 12) == (4, 3)

#Tras varios intentos la prueba pasó finalmente.