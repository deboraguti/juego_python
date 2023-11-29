import random


def inicio():
    print('Comienza el juego del ahorcado')

def intentos():
    try:
        numero = int(input('Introduce un número de intentos (del 1 al 10): '))
        while numero < 1 or numero > 10:
            print('Debe ser un entero entre 1 y 10')
            numero = int(input('Introduce un número de intentos (del 1 al 10): '))
        return numero
    except: 
       print('Había que introducir un número. Vuelve a ejecutar.')

def iniciar_juego(diccionario):
    palabra = random.choice(diccionario).lower() #para que esté en minúscula siempre
    tablero = ['_'] * len(palabra)
    return tablero, palabra, []


def mostrar_tablero(tablero, letras_erroneas):
    for casilla in tablero:
        print(casilla, end=' ')
    print()
    print()
    if len(letras_erroneas) > 0:
        print('Letras erróneas:', *letras_erroneas)
        print()


def pedir_letra():
    letras_posibles= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letra = input('Introduce una letra (a-z): ').lower()
    letras_no_coincidentes = []
    for i in letras_posibles:
        if letra != i :
            letras_no_coincidentes.append(i)
    if len(letras_posibles) == len(letras_no_coincidentes):  #sucede cuando 'letra' no está en la lista  
        print('La letra tiene que estar entre a y z. Pierdes una oportunidad.')
        
    return letra


def procesar_letra(letra, palabra, tablero, letras_erroneas):
    if letra in palabra:
        print('Has acertado una letra.')
        actualizar_tablero(letra, palabra, tablero)
    else:
        print('Has fallado.')
        letras_erroneas.append(letra)


def actualizar_tablero(letra, palabra, tablero):
    for j, letra_palabra in enumerate(palabra):
        if letra == letra_palabra:
            tablero[j] = letra


def comprobar_palabra(tablero):
    return '_' not in tablero


#El propio juego:
def jugar(diccionario): 

    tablero, palabra, letras_erroneas = iniciar_juego(diccionario)  
    num_intentos = intentos()  #Se elige el número de intentos
    while len(letras_erroneas) < num_intentos:  
        mostrar_tablero(tablero, letras_erroneas)  
        letra = pedir_letra() 
        procesar_letra(letra, palabra, tablero, letras_erroneas)  
        if comprobar_palabra(tablero):  
            print('¡Enhorabuena, lo has logrado!')
            break
    else:
        print(f'¡Has perdido! La palabra a adivinar era {palabra}.')
       

    mostrar_tablero(tablero, letras_erroneas)
    
    
if __name__ == '__main__':

    diccionario = ['elefante', 'ordenador', 'universo', 'guitarra', 'playa', 'espejo', 'programacion', 'montaña', 'aventura', 'fruta']
    inicio()
    jugar(diccionario)
