
# -*- 2160 - Nome no Formulário 
l = raw_input()
    
if(len(l) > 80): 
    print("NO")
else:
    print("YES")

# 2334 - Patinhos
negativo = -1
    
p = int(raw_input())
while(p!= -1):
    if(p == 0):
        print("0")
    else:
        print(p-1)
    
    p = int(input())

# 2344 - Notas da prova 
    
n = int(raw_input())
if(n == 0):
    print("E")
elif(n >= 1 and n <= 35):
        print("D")
elif(n >= 36 and n <= 60):
        print("C")
elif(n >= 61 and n <= 85):
    print("B");
elif(n >= 86 and n <= 100):
    print("A")

# 1847 - Bem-vindos e Bem-vindas ao Inverno! 
import math

valores = raw_input().split(' ')
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])
  
if(a > b and b <= c):
      print(":)")

elif(a < b and b >= c):
    print(":(")

elif(a < b and b < c):
      if(math.fabs(c-b) < math.fabs(b-a)):
          print(":(")
      else:
          print(":)")
 
elif(a > b and b > c):
    if(math.fabs(c-b) < math.fabs(b-a)):
        print(":)")
    else:
        print(":(")

elif a == b:
    if c > b:
        print(":)")
    else:
        print(":(")

#Media 3
valores = raw_input().split()
n1 = valores[0]
n2 = valores[1]
n3 = valores[2]
n4 = valores[3]

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (n1*2 + n2*3 + n3*4 + n4*1)/(2 + 3 + 4 + 1)
print('Media: %.1f' %media)
if media >= 7:
    print('Aluno aprovado.')
elif media >= 5 and media <= 6.9:
    print('Aluno em exame.')
    notaexame = raw_input('')
    notaexame = float(notaexame)
    print('Nota do exame: ' + str(notaexame))
    media = (media + notaexame)/2

    if media >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')

    print('Media final: %.1f' %media)

elif media < 5:
    print('Aluno reprovado.')

    #Mediana 
    import math

#while False:
    #try:
        
valores = "4 5 3"
valores = valores.split()
m1 = float(valores[0])
m2 = float(valores[1])
m3 = float(valores[2])

expressao1 = (8*math.pow(m1, 2) + 8*math.pow(m2, 2) - 4*math.pow(m3, 2))/9
if(expressao1 >= 0):
    l3 = math.sqrt(expressao1)
else:
    l3 = 0.0
expressao2 = (8*math.pow(m1, 2) + 4*math.pow(m2, 2) - 6*math.pow(l3, 2))/3
if(expressao2 >= 0):
    l2 = math.sqrt(expressao2)
else:
    l2 = 0.0
expressao3 = 2*(math.pow(l2, 2) + math.pow(l3, 2)) - 4*math.pow(m1, 2)
if(expressao3 >= 0):
    l1 = math.sqrt(expressao3)
else:
    l1 = 0.0

if(l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2):
    p = (l1 + l2 + l3) / 2
    a = math.sqrt(p*(p-l1)*(p-l2)*(p-l3))
    print('%.3f' %a)
else:
    print('%.3f' %-1.0)
        
    #except EOFError:
        #break

#TDA
from fractions import Fraction

numerador = 0; denominador = 0
n = raw_input()
n = int(n)

for i in range(n):
        entrada = raw_input().split()
        x = int(entrada[0])

        barra = entrada[1]

        y = int(entrada[2])

        fracao1 = {
            'numerador':x,
            'denominador':y
        }

        operacao = entrada[3]

        x = int(entrada[4])

        barra = entrada[5]

        y = int(entrada[6])

        fracao2 = {
            'numerador':x,
            'denominador':y
        }
       
        if operacao == '+':
            numerador = (fracao1['numerador']*fracao2['denominador'] + fracao2['numerador']*fracao1['denominador'])
            denominador = (fracao1['denominador'] * fracao2['denominador'])

        elif operacao == '-':
            numerador = (fracao1['numerador']*fracao2['denominador'] - fracao2['numerador']*fracao1['denominador'])
            denominador = (fracao1['denominador'] * fracao2['denominador'])

        elif operacao == '*':
            numerador = (fracao1['numerador']*fracao2['numerador'])
            denominador = (fracao1['denominador'] * fracao2['denominador'])
        
        elif operacao == '/':
            numerador = (fracao1['numerador']*fracao2['denominador'])
            denominador = (fracao2['numerador']*fracao1['denominador'])

        f = Fraction(numerador,denominador)

        if f.denominator == 1:
            print(str(numerador) + "/" + str(denominador) + " = " + str(f) + "/1")
        else:
            print(str(numerador) + "/" + str(denominador) + " = " + str(f))

