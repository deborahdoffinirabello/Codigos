#print com nome e sobrenome
print("Bem vindo a loja da Déborah Rabello!")

#implementação do input do valor do pedido e uantidade de parcelas
valorDoPedido = float(input('Insira o valor do pedido:'))
quantidadeParcelas = int(input ('Insira a quantidade de parcelas que deseja:'))

#logica para saber o valor de juros e implementação de if else e elif

if quantidadeParcelas <4:
    juros = 0
elif quantidadeParcelas >= 4 and quantidadeParcelas <6 :
    juros = (4/100)
elif quantidadeParcelas >=6 and quantidadeParcelas<9:
    juros = (8/100)
elif quantidadeParcelas >=9 and quantidadeParcelas<13:
    juros = (16/100)
else:
    juros = (32/100)
    
#calculo do valor de parcela e valor total parcelado
valorDaParcela = ((valorDoPedido * (1+ juros))/quantidadeParcelas)
valorTotalParcelado = valorDaParcela*quantidadeParcelas
 
#print para mostrar o valor total parcelado e o valor de cada parcela
print(f'O  valor de cada parcela é de : R$ {valorDaParcela:.2f} e o valor total parcelado é de : R$ {valorTotalParcelado:.2f}.') 
