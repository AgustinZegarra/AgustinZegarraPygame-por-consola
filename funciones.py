import random
from preguntas_original import *

#TABLERO
tablero_juego_de_la_vida = [
    {"casillero": "PARTIDA", "puntos": 0},
    {"casillero": "TRIVIA", "puntos": 0},
    {"casillero": "Dia de cobro", "puntos": +3000},
    {"casillero": "Tiene un hijo", "puntos": -3000},
    {"casillero": "Compra un auto", "puntos": -3000},
    {"casillero": "TRIVIA", "puntos": 0},
    {"casillero": "Gana la loteria", "puntos": +3000},
    {"casillero": "Compra una casa", "puntos": -3000},
    {"casillero": "Mala inversion", "puntos": -3000},
    {"casillero": "TRIVIA", "puntos": 0},
    {"casillero": "Dia de cobro", "puntos": +3000},
    {"casillero": "Tiene un hijo", "puntos": -3000},
    {"casillero": "TRIVIA", "puntos": 0},
    {"casillero": "Buena inversion", "puntos": +3000},
    {"casillero": "TRIVIA", "puntos": 0},
    {"casillero": "Vende el auto", "puntos": +3000},
    {"casillero": "Fin", "puntos": 0},
]

#MENU PRINCIPAL

def pausar():
    print(input("Presione ENTER para continuar........"))

def printear_menu():

    print(f"-----MENU PRINCIPAL-----")
    print("1- Jugar\n" \
    "2- Tabla de puntajes\n" \
    "3- Salir")

def verificar_menu(pregunta_menu):

    while pregunta_menu != "1" and pregunta_menu != "2" and pregunta_menu != "3":
        pregunta_menu = input("Eliga una opcion valida(1,2,3): ")

    return pregunta_menu

def iniciar_menu_principal():

    printear_menu()
    pregunta_menu = input("Eliga una opcion(1,2,3): ")
    pregunta_menu = verificar_menu(pregunta_menu)
    return pregunta_menu

#OPCION 1 JUEGO DE LA VIDA

def iniciar_juego_de_la_vida():

    tablero = tablero_juego_de_la_vida
    jugador = iniciar_jugador(tablero)
    preguntas = preguntas_original.copy()

    bandera = True
    while bandera:
        bandera = procesar_turno(jugador, tablero, preguntas)

    print(f"Partida finalizada, Puntaje de {jugador["nombre"]} guardado en la tabla de puntos")
    print(f"Terminaste con un total de: ${jugador["puntos"]}\n")
    guardar_puntaje(jugador["nombre"], jugador["puntos"])

def iniciar_jugador(tablero:list):
    nombre = input("Ingrese su nombre: ")
    verificar_nombre(nombre)

    posicion = 0
    puntos = 15000
    print(f"\n¡Bienvenido {nombre}!")
    print(f"Estás en la casilla: {tablero[posicion]["casillero"]}")
    print(f"Comenzás con ${puntos}\n")

    jugador = {
        "nombre": nombre,
        "posicion": posicion,
        "puntos": puntos
    }
    
    return jugador

def verificar_nombre (nombre):

    while len(nombre) == 0:
        nombre = input("Error. debe ingrese su nombre: ")


def procesar_turno(jugador, tablero, preguntas:list):

    bandera = True
    mover_jugador(jugador)
    if jugador["posicion"] >= len(tablero)- 1:
        print("\n¡LLEGASTE AL FINAL DEL TABLERO!\n")
        bandera = False

    if bandera:
        casillero = obtener_casillero(tablero, jugador)
        if casillero["casillero"] == "TRIVIA":
            jugador["puntos"] += hacer_trivia(preguntas)
    
        jugador["puntos"] = aplicar_casillero(jugador["puntos"], casillero)
        print(f"sus puntos son ${jugador["puntos"]}")

    return bandera

def mover_jugador(jugador):

    tirada = tirar_dados()
    jugador["posicion"] += tirada
    print(f"Su nueva posición es ----> {jugador["posicion"]}")

def tirar_dados():
    print(input("......Presione ENTER para tirar el dado......"))
    tirada = random.randint(1,6)
    print(f"Usted ha tirado el dado, saco el numero {tirada}")
    return tirada

