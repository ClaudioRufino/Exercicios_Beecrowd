
1213 - ONE

9999
3439
3441
3443
3447
3449
3451
3453
3457
3459
3461
3463
3467
3469

Resposta

36
180
15
312
3438
431
336
1725
384
1152
3460
3462
1733
3468

 
#1837 - Prefácio 
import math

valores  = input().split()    
a = int(valores[0])
b = int(valores[1])

if(a < 0 and b > 0):
    i = -1;
    while(i*b > a):
        i = i - 1;
    q = i;
    r = a - (i*b)
    
elif( a < 0 and b < 0):
    i = 1
    while(i*b > a):
        i = i + 1
    q = i
    r = a - (i*b)
else:
    q = int(a / b)
    r = int(a % math.fabs(b))
    
print(str(q)+ " " + str(r))