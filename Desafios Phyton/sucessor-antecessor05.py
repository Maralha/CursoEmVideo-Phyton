'''
Faça um programa que leia um número inteiro e 
mostre na tela seu sucessor e seu antecessor.
'''
n1 = int(input("Digite um nímero:"))
s = int(n1 + 1)
a = int(n1 - 1)
print ("Analisando o valor {} seu sucessor é {} e o antecessor é {} ".format(n1, s, a))