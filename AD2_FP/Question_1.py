list=[]

while True:
    list = input("").split(" ")
    print(f"Tamanho da Lista:{len(list)}")
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





    except ValueError:
        print("Digite números inteiros separados por espaço!")
        continue





    print(f"N:{N}")
    print(f"M:{M}")