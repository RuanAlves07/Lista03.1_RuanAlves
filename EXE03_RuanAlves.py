#3)	Uma empresa financeira consegue empréstimos a pessoas físicas quando o valor da parcela é menor que 8% do salário da pessoa. Escreva um programa que leia dois números reais o valor do salário e o valor da parcela e informe se o empréstimo será concedido ou não.

salario = int(input("Informe seu salario atual: "))
emprestimo = int(input("Informe o valor do emprestimo: "))
parcela = int(input("Informe a quantidade de parcelas: "))

if  salario * 0.08 > emprestimo / parcela:
    print("Emprestimo foi liberado!")
else:
    print("Emprestimo não foi liberado.")