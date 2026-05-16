def gerar_dicionario(nome_arquivo,min, max):
    dict = {}
    try:
        with open(nome_arquivo, 'r', encoding="utf-8") as file:
            print(f"\nConteúdo do Arquivo: {nome_arquivo}")
            for linha in file:
                print(linha,end='')
            
                palavras = linha.split()
                for p in palavras:
                    p_limpa = p.replace(',', '').upper()

                    if min <= len(p_limpa) <= max:
                        if p_limpa in dict:
                            dict[p_limpa] += 1
                        else:
                            dict[p_limpa] = 1

        print("\n\nDicionário de Palavras em Contagem de Ocorrências: ")
        chaves_ordenadas = sorted(dict.keys())
        for chave in chaves_ordenadas:
            if dict[chave] == 1:
                vezes = "vez"
            else:
                vezes = "vezes"
            print(f"{chave} ocorreu {dict[chave]} {vezes}")
    except:
        print("Arquivo não encontrado!")

nome = input("")
valores = input("").split()
tamanho_minimo = int(valores[0])
tamanho_maximo = int(valores[1])

gerar_dicionario(nome,tamanho_minimo, tamanho_maximo)