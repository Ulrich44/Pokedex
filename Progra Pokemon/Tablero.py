from tkinter import *
import pygame
import random
import time


##Ventana que da al tablero del juego
def mostrar_tablero():
    global x_poke4, y_poke4, banca_lados4, seleccion, ficha4_side, \
        ficha4_up_down, ficha4_matrizx, ficha4_matrizy, \
        matriz, x_poke5, y_poke5, banca_lados5, ficha5_side, \
        ficha5_up_down, ficha5_matrizx, ficha5_matrizy, x_poke6, y_poke6, banca_lados6, ficha6_side, \
        ficha6_up_down, ficha6_matrizx, ficha6_matrizy, x_poke1, y_poke1, banca_lados1, ficha1_side, \
        ficha1_up_down, ficha1_matrizx, ficha1_matrizy, x_poke2, y_poke2, banca_lados2, ficha2_side, \
        ficha2_up_down, ficha2_matrizx, ficha2_matrizy, x_poke3, y_poke3, banca_lados3, ficha3_side, \
        ficha3_up_down, ficha3_matrizx, ficha3_matrizy, turno, oponente, gana, ventanal, charizard, \
        blastoise, venusaur, pokebola, pikachu, raticate, pidgeot, raichu, banca_rival11, banca_rival12, \
        banca_rival13, banca_rival14, banca_rival15, banca_rival16, oponente, bloqueo, fondo_victoria
    ##  Se crea la ventana y se ajustan sus caracteristicas
    pygame.mixer.init()
    pygame.mixer.music.load("musica/Light the Fire Up in the Night.mp3")
    pygame.mixer.music.play(-1)
    ventanal = Toplevel()
    ventanal.title("Tablero")
    ventanal.update_idletasks()
    ventanal.focus_force()
    ancho = ventanal.winfo_screenwidth() - 660
    alto = ventanal.winfo_screenheight() - 720
    ventanal.geometry("%dx%d%+d%+d" % (560, 560, ancho / 2, alto / 2))
    canvas = Canvas(ventanal, width=660, height=660)
    canvas.pack()
    # Variables para ficha 1 que sirven ara restringir movimiento, conocer su posicion en matriz y demás
    x_poke1 = 160
    y_poke1 = 480
    seleccion = 0
    banca_lados1 = 0
    ficha1_side = 0
    ficha1_up_down = 0
    ficha1_matrizx = 0
    ficha1_matrizy = 2
    # Variables para ficha 2 que sirven ara restringir movimiento, conocer su posicion en matriz y demás
    x_poke2 = 240
    y_poke2 = 480
    seleccion = 0
    banca_lados2 = 0
    ficha2_side = 1
    ficha2_up_down = 0
    ficha2_matrizx = 0
    ficha2_matrizy = 3
    # Variables para ficha 3 que sirven ara restringir movimiento, conocer su posicion en matriz y demás
    x_poke3 = 320
    y_poke3 = 480
    seleccion = 0
    banca_lados3 = 0
    ficha3_side = 2
    ficha3_up_down = 0
    ficha3_matrizx = 0
    ficha3_matrizy = 4
    # Variables para ficha 4 que sirven ara restringir movimiento, conocer su posicion en matriz y demás
    x_poke4 = 160
    y_poke4 = 0
    seleccion = 0
    banca_lados4 = 0
    ficha4_side = 0
    ficha4_up_down = 0
    ficha4_matrizx = -1
    ficha4_matrizy = 2
    # Variables para ficha 5 que sirven ara restringir movimiento, conocer su posicion en matriz y demás
    x_poke5 = 240
    y_poke5 = 0
    banca_lados5 = 0
    ficha5_side = 1
    ficha5_up_down = 0
    ficha5_matrizx = -1
    ficha5_matrizy = 3
    # Variables para ficha 6 que sirven ara restringir movimiento, conocer su posicion en matriz y demás
    x_poke6 = 320
    y_poke6 = 0
    banca_lados6 = 0
    ficha6_side = 2
    ficha6_up_down = 0
    ficha6_matrizx = -1
    ficha6_matrizy = 4

    ##Variable que dice de cuál jugador es el turno
    turno = 1
    ##Variable que sirve para identificar quién es e rival
    oponente = 0
    ##Repara un error al encontrar duelo
    bloqueo = 0

    ##Se crea la matriz que controla los espacios en el tablero
    matriz = [
        [0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 0, 0, 0, 0]

    ]
    ##Se cargan las imagenes que seran utilizadas
    venusaur = PhotoImage(file="imagenes/fichas/venusaur.gif")
    blastoise = PhotoImage(file="imagenes/fichas/blastoise.gif")
    charizard = PhotoImage(file="imagenes/fichas/charizard.gif")
    pikachu = PhotoImage(file="imagenes/fichas/pikachu.gif")
    raticate = PhotoImage(file="imagenes/fichas/raticate.gif")
    pokebola = PhotoImage(file="imagenes/tablero/pokebola.gif")
    masterball = PhotoImage(file="imagenes/tablero/masterball.gif")
    pidgeot = PhotoImage(file="imagenes/fichas/pidgeot.gif")
    raichu = PhotoImage(file="imagenes/fichas/pidgeot.gif")
    fondo_victoria = PhotoImage(file="imagenes/fondo_victoria/pokemon.gif")

    ##Funciones con una variable que sirve para saber cual ficha se selecciona
    def banca_rival11():
        global seleccion, oponente
        seleccion = 1

    def banca_rival12():
        global seleccion, oponente
        seleccion = 2

    def banca_rival13():
        global seleccion, oponente
        seleccion = 3

    def banca_rival14():
        global seleccion, oponente
        seleccion = 4

    def banca_rival15():
        global seleccion, oponente
        seleccion = 5

    def banca_rival16():
        global seleccion, oponente
        seleccion = 6

    # Botones creados en la banca
    banca_rival3 = Button(ventanal, image=charizard, command=banca_rival14, width=80, height=80).place(x=160, y=0)
    banca_rival4 = Button(ventanal, image=blastoise, command=banca_rival15, width=80, height=80).place(x=240, y=0)
    banca_rival5 = Button(ventanal, image=venusaur, command=banca_rival16, width=80, height=80).place(x=320, y=0)
    # Botones de la primera fila
    board_11 = Button(ventanal, image=pokebola, width=80, height=80).place(x=0, y=80)
    board_12 = Button(ventanal, image=pokebola, width=80, height=80).place(x=80, y=80)
    board_13 = Button(ventanal, image=pokebola, width=80, height=80).place(x=160, y=80)
    board_14 = Button(ventanal, image=pokebola, width=80, height=80).place(x=240, y=80)
    board_15 = Button(ventanal, image=pokebola, width=80, height=80).place(x=320, y=80)
    board_16 = Button(ventanal, image=pokebola, width=80, height=80).place(x=400, y=80)
    board_17 = Button(ventanal, image=pokebola, width=80, height=80).place(x=480, y=80)
    # Botones de la segunda fila
    board_21 = Button(ventanal, image=pokebola, width=80, height=80).place(x=0, y=160)
    board_22 = Button(ventanal, image=pokebola, width=80, height=80).place(x=80, y=160)
    board_23 = Button(ventanal, image=pokebola, width=80, height=80).place(x=160, y=160)
    board_24 = Button(ventanal, image=pokebola, width=80, height=80).place(x=240, y=160)
    board_25 = Button(ventanal, image=pokebola, width=80, height=80).place(x=320, y=160)
    board_26 = Button(ventanal, image=pokebola, width=80, height=80).place(x=400, y=160)
    board_27 = Button(ventanal, image=pokebola, width=80, height=80).place(x=480, y=160)
    # Botones de la tercera fila
    board_31 = Button(ventanal, image=pokebola, width=80, height=80).place(x=0, y=240)
    board_32 = Button(ventanal, image=pokebola, width=80, height=80).place(x=80, y=240)
    board_33 = Button(ventanal, image=pokebola, width=80, height=80).place(x=160, y=240)
    board_34 = Button(ventanal, image=pokebola, width=80, height=80).place(x=240, y=240)
    board_35 = Button(ventanal, image=pokebola, width=80, height=80).place(x=320, y=240)
    board_36 = Button(ventanal, image=pokebola, width=80, height=80).place(x=400, y=240)
    board_37 = Button(ventanal, image=pokebola, width=80, height=80).place(x=480, y=240)
    # Botones de la cuarta fila
    board_41 = Button(ventanal, image=pokebola, width=80, height=80).place(x=0, y=320)
    board_42 = Button(ventanal, image=pokebola, width=80, height=80).place(x=80, y=320)
    board_43 = Button(ventanal, image=pokebola, width=80, height=80).place(x=160, y=320)
    board_44 = Button(ventanal, image=pokebola, width=80, height=80).place(x=240, y=320)
    board_45 = Button(ventanal, image=pokebola, width=80, height=80).place(x=320, y=320)
    board_46 = Button(ventanal, image=pokebola, width=80, height=80).place(x=400, y=320)
    board_47 = Button(ventanal, image=pokebola, width=80, height=80).place(x=480, y=320)
    # Botones de la quinta fila
    board_51 = Button(ventanal, image=pokebola, width=80, height=80).place(x=0, y=400)
    board_52 = Button(ventanal, image=pokebola, width=80, height=80).place(x=80, y=400)
    board_53 = Button(ventanal, image=pokebola, width=80, height=80).place(x=160, y=400)
    board_54 = Button(ventanal, image=pokebola, width=80, height=80).place(x=240, y=400)
    board_55 = Button(ventanal, image=pokebola, width=80, height=80).place(x=320, y=400)
    board_56 = Button(ventanal, image=pokebola, width=80, height=80).place(x=400, y=400)
    board_57 = Button(ventanal, image=pokebola, width=80, height=80).place(x=480, y=400)
    # Banca jugador
    banca_rival63 = Button(ventanal, image=pikachu, command=banca_rival11, width=80, height=80).place(x=160,
                                                                                                      y=480)
    banca_rival64 = Button(ventanal, image=raticate, command=banca_rival12, width=80, height=80).place(x=240,
                                                                                                       y=480)
    banca_rival65 = Button(ventanal, image=pidgeot, command=banca_rival13, width=80, height=80).place(x=320,
                                                                                                      y=480)

    ##Funcion para el movimiento de las fichas
    def mov_rival1(evento):
        global seleccion, x_poke4, y_poke4, ventana, banca_lados4, \
            ficha4_side, ficha4_up_down, ficha4_matrizx, ficha4_matrizy, \
            matriz, x_poke5, y_poke5, banca_lados5, ficha5_side, \
            ficha5_up_down, ficha5_matrizx, ficha5_matrizy, x_poke6, y_poke6, banca_lados6, ficha6_side, \
            ficha6_up_down, ficha6_matrizx, ficha6_matrizy, x_poke1, y_poke1, banca_lados1, ficha1_side, \
            ficha1_up_down, ficha1_matrizx, ficha1_matrizy, x_poke2, y_poke2, banca_lados2, ficha2_side, \
            ficha2_up_down, ficha2_matrizx, ficha2_matrizy, x_poke3, y_poke3, banca_lados3, ficha3_side, \
            ficha3_up_down, ficha3_matrizx, ficha3_matrizy, turno, oponente, bloqueo
        # movimiento ficha 1
        if evento.keysym == "Down" and seleccion == 1 and bloqueo > 1:
            if ficha1_up_down > 1 and matriz[ficha1_matrizx + 1][ficha1_matrizy] == 0 and turno == 1:
                Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke1, y=y_poke1)
                turno = 2
                x_poke1 += 0
                y_poke1 += 80
                seleccion = 0
                banca_lados1 += 1
                ficha1_up_down -= 1
                matriz[ficha1_matrizx][ficha1_matrizy] = 0
                ficha1_matrizy += 0
                ficha1_matrizx += 1
                bloqueo -= 1
                matriz[ficha1_matrizx][ficha1_matrizy] = 1
                Button(ventanal, image=pikachu, command=banca_rival11, width=80, height=80).place(x=x_poke1, y=y_poke1)
                return verificar_ganador()
            elif bloqueo > 2 and ficha1_up_down > 2 and matriz[ficha1_matrizx + 1][ficha1_matrizy] == 4 or \
                            matriz[ficha1_matrizx + 1][
                                ficha1_matrizy] == 5 or matriz[ficha1_matrizx + 1][ficha1_matrizy] == 6:
                turno = 2
                oponente = int(matriz[ficha1_matrizx + 1][ficha1_matrizy])
                return duelo()
        if evento.keysym == "Up" and seleccion == 1 and ficha1_up_down < 5:
            if ficha1_matrizx != 0:
                matriz[ficha1_matrizx][ficha1_matrizy] = 0
            if ficha1_up_down < 5 and matriz[ficha1_matrizx - 1][ficha1_matrizy] == 0 and turno == 1:
                Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke1, y=y_poke1)
                turno = 2
                x_poke1 += 0
                y_poke1 -= 80
                seleccion = 0
                banca_lados1 += 1
                ficha1_up_down += 1
                ficha1_matrizx -= 1
                ficha1_matrizy += 0
                matriz[ficha1_matrizx][ficha1_matrizy] = 1
                bloqueo += 1
                Button(ventanal, image=pikachu, command=banca_rival11, width=80, height=80).place(x=x_poke1, y=y_poke1)
                return verificar_ganador()
            elif bloqueo > 2 and matriz[ficha1_matrizx - 1][ficha1_matrizy] == 5 or matriz[ficha1_matrizx - 1][
                ficha1_matrizy] == 6 or \
                            matriz[ficha1_matrizx - 1][ficha1_matrizy] == 4:
                turno = 2
                oponente = int(matriz[ficha1_matrizx - 1][ficha1_matrizy])
                return duelo()
        if evento.keysym == "Left" and seleccion == 1 and banca_lados1 > 0 and -2 < ficha1_side <= 4 \
                and matriz[ficha1_matrizx][ficha1_matrizy - 1] == 0 and turno == 1:
            Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke1, y=y_poke1)
            turno = 2
            x_poke1 -= 80
            y_poke1 += 0
            seleccion = 0
            ficha1_side -= 1
            matriz[ficha1_matrizx][ficha1_matrizy] = 0
            ficha1_matrizy -= 1
            ficha1_matrizx += 0
            matriz[ficha1_matrizx][ficha1_matrizy] = 1
            Button(ventanal, image=pikachu, command=banca_rival11, width=80, height=80).place(x=x_poke1, y=y_poke1)
            return verificar_ganador()
        if evento.keysym == "Right" and seleccion == 1 and banca_lados1 > 0 and -2 <= ficha1_side < 4 \
                and matriz[ficha1_matrizx][ficha1_matrizy + 1] == 0 and turno == 1:
            Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke1, y=y_poke1)
            turno = 2
            x_poke1 += 80
            y_poke1 += 0
            seleccion = 0
            ficha1_side += 1
            matriz[ficha1_matrizx][ficha1_matrizy] = 0
            ficha1_matrizy += 1
            ficha1_matrizx += 0
            matriz[ficha1_matrizx][ficha1_matrizy] = 1
            Button(ventanal, image=pikachu, command=banca_rival11, width=80, height=80).place(x=x_poke1, y=y_poke1)
            return verificar_ganador()
        # movimiento ficha 2
        if evento.keysym == "Down" and seleccion == 2 and bloqueo > 1:
            if ficha2_up_down > 1 and matriz[ficha2_matrizx + 1][ficha2_matrizy] == 0 and turno == 1:
                Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke2, y=y_poke2)
                turno = 2
                x_poke2 += 0
                y_poke2 += 80
                seleccion = 0
                bloqueo -= 1
                banca_lados2 += 1
                ficha1_up_down += 1
                matriz[ficha2_matrizx][ficha2_matrizy] = 0
                ficha2_matrizy += 0
                ficha2_matrizx += 1
                matriz[ficha2_matrizx][ficha2_matrizy] = 2
                Button(ventanal, image=raticate, command=banca_rival12, width=80, height=80).place(x=x_poke2, y=y_poke2)
                return verificar_ganador()
            elif bloqueo > 2 and ficha2_up_down > 2 and matriz[ficha2_matrizx + 1][ficha2_matrizy] == 4 or \
                            matriz[ficha2_matrizx + 1][
                                ficha2_matrizy] == 5 \
                    or matriz[ficha2_matrizx + 1][ficha2_matrizy] == 6:
                turno = 2
                oponente = int(matriz[ficha2_matrizx + 1][ficha2_matrizy])
                return duelo()
        if evento.keysym == "Up" and seleccion == 2 and ficha2_up_down < 5:
            if ficha2_matrizx != 0:
                matriz[ficha2_matrizx][ficha2_matrizy] = 0
            if ficha2_up_down < 5 and matriz[ficha2_matrizx - 1][ficha2_matrizy] == 0 and turno == 1:
                Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke2, y=y_poke2)
                turno = 2
                x_poke2 += 0
                y_poke2 -= 80
                seleccion = 0
                banca_lados2 += 1
                ficha2_up_down += 1
                ficha2_matrizx -= 1
                ficha2_matrizy += 0
                matriz[ficha2_matrizx][ficha2_matrizy] = 2
                bloqueo += 1
                Button(ventanal, image=raticate, command=banca_rival12, width=80, height=80).place(x=x_poke2, y=y_poke2)
                return verificar_ganador()
            elif bloqueo > 2 and matriz[ficha2_matrizx - 1][ficha2_matrizy] == 4 or matriz[ficha2_matrizx - 1][
                ficha2_matrizy] == 5 \
                    or matriz[ficha2_matrizx - 1][ficha2_matrizy] == 6:
                turno = 2
                oponente = int(matriz[ficha2_matrizx - 1][ficha2_matrizy])
                return duelo()
        if evento.keysym == "Left" and seleccion == 2 and banca_lados2 > 0 and -2 < ficha2_side <= 4 \
                and matriz[ficha2_matrizx][ficha2_matrizy - 1] == 0 and turno == 1:
            Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke2, y=y_poke2)
            turno = 2
            x_poke2 -= 80
            y_poke2 += 0
            seleccion = 0
            ficha2_side -= 1
            matriz[ficha2_matrizx][ficha2_matrizy] = 0
            ficha2_matrizy -= 1
            ficha2_matrizx += 0
            matriz[ficha2_matrizx][ficha2_matrizy] = 2
            Button(ventanal, image=raticate, command=banca_rival12, width=80, height=80).place(x=x_poke2, y=y_poke2)
            return verificar_ganador()
        if evento.keysym == "Right" and seleccion == 2 and banca_lados2 > 0 and -2 <= ficha2_side < 4 \
                and matriz[ficha2_matrizx][ficha2_matrizy + 1] == 0 and turno == 1:
            Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke2, y=y_poke2)
            turno = 2
            x_poke2 += 80
            y_poke2 += 0
            seleccion = 0
            ficha2_side += 1
            matriz[ficha2_matrizx][ficha2_matrizy] = 0
            ficha2_matrizy += 1
            ficha2_matrizx += 0
            matriz[ficha2_matrizx][ficha2_matrizy] = 2
            Button(ventanal, image=raticate, command=banca_rival12, width=80, height=80).place(x=x_poke2, y=y_poke2)
            return verificar_ganador()
        # movimiento ficha 3
        if evento.keysym == "Down" and seleccion == 3 and bloqueo > 1:
            if ficha3_matrizx != -1:
                matriz[ficha3_matrizx][ficha3_matrizy] = 0
            if ficha3_up_down > 1 and matriz[ficha3_matrizx + 1][ficha3_matrizy] == 0 and turno == 1:
                Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke3, y=y_poke3)
                turno = 2
                x_poke3 += 0
                y_poke3 += 80
                seleccion = 0
                banca_lados3 += 1
                bloqueo -= 1
                ficha3_up_down += 1
                ficha3_matrizy += 0
                ficha3_matrizx += 1
                matriz[ficha3_matrizx][ficha3_matrizy] = 3
                Button(ventanal, image=pidgeot, command=banca_rival13, width=80, height=80).place(x=x_poke3, y=y_poke3)
                return verificar_ganador()
            elif bloqueo > 2 and ficha3_up_down > 2 and matriz[ficha3_matrizx + 1][ficha3_matrizy] == 4 or \
                            matriz[ficha3_matrizx + 1][
                                ficha3_matrizy] == 5 or matriz[ficha3_matrizx + 1][ficha3_matrizy] == 6:
                turno = 2
                oponente = int(matriz[ficha3_matrizx + 1][ficha3_matrizy])
                return duelo()
        if evento.keysym == "Up" and seleccion == 3 and ficha3_up_down < 5:
            if ficha3_matrizx != 0:
                matriz[ficha3_matrizx][ficha3_matrizy] = 0
            if ficha3_up_down < 5 and matriz[ficha3_matrizx - 1][ficha3_matrizy] == 0 and turno == 1:
                Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke3, y=y_poke3)
                turno = 2
                x_poke3 += 0
                y_poke3 -= 80
                seleccion = 0
                bloqueo += 1
                banca_lados3 += 1
                ficha3_up_down += 1
                ficha3_matrizx -= 1
                ficha3_matrizy += 0
                matriz[ficha3_matrizx][ficha3_matrizy] = 3
                Button(ventanal, image=pidgeot, command=banca_rival13, width=80, height=80).place(x=x_poke3, y=y_poke3)
                return verificar_ganador()
            elif bloqueo > 2 and matriz[ficha3_matrizx - 1][ficha3_matrizy] == 4 or matriz[ficha3_matrizx - 1][
                ficha3_matrizy] == 5 or \
                            matriz[ficha3_matrizx - 1][ficha3_matrizy] == 6:
                turno = 2
                oponente = int(matriz[ficha3_matrizx - 1][ficha3_matrizy])
                return duelo()
        if evento.keysym == "Left" and seleccion == 3 and banca_lados3 > 0 \
                and -2 < ficha3_side <= 4 and matriz[ficha3_matrizx][ficha3_matrizy - 1] == 0 and turno == 1:
            Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke3, y=y_poke3)
            turno = 2
            x_poke3 -= 80
            y_poke3 += 0
            seleccion = 0
            ficha3_side -= 1
            matriz[ficha3_matrizx][ficha3_matrizy] = 0
            ficha3_matrizy -= 1
            ficha3_matrizx += 0
            matriz[ficha3_matrizx][ficha3_matrizy] = 3
            Button(ventanal, image=pidgeot, command=banca_rival13, width=80, height=80).place(x=x_poke3, y=y_poke3)
            return verificar_ganador()
        if evento.keysym == "Right" and seleccion == 3 and banca_lados3 > 0 and -2 <= ficha3_side < 4 \
                and matriz[ficha3_matrizx][ficha3_matrizy + 1] == 0 and turno == 1:
            Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke3, y=y_poke3)
            turno = 2
            x_poke3 += 80
            y_poke3 += 0
            seleccion = 0
            ficha3_side += 1
            matriz[ficha3_matrizx][ficha3_matrizy] = 0
            ficha3_matrizy += 1
            ficha3_matrizx += 0
            matriz[ficha3_matrizx][ficha3_matrizy] = 3
            Button(ventanal, image=pidgeot, command=banca_rival13, width=80, height=80).place(x=x_poke3, y=y_poke3)
            return verificar_ganador()
        # movimiento ficha 4
        if evento.keysym == "Down" and seleccion == 4 and ficha4_up_down < 5:
            if ficha4_matrizx != -1:
                matriz[ficha4_matrizx][ficha4_matrizy] = 0
            if ficha4_up_down < 5 and matriz[ficha4_matrizx + 1][ficha4_matrizy] == 0 and turno == 2:
                Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke4, y=y_poke4)
                turno = 1
                x_poke4 += 0
                y_poke4 += 80
                seleccion = 0
                banca_lados4 += 1
                ficha4_up_down += 1
                ficha4_matrizy += 0
                ficha4_matrizx += 1
                matriz[ficha4_matrizx][ficha4_matrizy] = 4
                Button(ventanal, image=charizard, command=banca_rival14, width=80, height=80).place(x=x_poke4,
                                                                                                    y=y_poke4)
                return verificar_ganador()
            elif matriz[ficha4_matrizx + 1][ficha4_matrizy] == 1 or matriz[ficha4_matrizx + 1][ficha4_matrizy] == 2 or \
                            matriz[ficha4_matrizx + 1][ficha4_matrizy] == 3:
                turno = 1
                oponente = int(matriz[ficha4_matrizx + 1][ficha4_matrizy])
                return duelo()
        if evento.keysym == "Up" and seleccion == 4:
            if ficha4_up_down > 1 and matriz[ficha4_matrizx - 1][ficha4_matrizy] == 0 and turno == 2:
                Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke4, y=y_poke4)
                turno = 1
                x_poke4 += 0
                y_poke4 -= 80
                seleccion = 0
                banca_lados4 -= 1
                ficha4_up_down -= 1
                matriz[ficha4_matrizx][ficha4_matrizy] = 0
                ficha4_matrizx -= 1
                ficha4_matrizy += 0
                matriz[ficha4_matrizx][ficha4_matrizy] = 4
                Button(ventanal, image=charizard, command=banca_rival14, width=80, height=80).place(x=x_poke4,
                                                                                                    y=y_poke4)
                return verificar_ganador()
            elif ficha4_up_down > 1 and matriz[ficha4_matrizx - 1][ficha4_matrizy] == 1 or matriz[ficha4_matrizx - 1][
                ficha4_matrizy] == 2 or matriz[ficha4_matrizx - 1][ficha4_matrizy] == 3:
                oponente = int(matriz[ficha4_matrizx - 1][ficha4_matrizy])
                turno = 1
                return duelo()
        if evento.keysym == "Left" and seleccion == 4 and banca_lados4 > 0 and -2 < ficha4_side <= 4 \
                and matriz[ficha4_matrizx][ficha4_matrizy - 1] == 0 and turno == 2:
            Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke4, y=y_poke4)
            turno = 1
            x_poke4 -= 80
            y_poke4 += 0
            seleccion = 0
            ficha4_side -= 1
            matriz[ficha4_matrizx][ficha4_matrizy] = 0
            ficha4_matrizy -= 1
            ficha4_matrizx += 0
            matriz[ficha4_matrizx][ficha4_matrizy] = 4
            Button(ventanal, image=charizard, command=banca_rival14, width=80, height=80).place(x=x_poke4, y=y_poke4)
            return verificar_ganador()
        if evento.keysym == "Right" and seleccion == 4 and banca_lados4 > 0 and -2 <= ficha4_side < 4 \
                and matriz[ficha4_matrizx][ficha4_matrizy + 1] == 0 and turno == 2:
            Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke4, y=y_poke4)
            turno = 1
            x_poke4 += 80
            y_poke4 += 0
            seleccion = 0
            ficha4_side += 1
            matriz[ficha4_matrizx][ficha4_matrizy] = 0
            ficha4_matrizy += 1
            ficha4_matrizx += 0
            matriz[ficha4_matrizx][ficha4_matrizy] = 4
            Button(ventanal, image=charizard, command=banca_rival14, width=80, height=80).place(x=x_poke4, y=y_poke4)
            return verificar_ganador()
        ##movimiento para ficha 5
        if evento.keysym == "Down" and seleccion == 5 and ficha5_up_down < 5:
            if ficha5_matrizx != -1:
                matriz[ficha5_matrizx][ficha5_matrizy] = 0
            if ficha5_up_down < 5 and matriz[ficha5_matrizx + 1][ficha5_matrizy] == 0 and turno == 2:
                Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke5, y=y_poke5)
                turno = 1
                x_poke5 += 0
                y_poke5 += 80
                seleccion = 0
                banca_lados5 += 1
                ficha5_up_down += 1
                ficha5_matrizy += 0
                ficha5_matrizx += 1
                matriz[ficha5_matrizx][ficha5_matrizy] = 5
                Button(ventanal, image=blastoise, command=banca_rival15, width=80, height=80).place(x=x_poke5,
                                                                                                    y=y_poke5)
                return verificar_ganador()
            elif matriz[ficha5_matrizx + 1][ficha5_matrizy] == 1 or matriz[ficha5_matrizx + 1][ficha5_matrizy] == 2 or \
                            matriz[ficha5_matrizx + 1][ficha5_matrizy] == 3:
                oponente = int(matriz[ficha5_matrizx + 1][ficha5_matrizy])
                turno = 1
                return duelo()
        if evento.keysym == "Up" and seleccion == 5:
            if ficha5_up_down > 1 and matriz[ficha5_matrizx - 1][ficha5_matrizy] == 0 and turno == 2:
                Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke5, y=y_poke5)
                turno = 1
                x_poke5 += 0
                y_poke5 -= 80
                seleccion = 0
                banca_lados5 -= 1
                ficha5_up_down -= 1
                matriz[ficha5_matrizx][ficha5_matrizy] = 0
                ficha5_matrizx -= 1
                ficha5_matrizy += 0
                matriz[ficha5_matrizx][ficha5_matrizy] = 5
                Button(ventanal, image=blastoise, command=banca_rival15, width=80, height=80).place(x=x_poke5,
                                                                                                    y=y_poke5)
                return verificar_ganador()
            elif ficha5_up_down > 1 and matriz[ficha5_matrizx - 1][ficha5_matrizy] == 1 or matriz[ficha5_matrizx - 1][
                ficha5_matrizy] == 2 or matriz[ficha5_matrizx - 1][ficha5_matrizy] == 3:
                oponente = int(matriz[ficha5_matrizx - 1][ficha5_matrizy])
                turno = 1
                return duelo()
        if evento.keysym == "Left" and seleccion == 5 and banca_lados5 > 0 and -2 < ficha5_side <= 4 \
                and matriz[ficha5_matrizx][ficha5_matrizy - 1] == 0 and turno == 2:
            Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke5, y=y_poke5)
            turno = 1
            x_poke5 -= 80
            y_poke5 += 0
            seleccion = 0
            ficha5_side -= 1
            matriz[ficha5_matrizx][ficha5_matrizy] = 0
            ficha5_matrizy -= 1
            ficha5_matrizx += 0
            matriz[ficha5_matrizx][ficha5_matrizy] = 5
            Button(ventanal, image=blastoise, command=banca_rival15, width=80, height=80).place(x=x_poke5, y=y_poke5)
            return verificar_ganador()
        if evento.keysym == "Right" and seleccion == 5 and banca_lados5 > 0 and -2 <= ficha5_side < 4 \
                and matriz[ficha5_matrizx][ficha5_matrizy + 1] == 0 and turno == 2:
            Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke5, y=y_poke5)
            turno = 1
            x_poke5 += 80
            y_poke5 += 0
            seleccion = 0
            ficha5_side += 1
            matriz[ficha5_matrizx][ficha5_matrizy] = 0
            ficha5_matrizy += 1
            ficha5_matrizx += 0
            matriz[ficha5_matrizx][ficha5_matrizy] = 5
            Button(ventanal, image=blastoise, command=banca_rival15, width=80, height=80).place(x=x_poke5, y=y_poke5)
            return verificar_ganador()
            ##movimiento para ficha 6
        if evento.keysym == "Down" and seleccion == 6 and ficha6_up_down < 5:
            if ficha6_matrizx != -1:
                matriz[ficha6_matrizx][ficha6_matrizy] = 0
            if ficha6_up_down < 5 and matriz[ficha6_matrizx + 1][ficha6_matrizy] == 0 and turno == 2:
                Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke6, y=y_poke6)
                turno = 1
                x_poke6 += 0
                y_poke6 += 80
                seleccion = 0
                banca_lados6 += 1
                ficha6_up_down += 1
                ficha6_matrizy += 0
                ficha6_matrizx += 1
                matriz[ficha6_matrizx][ficha6_matrizy] = 6
                Button(ventanal, image=venusaur, command=banca_rival16, width=80, height=80).place(x=x_poke6, y=y_poke6)
                return verificar_ganador()
            elif matriz[ficha6_matrizx + 1][ficha6_matrizy] == 1 or matriz[ficha6_matrizx + 1][ficha6_matrizy] == 2 or \
                            matriz[ficha6_matrizx + 1][ficha6_matrizy] == 3:
                oponente = int(matriz[ficha6_matrizx + 1][ficha6_matrizy])
                turno = 1
                return duelo()
        if evento.keysym == "Up" and seleccion == 6:
            if ficha6_up_down > 1 and matriz[ficha6_matrizx - 1][ficha6_matrizy] == 0 and turno == 2:
                Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke6, y=y_poke6)
                turno = 1
                x_poke6 += 0
                y_poke6 -= 80
                seleccion = 0
                banca_lados6 -= 1
                ficha6_up_down -= 1
                matriz[ficha6_matrizx][ficha6_matrizy] = 0
                ficha6_matrizx -= 1
                ficha6_matrizy += 0
                matriz[ficha6_matrizx][ficha6_matrizy] = 6
                Button(ventanal, image=venusaur, command=banca_rival16, width=80, height=80).place(x=x_poke6, y=y_poke6)
                return verificar_ganador()
            elif ficha6_up_down > 1 and matriz[ficha6_matrizx - 1][ficha6_matrizy] == 1 or matriz[ficha6_matrizx - 1][
                ficha6_matrizy] == 2 or matriz[ficha6_matrizx - 1][ficha6_matrizy] == 3:
                oponente = int(matriz[ficha6_matrizx - 1][ficha6_matrizy])
                turno = 1
                return duelo()
        if evento.keysym == "Left" and seleccion == 6 and banca_lados6 > 0 and -2 < ficha6_side <= 4 \
                and matriz[ficha6_matrizx][ficha6_matrizy - 1] == 0 and turno == 2:
            Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke6, y=y_poke6)
            turno = 1
            x_poke6 -= 80
            y_poke6 += 0
            seleccion = 0
            ficha6_side -= 1
            matriz[ficha6_matrizx][ficha6_matrizy] = 0
            ficha6_matrizy -= 1
            ficha6_matrizx += 0
            matriz[ficha6_matrizx][ficha6_matrizy] = 6
            Button(ventanal, image=venusaur, command=banca_rival16, width=80, height=80).place(x=x_poke6, y=y_poke6)
            return verificar_ganador()
        if evento.keysym == "Right" and seleccion == 6 and banca_lados6 > 0 and -2 <= ficha6_side < 4 \
                and matriz[ficha6_matrizx][ficha6_matrizy + 1] == 0 and turno == 2:
            Button(ventanal, image=pokebola, width=80, height=80).place(x=x_poke6, y=y_poke6)
            turno = 1
            x_poke6 += 80
            y_poke6 += 0
            seleccion = 0
            ficha6_side += 1
            matriz[ficha6_matrizx][ficha6_matrizy] = 0
            ficha6_matrizy += 1
            ficha6_matrizx += 0
            matriz[ficha6_matrizx][ficha6_matrizy] = 6
            Button(ventanal, image=venusaur, command=banca_rival16, width=80, height=80).place(x=x_poke6, y=y_poke6)
            return verificar_ganador()

    ventanal.bind_all("<Down>", mov_rival1)
    ventanal.bind_all("<Left>", mov_rival1)
    ventanal.bind_all("<Right>", mov_rival1)
    ventanal.bind_all("<Up>", mov_rival1)
    ventanal.mainloop()


