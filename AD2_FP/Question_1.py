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

list2=[]
vi = []

while True:
    list2 = input("").split()
    if len(list2) < N:
        print("Valores insuficientes!\nTente Novamente.")
        continue
    elif len(list2) > N:
        print("Mais valores que o esperado!\nTente Novamente.")
        continue
    else:
        for i in range(len(list2)):
            vi.append(int(list2[i]))
            break
        break

mini=0
maxi=0

for i in range(len(vi)):

    if vi[i] < 1:
        mini=mini+1
        
        continue
    elif vi[i] > 100:
        maxi=maxi+1
        
        continue
    else:
        break
    

print(mini)
print(maxi)



print("Tempo não pode ser menor que 1!\nDigite novamente.")

print("Tempo não pode ser maior que 100!\nDigite novamente.")            
            



    