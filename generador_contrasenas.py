import random
import string

def generar_contrasena(longitud=12, mayusculas=True, numeros=True, simbolos=True):
    caracteres = string.ascii_lowercase
    if mayusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    # Generar contraseña aleatoria
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

if __name__ == "__main__":
    print("🔐 Generador de Contraseñas Seguras")
    longitud = int(input("Introduce la longitud de la contraseña: "))
    incluir_mayus = input("¿Incluir mayúsculas? (s/n): ").lower() == "s"
    incluir_num = input("¿Incluir números? (s/n): ").lower() == "s"
    incluir_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == "s"

    password = generar_contrasena(longitud, incluir_mayus, incluir_num, incluir_simbolos)
    print(f"\n✅ Tu contraseña generada es: {password}")

    '''Un ejercicio sencillo de hacer'''
