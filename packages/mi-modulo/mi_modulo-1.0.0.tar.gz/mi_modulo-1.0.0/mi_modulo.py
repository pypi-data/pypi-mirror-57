def print_lol(lista):
    for i in lista:
        if isinstance(i, list):
            print_lol(i)
        else:
            print(i)