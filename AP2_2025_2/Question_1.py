def processar_arquivo(arquivo):
    try:
        with open(arquivo, 'r') as file:
            print(f"Conteúdo em {arquivo}: ")
            for linha in file:
                print(linha,end='')
            print()
        soma = 0
        total_numeros = 0
        with open(arquivo, 'r') as file:
            for linha in file:
                numeros = linha.split()
                for x in numeros:
                    soma += float(x)
                    total_numeros +=1
            media = soma / total_numeros
        print(f"\nMédia dos números em {arquivo}: {media}")
        quantidade_acima = 0
        with open(arquivo, 'r') as file:
            for linha in file:
                numeros = linha.split()
                for x in numeros:
                    if float(x) > media:
                        quantidade_acima += 1
                    else:
                        continue
        print(f"Quantidade Acima de {media} em {arquivo}: {quantidade_acima}")
    except:
        print("Arquivo não encontrado!")
            
ark = input("Digite o nome do arquivo: ")
print()
processar_arquivo(ark)