# Se crean algunas variables
random_1 = 0
random_2 = 0
lista_pokes = ["pikachu", "raticate", "pidgeot", "charizard", "blastoise", "venusaur", "raichu"]
fondo_ganador = None


# Funcion que crea la la ventana de duelo, la musica de duelo y da los numeros random
def duelo():
    global random_1, random_2, duel, ventanal, seleccion, oponente
    duel = Toplevel()
    duel.title("Duel")
    duel.update_idletasks()
    duel.focus_force()
    fondo_duelo = PhotoImage(file="imagenes/fondos/fondo_duel.gif")
    ancho = duel.winfo_screenwidth() - 660
    alto = duel.winfo_screenheight() - 720
    duel.geometry("%dx%d%+d%+d" % (392, 700, ancho / 2, alto / 2))
    canvas = Canvas(duel, bg="black", width=392, height=700)
    canvas.pack()
    canvas.create_image(200, 350, image=fondo_duelo)
    Label(duel, text="Precione 'a' para continuar", font=("Arial Black", 18), bg="#000000", fg="#FFFFFF").place(x=0,
                                                                                                                y=655)
    pygame.mixer.init()
    pygame.mixer.music.load("musica/duelo.mp3")
    pygame.mixer.music.play(-1)
    random_1 = random.randrange(1, 101)
    random_2 = random.randrange(1, 101)
    Label(duel, text=str(random_1), font=("Arial", 20)).place(x=150, y=380)
    Label(duel, text=str(random_2), font=("Arial", 20)).place(x=210, y=240)

    # funcion que verifica los pokemon que estan en duelo y coloca sus imagenes
    for poke in range(len(lista_pokes)):
        if seleccion == poke + 1 and 0 < seleccion < 4:
            image_poke = PhotoImage(file="imagenes/pokes_duelo/" + lista_pokes[poke] + ".png")
            canvas.create_image(200, 575, image=image_poke)
        if oponente == poke + 1 and 0 < oponente < 4:
            image_poke = PhotoImage(file="imagenes/pokes_duelo/" + lista_pokes[poke] + ".png")
            canvas.create_image(200, 575, image=image_poke)
        if oponente == poke + 1 and 3 < oponente < 7:
            image_poke2 = PhotoImage(file="imagenes/pokes_duelo/" + lista_pokes[poke] + "2.png")
            canvas.create_image(200, 100, image=image_poke2)
        if seleccion == poke + 1 and 3 < seleccion < 7:
            image_poke2 = PhotoImage(file="imagenes/pokes_duelo/" + lista_pokes[poke] + "2.png")
            canvas.create_image(200, 100, image=image_poke2)

    # Funcion q verifica cual es el ganador
    def ganador(event):
        global random_1, random_2, ventana_ganador, duel, gana
        if event.keysym == "a":
            if random_1 >= random_2:
                gana = 1
                return victory()
            if random_1 < random_2:
                gana = 2
                return victory()

    duel.bind_all("<a>", ganador)
    duel.mainloop()


