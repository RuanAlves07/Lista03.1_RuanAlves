#Nas eleições municipais, os municípios com 200.000 eleitores ou mais tem segundo turno caso o primeiro colocado não tenha mais que 50% dos votos. Escreva um programa que leia o nome do município, a quantidade de eleitores, a quantidade de votos do candidato mais votado e informe se haverá segundo turno ou não

municipio = input("Insira o nome do municipio: ")
qntd_eleitores = int(input("Insira a quantidade de eleitores: "))
qntd_candidato = int(input("Insira a quantidade de votos do candidato mais votado: "))

if qntd_candidato > (qntd_eleitores / 2):
    print("Não haverá segundo turno, o candidato mais votado do municipio segue com {} votos dentre os {} votos no total.".format(qntd_candidato, qntd_eleitores))
else:
    print("Será necessário segundo turno.")


print("Ruan Augusto Alves")