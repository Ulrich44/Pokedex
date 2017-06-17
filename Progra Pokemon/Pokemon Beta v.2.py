# Se importan las librerias a utilizar
from tkinter import *
from utiles import *
from Tablero import *
import pygame

ventana = Tk()  # Se nombra la ventana inicial
ventana.title("Pokemon Go V.000000001")  # Se nombra la ventana principal
### Con distintos parametros de se coloca la ventana principal en el centro de la pantalla de la computadora
ventana.update_idletasks()
ancho = ventana.winfo_screenwidth() - 560
alto = ventana.winfo_screenheight() - 560
ventana.geometry("%dx%d%+d%+d" % (560, 560, ancho / 2, alto / 2))
# Se crea el primer canvas en el cual se montan las imagenes
canvas = Canvas(ventana, width=560, height=560)  ## Creacion de canvas
canvas.pack()
fondo = PhotoImage(file="imagenes/introduccion/oak1.gif")  # Se asigana a la variable el archio de imagen
ash = PhotoImage(file="imagenes/ash/ash_up.gif")  # Se asigana a la variable el archio de imagen
pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup.gif")  # Se asigana a la variable el archio de imagen
pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down.gif")  # Se asigana a la variable el archio de imagen
pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left.gif")  # Se asigana a la variable el archio de imagen
pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right.gif")  # Se asigana a la variable el archio de imagen
pokebola = PhotoImage(file="imagenes/repentinos/pokebola.gif")  # Se asigana a la variable el archio de imagen
compañero = PhotoImage(file="imagenes/repentinos/compañero.gif")  # Se asigana a la variable el archio de imagen
mesa = PhotoImage(file="imagenes/repentinos/mesa.gif")  # Se asigana a la variable el archio de imagen
fondo_change = canvas.create_image(280, 280, image=fondo)  # se crea la imagen en el canvas
# Se nombran variables globales
ash_moves = 0
x_ini = 0
y_ini = 0
func = 1
nombre = ""
pokemios = []
pikachu_moves = 0
nombre = ""
contador = 0
contador2 = 0
contador3 = 0
move_bosque_paleta = 0
move_plateada_bosque = 0
move_plata_gym = 0
menu = 0
bloqueo_conec = 0
bloqueo_acept = 1
lista_pokemon = []
move_batalla = 0
poke_list = 0
cantidad_poke = 0
# se carga y reproduce el archivo de musica
pygame.mixer.init()
pygame.mixer.music.load("musica/laboratorio.mp3")
pygame.mixer.music.play(-1)


# Se incia el primer modulo de movimiento
def mover_ash(evento):
    # Se importan las variables globales
    global ash, x_ini, y_ini, func, fondo, contador, contador2, \
        contador3, ash_moves, nombre, cajanombre, \
        shownombre, pikachu_moves, pikachu, pokebola, pikachuup, \
        pikachu_down, pikachul, pikachur, compañero, mesa, menu, valor_flecha
    # Condicionales para la animacion de la pantalla
    if func == 1:
        fondo = PhotoImage(file="imagenes/introduccion/oak2.gif")
        canvas.itemconfig(fondo_change, image=fondo)
        func = 2
    elif func == 2:
        fondo = PhotoImage(file="imagenes/introduccion/oak3.gif")
        canvas.itemconfig(fondo_change, image=fondo)
        nombre = StringVar()
        nombre.set("   Ash Ketchum")
        cajanombre = Entry(ventana, textvariable=nombre, bg="lightgreen")
        cajanombre.pack()
        cajanombre.place(x=30, y=460)
        cajanombre.focus_force()
        cajanombre.select_range(0, END)
        func = 3
    elif func == 3:
        nombre = cajanombre.get()
        cajanombre.destroy()
        fondo = PhotoImage(file="imagenes/introduccion/oak4.gif")
        canvas.itemconfig(fondo_change, image=fondo)
        shownombre = Label(ventana, text=nombre)
        shownombre.pack()
        shownombre.place(x=30, y=400)
        func = 4
    elif func == 4:
        shownombre.destroy()
        fondo = PhotoImage(file="imagenes/fondos/lab_oak.gif")
        canvas.itemconfig(fondo_change, image=fondo)
        ash_moves = canvas.create_image(280, 520, image=ash)
        canvas.create_image(400, 210, image=pokebola)
        func = 5
    # Condicionales que segun el evento o tecla presionada crean una accion y de esta forma se le da animacion al juego
    # Las acciones normalmento son cambio de imagenes en los canvas ya creados, en estos condicionales se puede dar
    # un cambio del valor en variables, llamada a nueva ventanas o lo explicado ateriormente, cambio de imagenes en canvas
    # Condicional del enevento o tecla abajo
    elif evento.keysym == "Down" and limites(x_ini, y_ini, "Down") and menu == 0:
        ash = PhotoImage(file="imagenes/ash/ash_down.gif")
        canvas.itemconfig(ash_moves, image=ash)
        canvas.move(2, 0, 10)
        x_ini -= 10
        if x_ini == 280 and y_ini == 120 and contador2 == 0:
            contador += 1
            contador2 += 1
            contador3 += 1
        if contador == 1:
            pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down.gif")
            canvas.itemconfig(pikachu_moves, image=pikachu_down)
            canvas.move(4, 0, 10)
        if x_ini == 0 and -20 < y_ini < 20 and contador2 == 1:
            ventana.quit()
            ventana.iconify()
            pygame.mixer.music.stop()
            return mostrar_ventana_paleta()
    # Condicional del enevento o tecla arriba
    elif evento.keysym == "Up" and limites(x_ini, y_ini, "Up") and menu == 0:
        ash = PhotoImage(file="imagenes/ash/ash_up.gif")
        canvas.itemconfig(ash_moves, image=ash)
        canvas.move(2, 0, -10)
        x_ini += 10
        if x_ini == 280 and y_ini == 120 and contador2 == 0:
            pikachu_moves = canvas.create_image(400, 280, image=pikachuup)
            contador += 1
            contador2 += 1
            compañero = PhotoImage(file="imagenes/repentinos/compañero.gif")
            canvas.create_image(400, 120, image=compañero)
            mesa = PhotoImage(file="imagenes/repentinos/mesa.gif")
            canvas.create_image(400, 210, image=mesa)
        if contador == 1:
            pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup.gif")
            canvas.itemconfig(pikachu_moves, image=pikachuup)
            canvas.move(4, 0, -10)
    # Condicional del enevento o tecla izquierda
    elif evento.keysym == "Left" and limites(x_ini, y_ini, "Left") and menu == 0:
        ash = PhotoImage(file="imagenes/ash/ash_left.gif")
        canvas.itemconfig(ash_moves, image=ash)
        canvas.move(2, -10, 0)
        y_ini -= 10
        if x_ini == 280 and y_ini == 120 and contador2 == 0:
            pikachu_moves = canvas.create_image(410, 270, image=pikachul)
            contador += 1
            contador2 += 1
            compañero = PhotoImage(file="imagenes/repentinos/compañero.gif")
            canvas.create_image(400, 120, image=compañero)
            mesa = PhotoImage(file="imagenes/repentinos/mesa.gif")
            canvas.create_image(400, 210, image=mesa)
            canvas.itemconfig(pikachu_moves, image=pikachul)
        if contador == 1:
            pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left.gif")
            canvas.itemconfig(pikachu_moves, image=pikachul)
            canvas.move(4, -10, 0)
    # Condicional del enevento o tecla derecha
    elif evento.keysym == "Right" and limites(x_ini, y_ini, "Right") and menu == 0:
        ash = PhotoImage(file="imagenes/ash/ash_right.gif")
        canvas.itemconfig(ash_moves, image=ash)
        canvas.move(2, 10, 0)
        y_ini += 10
        if x_ini == 280 and y_ini == 120 and contador2 == 0:
            contador += 1
            contador2 += 1
            pikachu_moves = canvas.create_image(390, 270, image=pikachur)
            canvas.itemconfig(pikachu_moves, image=pikachur)
            compañero = PhotoImage(file="imagenes/repentinos/compañero.gif")
            canvas.create_image(400, 120, image=compañero)
            mesa = PhotoImage(file="imagenes/repentinos/mesa.gif")
            canvas.create_image(400, 210, image=mesa)
        if contador == 1:
            canvas.itemconfig(pikachu_moves, image=pikachur)
            canvas.move(4, 10, 0)
    elif evento.keysym == "space":
        menu = 1
        return mostrar_ventana_menu()


