def print_lol(lista, identado=False,nivel=0):
    if nivel<0:
        nivel = 0
    for i in lista:
        if isinstance(i, list):
            print_lol(i,identado, nivel+1)
        else:
            if identado:
                for tabulaciones in range(nivel):
                    print("\t", end='')
            print(i)