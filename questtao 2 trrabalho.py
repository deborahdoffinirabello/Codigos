#mensagem de boas vindas e cardapio
print("     Bem-vindo à Loja de Marmitas do Deborah Rabello!   \n")
print("                         Cardápio                      \n ")
print("| Tamanho | Bife Acebolado (BA) | Filé de Frango (FF)  |")
print("|    P    |      R$ 16.00       |       R$ 15.00       |")
print("|    M    |      R$ 18.00       |       R$ 17.00       |")
print("|    G    |      R$ 22.00       |       R$ 21.00       |\n")
#zerando as variaveis e preparando o laço de while
acumulador = float
acumulador = 0
pedirMais = "1"
while pedirMais != '2' :
    #escolha de sabor
    sabor = input('Escolha o sabor desejado (BA para bife acebolado e FF para filé de frango) :')
    if sabor == 'BA' or sabor == 'FF':
        #escolha de tamanho
        tamanho = input('escolha o tamanho (P para pequeno, M para médio e G para grande) :')
        if tamanho == "P" or tamanho == "M" or tamanho == "G":
            #começo da implementação do modelo aninhado
            if sabor == "BA" and tamanho == 'P':
                print("Você pediu um Bife Acebolado no tamanho", tamanho,": R$16.00\n")
                acumulador = acumulador + 16
            elif sabor == "BA" and tamanho =='M':
                print("Você pediu um Bife Acebolado no tamanho", tamanho,": R$18.00\n")
                acumulador = acumulador + 18
            elif sabor =="BA" and tamanho =='G':
                print("Você pediu um Bife Acebolado no tamanho", tamanho ,": R$22.00\n")
                acumulador = acumulador + 22
            elif sabor =="FF" and tamanho =='P':
                print("Você pediu um File de Frango no tamanho", tamanho ,": R$15.00\n")
                acumulador = acumulador + 15
            elif sabor =="FF" and tamanho =='M':
                print("Você pediu um File de Frango no tamanho", tamanho ,": R$17.00\n")
                acumulador = acumulador + 17
            elif sabor =="FF" and tamanho =='G':
                print("Você pediu um File de Frango no tamanho", tamanho ,": R$21.00\n")
                acumulador = acumulador + 21
                #utilização do continue e do break  
                      
            Maispedidos = input('Deseja pedir mais alguma coisa? (S/N)\n') 
            if Maispedidos == 'S':
                continue
            else :
               break
           
        #Print caso seja inserido tamanho e sabor invalido
        else :
            print('Tamanho inválido. Tente novamente\n')
    else :
            print('Sabor inválido. Tente novamente\n')

print(f"O valor total do pedido foi de: R$ {acumulador:.2f}\n")
   