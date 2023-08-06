def print_lol(lista, nivel):
    for i in lista:
        if isinstance(i, list):
            print_lol(i, nivel+1)
        else:
            for tabulaciones in range(nivel):
                print("\t", end='')
            print(i)