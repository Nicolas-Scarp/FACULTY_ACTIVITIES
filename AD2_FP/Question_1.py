list=[]

while True:
    list = input("").split()
    try:
        N=int(list[0])
        M=int(list[1])

        if len(list) != 2:
            print("Digite dois números inteiros!")
            continue
        elif N < 1:
            print("Número de funcionários insuficiente!\nDigite novamente.")
            continue
        elif M < 1:
            print("Número de clientes insuficiente!\nDigite novamente.")
            continue
        elif N > 104:
            print("Número de funcionários não pode ser maior que 104!\nDigite novamente.")
            continue
        elif M > 104:
            print("Número de clientes não pode ser maior que 104!\nDigite novamente.")
            continue
        else:
            break

    except:
        if not list:
            print("Precisa conter dois números!")
        else:
            print("Digite números inteiros separados por espaço!")
        continue

