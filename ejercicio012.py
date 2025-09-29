'''Calcula la media aritmética de 4, 10, 6.'''
a=4
b=10
c=6
resultado=(4+10+6)/3
print(f"La media de {a}, {b} y de {c} es: {round(resultado, 2)}")

'''Otra manera'''
suma=[4, 10, 6]
media=sum(suma)/len(suma)
print(f"La media de:{suma} es:{round(media, 2)}")