# Funcion que crea la ventana de ganador la cual da el resultado
def victory():
    global fondo_ganador, ventana_ganador, duel, x_poke4, y_poke4, banca_lados4, seleccion, ficha4_side, \
        ficha4_up_down, ficha4_matrizx, ficha4_matrizy, \
        matriz, x_poke5, y_poke5, banca_lados5, ficha5_side, \
        ficha5_up_down, ficha5_matrizx, ficha5_matrizy, x_poke6, y_poke6, banca_lados6, ficha6_side, \
        ficha6_up_down, ficha6_matrizx, ficha6_matrizy, x_poke1, y_poke1, banca_lados1, ficha1_side, \
        ficha1_up_down, ficha1_matrizx, ficha1_matrizy, x_poke2, y_poke2, banca_lados2, ficha2_side, \
        ficha2_up_down, ficha2_matrizx, ficha2_matrizy, x_poke3, y_poke3, banca_lados3, ficha3_side, \
        ficha3_up_down, ficha3_matrizx, ficha3_matrizy, turno, ventanal, oponente, seleccion, \
        banca_rival11, banca_rival12, banca_rival13, banca_rival14, banca_rival15, banca_rival16, \
        blastoise, pidgeot, venusaur, pikachu, raichu, charizard, raticate, pokeball, gana
    duel.destroy()
    ventana_ganador = Toplevel()
    ventana_ganador.title("Duel")
    ventana_ganador.update_idletasks()
    ventana_ganador.focus_force()
    ancho = ventana_ganador.winfo_screenwidth() - 660
    alto = ventana_ganador.winfo_screenheight() - 720
    ventana_ganador.geometry("%dx%d%+d%+d" % (298, 195, ancho / 2, alto / 2))
    pygame.mixer.init()
    pygame.mixer.music.load("musica/Victory.mp3")
    pygame.mixer.music.play(-1)
    fondo_ganador = PhotoImage(file="imagenes/fondos/fondo_ganador.gif")
    Label(ventana_ganador, image=fondo_ganador).place(x=-2, y=0)
    Label(ventana_ganador, text="Ganador", font=("Arial Black", 20), bg="#FF8D00").place(x=130, y=20)
    Label(ventana_ganador, text="Precione 'a' para continuar", font=("Arial Black", 15), bg="#FF8D00").place(x=0, y=167)

    # Implementa un label del ganador
    if gana == 1:
        Label(ventana_ganador, text="Jugador 1", font=("Arial Black", 20), bg="#FF8D00").place(x=140, y=80)
    elif gana == 2:
        Label(ventana_ganador, text="Jugador 2", font=("Arial Black", 20), bg="#FF8D00").place(x=140, y=80)

    # Funcion que cierra la ventana
    def cerrar(evento):
        global ventana_ganador
        if evento.keysym == "a":
            pygame.mixer.music.stop()
            ventana_ganador.destroy()
            pygame.mixer.music.load("musica/Light the Fire Up in the Night.mp3")
            pygame.mixer.music.play(-1)
            return volver_banca()

    ventana_ganador.bind_all("<a>", cerrar)
    ventana_ganador.mainloop()


