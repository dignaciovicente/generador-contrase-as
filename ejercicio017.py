'''Reemplaza "verde" por "azul" en "casa verde".'''
palabra="casa verde"
resultado="casa azul"
print(f" en la 'casa verde' la sustituimos por: {resultado}")

'''Otra menera y mejor'''
palabra1="casa verde"
resultado=palabra.replace("verde", "azul")
print(f"En la 'casa verde' sustituimos 'verde' por 'azul': {resultado}")