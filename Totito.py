#mini proyecto 2 TOTITO


# matriz para el tablero
tablero= [["          |         |          "],\
          ["          |         |          "],\
          ["          |         |          "],\
          ["----------|---------|----------"],\
          ["          |         |          "],\
          ["          |         |          "],\
          ["          |         |          "],\
          ["----------|---------|----------"],\
          ["          |         |          "],\
          ["          |         |          "],\
          ["          |         |          "],\
          ["          |         |          "],\
 ]

import random
from random import choice

# menu
print("")
print("-------------------------------------------------------------------------------------------------------")
print("")
print("")
print("                                Bienvenido al juego de  - T O T I T O -                                ")
print("")
print("")

print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
print("")
print("")
print("                              (1) --> F A S E 1:     Jugador vs Jugador                                ")
print("")
print("                              (2) --> F A S E 2:   Jugador vs Computadora                              ")
print("")
print("                              (3) --> F A S E 3:     - PLAY TO LOOSE -                                 ")
print("")
print("")
print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
print("")
opt = input("                 Presiona el número correspondiente a la fase en la que deseas jugar: ")


#------------------------------------------------------------------------------------------------------------------
# funcion para imprimir las instruciiones Instrucciones
def ImprimirInstrucciones():
    print("/////////    INSTRUCCIONES:    /////////////////////////////////////////////////////////////////////////")
    print("")
    print("")
    print("* Cuando sea tu turno presiona la letra correspondiente a la posición en la que deseas poner tu dibujo *")  
    print("")
    print("                                               |     |     ")
    print("                                            Q  |  W  |  E  ")
    print("                                          -----|-----|-----")
    print("                                            A  |  S  |  D  ")
    print("                                          -----|-----|-----")
    print("                                            Z  |  X  |  C  ")
    print("                                               |     |     ")
    print("")
    print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
    return()
#------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# función para imprimir el tablero (opcion 1)
def ImprimirTablero():
   for i in range(len(tablero)):
       print(*tablero[i])
   print("")
   print("")
   return()
#----------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# función para imprimir el tablero (opcion 2)
tablero2 = ["         ", "         ", "         ",
            "         ", "         ", "         ",
            "         ", "         ", "         "]

def ImprimirTablero2():
    print("          |           |          ")
    print(tablero2[0], "|", tablero2[1], "|", tablero2[2], "")   
    print("          |           |          ")
    print("----------|-----------|----------")
    print("          |           |          ")
    print(tablero2[3], "|", tablero2[4], "|", tablero2[5], "")
    print("          |           |          ")
    print("----------|-----------|----------")
    print("          |           |          ")
    print(tablero2[6], "|", tablero2[7], "|", tablero2[8], "")
    print("          |           |          ")
    print("          |           |          ")
    print("")
    print("")
    
    return()
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# función para turno 1
TraducirPosicion = {"q":1, "w":2, "e":3, "a":4, "s":5, "d":6, "z":7, "x":8, "c": 9}
def turno1():
    posicion = input("¿Qué posición quieres?: ")
    print("")

    # cambiar el valor del indice por el dibujo
    posicion = TraducirPosicion[posicion]
    posicion = int(posicion) - 1
    tablero2[posicion] = "    x    "
    ImprimirTablero2()
    return()
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# función para turno 2
TraducirPosicion = {"q":1, "w":2, "e":3, "a":4, "s":5, "d":6, "z":7, "x":8, "c": 9}
def turno2():
    posicion = input("¿Qué posición quieres?: ").lower()
    print("")

    # cambiar el valor del indice por el dibujo
    posicion = TraducirPosicion[posicion]
    posicion = int(posicion) - 1
    tablero2[posicion] = "    o    "
    ImprimirTablero2()
    return()
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# función para turno compu
#TraducirPosicion = {"q":1, "w":2, "e":3, "a":4, "s":5, "d":6, "z":7, "x":8, "c": 9}
#claves = TraducirPosicion.keys()
posicionesTab = ["q", "w", "e", "a", "s", "d", "z", "x", "c"]
def turnocompu():
    #posicion = input("¿Qué posición quieres?: ", random.choice(claves))
    posicion = (random.choice(posicionesTab))
    print("¿Qué posición quieres?: ", posicion)
    print("")

    # cambiar el valor del indice por el dibujo
    posicion = TraducirPosicion[posicion]
    posicion = int(posicion) - 1
    tablero2[posicion] = "    o    "
    ImprimirTablero2()
    return()
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# función para comprobar si las FILAS son iguales
def CompararFilas():
    fila1 = tablero2[0] == tablero2[1] == tablero2[2] != "         "
    fila2 = tablero2[3] == tablero2[4] == tablero2[5] != "         "
    fila3 = tablero2[6] == tablero2[7] == tablero2[8] != "         "

    if fila1 or fila2 or fila3:
        return(False)

    return(True)
   

    return()
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# función para comprobar si las COLUMNAS son iguales
def CompararColumnas():
    columna1 = tablero2[0] == tablero2[3] == tablero2[6] != "         "
    columna2 = tablero2[1] == tablero2[4] == tablero2[7] != "         "
    columna3 = tablero2[2] == tablero2[5] == tablero2[8] != "         "

    if columna1 or columna2 or columna3:
        return(False)
    
    return(True)

  

    return()
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# función para comprobar si las DIAGONALES son iguales
def CompararDiagonales():
    diag1 = tablero2[0] == tablero2[4] == tablero2[8] != "         "
    diag2 = tablero2[6] == tablero2[4] == tablero2[2] != "         "

    if diag1 or diag2:
        return(False)

    return(True)
   

    return()
