def first_n_smallest(pp, n):
    if n >= len(pp):
        return pp
    num_peq = sorted (pp)[:n] 
    resultado = []
    for numero in pp:
        if numero in num_peq:
            resultado.append(numero)
            num_peq.remove(numero)
    return resultado