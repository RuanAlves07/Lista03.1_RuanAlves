#    1: Escreva um programa que forneça o tipo de aplicação financeira adequado a um investidor a partir de dois dados fornecidos: 
	 #O grau de aceitação de risco
	 #E o valor aceito investido.
# O grau de aceitação de risco deve ser lido no teclado na forma BX para baixo ou AL para alto se for fornecido algo diferente disso o programa deve mostrar uma mensagem indicando que foi fornecido um dado invalido. Para o valor deve ser um numero real

risco = input("Insira o grau de aceitação de risco (BX para Baixo, AL para Alto.)")
investimento = int(input("Insira o valor que queira investir: "))


if investimento < 1000 and risco == "BX":
    print("Você deve investir em poupança!")
elif investimento >= 1000 and risco == "BX":
    print("Você deve investir na renda fixa!")
elif investimento < 1000 and risco == "AL":
    print("Você deve investir em BitCoins!")
elif investimento >= 1000 and risco == "AL":
    print("Você deve investir em ações!")

else:
    print("Dados invalidos!")
    

print("Ruan Augusto Alves")