#----------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------
# función para escoger un nombre a la computadora
#NombresCompu = ["Saku", "Manzi", "Hibiki", "Eiki", "Kiyuki", "Hono-hono", "Chizu", "Genki", "Itsuki", "Mitsu", "Haruka"]
#def nombres():
 #   computadora = (random.choice(NombresCompu))
  #  print("Tu oponente es: ", computadora)

   # return()
#--------------------------------------------------------------------------------------------------------------------------




# ----------------------------------------------- (fase 1) -----------------------------------------------
if opt == ("1"):
    print("")
    print("")
    print("")
    print("-------------------------------------------------------------------------------------------------------")
    print("")
    print("                                           | F A S E  1 |                                              ")
    print("")
    print("")
    print("")

    # imprimir instrucciones:
    ImprimirInstrucciones()
    print("")

    # variable que guarda el nombre del jugador 1
    jugador1 = input("JUGADOR 1: ")
    print("")

    # variable que guarda el nombre del jugador 2
    jugador2 = (input("JUGADOR 2: "))
    print("")
    print("                                      -  ", jugador1, "  vs  ", jugador2, "  -                      ")
    print("")
    print("")

    # imprimir tablero
    #ImprimirTablero2()

    #print("Es turno de: ", random.choice([jugador1, jugador2]), " ( x ) ")
    #print("")


    SeguirJuego = True

    alternador = random.randint(0,1)

# while para cambiar de turno
    while SeguirJuego:
        if alternador == 1:
            print("Es turno de: ", jugador1, " ( x ) ")
            print("")
            turno1()
            alternador = 0

        
        elif alternador == 0:
            print("Es turno de: ", jugador2, " ( o ) ")
            print("")
            turno2()
            alternador = 1

        SeguirJuego = CompararColumnas() and CompararFilas() and CompararDiagonales()



    if alternador == 0:
        print("--------------------------------->   ¡ G A N A S T E ", jugador1, "!")
        print("")
        print("")
    
    elif alternador == 1:
        print("--------------------------------->   ¡ G A N A S T E ", jugador2, "!")
        print("")
        print("")

# --------------------------------------------------------------------------------------------------------


# ----------------------------------------------- (fase 2) -----------------------------------------------
if opt == ("2"):
    print("")
    print("")
    print("")
    print("-------------------------------------------------------------------------------------------------------")
    print("")
    print("                                           | F A S E  2 |                                              ")
    print("")
    print("")
    print("")

    # imprimir instrucciones:
    ImprimirInstrucciones()
    print("")

    # variable que guarda el nombre del jugador 1
    jugador1 = input("JUGADOR: ")
    print("")

    # escoger nombre random de la computadora
    NombresCompu = ["Saku", "Manzi", "Hibiki", "Eiki", "Kiyuki", "Hono-hono", "Chizu", "Genki", "Itsuki", "Mitsu", "Haruka"]

    computadora = (random.choice(NombresCompu))
    print("OPONENTE: ", computadora)
    print("")
    print("                                      -  ", jugador1, "  vs  ", computadora, "  -                      ")
    print("")
    print("")


    SeguirJuego = True

    alternador = random.randint(0,1)

# while para cambiar de turno
    while SeguirJuego:
        if alternador == 1:
            print("Es turno de: ", jugador1, " ( x ) ")
            print("")
            turno1()
            alternador = 0

        
        elif alternador == 0:
            print("Es turno de: ", computadora, " ( o ) ")
            print("")
            turnocompu()
            alternador = 1

        SeguirJuego = CompararColumnas() and CompararFilas() and CompararDiagonales()



    if alternador == 0:
        print("--------------------------------->   ¡ G A N A S T E ", jugador1, "!")
        print("")
        print("")
    
    elif alternador == 1:
        print("--------------------------------->   ¡ G A N A S T E ", computadora, "!")
        print("")
        print("")

#---------------------------------------------------------------------------------------------------------------------------------



# ----------------------------------------------- (fase 3) -----------------------------------------------
if opt == ("3"):
    print("")
    print("")
    print("")
    print("-------------------------------------------------------------------------------------------------------")
    print("")
    print("                                           | F A S E  3 |                                              ")
    print("")
    print("")
    print("")

    # imprimir instrucciones:
    ImprimirInstrucciones()
    print("")

    # variable que guarda el nombre del jugador 1
    jugador1 = input("JUGADOR 1: ")
    print("")

    # variable que guarda el nombre del jugador 2
    jugador2 = (input("JUGADOR 2: "))
    print("")
    print("                                      -  ", jugador1, "  vs  ", jugador2, "  -                      ")
    print("")
    print("")


    SeguirJuego = True

    alternador = random.randint(0,1)

# while para cambiar de turno
    while SeguirJuego:
        if alternador == 1:
            print("Es turno de: ", jugador1, " ( x ) ")
            print("")
            turno1()
            alternador = 0

        
        elif alternador == 0:
            print("Es turno de: ", jugador2, " ( o ) ")
            print("")
            turno2()
            alternador = 1

        SeguirJuego = CompararColumnas() and CompararFilas() and CompararDiagonales()



    if alternador == 0:
        print("--------------------------------->   ¡ G A N A S T E ", jugador2, "!")
        print("")
        print("")
    
    elif alternador == 1:
        print("--------------------------------->   ¡ G A N A S T E ", jugador1, "!")
        print("")
        print("")

# --------------------------------------------------------------------------------------------------------