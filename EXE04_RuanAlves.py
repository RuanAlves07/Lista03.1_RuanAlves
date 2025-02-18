#4)	No Senailandia, mulheres e homens podem servir o exercito do país. O serviço é opcional e é muito comum que as pessoas se apresentem para o serviço em algum momento da vida. Existe uma única restrição para o ingresso que é a idade da pessoa: 

#A)	Para mulheres, a idade aceita é entre 21-34 anos 
#B)	Para homens, a idade aceita é entre 18-39 anos
#Escreva um programa que leia 3 dados de entrada:
#A)	Nome da pessoa
#B)	Idade
#C)	Sexualidade
#E informe se a pessoa será aceita ou não para o serviço.
#OBS: PARA O SEXO DEVE SER LIDO APENAS UM CARACTERE (F/M), QUALQUER COISA DIFERENTE, DEVE SER INFORMADO COMO INVALIDO

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
sexualidade = input("Insira seu genero: (M/F) ")

if sexualidade == "F" and idade >= 21 and idade <= 34:
    print("Você está alistado!")

elif sexualidade == "M" and idade >= 18 and idade <= 39:
        print("Você está alistado!")
        
else:
    print("Você não foi convocado(a)")

print("Ruan Augusto Alves")