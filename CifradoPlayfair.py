#Abad Gonzalez Pablo
#Herrera Rojas Ximena
#Lozano Bustamante Miguel Alejandro
#Ramos Cabrera Paul Manuel

def preparar_mensaje_sustituyendo(texto):
    texto = "".join(filter(str.isalpha, texto.upper())).replace("J", "I")
    
    pares = []
    i = 0
    while i < len(texto):
        a = texto[i]
        
        if i + 1 == len(texto):
            pares.append(a + "X")
            i += 2
        else:
            b = texto[i+1]
            if a == b:
                pares.append(a + "X")
            else:
                pares.append(a + b)
            i += 2
            
    return pares

def generar_matriz_5x5(llave):
    llave = llave.upper().replace("J", "I")
    alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    caracteres = []
    for char in (llave + alfabeto):
        if char not in caracteres and char.isalpha():
            caracteres.append(char)
    
    return [caracteres[i:i+5] for i in range(0, 25, 5)]

def buscar_coords(matriz, letra):
    for r in range(5):
        for c in range(5):
            if matriz[r][c] == letra:
                return r, c
    return None

def cifrar_descifrar(pares, matriz, modo="encriptar"):
    salto = 1 if modo == "encriptar" else -1
    resultado = ""
    
    for par in pares:
        r1, c1 = buscar_coords(matriz, par[0])
        r2, c2 = buscar_coords(matriz, par[1])
        
        if r1 == r2: 
            resultado += matriz[r1][(c1 + salto) % 5]
            resultado += matriz[r2][(c2 + salto) % 5]
        elif c1 == c2: 
            resultado += matriz[(r1 + salto) % 5][c1]
            resultado += matriz[(r2 + salto) % 5][c2]
        else: 
            resultado += matriz[r1][c2]
            resultado += matriz[r2][c1]
            
    return resultado

mensaje = input("Introduce el mensaje: ")
llave = input("Introduce la llave: ")

pares = preparar_mensaje_sustituyendo(mensaje)
print(f"\nPares generados. Repetidas se sustituyen por x: {pares}")

matriz = generar_matriz_5x5(llave)
print("\nMatriz:")
for fila in matriz:
    print(fila)

texto_cifrado = cifrar_descifrar(pares, matriz, "encriptar")
print(f"\nMensaje Cifrado: {texto_cifrado}")

pares_cifrados = [texto_cifrado[i:i+2] for i in range(0, len(texto_cifrado), 2)]
texto_descifrado = cifrar_descifrar(pares_cifrados, matriz, "descifrar")
print(f"Mensaje Descifrado: {texto_descifrado}")