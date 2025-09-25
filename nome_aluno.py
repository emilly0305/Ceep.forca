nome_cadastrado = "Joao Silva"  # Nome pré-definido no programa
tentativas_max = 6  # Número máximo de tentativas
tentativas = 0  # Contador de tentativas

print("Bem-vindo! Você tem 6 tentativas para acertar o nome do aluno.")
print("Escolha uma opção:")
print("1 - Digitar o nome completo")
print("2 - Tentar letra por letra")

opcao = input("Digite 1 ou 2: ")

if opcao == "1":
    # Modo 1: Digitar o nome completo
    while tentativas < tentativas_max:
        nome_digitado = input("Digite o nome do aluno: ")
        tentativas += 1
        
        if nome_digitado == nome_cadastrado:
            print(f"Parabéns! O nome digitado corresponde ao nome cadastrado em {tentativas} tentativa(s)!")
            break
        else:
            tentativas_restantes = tentativas_max - tentativas
            if tentativas_restantes > 0:
                print(f"Nome incorreto. Você ainda tem {tentativas_restantes} tentativa(s).")
            else:
                print("Você esgotou todas as tentativas. O nome correto era Joao Silva.")

elif opcao == "2":
    # Modo 2: Tentar letra por letra
    nome_lista = list(nome_cadastrado)  # Converte o nome em uma lista de letras
    posicao = 0  # Controla a posição da letra atual
    
    while tentativas < tentativas_max and posicao < len(nome_lista):
        letra_correta = nome_lista[posicao]
        letra_digitada = input(f"Digite a letra na posição {posicao + 1}: ")
        tentativas += 1
        
        if letra_digitada == letra_correta:
            print(f"Correto! A letra '{letra_digitada}' está na posição {posicao + 1}.")
            posicao += 1  # Avança para a próxima letra
            if posicao == len(nome_lista):
                print(f"Parabéns! Você acertou todas as letras do nome 'Joao Silva' em {tentativas} tentativa(s)!")
                break
        else:
            tentativas_restantes = tentativas_max - tentativas
            if tentativas_restantes > 0:
                print(f"Letra incorreta. Você ainda tem {tentativas_restantes} tentativa(s).")
            else:
                print("Você esgotou todas as tentativas. O nome correto era Joao Silva.")
else:
    print("Opção inválida. Execute o programa novamente e escolha 1 ou 2.")