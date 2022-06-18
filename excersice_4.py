def numer_primo(inicio, fin):
    nPrimo = [];

    while inicio <= fin:
        contador = 1
        x = 0
        while contador <= inicio:
            if inicio % contador == 0:
                x=x+1
            contador = contador + 1
        if x == 2:
            print(inicio)
            nPrimo.append(inicio)
        inicio = inicio + 1
    return nPrimo

numer_primo(inicio=120, fin=18720)