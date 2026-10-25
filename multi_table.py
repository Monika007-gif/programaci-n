def multi_table(number):
    tabla = ""
    for i in range(1, 11):
        tabla += f"{i} * {number} = {i * number}\n"
    return tabla.rstrip("\n")
    print(multi_table(9))
        