#1198 - O bravo guerreiro Hashmat
while True:
    try:
        valores = input().split()
        n1 = int(valores[0])
        n2 = int(valores[1])
    
        if(n1> n2):
            print(n1 - n2)
        
        else:
            print(n2 - n1)
    except EOFError:
        break

#1212 - Aritmétrica Primária
valores = raw_input().split()
x1 = int(valores[0])
x2 = int(valores[1])

totCarry = 0; resto = 0
   
while(x1 != 0 or x2 != 0):
    while(x1 > 0  or x2 > 0):
         r1 = x1 % 10
         r2 = x2 % 10

         x1 = int (x1 / 10)
         x2 = int (x2 / 10)
         
         if(resto == 1):
             resp = r1 + r2 + resto
             resto = 0
         
         else:
             resp = r1 + r2 + resto
         
         if(resp >= 10):
             totCarry = totCarry + 1
             resto = resto + 1
    
    if(totCarry == 0):
        print("No carry operation.")
    
    elif(totCarry == 1):
        print(str(totCarry) + " carry operation.")
    
    else:
        print(str(totCarry) + " carry operations.")
    
    totCarry = 0
    resto = 0
    valores = raw_input().split()
    if(valores[0].isdigit()):
        x1 = int(valores[0])
    if(valores[1].isdigit()):
        x2 = int(valores[1])


# 1828 - Bazinga    
t = int(input());
    
for i  in range(1, t+1):
    valores = input().split(' ')
    sheldom = valores[0]
    raj = valores[1]
    if(sheldom == "papel" and raj == "papel"):
        print("Caso #"+str(i)+": De novo!")
    elif(sheldom == "tesoura" and raj == "tesoura"):
        print("Caso #"+str(i)+": De novo!")
    elif(sheldom == "pedra" and raj == "pedra"):
        print("Caso #"+str(i)+": De novo!")
    elif(sheldom == "lagarto" and raj == "lagarto"):
        print("Caso #"+str(i)+": De novo!")
    
    elif(sheldom == "Spock" and raj == "Spock"):
        print("Caso #"+str(i)+": De novo!")
    elif(sheldom == "tesoura" and  (raj == "papel" or raj == "lagarto")):
        print("Caso #"+str(i)+": Bazinga!")
    
    elif(sheldom == "papel" and (raj == "pedra" or raj == "Spock")):
        print("Caso #"+str(i)+": Bazinga!")
    
    elif(sheldom == "pedra" and (raj == "lagarto" or raj == "tesoura")):
        print("Caso #"+str(i)+": Bazinga!")
    elif(sheldom == "lagarto" and  (raj == "Spock" or raj == "papel")):
        print("Caso #"+str(i)+": Bazinga!")
    elif(sheldom == "Spock" and  (raj == "tesoura" or raj == "pedra")):
        print("Caso #"+str(i)+": Bazinga!")
    elif(sheldom == "lagarto" and  (raj == "Spock" or raj == "papel")):
        print("Caso #"+str(i)+": Bazinga!")
    else:
        print("Caso #"+str(i)+": Raj trapaceou!")
        
        
#Kage Bushin no Jutsu
import math
while True:
    try:
        n = int(input())
        i = 0;
        while(int(math.pow(2, i)) <= n):
            resultado = i
            i = i + 1
        print(resultado);
    except EOFError:
        break
    
#1219 - Flores cloridas
import math
while True:
    try:
        valores = input().split()
        a = int(valores[0])
        b = int(valores[1])
        c = int(valores[2])

        p = (a + b + c)/2.0

        Area_triangulo = math.sqrt(p*(p - a)*(p - b)*(p - c))
        R = (a*b*c)/(4.0*Area_triangulo)
            
        Area_amarela = math.pi*math.pow(R, 2) - Area_triangulo
            
        r = Area_triangulo / p
        Area_azul = Area_triangulo - math.pi*math.pow(r, 2)
            
        Area_vermelha = math.pi*math.pow(r, 2)
            
        print('%.4f %.4f %.4f'%(Area_amarela, Area_azul, Area_vermelha))

    except EOFError:
        break
