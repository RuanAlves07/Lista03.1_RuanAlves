#2)	Escreva um programa para exibir na tela o nome e a categoria de um lutador, o programa deve ler um String para o nome e um numero real para o peso. Conforme o peso ocorrera o enquadramento na categoria  

nome = input("Insira seu nome: ")
peso = int(input("Insira seu peso: "))

if peso < 52:
    print("Peso invalido!")
if peso >= 52 and peso < 65:
    print("Seu peso é Pena!")
if peso >= 65 and peso < 72:
    print("Seu peso é Leve!")
if peso >= 72 and peso < 79:
    print("Seu peso é Ligeiro!")
if peso >= 79 and peso < 86:
    print("Seu peso é Meio-Médio!")
if peso >= 86 and peso < 90:
    print("Seu peso é Médio!")
if peso >= 90 and peso < 100:
    print("Seu peso é Meio-pesado!")
if peso >= 100:
    print("Seu peso é Pesado!")