from funciones import *

bandera = True

while bandera:

    respuesta_menu = iniciar_menu_principal()
        
    if respuesta_menu == "1":
        iniciar_juego_de_la_vida()

    elif respuesta_menu == "2":
        mostrar_puntaje()

    else: 
        bandera = False
        despedida()

    if respuesta_menu != "3":
        pausar()

#try except