#    1: Escreva um programa que forneça o tipo de aplicação financeira adequado a um investidor a partir de dois dados fornecidos: 
	 #O grau de aceitação de risco
	 #E o valor aceito investido.
# O grau de aceitação de risco deve ser lido no teclado na forma BX para baixo ou AL para alto se for fornecido algo diferente disso o programa deve mostrar uma mensagem indicando que foi fornecido um dado invalido. Para o valor deve ser um numero real

risco = input("Insira o grau de aceitação de risco (BX para Baixo, AL para Alto.)")

if risco != "BX" or "AL":
    print("Por favor, insira uma das opções validas citadas acima.")

investimento = int(input("Insira o valor aceito investido."))


if investimento < 1000 and risco == "BX":
    print("Você deve investir em poupança!")
if investimento >= 1000 and risco == "BX":
    print("Você deve investir na renda fixa!")
if investimento < 1000 and risco == "AL":
    print("Você deve investir em BitCoins!")
if investimento >= 1000 and risco == "AL":
    print("Você deve investir em ações!")