# Funcion que devuelve el pokemon perdedor a la banca y posicion correspondiente
def volver_banca():
    global fondo_ganador, ventana_ganador, duel, x_poke4, y_poke4, banca_lados4, seleccion, ficha4_side, \
        ficha4_up_down, ficha4_matrizx, ficha4_matrizy, \
        matriz, x_poke5, y_poke5, banca_lados5, ficha5_side, \
        ficha5_up_down, ficha5_matrizx, ficha5_matrizy, x_poke6, y_poke6, banca_lados6, ficha6_side, \
        ficha6_up_down, ficha6_matrizx, ficha6_matrizy, x_poke1, y_poke1, banca_lados1, ficha1_side, \
        ficha1_up_down, ficha1_matrizx, ficha1_matrizy, x_poke2, y_poke2, banca_lados2, ficha2_side, \
        ficha2_up_down, ficha2_matrizx, ficha2_matrizy, x_poke3, y_poke3, banca_lados3, ficha3_side, \
        ficha3_up_down, ficha3_matrizx, ficha3_matrizy, turno, ventanal, oponente, seleccion, \
        banca_rival11, banca_rival12, banca_rival13, banca_rival14, banca_rival15, banca_rival16, \
        blastoise, pidgeot, venusaur, pikachu, raichu, charizard, raticate, pokebola, gana, \
        ventanal, banca_rival11, banca_rival12, banca_rival13, banca_rival14, banca_rival15, \
        banca_rival16, matriz, oponente
    if gana == 1:
        if seleccion == 4:
            Button(ventanal, image=charizard, command=banca_rival14, width=80, height=80).place(x=160, y=0)
            Button(ventanal, image=pokebola, command=banca_rival14, width=80, height=80).place(x=x_poke4, y=y_poke4)
            x_poke4 = 160
            y_poke4 = 0
            seleccion = 0
            banca_lados4 = 0
            ficha4_side = 0
            ficha4_up_down = 0
            matriz[ficha4_matrizx][ficha4_matrizy] = 0
            ficha4_matrizx = -1
            ficha4_matrizy = 2
        if oponente == 4:
            Button(ventanal, image=charizard, command=banca_rival14, width=80, height=80).place(x=160, y=0)
            Button(ventanal, image=pokebola, command=banca_rival14, width=80, height=80).place(x=x_poke4, y=y_poke4)
            x_poke4 = 160
            y_poke4 = 0
            seleccion = 0
            banca_lados4 = 0
            ficha4_side = 0
            ficha4_up_down = 0
            matriz[ficha4_matrizx][ficha4_matrizy] = 0
            ficha4_matrizx = -1
            ficha4_matrizy = 2
        if oponente == 5:
            Button(ventanal, image=blastoise, command=banca_rival15, width=80, height=80).place(x=240, y=0)
            Button(ventanal, image=pokebola, command=banca_rival15, width=80, height=80).place(x=x_poke5, y=y_poke5)
            x_poke5 = 240
            y_poke5 = 0
            banca_lados5 = 0
            ficha5_side = 1
            ficha5_up_down = 0
            matriz[ficha5_matrizx][ficha5_matrizy] = 0
            ficha5_matrizx = -1
            ficha5_matrizy = 3
        if seleccion == 5:
            Button(ventanal, image=blastoise, command=banca_rival15, width=80, height=80).place(x=240, y=0)
            Button(ventanal, image=pokebola, command=banca_rival15, width=80, height=80).place(x=x_poke5, y=y_poke5)
            x_poke5 = 240
            y_poke5 = 0
            banca_lados5 = 0
            ficha5_side = 1
            ficha5_up_down = 0
            matriz[ficha5_matrizx][ficha5_matrizy] = 0
            ficha5_matrizx = -1
            ficha5_matrizy = 3
        if seleccion == 6:
            Button(ventanal, image=venusaur, command=banca_rival16, width=80, height=80).place(x=320, y=0)
            Button(ventanal, image=pokebola, command=banca_rival16, width=80, height=80).place(x=x_poke6, y=y_poke6)
            x_poke6 = 320
            y_poke6 = 0
            banca_lados6 = 0
            ficha6_side = 2
            ficha6_up_down = 0
            matriz[ficha6_matrizx][ficha6_matrizy] = 0
            ficha6_matrizx = -1
            ficha6_matrizy = 4
        if oponente == 6:
            Button(ventanal, image=venusaur, command=banca_rival16, width=80, height=80).place(x=320, y=0)
            Button(ventanal, image=pokebola, command=banca_rival16, width=80, height=80).place(x=x_poke6, y=y_poke6)
            x_poke6 = 320
            y_poke6 = 0
            banca_lados6 = 0
            ficha6_side = 2
            ficha6_up_down = 0
            matriz[ficha6_matrizx][ficha6_matrizy] = 0
            ficha6_matrizx = -1
            ficha6_matrizy = 4
    if gana == 2:
        if seleccion == 1:
            Button(ventanal, image=pikachu, command=banca_rival11, width=80, height=80).place(x=160, y=480)
            Button(ventanal, image=pokebola, command=banca_rival11, width=80, height=80).place(x=x_poke1, y=y_poke1)
            x_poke1 = 160
            y_poke1 = 480
            seleccion = 0
            banca_lados1 = 0
            ficha1_side = 0
            ficha1_up_down = 0
            matriz[ficha1_matrizx][ficha1_matrizy] = 0
            ficha1_matrizx = 0
            ficha1_matrizy = 2

        if seleccion == 2:
            Button(ventanal, image=raticate, command=banca_rival12, width=80, height=80).place(x=240, y=480)
            Button(ventanal, image=pokebola, command=banca_rival12, width=80, height=80).place(x=x_poke2, y=y_poke2)
            x_poke2 = 240
            y_poke2 = 480
            seleccion = 0
            banca_lados2 = 0
            ficha2_side = 1
            ficha2_up_down = 0
            matriz[ficha2_matrizx][ficha2_matrizy] = 0
            ficha2_matrizx = 0
            ficha2_matrizy = 3

        if seleccion == 3:
            Button(ventanal, image=pidgeot, command=banca_rival13, width=80, height=80).place(x=320, y=480)
            Button(ventanal, image=pokebola, command=banca_rival13, width=80, height=80).place(x=x_poke3, y=y_poke3)
            x_poke3 = 320
            y_poke3 = 480
            seleccion = 0
            banca_lados3 = 0
            ficha3_side = 2
            ficha3_up_down = 0
            matriz[ficha3_matrizx][ficha3_matrizy] = 0
            ficha3_matrizx = 0
            ficha3_matrizy = 4
        if oponente == 1:
            Button(ventanal, image=pikachu, command=banca_rival11, width=80, height=80).place(x=160, y=480)
            Button(ventanal, image=pokebola, command=banca_rival11, width=80, height=80).place(x=x_poke1, y=y_poke1)
            x_poke1 = 160
            y_poke1 = 480
            seleccion = 0
            banca_lados1 = 0
            ficha1_side = 0
            ficha1_up_down = 0
            matriz[ficha1_matrizx][ficha1_matrizy] = 0
            ficha1_matrizx = 0
            ficha1_matrizy = 2

        if oponente == 2:
            Button(ventanal, image=raticate, command=banca_rival12, width=80, height=80).place(x=240, y=480)
            Button(ventanal, image=pokebola, command=banca_rival12, width=80, height=80).place(x=x_poke2, y=y_poke2)
            x_poke2 = 240
            y_poke2 = 480
            seleccion = 0
            banca_lados2 = 0
            ficha2_side = 1
            ficha2_up_down = 0
            matriz[ficha2_matrizx][ficha2_matrizy] = 0
            ficha2_matrizx = 0
            ficha2_matrizy = 3

        if oponente == 3:
            Button(ventanal, image=pidgeot, command=banca_rival13, width=80, height=80).place(x=320, y=480)
            Button(ventanal, image=pokebola, command=banca_rival13, width=80, height=80).place(x=x_poke3, y=y_poke3)
            x_poke3 = 320
            y_poke3 = 480
            seleccion = 0
            banca_lados3 = 0
            ficha3_side = 2
            ficha3_up_down = 0
            matriz[ficha3_matrizx][ficha3_matrizy] = 0
            ficha3_matrizx = 0
            ficha3_matrizy = 4


