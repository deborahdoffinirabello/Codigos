#Boas vindas e nome e sobrenome
print("seja bem vindo a loja de camisetas da Déborah Rabello")

#funcao de modelo
def escolha_modelo():
    while True:
            modelo = input("Qual modelo desejado?\nMCS - Manga Curta Simples\nMLS - Manga Longa Simples\nMCE - Manga Curta com Estampa\nMLE - Manga Longa com Estampa\n")
            if modelo == 'MCS' or modelo == 'MLS' or modelo == 'MCE' or modelo == 'MLE' :
                break
            else:
                print("Este modelo não existe, tente novamente.\n")    
    if modelo == "MCS":
        valormodelo = 1.8
    elif modelo == "MLS":
        valormodelo = 2.1
    elif modelo == "MCE":
        valormodelo = 2.9
    elif modelo == "MLE":
        valormodelo = 3.2
        
    return valormodelo


#função de numero de camisetas
def num_camisetas():
    while True:
        try:
            quantidade = int(input("Qual o numero de camisetas? "))
            if quantidade > 20000:
                print("Não aceitamos pedido com mais de 20000 camisetas.\nPor favor, insira o número de camisetas novamente.\n")
            elif quantidade <= 0:
                print("Por favor, insira o número de camisetas novamente.\n")
            else:
                break
        except ValueError:
            print("Por favor, insira o número de camisetas novamente.\n")

    #aplicando o desconto
    if quantidade < 20:
        desconto = 0  
    elif quantidade >= 20 and quantidade < 200:
        desconto = 5/100  
    elif quantidade  >= 200 and quantidade < 2000:
        desconto = 7/100  
    else: 
        desconto = 12/100  
    return quantidade, desconto

def frete():
    while True:
        try:
            valorfrete = int(input('Escolha o tipo de frete:\n 1 - Frete por transportadora - R$ 100.00\n 2 - Frete por Sedex - R$ 200.00\n 0 - Retirar pedido na fábrica = R$ 0.00 \n'))
            if valorfrete > 2:
                print("Frete inválido, escolha o tipo de frete novamente\n")
            elif valorfrete <0:
                print("Frete inválido, escolha o tipo de frete novamente\n")
            else :
                break
        except ValueError:
            print("Frete inválido, escolha o tipo de frete novamente\n")
            
 #calculo do frete      
    if valorfrete == 1:
        valor = 100
    elif valorfrete == 2:
        valor = 200
    elif valorfrete == 0:
        valor = 0
    return valor 

#codigo principal
valormodelo = escolha_modelo()       
quantidade, desconto = num_camisetas()
valor = frete()
#calculando o preço final
precofinal = ((valormodelo * quantidade )* (1 - desconto)) + valor

print(f'O valor total do pedido foi de: R$ {precofinal:.2f}. (Modelo : {valormodelo:.2f} * Quantidade (com desconto) : {((valormodelo * quantidade )* (1 - desconto)):.2f} + Frete : {valor:.2f})')




