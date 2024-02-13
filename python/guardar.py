#1199 - Conversão simples de Base.

#2147483645 - 0x7FFFFFFD
#0x7FffFFfD - 2147483645
#0x1   -  1
#1     -  0x1
#2425   -   0x979
#0xab495C  -  11225436

novo = ''
valor = ''
lista = []
copia_valor = 0; solucao = 0; resto = 0; controlo = 0

while controlo >= 0:
    valor = input()
    if valor.startswith('0x'):
        for i in range(len(valor)):
            if valor[i] == 'x':
                continue
            elif valor[i] == 'a' or valor[i] == 'A':
                novo += str(10)
            elif valor[i] == 'b' or valor[i] == 'B':
                novo += str(11)
            elif valor[i] == 'c' or valor[i] == 'C':
                novo += str(12)
            elif valor[i] == 'd' or valor[i] == 'D':
                novo += str(13)
            elif valor[i] == 'e' or valor[i] == 'E':
                novo += str(14)
            elif valor[i] == 'f' or valor[i] == 'F':
                novo += str(15)
            else:
                novo += valor[i]
       
        if novo.isdigit():
            copia_valor = int(novo)
            controlo = copia_valor

        for i in range(len(novo) - 1):
            resto = copia_valor % 10
            copia_valor = int(copia_valor / 10)
            solucao += resto * (16 ** i)
           
        print(solucao)

    elif int(valor) >= 0:
        copia_valor = int(valor)
        if copia_valor < 16:
            print('0x'+str(copia_valor) )
        
        else:
            while copia_valor >= 16:
                resto = copia_valor % 16
                if resto == 10: lista.append('A')
                elif resto == 11: lista.append('B')
                elif resto == 12: lista.append('C')
                elif resto == 13: lista.append('D')
                elif resto == 14: lista.append('E')
                elif resto == 15: lista.append('F')
                else:
                    lista.append(resto)
                
                copia_valor = int(copia_valor / 16)
            lista.append(copia_valor)
            lista.reverse()
            y = ''
            for i in lista:
                y += str(i)

            print('0x'+ y)
    else:
        controlo = int(valor)
    
    lista = []
    solucao = 0
    novo = ''