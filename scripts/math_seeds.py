from decimal import Decimal,ROUND_HALF_UP
from fractions import Fraction
import math
MATH=[]
def fmt(n):
    if isinstance(n,Fraction):return str(n.numerator) if n.denominator==1 else f'{n.numerator}/{n.denominator}'
    if isinstance(n,Decimal):return f'{n:.2f}'.replace('.',',')
    return str(n).replace('.',',')
def add(section,prompt,answer,distractors,explanation):
    opts=[]
    for x in distractors:
        s=fmt(x)
        if s!=fmt(answer) and s not in opts:opts.append(s)
    assert len(opts)>=3,(prompt,answer,opts)
    MATH.append(dict(topic=8,section=section,prompt=prompt,correct=fmt(answer),wrong=opts[:3],explanation=explanation,
      source={'kind':'manual','label':'Ejercicio nuevo · reglas del temario','reference':'PDF 207–214 · operaciones y proporcionalidad'},format='cálculo',coverage=section))
for n in range(1,25):
    a=100+7*n;b=20+3*n;c=15+2*n;r=a+b-c
    add('Cálculo: inventario',f'Hay {a} carpetas. Llegan {b} y se entregan {c}. ¿Cuántas quedan?',r,[a+b+c,a-b-c,a+b,r+5],f'Stock final = {a} + {b} − {c} = {r}.')
    a=10+n;b=2+n%4;c=8+n%3;d=3;r=a+b*(c-d)
    add('Cálculo: jerarquía',f'Calcula {a} + {b} × ({c} − {d}).',r,[(a+b)*(c-d),a+b*c-d,r+b],f'Primero {c} − {d} = {c-d}; después multiplicar por {b} y sumar {a}: {r}.')
    a=3+n;b=2+n%5;r=-(a*b)
    add('Cálculo: signos',f'¿Cuál es el resultado de (−{a}) × {b}?',r,[a*b,-a-b,a+b],f'Signos distintos: producto negativo. {a} × {b} = {a*b}, por tanto {r}.')
    d=4+n%7;q=12+n;rest=1+n%(d-1);D=d*q+rest
    add('Cálculo: división y resto',f'Se reparten {D} sobres en grupos de {d}. ¿Cuántos sobres sobran?',rest,[0,d,d-rest,rest+1,rest+2],f'{D} = {d} × {q} + {rest}; el resto {rest} es menor que {d}.')
    f=Fraction(n+1,n+3);g=Fraction(1,n+2);r=f+g
    add('Cálculo: fracciones',f'Calcula {fmt(f)} + {fmt(g)} y simplifica.',r,[f-g,f*g,Fraction(f.numerator+g.numerator,f.denominator+g.denominator),r+1],f'Denominador común y suma de numeradores; resultado reducido: {fmt(r)}.')
    total=100*(n+2);p=[5,10,15,20,25,30][n%6];r=total*p//100
    add('Cálculo: porcentajes',f'¿Cuánto es el {p} % de {total} documentos?',r,[total-r,total//p,r+10,total],f'{total} × {p}/100 = {r}.')
    total=4*(n+6);part=3*(n+6)
    add('Cálculo: porcentaje inverso',f'De {total} personas inscritas asisten {part}. ¿Qué porcentaje asiste?',75,[25,50,100],f'{part}/{total} × 100 = 75. La parte es tres cuartas partes del total.')
    workers=2+n%4;other=workers+1;unit=30+n;total=workers*unit;r=other*unit
    add('Cálculo: proporción directa',f'{workers} personas clasifican {total} documentos en un tiempo. Al mismo ritmo y tiempo, ¿cuántos clasifican {other}?',r,[total+other,total*other,r-unit],f'Proporción directa: {total} × {other}/{workers} = {r}.')
    workers=2+n%4;h=2*(n+3);r=h//2
    add('Cálculo: proporción inversa',f'{workers} personas tardan {h} horas en el mismo trabajo. Con rendimiento igual, ¿cuántas horas tardan {workers*2}?',r,[h*2,h,r+1],f'Doblar personal reduce tiempo a la mitad: {workers} × {h}/({workers*2}) = {r}.')
    pages=2*n+9;people=3+n%8;r=math.ceil(pages/2)*people
    add('Cálculo: copias a doble cara',f'Cada juego tiene {pages} páginas. Se necesitan {people} juegos separados a doble cara. ¿Cuántas hojas hacen falta?',r,[pages*people,(pages*people)//2,r+people,r-1],f'Cada juego impar precisa {(pages+1)//2} hojas; multiplicar por {people}: {r}.')
    price=Decimal(100+20*n);discount=[5,10,15,20][n%4];r=(price*(1-Decimal(discount)/100)).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
    add('Cálculo: descuento',f'Un pedido cuesta {fmt(price)} €. Se descuenta {discount} %. ¿Cuál es el importe final en euros?',r,[price+price*Decimal(discount)/100,price*Decimal(discount)/100,r+Decimal(10)],f'{fmt(price)} × (1 − {discount}/100) = {fmt(r)} €.')
    h=1+n%5;mins=10+n;r=h*60+mins
    add('Cálculo: tiempo',f'¿Cuántos minutos son {h} horas y {mins} minutos?',r,[h*100+mins,h+mins,r+60],f'{h} × 60 + {mins} = {r} minutos.')
