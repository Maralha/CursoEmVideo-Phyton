'''
Crie um algoritmo que leia um número e mostre o seu 
dobro, tiplo e raiz quadrada.
'''
n1  = int(input("Digite um número:"))
print ("O dobro de {} vale: {} \nO tiplo de {} vale: {} \nA raiz quadrada de {} vale: {:.2f} ".format(n1, n1*2, n1, n1*3, n1, n1 ** (1/2)))