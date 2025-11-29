import sys
from solucion import reloj_de_arena

def main():
    # Leemos toda la entrada estándar y separamos por líneas
    # Esto es más robusto que input() para validar la cantidad de líneas recibidas
    entrada = sys.stdin.read().splitlines()

    # 1. Validar cantidad de líneas
    if len(entrada) < 2:
        print("Error: Se esperan 2 lineas de entrada (altura, caracter)")
        return

    linea_altura = entrada[0]
    linea_caracter = entrada[1]

    # 2. Validar que la altura sea un entero
    try:
        m = int(linea_altura)
    except ValueError:
        print("Error: La altura debe ser un numero entero")
        return

    # 3. Validar que el caracter no sea vacío
    if len(linea_caracter) == 0:
        print("Error: El caracter no puede ser vacío")
        return
    
    # Tomamos solo el primer caracter de la cadena ingresada
    s = linea_caracter[0]

    # Llamamos a la lógica principal
    # Nota: La validación de m > 0 se hace dentro de esta función según instrucciones
    reloj_de_arena(m, s)

if __name__ == "__main__":
    main()