def obtener_casillero(tablero, jugador):
    casillero = tablero[jugador["posicion"]]
    print(f"Caiste en la casilla ----> {tablero[jugador["posicion"]]["casillero"]}")

    return casillero


def hacer_trivia(preguntas:list):

    pregunta_seleccionada = random.choice(preguntas)

    print("\n------ TRIVIA ------\n")
    print(pregunta_seleccionada["pregunta"])
    print(f"A){pregunta_seleccionada["respuesta_a"]}\n"
          f"B){pregunta_seleccionada["respuesta_b"]}\n"
          f"C){pregunta_seleccionada["respuesta_c"]}\n")
    
    respuesta = validar_respuesta_trivia()
    
    puntos_trivia = verificaion_puntos_trivia(respuesta, pregunta_seleccionada)

    preguntas.remove(pregunta_seleccionada)

    return puntos_trivia

def validar_respuesta_trivia():

    respuesta = input("Ingrese su respuesta (a/b/c): ")

    if verificar_mayuscula(respuesta):
        respuesta = cambiar_letra_minus_mayus(respuesta, booleano= False)

    while respuesta != "a" and respuesta != "b" and respuesta != "c":
        respuesta = input("error. Ingrese una respuesta valida (a/b/c)")

        if verificar_mayuscula(respuesta):
            respuesta = cambiar_letra_minus_mayus(respuesta, booleano= False)

    return respuesta

def verificaion_puntos_trivia(respuesta:str, pregunta_seleccionada:dict):
    if respuesta == pregunta_seleccionada["respuesta_correcta"]:
        puntos_trivia = 3000
        print(f"Respuesta correcta usted gana ${puntos_trivia}")
    else:
        puntos_trivia = -3000
        print(f"Respuesta incorrecta usted pierde ${puntos_trivia}")
    
    return puntos_trivia

def aplicar_casillero(puntos:int, evento:dict):

    cambio_puntos = evento["puntos"]
    if cambio_puntos > 0:
        print(f"¡Ganaste ${cambio_puntos} por caer en la casilla {evento["casillero"]}!")
    elif cambio_puntos < 0:
        print(f"Perdiste ${cambio_puntos} por caer en la casilla {evento["casillero"]}")


    puntos_nuevos = puntos + evento["puntos"]
    return puntos_nuevos

#PASAR A MINUSCULA

def verificar_mayuscula(letra:str):
    """Verifica si un caracter es mayuscula.
    Recibe un caracter.
    Devuelve True si es mayuscula, False si no lo es o le pasaron algo mas largo que un solo caracter.
    """
    mayuscula = False
    if len(letra) == 1:
        if (ord(letra) >= 65 and ord(letra) <= 90) or ord(letra) == 165 or ord(letra) == 209:
            mayuscula = True
    return mayuscula

def cambiar_letra_minus_mayus(letra:str, booleano:bool = True) -> str:
    """Cambia una letra de mayuscula a minuscula o viceversa dependiendo del booleano indicado. Si la letra ya esta en el formato indicado no realiza ningun cambio y la devuelve igual.
    Recibe una letra (string de un carácter) y un booleano (True por defecto para convertir a mayúsculas).
    Devuelve una letra convertida o el mismo valor si no es un carácter único."""
    if type(letra) == str and len(letra) == 1:
        if booleano and verificar_minuscula(letra):
            letra = chr(ord(letra) - 32) 
        elif not booleano and verificar_mayuscula(letra):
            letra = chr(ord(letra) + 32) 
    return letra

def verificar_minuscula(letra:str):
    """Verifica si un caracter es minuscula.
    Recibe un caracter.
    Devuelve True si es minusucla, False si no lo es o le pasaron algo mas largo que un solo caracter.
    """
    minuscula = False
    if len(letra) == 1:
        if (ord(letra) >= 97 and ord(letra) <= 122) or ord(letra) == 164 or ord(letra) == 241:
            minuscula = True
    return minuscula

#GUARDAR PUNTAJE 

def guardar_puntaje (nombre:str, puntos:int, archivo:str = "Tabla de puntajes.csv"):

    with open(archivo, "a") as archivo:
        archivo.write(f"{nombre} ----> {puntos}\n")
        archivo.close()
    
def mostrar_puntaje(archivo:str = "Tabla de puntajes.csv"):

    with open(archivo, "r") as archivo:
        for i in archivo:
            print(i)
    
