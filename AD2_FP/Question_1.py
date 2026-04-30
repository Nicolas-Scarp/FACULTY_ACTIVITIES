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

parar=False
temp=[]

while True:

    mini=0
    maxi=0
    list2=[]
    vi = []

    if parar == True:
        break
    list2 = input("").split()

    try:
        for i in range(len(list2)):
            valor=int(list2[i])
    except:
        print("Digite números!")
        continue

    if len(list2) < N:
        print("Valores insuficientes!\nTente Novamente.")
        continue
    elif len(list2) > N:
        print("Mais valores que o esperado!\nTente Novamente.")
        continue
    else:
        for i in range(len(list2)):
            vi.append(int(list2[i]))
        for i in range(len(vi)):
            if vi[i] < 1:
                mini=mini+1
                continue
            elif vi[i] > 100:
                maxi=maxi+1
                continue
            else:
                continue
        while True:
            if mini != 0 or maxi != 0:
                print("Tempo precisa ser entre 1 e 100!\nDigite novamente.")
                break
            else:
                parar = True
                temp=vi
                break

parar=False
itens=[]

while True:

    mini2=0
    maxi2=0
    list3=[]
    vi2 = []

    if parar == True:
        break
    list3 = input("").split()

    try:
        for i in range(len(list3)):
            valor=int(list3[i])
    except:
        print("Digite números!")
        continue

    if len(list3) < M:
        print("Valores insuficientes!\nTente Novamente.")
        continue
    elif len(list3) > M:
        print("Mais valores que o esperado!\nTente Novamente.")
        continue
    else:
        for i in range(len(list3)):
            vi2.append(int(list3[i]))
        for i in range(len(vi2)):
            if vi2[i] < 1:
                mini2=mini2+1
                continue
            elif vi2[i] > 100:
                maxi2=maxi2+1
                continue
            else:
                continue
        while True:
            if mini2 != 0 or maxi2 != 0:
                print("A quantidade de itens precisa ser entre 1 e 100!\nDigite novamente.")
                break
            else:
                itens=vi2
                parar = True
                break

soma = 0
soma_list = []

while True:
    if N < M:
        for i in range(N):
            soma_list.append(temp[i]*itens[i])

        break

    elif M < N:
        for i in range(M):
            soma_list.append(temp[i]*itens[i])
        for i in range(soma_list):
            soma = soma + soma_list[i]
        break

    else:
        for i in range(N):
            soma = soma + temp[i]*itens[i]
        for i in range(soma_list):
            soma = soma + soma_list[i]
        break

print(soma_list)
print(soma)
       
            



    