##Funcion que verifica las posiciones de la matriz donde puede ganar un jugador
def verificar_ganador():
    if matriz[0][3] == 1 or matriz[0][3] == 2 or matriz[0][3] == 3:
        return victoria_partida(1)
    if matriz[4][3] == 4 or matriz[4][3] == 5 or matriz[4][3] == 6:
        return victoria_partida(2)
    else:
        print("no")


##Funcion que abre la ventana donde se muestra quien gano la partida
def victoria_partida(ganador):
    global fondo_victoria, ventana_victoria, ventanal
    ventana_victoria = Toplevel()
    ventana_victoria.title("Final del juego")
    ventana_victoria.update_idletasks()
    ventana_victoria.focus_force()
    ancho = ventana_victoria.winfo_screenwidth() - 660
    alto = ventana_victoria.winfo_screenheight() - 720
    ventana_victoria.geometry("%dx%d%+d%+d" % (700, 393, ancho / 2, alto / 2))
    pygame.mixer.init()
    pygame.mixer.music.load("musica/Victory.mp3")
    pygame.mixer.music.play(-1)
    Label(ventana_victoria, image=fondo_victoria).place(x=0, y=0)

    if ganador == 1:
        Label(ventana_victoria, text="Victoria para: Jugador 1", font=("Arial Blsck", 30), bg="#2B3674").place(x=200,
                                                                                                               y=50)
    if ganador == 2:
        Label(ventana_victoria, text="Victoria para: Jugador 2", font=("Arial Blsck", 30), bg="#2B3674").place(x=200,
                                                                                                               y=50)

    ##Funcion evento para cerrar el juego
    def close_game(evento):
        global ventana_victoria, ventanal
        if evento.keysym == "a":
            pygame.mixer.music.stop()
            ventana_victoria.destroy()
            ventanal.destroy()

    ventana_victoria.bind_all("<a>", close_game)
    ventana_victoria.mainloop()
