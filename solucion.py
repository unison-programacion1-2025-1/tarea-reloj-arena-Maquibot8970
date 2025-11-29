def reloj_de_arena(m, s):
    """
    Imprime un reloj de arena centrado de altura m usando el caracter s.
    """
    # Validación de lógica de negocio (altura positiva)
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return

    # 1. Triángulo decreciente (Parte superior)
    # Va desde i = 0 hasta m-1
    for i in range(m):
        # Espacios: i
        # Caracteres: 2 * (m - i) - 1
        espacios = " " * i
        caracteres = s * (2 * (m - i) - 1)
        print(f"{espacios}{caracteres}")

    # 2. Triángulo creciente (Parte inferior)
    # Debe tener m-1 líneas.
    # La lógica inversa de la parte superior, excluyendo la punta (i = m-1).
    # Vamos desde m-2 hasta 0.
    for i in range(m - 2, -1, -1):
        # Espacios: i
        # Caracteres: 2 * (m - i) - 1
        espacios = " " * i
        caracteres = s * (2 * (m - i) - 1)
        print(f"{espacios}{caracteres}")
