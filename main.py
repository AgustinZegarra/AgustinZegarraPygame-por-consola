from funciones import *

bandera = True

while bandera:

    respuesta_menu = iniciar_menu_principal()
        
    if respuesta_menu == "1":
        iniciar_juego_de_la_vida()
        pausar()

    elif respuesta_menu == "2":
        mostrar_puntaje()
        pausar()

    else: 
        bandera = False