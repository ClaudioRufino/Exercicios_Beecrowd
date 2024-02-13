
# Resolvendo exercicio de um Perceptron

v = 0
bias = 0
x = [1.4, -2.5, 0.7]
w = [0.4, 0.6, 0.3]


for i in range(len(x)):
    v = v + w[i]*x[i]

v = v + bias

if(v >= 0):
    v = 1
else:
    v = -1


print(str(v))







# /* 1235 - De dentro pra fora - 5 pontos
# n = int(input())
# for i in  range(n):
#     frase = input()
#     resultado = ""
#     j = (frase.count(frase) / 2) - 1
#     while(j >= 0):
#         if(frase.charAt(j)==' '):
#             resultado += " "
#         else:
#             resultado += frase.charAt(j)
#         j = j - 1

#     j = frase.count(frase)-1

#     j = (frase.count(frase)/ 2 ) - 1
#     while(j >= frase.count(frase)/ 2):
#         if(frase.charAt(j)==' '):
#             resultado += " "
#         else:
#             resultado += frase.charAt(j)
#         j = j - 1
    
#     print(resultado)
#     resultado = ""


