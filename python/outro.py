
import math

valores = input().split(' ')
hi = int(valores[0])
mi = int(valores[1])
hf = int(valores[2])
mf = int(valores[3])

mT = 0

if (hf > hi) :
    hT = (hf - hi)
    if (mf > mi) :
        mT = (mf - mi)

    elif(mf < mi) :
        hT=hT-1
        mT = math.fabs(mf - mi)
        mT = 60 - mT

elif(hf < hi) :
    hT = math.fabs(hf - hi)
    hT = 24 - hT
    if (mf > mi) :
        mT = (mf - mi)
    elif(mf < mi) :
        hT=hT-1
        mT = math.fabs(mf - mi)
        mT = 60 - mT

elif(hf == hi) :
    if (mf > mi) :
        hT = (hf - hi)
        mT = (mf - mi)

    elif(mf < mi) :
        mT = math.fabs(mf - mi)
        mT = 60 - mT
        hT = 23
    else :
        hT = 24



print("O JOGO DUROU " + str(math.trunc(hT)) + " HORA(S) E " + str(math.trunc(mT)) + " MINUTO(S)")