# Se incia el modulo de ventaba paleta
def mostrar_ventana_paleta():
    # Variables globales
    global contenedor, ventanaB, mover_ash, fondo_change, \
        cajanombre, ash_moves, x_ini, y_ini, func, canvas, ventanaP, \
        ventana, pueblo_paleta, pikachu_moves, move_bosque_paleta
    # Se carga y reproduce la musica en este escenario
    pygame.mixer.init()
    pygame.mixer.music.load("musica/Azalea Town.mp3")
    pygame.mixer.music.play(-1)
    # Se crea al nueva ventana y se muestra en primer plano
    ventanaP = Toplevel()
    ventanaP.title("Pueblo_Paleta")  # Se le da un nuevo nombre a la ventana
    ### Con distintos parametros de se coloca la ventana principal en el centro de la pantalla de la computadora
    ventanaP.focus_force()
    ventanaP.update_idletasks()
    ancho = ventanaP.winfo_screenwidth() - 660
    alto = ventanaP.winfo_screenheight() - 660
    ventanaP.geometry("%dx%d%+d%+d" % (660, 660, ancho / 2, alto / 2))
    # Se crea el primer canvas en el cual se montan las imagenes
    canvas = Canvas(ventanaP, width=660, height=660)
    canvas.pack()
    fondo2 = PhotoImage(file="imagenes/fondos/afueras_pic.gif")  # Se carga una imagen
    ash = PhotoImage(file="imagenes/ash/ash_down.gif")  # Se carga una imagen
    canvas.create_image(330, 310, image=fondo2)  # Se crea la imagen
    if move_bosque_paleta == 0:
        mover_ash = canvas.create_image(470, 420, image=ash)  # Se crea la imagen
        pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup.gif")  # Se carga una imagen
        pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down.gif")  # Se carga una imagen
        pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left.gif")  # Se carga una imagen
        pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right.gif")  # Se carga una imagen
        pikachu_moves = canvas.create_image(500, 420, image=pikachu_down)  # Se crea la imagen
        # Se asigna un valor a las variables globales
        cajanombre = 0
        ash_moves = 0
        x_ini = 0
        y_ini = 0
        func = 1
    else:
        mover_ash = canvas.create_image(320, 30, image=ash)  # Se crea la imagen
        pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup.gif")  # Se carga una imagen
        pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down.gif")  # Se carga una imagen
        pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left.gif")  # Se carga una imagen
        pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right.gif")  # Se carga una imagen
        pikachu_moves = canvas.create_image(350, 30, image=pikachu_down)  # Se crea la imagen
        # Se asigna un valor a las variables globales
        cajanombre = 0
        ash_moves = 0
        x_ini = 390
        y_ini = -150
        func = 1

    # Se da incio al modulo de animacion en esta ventana
    def pueblo_paleta(evento):
        # VAriables globales
        global ventanaP, ventanaB, ash, x_ini, y_ini, func, fondo2, ash_moves, contador, \
            contador2, pikachu_moves, nombre, cajanombre, \
            canvas, mover_ash, Pokemon_beta, pikachul, pikachur, \
            pikachuup, pikachu_down, pikachu_moves, move_bosque_paleta, menu
        # Condicionales que segun el evento o tecla presionada crean una accion y de esta forma se le da animacion al juego
        # Las acciones normalmento son cambio de imagenes en los canvas ya creados, en estos condicionales se puede dar
        # un cambio del valor en variables, llamada a nueva ventanas o lo explicado ateriormente, cambio de imagenes en canvas
        # Condicional del enevento o tecla abajo
        if evento.keysym == "Down" and limites_paleta(x_ini, y_ini, "Down") and menu == 0:
            ash = PhotoImage(file="imagenes/ash/ash_down.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 0, 10)
            x_ini -= 10
            pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down.gif")
            canvas.itemconfig(pikachu_moves, image=pikachu_down)
            canvas.move(3, 0, 10)
            # Condicional del enevento o tecla arriba
        elif evento.keysym == "Up" and limites_paleta(x_ini, y_ini, "Up") and menu == 0:
            ash = PhotoImage(file="imagenes/ash/ash_up.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 0, -10)
            x_ini += 10
            pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup.gif")
            canvas.itemconfig(pikachu_moves, image=pikachuup)
            canvas.move(3, 0, -10)
            if x_ini == 410 and -190 < y_ini < -90:
                move_bosque_paleta = 1
                ventanaP.destroy()
                pygame.mixer.music.stop()
                return mostrar_ventana_bosque(0)
            if x_ini == 10 and y_ini == 0:
                move_bosque_paleta = 0
                ventanaP.destroy()
                pygame.mixer.music.stop()
                return laboratorio_oak()
                # Condicional del enevento o tecla izquierda
        elif evento.keysym == "Left" and limites_paleta(x_ini, y_ini, "Left") and menu == 0:
            ash = PhotoImage(file="imagenes/ash/ash_left.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, -10, 0)
            y_ini -= 10
            pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left.gif")
            canvas.itemconfig(pikachu_moves, image=pikachul)
            canvas.move(3, -10, 0)
            if x_ini == 410 and -190 < y_ini < -90:
                move_bosque_paleta = 1
                ventanaP.destroy()
                pygame.mixer.music.stop()
                return mostrar_ventana_bosque(0)
            if x_ini == 10 and y_ini == 0:
                ventanaP.destroy()
                pygame.mixer.music.stop()
                return laboratorio_oak()
                # Condicional del enevento o tecla derecha
        elif evento.keysym == "Right" and limites_paleta(x_ini, y_ini, "Right") and menu == 0:
            ash = PhotoImage(file="imagenes/ash/ash_right.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 10, 0)
            y_ini += 10
            pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right.gif")
            canvas.itemconfig(pikachu_moves, image=pikachur)
            canvas.move(3, 10, 0)
            if x_ini == 410 and -190 < y_ini < -90:
                move_bosque_paleta = 1
                ventanaP.destroy()
                pygame.mixer.music.stop()
                return mostrar_ventana_bosque(0)
            if x_ini == 10 and y_ini == 0:
                ventanaP.destroy()
                pygame.mixer.music.stop()
                return laboratorio_oak()
        elif evento.keysym == "space":
            menu = 1
            return mostrar_ventana_menu()

    # Se le de teclado las acciones del usuario para dar incio a la animacion corecta
    ventanaP.bind_all("<Up>", pueblo_paleta)
    ventanaP.bind_all("<Left>", pueblo_paleta)
    ventanaP.bind_all("<Right>", pueblo_paleta)
    ventanaP.bind_all("<Down>", pueblo_paleta)
    ventanaP.bind_all("<space>", pueblo_paleta)
    ventanaP.mainloop()


# Se inicia el modulo de la ventana bosque
def mostrar_ventana_bosque(batalla):
    # Variables globales
    global contenedor, ventanaB, mover_ash, fondo_change, cajanombre, \
        ash_moves, x_ini, y_ini, func, canvas, ventana_up, ventanaP, ventanaB, \
        posalvaje1, posalvaje2, posalvaje3, posalvaje4, poke_elejidos, pokeselec, \
        pikachu_moves, pikachuup, pikachur, pikachu_down, pikachul, pokeactivos, \
        pokesalvaje1, pokesalvaje2, pokesalvaje3, pokesalvaje4, move_bosque_paleta, \
        move_plateada_bosque, ash_down, lista_pokemon
    # Se carga y reproduce la musica, esta funcion se repite reitaradaveces en este modulo
    pygame.mixer.init()
    pygame.mixer.music.load("musica/bosque.mp3")
    pygame.mixer.music.play(-1)

    # Condiciional que permite mostrar la vetana cuando se abre desde un primer momento o por segunda
    # ves desde pantalla de batalla sin cambios
    if batalla == 0:
        # Se muestra la pantalla en primer plano
        ventanaB = Toplevel()
        ventanaB.title("Bosque_Verde")  # Nombre de pantallas
        # Segun los parametros al igual que con la primera pantalla se coloca en el centro del monitor
        ventanaB.update_idletasks()
        ancho = ventanaB.winfo_screenwidth() - 660
        alto = ventanaB.winfo_screenheight() - 800
        ventanaB.geometry("%dx%d%+d%+d" % (660, 700, ancho / 2, alto / 2))
        # Se crean los canvas que se van a utilizar en este modulo
        canvas = Canvas(ventanaB, width=500, height=700)
        canvas.pack()
        fondo3 = PhotoImage(file="imagenes/fondos/bosque_verde.gif")  # carga de imagen
        ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")  # carga de imagen
        ash_down = PhotoImage(file="imagenes/ash/ash_down_min.gif")
        pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")  # carga de imagen
        pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")  # carga de imagen
        pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")  # carga de imagen
        pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")  # carga de imagen
        if move_plateada_bosque == 0:
            canvas.create_image(250, 350, image=fondo3)  # creacion de imagen en canvas
            mover_ash = canvas.create_image(250, 690, image=ash)  # creacion de imagen en canvas
            pikachu_moves = canvas.create_image(270, 690, image=pikachuup)  # creacion de imagen en canvas
            # Variables globales
            cajanombre = 0
            ash_moves = 0
            x_ini = 0
            y_ini = 0
            func = 1
            pokeactivos = [1, 1, 1, 1]
            posalvaje1 = ubicapoke()[0]
            posalvaje2 = ubicapoke()[1]
            posalvaje3 = ubicapoke()[2]
            posalvaje4 = ubicapoke()[3]
            poke_elejidos = yotelijo()
            pokesalvaje1 = PhotoImage(
                file="imagenes/pokes\pokepos" + str(poke_elejidos[0]) + ".gif")  # Carga de imagenes segun variables
            pokesalvaje2 = PhotoImage(
                file="imagenes/pokes\pokepos" + str(poke_elejidos[1]) + ".gif")  # Carga de imagenes segun variables
            pokesalvaje3 = PhotoImage(
                file="imagenes/pokes\pokepos" + str(poke_elejidos[2]) + ".gif")  # Carga de imagenes segun variables
            pokesalvaje4 = PhotoImage(
                file="imagenes/pokes\pokepos" + str(poke_elejidos[3]) + ".gif")  # Carga de imagenes segun variables
            canvas.create_image(250 + posalvaje1[1], 690 - posalvaje1[0],
                                image=pokesalvaje1)  # Creacion de nuevas imagenes
            canvas.create_image(250 + posalvaje2[1], 690 - posalvaje2[0],
                                image=pokesalvaje2)  # Creacion de nuevas imagenes
            canvas.create_image(250 + posalvaje3[1], 690 - posalvaje3[0],
                                image=pokesalvaje3)  # Creacion de nuevas imagenes
            canvas.create_image(250 + posalvaje4[1], 690 - posalvaje4[0],
                                image=pokesalvaje4)  # Creacion de nuevas imagenes
            pokeselec = 0
            ventanaB.focus_force()
        else:
            move_plateada_bosque = 0
            canvas.create_image(250, 350, image=fondo3)  # creacion de imagen en canvas
            mover_ash = canvas.create_image(20, 10, image=ash_down)  # creacion de imagen en canvas
            pikachu_moves = canvas.create_image(20, 30, image=pikachu_down)  # creacion de imagen en canvas
            # Variables globales
            cajanombre = 0
            ash_moves = 0
            x_ini = 680
            y_ini = -230
            func = 1
            pokeactivos = [1, 1, 1, 1]
            posalvaje1 = ubicapoke()[0]
            posalvaje2 = ubicapoke()[1]
            posalvaje3 = ubicapoke()[2]
            posalvaje4 = ubicapoke()[3]
            poke_elejidos = yotelijo()
            pokesalvaje1 = PhotoImage(
                file="imagenes/pokes\pokepos" + str(poke_elejidos[0]) + ".gif")  # Carga de imagenes segun variables
            pokesalvaje2 = PhotoImage(
                file="imagenes/pokes\pokepos" + str(poke_elejidos[1]) + ".gif")  # Carga de imagenes segun variables
            pokesalvaje3 = PhotoImage(
                file="imagenes/pokes\pokepos" + str(poke_elejidos[2]) + ".gif")  # Carga de imagenes segun variables
            pokesalvaje4 = PhotoImage(
                file="imagenes/pokes\pokepos" + str(poke_elejidos[3]) + ".gif")  # Carga de imagenes segun variables
            canvas.create_image(250 + posalvaje1[1], 690 - posalvaje1[0],
                                image=pokesalvaje1)  # Creacion de nuevas imagenes
            canvas.create_image(250 + posalvaje2[1], 690 - posalvaje2[0],
                                image=pokesalvaje2)  # Creacion de nuevas imagenes
            canvas.create_image(250 + posalvaje3[1], 690 - posalvaje3[0],
                                image=pokesalvaje3)  # Creacion de nuevas imagenes
            canvas.create_image(250 + posalvaje4[1], 690 - posalvaje4[0],
                                image=pokesalvaje4)  # Creacion de nuevas imagenes
            pokeselec = 0
            ventanaB.focus_force()

    # Modulo de animacion en la pantalla del bosque
    def bosque_verde(evento):
        # Variables globales
        global ventanaP, ventanaB, ash, x_ini, y_ini, func, fondo3, ash_moves, nombre, \
            cajanombre, canvas, mover_ash, ventana_up, posalvaje1, posalvaje2, posalvaje3, \
            posalvaje4, poke_elejidos, pokeselec, pikachu_moves, pikachuup, \
            pikachur, pikachu_down, pikachul, pokeactivos, pokesalvaje1, \
            pokesalvaje2, pokesalvaje3, pokesalvaje4, move_bosque_paleta, menu, move_batalla
        # Condicional que cuando se presione la tecla abajo, realiza cambios en la animacion del presonaje principal
        # como el moviemiento del mismo, con cambio de posicion del canvas y cambio de imagen del mismo
        if evento.keysym == "Down" and limites_bosque(x_ini, y_ini, "Down") and menu == 0 and move_batalla == 0:
            ash = PhotoImage(file="imagenes/ash/ash_down_min.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 0, 10)
            x_ini -= 10
            pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")
            canvas.itemconfig(pikachu_moves, image=pikachu_down)
            canvas.move(3, 0, 10)
            # Condicionale que previene la entrada en batalla con un pokemon
            # Realiza cambio de variables para que no vuelva a aprecer el mismo
            # Estudia el encuentro con otros por medio de variables
            # realiza cambio de canas, imagenes y posiciones
            if [x_ini, y_ini] == posalvaje1:
                pokeactivos[0] = [0]
                pokeselec = poke_elejidos[0]
                posalvaje1 = 0
                canvas.destroy()
                canvas = Canvas(ventanaB, width=500, height=700)
                canvas.pack()
                fondo3 = PhotoImage(file="imagenes/fondos/bosque_verde.gif")
                ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")
                pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")
                pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")
                pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")
                pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")
                canvas.create_image(250, 350, image=fondo3)
                mover_ash = canvas.create_image(250 + y_ini, 690 - x_ini, image=ash)
                pikachu_moves = canvas.create_image(230 + y_ini, 690 - x_ini, image=pikachuup)
                if pokeactivos[1] == 1:
                    canvas.create_image(250 + posalvaje2[1], 690 - posalvaje2[0], image=pokesalvaje2)
                if pokeactivos[2] == 1:
                    canvas.create_image(250 + posalvaje3[1], 690 - posalvaje3[0], image=pokesalvaje3)
                if pokeactivos[3] == 1:
                    canvas.create_image(250 + posalvaje4[1], 690 - posalvaje4[0], image=pokesalvaje4)
                pygame.mixer.music.stop()
                ventana_batalla()
                # Condicionale que previene la entrada en batalla con un pokemon
                # Realiza cambio de variables para que no vuelva a aprecer el mismo
                # Estudia el encuentro con otros por medio de variables
                # realiza cambio de canas, imagenes y posiciones
            elif [x_ini, y_ini] == posalvaje2:
                pokeactivos[1] = [0]
                pokeselec = poke_elejidos[1]
                posalvaje2 = 0
                canvas.destroy()
                canvas = Canvas(ventanaB, width=500, height=700)
                canvas.pack()
                fondo3 = PhotoImage(file="imagenes/fondos/bosque_verde.gif")
                ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")
                pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")
                pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")
                pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")
                pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")
                canvas.create_image(250, 350, image=fondo3)
                mover_ash = canvas.create_image(250 + y_ini, 690 - x_ini, image=ash)
                pikachu_moves = canvas.create_image(230 + y_ini, 690 - x_ini, image=pikachuup)
                if pokeactivos[0] == 1:
                    canvas.create_image(250 + posalvaje1[1], 690 - posalvaje1[0], image=pokesalvaje1)
                if pokeactivos[2] == 1:
                    canvas.create_image(250 + posalvaje3[1], 690 - posalvaje3[0], image=pokesalvaje3)
                if pokeactivos[3] == 1:
                    canvas.create_image(250 + posalvaje4[1], 690 - posalvaje4[0], image=pokesalvaje4)
                pygame.mixer.music.stop()
                ventana_batalla()
                # Condicionale que previene la entrada en batalla con un pokemon
                # Realiza cambio de variables para que no vuelva a aprecer el mismo
                # Estudia el encuentro con otros por medio de variables
                # realiza cambio de canas, imagenes y posiciones
            elif [x_ini, y_ini] == posalvaje3:
                pokeactivos[2] = [0]
                pokeselec = poke_elejidos[2]
                posalvaje3 = 0
                canvas.destroy()
                canvas = Canvas(ventanaB, width=500, height=700)
                canvas.pack()
                fondo3 = PhotoImage(file="imagenes/fondos/bosque_verde.gif")
                ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")
                pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")
                pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")
                pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")
                pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")
                canvas.create_image(250, 350, image=fondo3)
                mover_ash = canvas.create_image(250 + y_ini, 690 - x_ini, image=ash)
                pikachu_moves = canvas.create_image(230 + y_ini, 690 - x_ini, image=pikachuup)
                if pokeactivos[1] == 1:
                    canvas.create_image(250 + posalvaje2[1], 690 - posalvaje2[0], image=pokesalvaje2)
                if pokeactivos[0] == 1:
                    canvas.create_image(250 + posalvaje1[1], 690 - posalvaje1[0], image=pokesalvaje1)
                if pokeactivos[3] == 1:
                    canvas.create_image(250 + posalvaje4[1], 690 - posalvaje4[0], image=pokesalvaje4)
                pygame.mixer.music.stop()
                ventana_batalla()
                # Condicionale que previene la entrada en batalla con un pokemon
                # Realiza cambio de variables para que no vuelva a aprecer el mismo
                # Estudia el encuentro con otros por medio de variables
                # realiza cambio de canas, imagenes y posiciones
            elif [x_ini, y_ini] == posalvaje4:
                pokeactivos[3] = [0]
                pokeselec = poke_elejidos[3]
                posalvaje4 = 0
                canvas.destroy()
                canvas = Canvas(ventanaB, width=500, height=700)
                canvas.pack()
                fondo3 = PhotoImage(file="imagenes/fondos/bosque_verde.gif")
                ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")
                pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")
                pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")
                pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")
                pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")
                canvas.create_image(250, 350, image=fondo3)
                mover_ash = canvas.create_image(250 + y_ini, 690 - x_ini, image=ash)
                pikachu_moves = canvas.create_image(230 + y_ini, 690 - x_ini, image=pikachuup)
                if pokeactivos[1] == 1:
                    canvas.create_image(250 + posalvaje2[1], 690 - posalvaje2[0], image=pokesalvaje2)
                if pokeactivos[2] == 1:
                    canvas.create_image(250 + posalvaje3[1], 690 - posalvaje3[0], image=pokesalvaje3)
                if pokeactivos[0] == 1:
                    canvas.create_image(250 + posalvaje1[1], 690 - posalvaje1[0], image=pokesalvaje1)
                pygame.mixer.music.stop()
                ventana_batalla()
                # condicional final para tecla abajo, el cual, cumpliendose, destruye la ventana del bosque y regresa a pueblo paleta
            elif x_ini == -20 and -30 < y_ini < 30:
                ventanaB.destroy()
                pygame.mixer.music.stop()
                return mostrar_ventana_paleta()
        # Condicional que cuando se presione la tecla arriba, realiza cambios en la animacion del presonaje principal
        # como el moviemiento del mismo, con cambio de posicion del canvas y cambio de imagen del mismo
        elif evento.keysym == "Up" and limites_bosque(x_ini, y_ini, "Up") and menu == 0 and move_batalla == 0:
            ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 0, -10)
            x_ini += 10
            pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")
            canvas.itemconfig(pikachu_moves, image=pikachuup)
            canvas.move(3, 0, -10)
            ##Unico condicional que la cumplirse destruye la ventana actual y llama la fuencion mostrar_ventana_plateada()
            if x_ini == 690 and y_ini == -230:
                ventanaB.destroy()
                pygame.mixer.music.stop()
                return mostrar_ventana_plateada()
                # Condicionale que previene la entrada en batalla con un pokemon
                # Realiza cambio de variables para que no vuelva a aprecer el mismo
                # Estudia el encuentro con otros por medio de variables
                # realiza cambio de canas, imagenes y posiciones
            elif [x_ini, y_ini] == posalvaje1:
                pokeactivos[0] = [0]
                pokeselec = poke_elejidos[0]
                posalvaje1 = 0
                canvas.destroy()
                canvas = Canvas(ventanaB, width=500, height=700)
                canvas.pack()
                fondo3 = PhotoImage(file="imagenes/fondos/bosque_verde.gif")
                ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")
                pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")
                pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")
                pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")
                pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")
                canvas.create_image(250, 350, image=fondo3)
                mover_ash = canvas.create_image(250 + y_ini, 690 - x_ini, image=ash)
                pikachu_moves = canvas.create_image(230 + y_ini, 690 - x_ini, image=pikachuup)
                if pokeactivos[1] == 1:
                    canvas.create_image(250 + posalvaje2[1], 690 - posalvaje2[0], image=pokesalvaje2)
                if pokeactivos[2] == 1:
                    canvas.create_image(250 + posalvaje3[1], 690 - posalvaje3[0], image=pokesalvaje3)
                if pokeactivos[3] == 1:
                    canvas.create_image(250 + posalvaje4[1], 690 - posalvaje4[0], image=pokesalvaje4)
                pygame.mixer.music.stop()
                ventana_batalla()
                # Condicionale que previene la entrada en batalla con un pokemon
                # Realiza cambio de variables para que no vuelva a aprecer el mismo
                # Estudia el encuentro con otros por medio de variables
                # realiza cambio de canas, imagenes y posiciones
            elif [x_ini, y_ini] == posalvaje2:
                pokeactivos[1] = [0]
                pokeselec = poke_elejidos[1]
                posalvaje2 = 0
                canvas.destroy()
                canvas = Canvas(ventanaB, width=500, height=700)
                canvas.pack()
                fondo3 = PhotoImage(file="imagenes/fondos/bosque_verde.gif")
                ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")
                pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")
                pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")
                pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")
                pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")
                canvas.create_image(250, 350, image=fondo3)
                mover_ash = canvas.create_image(250 + y_ini, 690 - x_ini, image=ash)
                pikachu_moves = canvas.create_image(230 + y_ini, 690 - x_ini, image=pikachuup)
                if pokeactivos[0] == 1:
                    canvas.create_image(250 + posalvaje1[1], 690 - posalvaje1[0], image=pokesalvaje1)
                if pokeactivos[2] == 1:
                    canvas.create_image(250 + posalvaje3[1], 690 - posalvaje3[0], image=pokesalvaje3)
                if pokeactivos[3] == 1:
                    canvas.create_image(250 + posalvaje4[1], 690 - posalvaje4[0], image=pokesalvaje4)
                pygame.mixer.music.stop()
                ventana_batalla()
                # Condicionale que previene la entrada en batalla con un pokemon
                # Realiza cambio de variables para que no vuelva a aprecer el mismo
                # Estudia el encuentro con otros por medio de variables
                # realiza cambio de canas, imagenes y posiciones
            elif [x_ini, y_ini] == posalvaje3:
                pokeactivos[2] = [0]
                pokeselec = poke_elejidos[2]
                posalvaje3 = 0
                canvas.destroy()
                canvas = Canvas(ventanaB, width=500, height=700)
                canvas.pack()
                fondo3 = PhotoImage(file="imagenes/fondos/bosque_verde.gif")
                ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")
                pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")
                pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")
                pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")
                pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")
                canvas.create_image(250, 350, image=fondo3)
                mover_ash = canvas.create_image(250 + y_ini, 690 - x_ini, image=ash)
                pikachu_moves = canvas.create_image(230 + y_ini, 690 - x_ini, image=pikachuup)
                if pokeactivos[1] == 1:
                    canvas.create_image(250 + posalvaje2[1], 690 - posalvaje2[0], image=pokesalvaje2)
                if pokeactivos[0] == 1:
                    canvas.create_image(250 + posalvaje1[1], 690 - posalvaje1[0], image=pokesalvaje1)
                if pokeactivos[3] == 1:
                    canvas.create_image(250 + posalvaje4[1], 690 - posalvaje4[0], image=pokesalvaje4)
                pygame.mixer.music.stop()
                ventana_batalla()
                # Condicionale que previene la entrada en batalla con un pokemon
                # Realiza cambio de variables para que no vuelva a aprecer el mismo
                # Estudia el encuentro con otros por medio de variables
                # realiza cambio de canas, imagenes y posiciones
            elif [x_ini, y_ini] == posalvaje4:
                pokeactivos[3] = [0]
                pokeselec = poke_elejidos[3]
                posalvaje4 = 0
                canvas.destroy()
                canvas = Canvas(ventanaB, width=500, height=700)
                canvas.pack()
                fondo3 = PhotoImage(file="imagenes/fondos/bosque_verde.gif")
                ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")
                pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")
                pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")
                pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")
                pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")
                canvas.create_image(250, 350, image=fondo3)
                mover_ash = canvas.create_image(250 + y_ini, 690 - x_ini, image=ash)
                pikachu_moves = canvas.create_image(230 + y_ini, 690 - x_ini, image=pikachuup)
                if pokeactivos[1] == 1:
                    canvas.create_image(250 + posalvaje2[1], 690 - posalvaje2[0], image=pokesalvaje2)
                if pokeactivos[2] == 1:
                    canvas.create_image(250 + posalvaje3[1], 690 - posalvaje3[0], image=pokesalvaje3)
                if pokeactivos[0] == 1:
                    canvas.create_image(250 + posalvaje1[1], 690 - posalvaje1[0], image=pokesalvaje1)
                pygame.mixer.music.stop()
                ventana_batalla()
        # Condicional que cuando se presione la tecla izquierda, realiza cambios en la animacion del presonaje principal
        # como el moviemiento del mismo, con cambio de posicion del canvas y cambio de imagen del mismo
        elif evento.keysym == "Left" and limites_bosque(x_ini, y_ini, "Left") and menu == 0:
            ash = PhotoImage(file="imagenes/ash/ash_left_min.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, -10, 0)
            y_ini -= 10
            pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")
            canvas.itemconfig(pikachu_moves, image=pikachul)
            canvas.move(3, -10, 0)
            if [x_ini, y_ini] == posalvaje1:
                pokeactivos[0] = [0]
                pokeselec = poke_elejidos[0]
                posalvaje1 = 0
                canvas.destroy()
                canvas = Canvas(ventanaB, width=500, height=700)
                canvas.pack()
                fondo3 = PhotoImage(file="imagenes/fondos/bosque_verde.gif")
                ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")
                pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")
                pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")
                pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")
                pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")
                canvas.create_image(250, 350, image=fondo3)
                mover_ash = canvas.create_image(250 + y_ini, 690 - x_ini, image=ash)
                pikachu_moves = canvas.create_image(230 + y_ini, 690 - x_ini, image=pikachuup)
                if pokeactivos[1] == 1:
                    canvas.create_image(250 + posalvaje2[1], 690 - posalvaje2[0], image=pokesalvaje2)
                if pokeactivos[2] == 1:
                    canvas.create_image(250 + posalvaje3[1], 690 - posalvaje3[0], image=pokesalvaje3)
                if pokeactivos[3] == 1:
                    canvas.create_image(250 + posalvaje4[1], 690 - posalvaje4[0], image=pokesalvaje4)
                pygame.mixer.music.stop()
                ventana_batalla()
            elif [x_ini, y_ini] == posalvaje2:
                pokeactivos[1] = [0]
                pokeselec = poke_elejidos[1]
                posalvaje2 = 0
                canvas.destroy()
                canvas = Canvas(ventanaB, width=500, height=700)
                canvas.pack()
                fondo3 = PhotoImage(file="imagenes/fondos/bosque_verde.gif")
                ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")
                pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")
                pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")
                pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")
                pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")
                canvas.create_image(250, 350, image=fondo3)
                mover_ash = canvas.create_image(250 + y_ini, 690 - x_ini, image=ash)
                pikachu_moves = canvas.create_image(230 + y_ini, 690 - x_ini, image=pikachuup)
                if pokeactivos[0] == 1:
                    canvas.create_image(250 + posalvaje1[1], 690 - posalvaje1[0], image=pokesalvaje1)
                if pokeactivos[2] == 1:
                    canvas.create_image(250 + posalvaje3[1], 690 - posalvaje3[0], image=pokesalvaje3)
                if pokeactivos[3] == 1:
                    canvas.create_image(250 + posalvaje4[1], 690 - posalvaje4[0], image=pokesalvaje4)
                pygame.mixer.music.stop()
                ventana_batalla()
            elif [x_ini, y_ini] == posalvaje3:
                pokeactivos[2] = [0]
                pokeselec = poke_elejidos[2]
                posalvaje3 = 0
                canvas.destroy()
                canvas = Canvas(ventanaB, width=500, height=700)
                canvas.pack()
                fondo3 = PhotoImage(file="imagenes/fondos/bosque_verde.gif")
                ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")
                pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")
                pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")
                pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")
                pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")
                canvas.create_image(250, 350, image=fondo3)
                mover_ash = canvas.create_image(250 + y_ini, 690 - x_ini, image=ash)
                pikachu_moves = canvas.create_image(230 + y_ini, 690 - x_ini, image=pikachuup)
                if pokeactivos[1] == 1:
                    canvas.create_image(250 + posalvaje2[1], 690 - posalvaje2[0], image=pokesalvaje2)
                if pokeactivos[0] == 1:
                    canvas.create_image(250 + posalvaje1[1], 690 - posalvaje1[0], image=pokesalvaje1)
                if pokeactivos[3] == 1:
                    canvas.create_image(250 + posalvaje4[1], 690 - posalvaje4[0], image=pokesalvaje4)
                pygame.mixer.music.stop()
                ventana_batalla()
            elif [x_ini, y_ini] == posalvaje4:
                pokeactivos[3] = [0]
                pokeselec = poke_elejidos[3]
                posalvaje4 = 0
                canvas.destroy()
                canvas = Canvas(ventanaB, width=500, height=700)
                canvas.pack()
                fondo3 = PhotoImage(file="imagenes/fondos/bosque_verde.gif")
                ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")
                pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")
                pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")
                pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")
                pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")
                canvas.create_image(250, 350, image=fondo3)
                mover_ash = canvas.create_image(250 + y_ini, 690 - x_ini, image=ash)
                pikachu_moves = canvas.create_image(230 + y_ini, 690 - x_ini, image=pikachuup)
                if pokeactivos[1] == 1:
                    canvas.create_image(250 + posalvaje2[1], 690 - posalvaje2[0], image=pokesalvaje2)
                if pokeactivos[2] == 1:
                    canvas.create_image(250 + posalvaje3[1], 690 - posalvaje3[0], image=pokesalvaje3)
                if pokeactivos[0] == 1:
                    canvas.create_image(250 + posalvaje1[1], 690 - posalvaje1[0], image=pokesalvaje1)
                pygame.mixer.music.stop()
                ventana_batalla()

            elif x_ini == -20 and -30 < y_ini < 30:
                ventanaB.destroy()
                pygame.mixer.music.stop()
                return mostrar_ventana_paleta()
        elif evento.keysym == "space":
            menu = 1
            return mostrar_ventana_menu()
        # Condicional que cuando se presione la tecla derecha, realiza cambios en la animacion del presonaje principal
        # como el moviemiento del mismo, con cambio de posicion del canvas y cambio de imagen del mismo
        elif evento.keysym == "Right" and limites_bosque(x_ini, y_ini, "Right") and menu == 0:
            ash = PhotoImage(file="imagenes/ash/ash_right_min.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 10, 0)
            y_ini += 10
            pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")
            canvas.itemconfig(pikachu_moves, image=pikachur)
            canvas.move(3, 10, 0)
            # Condicionale que previene la entrada en batalla con un pokemon
            # Realiza cambio de variables para que no vuelva a aprecer el mismo
            # Estudia el encuentro con otros por medio de variables
            # realiza cambio de canas, imagenes y posiciones
            if [x_ini, y_ini] == posalvaje1:
                pokeactivos[0] = [0]
                pokeselec = poke_elejidos[0]
                posalvaje1 = 0
                canvas.destroy()
                canvas = Canvas(ventanaB, width=500, height=700)
                canvas.pack()
                fondo3 = PhotoImage(file="imagenes/fondos/bosque_verde.gif")
                ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")
                pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")
                pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")
                pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")
                pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")
                canvas.create_image(250, 350, image=fondo3)
                mover_ash = canvas.create_image(250 + y_ini, 690 - x_ini, image=ash)
                pikachu_moves = canvas.create_image(230 + y_ini, 690 - x_ini, image=pikachuup)
                if pokeactivos[1] == 1:
                    canvas.create_image(250 + posalvaje2[1], 690 - posalvaje2[0], image=pokesalvaje2)
                if pokeactivos[2] == 1:
                    canvas.create_image(250 + posalvaje3[1], 690 - posalvaje3[0], image=pokesalvaje3)
                if pokeactivos[3] == 1:
                    canvas.create_image(250 + posalvaje4[1], 690 - posalvaje4[0], image=pokesalvaje4)
                pygame.mixer.music.stop()
                ventana_batalla()
                # Condicionale que previene la entrada en batalla con un pokemon
                # Realiza cambio de variables para que no vuelva a aprecer el mismo
                # Estudia el encuentro con otros por medio de variables
                # realiza cambio de canas, imagenes y posiciones
            elif [x_ini, y_ini] == posalvaje2:
                pokeactivos[1] = [0]
                pokeselec = poke_elejidos[1]
                posalvaje2 = 0
                canvas.destroy()
                canvas = Canvas(ventanaB, width=500, height=700)
                canvas.pack()
                fondo3 = PhotoImage(file="imagenes/fondos/bosque_verde.gif")
                ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")
                pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")
                pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")
                pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")
                pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")
                canvas.create_image(250, 350, image=fondo3)
                mover_ash = canvas.create_image(250 + y_ini, 690 - x_ini, image=ash)
                pikachu_moves = canvas.create_image(230 + y_ini, 690 - x_ini, image=pikachuup)
                if pokeactivos[0] == 1:
                    canvas.create_image(250 + posalvaje1[1], 690 - posalvaje1[0], image=pokesalvaje1)
                if pokeactivos[2] == 1:
                    canvas.create_image(250 + posalvaje3[1], 690 - posalvaje3[0], image=pokesalvaje3)
                if pokeactivos[3] == 1:
                    canvas.create_image(250 + posalvaje4[1], 690 - posalvaje4[0], image=pokesalvaje4)
                pygame.mixer.music.stop()
                ventana_batalla()
                # Condicionale que previene la entrada en batalla con un pokemon
                # Realiza cambio de variables para que no vuelva a aprecer el mismo
                # Estudia el encuentro con otros por medio de variables
                # realiza cambio de canas, imagenes y posiciones
            elif [x_ini, y_ini] == posalvaje3:
                pokeactivos[2] = [0]
                pokeselec = poke_elejidos[2]
                posalvaje3 = 0
                canvas.destroy()
                canvas = Canvas(ventanaB, width=500, height=700)
                canvas.pack()
                fondo3 = PhotoImage(file="imagenes/fondos/bosque_verde.gif")
                ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")
                pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")
                pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")
                pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")
                pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")
                canvas.create_image(250, 350, image=fondo3)
                mover_ash = canvas.create_image(250 + y_ini, 690 - x_ini, image=ash)
                pikachu_moves = canvas.create_image(230 + y_ini, 690 - x_ini, image=pikachuup)
                if pokeactivos[1] == 1:
                    canvas.create_image(250 + posalvaje2[1], 690 - posalvaje2[0], image=pokesalvaje2)
                if pokeactivos[0] == 1:
                    canvas.create_image(250 + posalvaje1[1], 690 - posalvaje1[0], image=pokesalvaje1)
                if pokeactivos[3] == 1:
                    canvas.create_image(250 + posalvaje4[1], 690 - posalvaje4[0], image=pokesalvaje4)
                pygame.mixer.music.stop()
                ventana_batalla()
                # Condicionale que previene la entrada en batalla con un pokemon
                # Realiza cambio de variables para que no vuelva a aprecer el mismo
                # Estudia el encuentro con otros por medio de variables
                # realiza cambio de canas, imagenes y posiciones
            elif [x_ini, y_ini] == posalvaje4:
                pokeactivos[3] = [0]
                pokeselec = poke_elejidos[3]
                posalvaje4 = 0
                canvas.destroy()
                canvas = Canvas(ventanaB, width=500, height=700)
                canvas.pack()
                fondo3 = PhotoImage(file="imagenes/fondos/bosque_verde.gif")
                ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")
                pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")
                pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")
                pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")
                pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")
                canvas.create_image(250, 350, image=fondo3)
                mover_ash = canvas.create_image(250 + y_ini, 690 - x_ini, image=ash)
                pikachu_moves = canvas.create_image(230 + y_ini, 690 - x_ini, image=pikachuup)
                if pokeactivos[1] == 1:
                    canvas.create_image(250 + posalvaje2[1], 690 - posalvaje2[0], image=pokesalvaje2)
                if pokeactivos[2] == 1:
                    canvas.create_image(250 + posalvaje3[1], 690 - posalvaje3[0], image=pokesalvaje3)
                if pokeactivos[0] == 1:
                    canvas.create_image(250 + posalvaje1[1], 690 - posalvaje1[0], image=pokesalvaje1)
                pygame.mixer.music.stop()
                ventana_batalla()
            # Condicion que cumplirse, destruye la ventana actual y llama de vuelta a a funcion mostrar_ventana_paleta_ip()
            elif x_ini == -20 and -30 < y_ini < 30:
                ventanaB.destroy()
                pygame.mixer.music.stop()
                return mostrar_ventana_paleta()

    # Se leen del teclado las acciones del jugador para ejecutar la animacion correcta
    ventanaB.bind_all("<Up>", bosque_verde)
    ventanaB.bind_all("<Left>", bosque_verde)
    ventanaB.bind_all("<Right>", bosque_verde)
    ventanaB.bind_all("<Down>", bosque_verde)
    ventanaB.bind_all("<space>", bosque_verde)

    ventanaB.mainloop()


# Se da inicio al modulo del laboratorio
def laboratorio_oak():
    # Variables globales
    global contenedor, ventanaB, mover_ash, fondo_change, cajanombre, \
        ash_moves, x_ini, y_ini, func, canvas, ventana_up, ventanaP, ventanaB, ventanaO, \
        pikachuup, pikachur, pikachul, pikachu_down, pikachu_moves, music_lab, move_bosque_paleta
    # Se carga y reproduce la musica, esta funcion se repite reitaradaveces en este modulo
    pygame.mixer.init()
    pygame.mixer.music.load("musica/laboratorio.mp3")
    pygame.mixer.music.play(-1)
    # Se muestra la pantalla en primer plano
    ventanaO = Toplevel()
    # Se da un titulo a la pantalla
    ventanaO.title("Laboratorio_Oak")
    # Segun los parametros al igual que con la primera pantalla se coloca en el centro del monitor
    ventanaO.update_idletasks()
    ventanaO.focus_force()
    ancho = ventanaO.winfo_screenwidth() - 560
    alto = ventanaO.winfo_screenheight() - 560
    ventanaO.geometry("%dx%d%+d%+d" % (560, 560, ancho / 2, alto / 2))
    # Se crean los canvas que se van a utilizar en este modulo
    canvas = Canvas(ventanaO, width=560, height=560)  # Se crea el canvas a utilizar y se nombra
    canvas.pack()
    fondo4 = PhotoImage(file="imagenes/fondos/lab_oak.gif")  # Se carga iamgen
    ash = PhotoImage(file="imagenes/ash/ash_up.gif")  # Se carga iamgen
    canvas.create_image(280, 280, image=fondo4)  # Se crea la imagen
    mover_ash = canvas.create_image(280, 520, image=ash)  # Se crea la imagen
    pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup.gif")  # Se carga iamgen
    pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down.gif")  # Se carga iamgen
    pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left.gif")  # Se carga iamgen
    pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right.gif")  # Se carga iamgen
    pikachu_moves = canvas.create_image(250, 520, image=pikachu_down)  # Se crea la imagen
    # Se nombran valores a variables globales
    cajanombre = 0
    ash_moves = 0
    x_ini = 0
    y_ini = 0
    func = 1

    # Se ionicia el modulo de animacion dentro del laboratorio
    def move_lab(evento):
        # VAriables globales
        global ventanaP, ventanaB, ash, x_ini, y_ini, func, fondo3, ash_moves, nombre, \
            cajanombre, canvas, mover_ash, ventana_up, ventanaO, \
            pikachuup, pikachur, pikachul, pikachu_down, pikachu_moves, move_bosque_paleta, menu
        # Condicional que cuando se presione la tecla abajo, realiza cambios en la animacion del presonaje principal
        # como el moviemiento del mismo, con cambio de posicion del canvas y cambio de imagen del mismo
        if evento.keysym == "Down" and limites(x_ini, y_ini, "Down") and menu == 0:
            ash = PhotoImage(file="imagenes/ash/ash_down.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 0, 10)
            x_ini -= 10
            pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down.gif")
            canvas.itemconfig(pikachu_moves, image=pikachu_down)
            canvas.move(3, 0, 10)
            if y_ini == 0 and x_ini == 0:
                ventanaO.destroy()
                pygame.mixer.music.stop()
                return ventana_gimnasio()
                # Condicional que cuando se presione la tecla arriba, realiza cambios en la animacion del presonaje principal
                # como el moviemiento del mismo, con cambio de posicion del canvas y cambio de imagen del mismo
        elif evento.keysym == "Up" and limites(x_ini, y_ini, "Up") and menu == 0:
            ash = PhotoImage(file="imagenes/ash/ash_up.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 0, -10)
            x_ini += 10
            pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup.gif")
            canvas.itemconfig(pikachu_moves, image=pikachuup)
            canvas.move(3, 0, -10)
            # Condicional que cuando se presione la tecla izquierda, realiza cambios en la animacion del presonaje principal
            # como el moviemiento del mismo, con cambio de posicion del canvas y cambio de imagen del mismo
        elif evento.keysym == "Left" and limites(x_ini, y_ini, "Left") and menu == 0:
            ash = PhotoImage(file="imagenes/ash/ash_left.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, -10, 0)
            y_ini -= 10
            pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left.gif")
            canvas.itemconfig(pikachu_moves, image=pikachul)
            canvas.move(3, -10, 0)
            if y_ini == 0 and x_ini == 0:
                ventanaO.destroy()
                pygame.mixer.music.stop()
                return mostrar_ventana_paleta()
                # Condicional que cuando se presione la tecla derecha, realiza cambios en la animacion del presonaje principal
                # como el moviemiento del mismo, con cambio de posicion del canvas y cambio de imagen del mismo
        elif evento.keysym == "Right" and limites(x_ini, y_ini, "Right") and menu == 0:
            ash = PhotoImage(file="imagenes/ash/ash_right.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 10, 0)
            y_ini += 10
            pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right.gif")
            canvas.itemconfig(pikachu_moves, image=pikachur)
            canvas.move(3, 10, 0)
            if y_ini == 0 and x_ini == 0:
                ventanaO.destroy()
                pygame.mixer.music.stop()
                return mostrar_ventana_paleta()
        elif evento.keysym == "space":
            menu = 1
            return mostrar_ventana_menu()

    # Lectura de acciones en el teclado para ejecutar acciones segun cada escenario
    ventanaO.bind_all("<Up>", move_lab)
    ventanaO.bind_all("<Left>", move_lab)
    ventanaO.bind_all("<Right>", move_lab)
    ventanaO.bind_all("<Down>", move_lab)
    ventanaO.bind_all("<space>", move_lab)
    ventanaO.mainloop()


# Se inicia el modulo de ventana plateado
def mostrar_ventana_plateada():
    # variables globales
    global contenedor, ventanaB, mover_ash, fondo_change, \
        cajanombre, ash_moves, x_ini, y_ini, func, canvas, ventanaP, \
        ventana, pueblo_paleta, ventana_pl, menu, move_plata_gym, pikachu_down
    # Se inicia la musica en este modulo
    pygame.mixer.init()
    pygame.mixer.music.load("musica/final.mp3")
    pygame.mixer.music.play(-1)
    # Se crea la nueva ventana en primer plano
    ventana_pl = Toplevel()
    ventana_pl.title("Ciudad_Plateada")  # Se nombra la ventana
    ##Segun los parametros del monitor de la pc en la que se juega, se alinea la nueva ventana en el centro del monitor
    ventana_pl.update_idletasks()
    ventana_pl.focus_force()
    ancho = ventana_pl.winfo_screenwidth() - 660
    alto = ventana_pl.winfo_screenheight() - 520
    ventana_pl.geometry("%dx%d%+d%+d" % (660, 520, ancho / 2, alto / 2))
    canvas = Canvas(ventana_pl, width=660, height=520)
    canvas.pack()
    fondo5 = PhotoImage(file="imagenes/fondos/Ciudad_Plateada.gif")  # Se carga una imagen
    canvas.create_image(330, 250, image=fondo5)  # Se crea la imagen
    ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")  # Se carga una imagen
    pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")  # Se carga una imagen
    pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")  # Se carga una imagen
    pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")  # Se carga una imagen
    pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")  # Se carga una imagen
    if move_plata_gym == 0:
        mover_ash = canvas.create_image(300, 500, image=ash)  # Se crea la imagen
        pikachu_moves = canvas.create_image(320, 500, image=pikachuup)  # Se crea la imagen
        # Se asiganan valor a las variables globales
        cajanombre = 0
        ash_moves = 0
        x_ini = 0
        y_ini = 0
        func = 1
    else:
        ash = PhotoImage(file="imagenes/ash/ash_down_min.gif")
        move_plata_gym = 0
        mover_ash = canvas.create_image(240, 330, image=ash)  # Se crea la imagen
        pikachu_moves = canvas.create_image(260, 330, image=pikachu_down)  # Se crea la imagen
        # Se asiganan valor a las variables globales
        cajanombre = 0
        ash_moves = 0
        x_ini = 170
        y_ini = -60
        func = 1

    def ventana_plateada(evento):
        # Variables globales
        global ventanaP, ventanaB, ventana_up, ventana_pl, ash, x_ini, y_ini, func, fondo2, \
            nombre, cajanombre, canvas, mover_ash, Pokemon_beta, \
            ventana_up, pikachuup, pikachur, pikachul, pikachu_down, \
            pikachu_moves, move_plateada_bosque, menu
        # Condicional que cuando se presione la tecla abajo, realiza cambios en la animacion del presonaje principal
        # como el moviemiento del mismo, con cambio de posicion del canvas y cambio de imagen del mismo
        if evento.keysym == "Down" and plateada_limite(x_ini, y_ini, "Down") and menu == 0:
            ash = PhotoImage(file="imagenes/ash/ash_down_min.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 0, 10)
            x_ini -= 10
            pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down_min.gif")
            canvas.itemconfig(pikachu_moves, image=pikachu_down)
            canvas.move(3, 0, 10)
            if x_ini == -10 and -30 < y_ini < 30:
                move_plateada_bosque = 1
                ventana_pl.destroy()
                pygame.mixer.music.stop()
                return mostrar_ventana_bosque(0)
                # Condicional que cuando se presione la tecla arriba, realiza cambios en la animacion del presonaje principal
                # como el moviemiento del mismo, con cambio de posicion del canvas y cambio de imagen del mismo
        elif evento.keysym == "Up" and plateada_limite(x_ini, y_ini, "Up") and menu == 0:
            ash = PhotoImage(file="imagenes/ash/ash_up_min.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 0, -10)
            x_ini += 10
            pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup_min.gif")
            canvas.itemconfig(pikachu_moves, image=pikachuup)
            canvas.move(3, 0, -10)
            if x_ini == 180 and y_ini == -60:
                ventana_pl.destroy()
                pygame.mixer.music.stop()
                return ventana_gimnasio()
                # Condicional que cuando se presione la tecla izquierda, realiza cambios en la animacion del presonaje principal
                # como el moviemiento del mismo, con cambio de posicion del canvas y cambio de imagen del mismo
        elif evento.keysym == "Left" and plateada_limite(x_ini, y_ini, "Left") and menu == 0:
            ash = PhotoImage(file="imagenes/ash/ash_left_min.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, -10, 0)
            y_ini -= 10
            pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left_min.gif")
            canvas.itemconfig(pikachu_moves, image=pikachul)
            canvas.move(3, -10, 0)
            # Accion espacio que abre el menu
        elif evento.keysym == "space":
            menu = 1
            return mostrar_ventana_menu()
            # Condicional que cuando se presione la tecla derecha, realiza cambios en la animacion del presonaje principal
            # como el moviemiento del mismo, con cambio de posicion del canvas y cambio de imagen del mismo
        elif evento.keysym == "Right" and plateada_limite(x_ini, y_ini, "Right") and menu == 0:
            ash = PhotoImage(file="imagenes/ash/ash_right_min.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 10, 0)
            y_ini += 10
            pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right_min.gif")
            canvas.itemconfig(pikachu_moves, image=pikachur)
            canvas.move(3, 10, 0)

    def plateada_limite(x_ini, y_ini, direct):
        if direct == "Up":
            if x_ini == 90 and -200 < y_ini < -110 or \
                                    x_ini == 160 and -130 < y_ini < -60 or \
                                    x_ini == 160 and -60 < y_ini < 10 or \
                                    x_ini == 90 and -40 < y_ini < 0 or \
                                    x_ini == 230 and -220 < y_ini < 10 or \
                                    x_ini == 290 and -180 < y_ini < 10 or \
                                    x_ini == 410 and -260 < y_ini < -190 or \
                                    x_ini == 410 and -190 < y_ini < 220 or \
                                    x_ini == 490 and -250 < y_ini < 260 or \
                                    x_ini == 450 and 10 < y_ini < 150 or \
                                    x_ini == 440 and 210 < y_ini < 270 or \
                                    x_ini == 350 and 130 < y_ini < 220 or \
                                    x_ini == 260 and 50 < y_ini < 150 or \
                                    x_ini == 90 and 50 < y_ini < 130 or \
                                    x_ini == 90 and 140 < y_ini < 220 or \
                                    x_ini == 240 and 220 < y_ini < 370 or \
                                    x_ini == 160 and 60 < y_ini < 200:
                return False
            return True
        if direct == "Down":
            if x_ini == 50 and -230 < y_ini < -20 or \
                                    x_ini == 50 and 20 < y_ini < 270 or \
                                    x_ini == 120 and -40 < y_ini < 0 or \
                                    x_ini == 150 and -200 < y_ini < -110 or \
                                    x_ini == 260 and -230 < y_ini < 0 or \
                                    x_ini == 370 and -180 < y_ini < 10 or \
                                    x_ini == 450 and -250 < y_ini < -190 or \
                                    x_ini == 440 and -190 < y_ini < 220 or \
                                    x_ini == 450 and 30 < y_ini < 150 or \
                                    x_ini == 480 and 90 < y_ini < 150 or \
                                    x_ini == 280 and 220 < y_ini < 270 or \
                                    x_ini == 330 and 50 < y_ini < 120 or \
                                    x_ini == 310 and 110 < y_ini < 150 or \
                                    x_ini == 230 and 50 < y_ini < 200 or \
                                    x_ini == 190 and 190 < y_ini < 220 or \
                                    x_ini == 120 and 60 < y_ini < 130 or \
                                    x_ini == 120 and 140 < y_ini < 210 or \
                                    x_ini == 220 and 240 < y_ini < 360:
                return False
            return True
        if direct == "Left":
            if y_ini == -210 and 40 < x_ini < 410 or \
                                    y_ini == -240 and 400 < x_ini < 500 or \
                                    y_ini == -190 and 410 < x_ini < 450 or \
                                    y_ini == 10 and 160 < x_ini < 370 or \
                                    y_ini == 0 and 90 < x_ini < 120 or \
                                    y_ini == -110 and 90 < x_ini < 150 or \
                                    y_ini == 20 and 430 < x_ini < 460 or \
                                    y_ini == 150 and 430 < x_ini < 450 or \
                                    y_ini == 150 and 450 < x_ini < 480 or \
                                    y_ini == 110 and 470 < x_ini < 500 or \
                                    y_ini == 220 and 350 < x_ini < 440 or \
                                    y_ini == 120 and 300 < x_ini < 330 or \
                                    y_ini == 150 and 260 < x_ini < 310 or \
                                    y_ini == 200 and 180 < x_ini < 230 or \
                                    y_ini == 220 and 90 < x_ini < 190 or \
                                    y_ini == 70 and 110 < x_ini < 170 or \
                                    y_ini == 130 and 90 < x_ini < 120 or \
                                    y_ini == -20 and -30 < x_ini < 50:
                return False
            return True
        if direct == "Right":
            if y_ini == -200 and 90 < x_ini < 150 or \
                                    y_ini == -130 and 160 < x_ini < 240 or \
                                    y_ini == -40 and 90 < x_ini < 120 or \
                                    y_ini == -180 and 290 < x_ini < 370 or \
                                    y_ini == -20 and 250 < x_ini < 300 or \
                                    y_ini == 130 and 350 < x_ini < 420 or \
                                    y_ini == 220 and 240 < x_ini < 280 or \
                                    y_ini == 240 and 270 < x_ini < 450 or \
                                    y_ini == 50 and 260 < x_ini < 330 or \
                                    y_ini == 50 and 90 < x_ini < 230 or \
                                    y_ini == 140 and 90 < x_ini < 120 or \
                                    y_ini == 190 and 110 < x_ini < 170 or \
                                    y_ini == 240 and 40 < x_ini < 220 or \
                                    y_ini == 350 and 200 < x_ini < 250 or \
                                    y_ini == 210 and 440 < x_ini < 500 or \
                                    y_ini == 20 and -30 < x_ini < 50:
                return False
            return True

    ventana_pl.bind_all("<Up>", ventana_plateada)
    ventana_pl.bind_all("<Left>", ventana_plateada)
    ventana_pl.bind_all("<Right>", ventana_plateada)
    ventana_pl.bind_all("<Down>", ventana_plateada)
    ventana_pl.bind_all("<space>", ventana_plateada)
    ventana_pl.mainloop()


# Se crea la ventana que sera el menu
def mostrar_ventana_menu():
    # VAriables globales
    global contenedor, ventanaB, fondo_change, \
        cajanombre, ash_moves, x_ini, y_ini, func, canvas, \
        ventanaP, ventana, pueblo_paleta, ventana_pl, menu, \
        valor_flecha, move_flecha, menu_fondo, move_flecha, menu2, \
        menu3, fondo_menu1, lista_pokemon, ventana_pokes, poke_list
    # Se crea, se nombra y se centra la nueva ventana en el monitro
    ventana_menu = Toplevel()
    ventana_menu.title("Menu")
    ventana_menu.update_idletasks()
    ventana_menu.focus_force()
    ancho = ventana_menu.winfo_screenwidth() - 293
    alto = ventana_menu.winfo_screenheight() - 467
    ventana_menu.geometry("%dx%d%+d%+d" % (293, 467, ancho / 2, alto / 2))
    fondo6 = PhotoImage(file="imagenes/menu/menu1.gif")
    menu2 = PhotoImage(file="imagenes/menu/menu2.gif")
    menu3 = PhotoImage(file="imagenes/menu/menu3.gif")
    fondo_menu1 = Label(ventana_menu, image=fondo6).place(x=0, y=0)
    move_flecha = 0

    # Se da inicio al modulo de animacion dentro de ventana menu
    def mostrar_ventana_menu(evento):
        # Variables globales
        global ventana_up, \
            func, fondo2, nombre, \
            cajanombre, Pokemon_beta, menu, move_flecha, menu2, menu3, \
            fondo_menu1, lista_pokemon, ventana_pokes, poke_list
        # Condicionales que segun eventos del teclado por el usuario cierran el menu o el juego por completo
        if evento.keysym == "s" and poke_list == 0:
            menu = 0
            ventana_menu.destroy()
        if evento.keysym == "s" and poke_list == 1:
            poke_list = 0
            ventana_pokes.destroy()
        if evento.keysym == "f" and move_flecha < 2 and poke_list == 0:
            if move_flecha == 0:
                move_flecha += 1
                Label(ventana_menu, image=menu2).place(x=-1, y=-1)
            else:
                move_flecha += 1
                Label(ventana_menu, image=menu3).place(x=-1, y=1)
        if evento.keysym == "d" and move_flecha > 0 and poke_list == 0:
            if move_flecha == 1:
                move_flecha -= 1
                Label(ventana_menu, image=fondo6).place(x=0, y=0)
            if move_flecha == 2:
                move_flecha -= 1
                Label(ventana_menu, image=menu2).place(x=-1, y=-1)
        if evento.keysym == "a" and move_flecha == 2 and poke_list == 0:
            ventana_menu.destroy()
            ventana.destroy()
        if evento.keysym == "a" and move_flecha == 0 and poke_list == 0:
            poke_list = 1
            ventana_pokes = Toplevel()
            ventana_pokes.title("Pokemon")
            ventana_pokes.update_idletasks()
            ventana_pokes.focus_force()
            ancho = ventana_pokes.winfo_screenwidth() - 293
            alto = ventana_pokes.winfo_screenheight() - 467
            ventana_pokes.geometry("%dx%d%+d%+d" % (293, 467, ancho / 2, alto / 2))
            Label(ventana_pokes, text=lista_pokemon[0]).place(x=10, y=50)
            Label(ventana_pokes, text=lista_pokemon[1]).place(x=10, y=180)
            Label(ventana_pokes, text=lista_pokemon[2]).place(x=10, y=300)
            # Lectura de acciones en el teclado para ejecutar acciones segun cada escenario

    ventana_menu.bind_all("<f>", mostrar_ventana_menu)
    ventana_menu.bind_all("<d>", mostrar_ventana_menu)
    ventana_menu.bind_all("<s>", mostrar_ventana_menu)
    ventana_menu.bind_all("<a>", mostrar_ventana_menu)
    ventana_menu.mainloop()


# Modulo ventana batalla en el cual se da la animacion completa de los enfrentamientos contra los pokemon
def ventana_batalla():
    # Variables globales
    global vida, pokelife, pokemon, nombre, opcion, canvaBattalla, attack, \
        fondoBatalla, atacante, pokecanva, pokeataca, pokeselec, pokemios, move_batalla
    # Inicio a la musica
    pygame.mixer.init()
    pygame.mixer.music.load("musica/batalla.mp3")
    pygame.mixer.music.play(-1)
    move_batalla = 1
    # Se coloca la ventana en primer plano y centrada en el monitor
    ventanaBatalla = Toplevel()
    ventanaBatalla.title("Batalla Pokemon")
    ventanaBatalla.update_idletasks()
    ventanaBatalla.focus_force()
    ancho = ventanaBatalla.winfo_screenwidth() - 340
    alto = ventanaBatalla.winfo_screenheight() - 200
    ventanaBatalla.geometry("%dx%d%+d%+d" % (340, 200, ancho / 2, alto / 2))
    # Variables globales
    vida = 6
    pokelife = 14
    pokemon = 0
    opcion = 2
    hiperattack = 3
    # Se crea el canvas y las imagenes que se colocan en este
    canvaBattalla = Canvas(ventanaBatalla, width=340, height=200)
    canvaBattalla.pack()
    fondoBatalla = PhotoImage(file="imagenes/pokes\Battle_White - Placaje 1.gif")
    attack = canvaBattalla.create_image(170, 100, image=fondoBatalla)
    pokeataca = PhotoImage(file="imagenes/pokes\poke" + str(pokeselec) + str(4) + ".gif")
    atacante = canvaBattalla.create_image(170, 53, image=pokeataca)
    nombreattack = Label(ventanaBatalla, text=nombre, bg="darkgreen")
    nombreattack.pack()
    nombreattack.place(x=80, y=5)
    nombreattack.config(text="Batalla Pokemon de" + nombre, font=("Helvetica", 8), fg="white")

    # Modulo interno de animacion de batalla, en este se da la animacion por completo de batalla, con variables gnerales
    # Se cambian las imagenes de cada uno de los enventos o selecciones
    def hora_del_duelo(event):
        # Variables globales
        global vida, pokelife, pokemon, opcion, attack, fondoBatalla, \
            pokeselec, atacante, pokeataca, pokemios, hiperattack, lista_pokemon, move_batalla, cantidad_poke
        # Condicion que la cumplir cierra la venta actual, detiene la musica y coloca de nuevo la del bosque
        if vida <= 1:
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load("musica/bosque.mp3")
            pygame.mixer.music.play(-1)
            ventanaBatalla.destroy()
            move_batalla = 0
            return mostrar_ventana_bosque(1)
        # Condicion que la cumplir cierra la venta actual, detiene la musica y coloca de nuevo la del bosque
        elif pokelife < 4 and event.keysym == "a":
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load("musica/bosque.mp3")
            pygame.mixer.music.play(-1)
            ventanaBatalla.destroy()
            move_batalla = 0
            return mostrar_ventana_bosque(1)
        # Condicion que la cumplir cierra la venta actual, detiene la musica y coloca de nuevo la del bosque
        if event.keysym == "a" and opcion == 2:
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load("musica/bosque.mp3")
            pygame.mixer.music.play(-1)
            ventanaBatalla.destroy()
            move_batalla = 0
            return mostrar_ventana_bosque(1)
        # Condicional que segun la vida y la accion del jugador, cambia las imagenes para dar animacion
        elif event.keysym == "a" and opcion == 3:
            pokelife -= 4
            vida -= 1
            fondoBatalla = PhotoImage(file="imagenes/pokes\Battle_White - Impactrueno " + str(vida) + ".gif")
            canvaBattalla.itemconfig(attack, image=fondoBatalla)
            if 12 > pokelife >= 8:
                pokeataca = PhotoImage(file="imagenes/pokes\poke" + str(pokeselec) + str(3) + ".gif")
                canvaBattalla.itemconfig(atacante, image=pokeataca)
            elif 8 > pokelife >= 6:
                pokeataca = PhotoImage(file="imagenes/pokes\poke" + str(pokeselec) + str(2) + ".gif")
                canvaBattalla.itemconfig(atacante, image=pokeataca)
            elif 6 > pokelife >= 4:
                pokeataca = PhotoImage(file="imagenes/pokes\poke" + str(pokeselec) + str(1) + ".gif")
                canvaBattalla.itemconfig(atacante, image=pokeataca)
            elif pokelife < 4:
                canvaBattalla.destroy()
                canvaBattalla2 = Canvas(ventanaBatalla, width=340, height=200)
                canvaBattalla2.pack()
                fondoBatalla = PhotoImage(file="imagenes/pokes\escapado.gif")
                attack = canvaBattalla2.create_image(170, 100, image=fondoBatalla)
        # Condicional que segun la accion elejida por el juagdor, indica si la vida del pokemon le permite ser capturado
        elif event.keysym == "a" and opcion == 4 and pokelife == 6:
            canvaBattalla.destroy()
            canvaBattalla2 = Canvas(ventanaBatalla, width=340, height=200)
            canvaBattalla2.pack()
            fondoBatalla = PhotoImage(file="imagenes/pokes\Capturado.gif")
            attack = canvaBattalla2.create_image(170, 100, image=fondoBatalla)
            pokelife = 0
            move_batalla = 0
            cantidad_poke += 1
            if pokeselec == 1:
                lista_pokemon += ["charizard"]
                print(lista_pokemon)
            if pokeselec == 2:
                lista_pokemon += ["venusaur"]
                print(lista_pokemon)
            if pokeselec == 3:
                lista_pokemon += ["pikachu"]
                print(lista_pokemon)
            if pokeselec == 4:
                lista_pokemon += ["blastoise"]
                print(lista_pokemon)
            if pokeselec == 5:
                lista_pokemon += ["raticate"]
                print(lista_pokemon)
            if pokeselec == 6:
                lista_pokemon += ["pidgeot"]
                print(lista_pokemon)
            if pokeselec == 7:
                lista_pokemon += ["raichu"]
                print(lista_pokemon)

        # Condicional que indica si la vida del poke es suficiente para que este escape en ves de ser capturado
        # por medio de variables
        elif event.keysym == "a" and opcion == 4 and pokelife == 6:
            canvaBattalla.destroy()
            canvaBattalla2 = Canvas(ventanaBatalla, width=340, height=200)
            canvaBattalla2.pack()
            fondoBatalla = PhotoImage(file="imagenes/pokes\escapado.gif")
            attack = canvaBattalla2.create_image(170, 100, image=fondoBatalla)
            pokelife = 0
            move_batalla = 0
        # Condicional que cambia imagenes para dar la animacion de selecion y movimiento en pantalla
        elif event.keysym == "Right" and opcion == 2:
            opcion = 3
            fondoBatalla = PhotoImage(file="imagenes/pokes\Battle_White - Impactrueno " + str(vida) + ".gif")
            canvaBattalla.itemconfig(attack, image=fondoBatalla)
            if 12 > pokelife >= 8:
                pokeataca = PhotoImage(file="imagenes/pokes\poke" + str(pokeselec) + str(3) + ".gif")
                canvaBattalla.itemconfig(atacante, image=pokeataca)
            elif 8 > pokelife >= 6:
                pokeataca = PhotoImage(file="imagenes/pokes\poke" + str(pokeselec) + str(2) + ".gif")
                canvaBattalla.itemconfig(atacante, image=pokeataca)
            elif 6 > pokelife >= 4:
                pokeataca = PhotoImage(file="imagenes/pokes\poke" + str(pokeselec) + str(1) + ".gif")
                canvaBattalla.itemconfig(atacante, image=pokeataca)
            print("Fun 2")
        # Condicional que cambia imagenes para dar la animacion de selecion y movimiento en pantalla
        elif event.keysym == "Right" and opcion == 3:
            opcion = 4
            fondoBatalla = PhotoImage(file="imagenes/pokes\Battle_White -  Atrapar " + str(vida) + ".gif")
            canvaBattalla.itemconfig(attack, image=fondoBatalla)
            if 12 > pokelife >= 8:
                pokeataca = PhotoImage(file="imagenes/pokes\poke" + str(pokeselec) + str(3) + ".gif")
                canvaBattalla.itemconfig(atacante, image=pokeataca)
            elif 8 > pokelife >= 6:
                pokeataca = PhotoImage(file="imagenes/pokes\poke" + str(pokeselec) + str(2) + ".gif")
                canvaBattalla.itemconfig(atacante, image=pokeataca)
            elif 6 > pokelife >= 4:
                pokeataca = PhotoImage(file="imagenes/pokes\poke" + str(pokeselec) + str(1) + ".gif")
                canvaBattalla.itemconfig(atacante, image=pokeataca)
            print("Fun 3")
        # Condicional que cambia imagenes para dar la animacion de selecion y movimiento en pantalla
        elif event.keysym == "Left" and opcion == 4:
            opcion = 3
            fondoBatalla = PhotoImage(file="imagenes/pokes\Battle_White - Impactrueno " + str(vida) + ".gif")
            canvaBattalla.itemconfig(attack, image=fondoBatalla)
            if 12 > pokelife >= 8:
                pokeataca = PhotoImage(file="imagenes/pokes\poke" + str(pokeselec) + str(3) + ".gif")
                canvaBattalla.itemconfig(atacante, image=pokeataca)
            elif 8 > pokelife >= 6:
                pokeataca = PhotoImage(file="imagenes/pokes\poke" + str(pokeselec) + str(2) + ".gif")
                canvaBattalla.itemconfig(atacante, image=pokeataca)
            elif 6 > pokelife >= 4:
                pokeataca = PhotoImage(file="imagenes/pokes\poke" + str(pokeselec) + str(1) + ".gif")
                canvaBattalla.itemconfig(atacante, image=pokeataca)
            print("Fun 4")
        # Condicional que cambia imagenes para dar la animacion de selecion y movimiento en pantalla
        elif event.keysym == "Left" and opcion == 3:
            opcion = 2
            fondoBatalla = PhotoImage(file="imagenes/pokes\Battle_White - Placaje " + str(vida) + ".gif")
            canvaBattalla.itemconfig(attack, image=fondoBatalla)
            if 12 > pokelife >= 8:
                pokeataca = PhotoImage(file="imagenes/pokes\poke" + str(pokeselec) + str(3) + ".gif")
                canvaBattalla.itemconfig(atacante, image=pokeataca)
            elif 8 > pokelife >= 6:
                pokeataca = PhotoImage(file="imagenes/pokes\poke" + str(pokeselec) + str(2) + ".gif")
                canvaBattalla.itemconfig(atacante, image=pokeataca)
            elif 6 > pokelife >= 4:
                pokeataca = PhotoImage(file="imagenes/pokes\poke" + str(pokeselec) + str(1) + ".gif")
                canvaBattalla.itemconfig(atacante, image=pokeataca)
            print("Fun 5")

    ventana.bind_all("<a>", hora_del_duelo)
    ventana.bind_all("<Left>", hora_del_duelo)
    ventana.bind_all("<Right>", hora_del_duelo)

    ventanaBatalla.mainloop()


def ventana_gimnasio():
    global contenedor, mover_ash, fondo_change, \
        cajanombre, ash_moves, x_ini, y_ini, func, canvas, ventanaG, \
        ventana, pueblo_paleta, pikachu_moves, move_plata_gym, bloque_conec, cantidad_poke
    # Se carga y reproduce la musica en este escenario
    pygame.mixer.init()
    pygame.mixer.music.load("musica/Azalea Town.mp3")
    pygame.mixer.music.play(-1)
    # Se crea al nueva ventana y se muestra en primer plano
    ventanaG = Toplevel()
    ventanaG.title("centro")  # Se le da un nuevo nombre a la ventana
    ### Con distintos parametros de se coloca la ventana principal en el centro de la pantalla de la computadora
    ventanaG.focus_force()
    ventanaG.update_idletasks()
    ancho = ventanaG.winfo_screenwidth() - 660
    alto = ventanaG.winfo_screenheight() - 440
    ventanaG.geometry("%dx%d%+d%+d" % (660, 440, ancho / 2, alto / 2))
    # Se crea el primer canvas en el cual se montan las imagenes
    canvas = Canvas(ventanaG, width=660, height=660)
    canvas.pack()
    fondo7 = PhotoImage(file="imagenes/fondos/gimnasio.gif")  # Se carga una imagen
    ash = PhotoImage(file="imagenes/ash/ash_up.gif")  # Se carga una imagen
    canvas.create_image(330, 220, image=fondo7)  # Se crea la imagen
    mover_ash = canvas.create_image(310, 350, image=ash)  # Se crea la imagen
    pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup.gif")  # Se carga una imagen
    pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down.gif")  # Se carga una imagen
    pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left.gif")  # Se carga una imagen
    pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right.gif")  # Se carga una imagen
    pikachu_moves = canvas.create_image(340, 350, image=pikachuup)  # Se crea la imagen
    # Se asigna un valor a las variables globales
    cajanombre = 0
    ash_moves = 0
    x_ini = 0
    y_ini = 0
    func = 1

    # Se da incio al modulo de animacion en esta ventana
    def ventana_gimnasio(evento):
        # VAriables globales
        global ventanaG, ash, x_ini, y_ini, func, fondo2, ash_moves, contador, \
            contador2, pikachu_moves, nombre, cajanombre, \
            canvas, mover_ash, Pokemon_beta, pikachul, pikachur, \
            pikachuup, pikachu_down, pikachu_moves, move_bosque_paleta, menu, move_plata_gym, bloqueo_conec, cantidad_poke
        # Condicionales que segun el evento o tecla presionada crean una accion y de esta forma se le da animacion al juego
        # Las acciones normalmento son cambio de imagenes en los canvas ya creados, en estos condicionales se puede dar
        # un cambio del valor en variables, llamada a nueva ventanas o lo explicado ateriormente, cambio de imagenes en canvas
        # Condicional del enevento o tecla abajo
        if evento.keysym == "Down" and gimansio_limite(x_ini, y_ini, "Down") and bloqueo_conec == 0:
            ash = PhotoImage(file="imagenes/ash/ash_down.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 0, 10)
            x_ini -= 10
            pikachu_down = PhotoImage(file="imagenes/pikachu/pika_down.gif")
            canvas.itemconfig(pikachu_moves, image=pikachu_down)
            canvas.move(3, 0, 10)
            if x_ini == -10 and -10 < y_ini < 40:
                move_plata_gym = 1
                ventanaG.destroy()
                pygame.mixer.music.stop()
                return mostrar_ventana_plateada()

                # Condicional del enevento o tecla arriba
        elif evento.keysym == "Up" and gimansio_limite(x_ini, y_ini, "Up") and bloqueo_conec == 0:
            ash = PhotoImage(file="imagenes/ash/ash_up.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 0, -10)
            x_ini += 10
            pikachuup = PhotoImage(file="imagenes/pikachu/pikachuup.gif")
            canvas.itemconfig(pikachu_moves, image=pikachuup)
            canvas.move(3, 0, -10)
            # Condicional del enevento o tecla izquierda
        elif evento.keysym == "Left" and gimansio_limite(x_ini, y_ini, "Left") and bloqueo_conec == 0:
            ash = PhotoImage(file="imagenes/ash/ash_left.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, -10, 0)
            y_ini -= 10
            pikachul = PhotoImage(file="imagenes/pikachu/pikachu_left.gif")
            canvas.itemconfig(pikachu_moves, image=pikachul)
            canvas.move(3, -10, 0)
        elif evento.keysym == "Right" and gimansio_limite(x_ini, y_ini, "Right") and bloqueo_conec == 0:
            ash = PhotoImage(file="imagenes/ash/ash_right.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 10, 0)
            y_ini += 10
            pikachur = PhotoImage(file="imagenes/pikachu/pikachu_right.gif")
            canvas.itemconfig(pikachu_moves, image=pikachur)
            canvas.move(3, 10, 0)
        elif evento.keysym == "w" and x_ini == 250 and y_ini == 190 and bloqueo_conec == 0 and cantidad_poke >= 3:
            return mostrar_ventana_conec()
        elif evento.keysym == "space":
            menu = 1
            return mostrar_ventana_menu()

    def gimansio_limite(x_ini, y_ini, direct):
        if direct == "Up":
            if x_ini == 10 and 150 < y_ini < 280 or \
                                    x_ini == 250 and 170 < y_ini < 230 or \
                                    x_ini == 220 and -190 < y_ini < -140 or \
                                    x_ini == 250 and -330 < y_ini < -160 or \
                                    x_ini == 180 and -160 < y_ini < 190 or \
                                    x_ini == 90 and -20 < y_ini < 50 or \
                                    x_ini == 0 and -150 < y_ini < -80 or \
                                    x_ini == 30 and -310 < y_ini < -210 or \
                                    x_ini == 270 and 210 < y_ini < 360 or \
                                    x_ini == 230 and 280 < y_ini < 350:
                return False
            else:
                return True
        if direct == "Down":
            if x_ini == 150 and -290 < y_ini < -210 or \
                                    x_ini == 100 and -160 < y_ini < -80 or \
                                    x_ini == 0 and -270 < y_ini < 0 or \
                                    x_ini == 0 and 30 < y_ini < 310 or \
                                    x_ini == 180 and -20 < y_ini < 50 or \
                                    x_ini == 170 and 150 < y_ini < 280 or \
                                    x_ini == 130 and 280 < y_ini < 350:
                return False
            else:
                return True
        if direct == "Left":
            if y_ini == -200 and 0 < x_ini < 150 or \
                                    y_ini == -80 and 0 < x_ini < 100 or \
                                    y_ini == -260 and -10 < x_ini < 40 or \
                                    y_ini == -280 and 150 < x_ini < 260 or \
                                    y_ini == 50 and 90 < x_ini < 180 or \
                                    y_ini == 280 and 10 < x_ini < 170 or \
                                    y_ini == 190 and 180 < x_ini < 260 or \
                                    y_ini == 230 and 250 < x_ini < 280 or \
                                    y_ini == -210 and 30 < x_ini < 150:
                return False
            return True
        if direct == "Right":
            if y_ini == -190 and 220 < x_ini < 260 or \
                                    y_ini == -160 and 180 < x_ini < 230 or \
                                    y_ini == -20 and 90 < x_ini < 180 or \
                                    y_ini == 150 and 10 < x_ini < 170 or \
                                    y_ini == 280 and -10 < x_ini < 130 or \
                                    y_ini == -150 and 0 < x_ini < 100 or \
                                    y_ini == 280 and 230 < x_ini < 280 or \
                                    y_ini == 320 and 120 < x_ini < 240:
                return False
            return True

    ventanaG.bind_all("<Up>", ventana_gimnasio)
    ventanaG.bind_all("<Left>", ventana_gimnasio)
    ventanaG.bind_all("<Right>", ventana_gimnasio)
    ventanaG.bind_all("<Down>", ventana_gimnasio)
    ventanaG.bind_all("<w>", ventana_gimnasio)
    ventanaG.bind_all("<space>", ventana_gimnasio)
    ventanaG.mainloop()


def mostrar_ventana_conec():
    # VAriables globales
    global contenedor, ventana_conec, fondo_change, \
        cajanombre, ash_moves, x_ini, y_ini, func, canvas, \
        ventanaP, ventana, pueblo_paleta, ventana_pl, menu, \
        valor_flecha, move_flecha, menu_fondo, conec1, \
        conec2, fondo_menu1, lista_pokemon, ventana_pokes, poke_list, move_conec, bloqueo_conec, bloqueo_acept
    # Se crea, se nombra y se centra la nueva ventana en el monitro
    ventana_conec = Toplevel()
    ventana_conec.title("Conexion")
    ventana_conec.update_idletasks()
    ventana_conec.focus_force()
    ancho = ventana_conec.winfo_screenwidth() - 293
    alto = ventana_conec.winfo_screenheight() - 467
    ventana_conec.geometry("%dx%d%+d%+d" % (500, 312, ancho / 2, alto / 2))
    conec1 = PhotoImage(file="imagenes/menu_conec/fondo_conexion_server.gif")
    conec2 = PhotoImage(file="imagenes/menu_conec/fondo_conexion_cliente.gif")
    move_conec = 0
    Label(ventana_conec, image=conec1).place(x=0, y=0)
    bloqueo_conec = 1
    bloqueo_acept = 0

    # Se da inicio al modulo de animacion dentro de ventana menu
    def mostrar_conec(evento):
        # Variables globales
        global ventana_conec, \
            func, fondo2, nombre, \
            cajanombre, Pokemon_beta, menu, move_flecha, menu2, menu3, \
            fondo_menu1, lista_pokemon, ventana_pokes, poke_list, move_conec, bloqueo_conec, bloqueo_acept
        # Condicionales que segun eventos del teclado por el usuario cierran el menu o el juego por completo
        if evento.keysym == "s":
            bloqueo_acept = 1
            bloqueo_conec = 0
            move_conec = 0
            ventana_conec.destroy()
        if evento.keysym == "f" and move_conec < 1 and poke_list == 0:
            move_conec += 1
            Label(ventana_conec, image=conec2).place(x=0, y=0)
        if evento.keysym == "d" and move_conec > 0 and poke_list == 0:
            move_conec -= 1
            Label(ventana_conec, image=conec1).place(x=0, y=0)
        if evento.keysym == "a" and move_conec == 1 and poke_list == 0 and bloqueo_acept == 0:
            ventana_conec.destroy()
            ventana.destroy()
            return mostrar_tablero()
        if evento.keysym == "a" and move_conec == 0 and poke_list == 0 and bloqueo_acept == 0:
            ventana_conec.destroy()
            ventana.destroy()
            return mostrar_tablero()

            # Lectura de acciones en el teclado para ejecutar acciones segun cada escenario

    ventana_conec.bind_all("<d>", mostrar_conec)
    ventana_conec.bind_all("<f>", mostrar_conec)
    ventana_conec.bind_all("<s>", mostrar_conec)
    ventana_conec.bind_all("<a>", mostrar_conec)
    ventana_conec.mainloop()


# Lectura de acciones en el teclado para ejecutar acciones segun cada escenario
ventana.bind_all("<Up>", mover_ash)
ventana.bind_all("<Left>", mover_ash)
ventana.bind_all("<Right>", mover_ash)
ventana.bind_all("<Down>", mover_ash)
ventana.bind_all("<space>", mover_ash)

# Se da inicio el programa ejecuntandolo apenas se corre este
ventana.mainloop()
