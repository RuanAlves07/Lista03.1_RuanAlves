#5)	No comercio o conceito de margem-bruta é uma porcentagem que é aplicada ao preço de custo para se obter o preço de venda. Uma loja de tem como politica comercial aplicar uma margem bruta de 45% quando o preço de custo é <= de R$100,00, se o produto custa mais que isso a margem bruta é de 35% , escreva um programa que leia o preço de custo do produto e mostre na tela qual o seu preço de venda com duas casas decimais 

preço_custo = int(input("Insira o preço de custo do produto: "))

if preço_custo <= 100:
    preço_total = preço_custo * 0.45
    preço_total = preço_total + preço_custo
    print("Valor total deu: {}".format(preço_total))
else:
    preço_total = preço_custo * 0.35
    preço_total = preço_total + preço_custo
    print("Valor total deu: {}".format(preço_total))