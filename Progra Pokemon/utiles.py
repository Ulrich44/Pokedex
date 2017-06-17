# Se importan las librerias
from random import randrange
from random import choice


# Por medios de condicionales se asigan los obstaculas para que la animacion del personaje principal no
# de la apariencia de que atraviesa cosas, un condicional distinto para cada pantalla
def limites(x_ini, y_ini, direc):
    if direc == "Up":
        if (x_ini == 130 and y_ini < -40) \
                or (x_ini == 130 and y_ini > 40) \
                or (x_ini == 280 and (40 < y_ini < 200)) \
                or (x_ini == 270 and (-230 < y_ini < -120)) \
                or (x_ini == 320 and (-260 < y_ini < -220)
                    or x_ini == 420):
            return False
        return True
    if direc == "Down":
        if (x_ini == 220 and y_ini < -40) \
                or (x_ini == 220 and y_ini > 40) \
                or (x_ini == 350 and (40 < y_ini < 200)) \
                or (x_ini == 380 and (-280 < y_ini < -120)) \
                or (x_ini == 400 and (-260 < y_ini < -200)) \
                or (x_ini == 70 and -200 > y_ini) \
                or (x_ini == 70 and 200 < y_ini) \
                or (x_ini == 400 and (70 < y_ini < 160)) \
                or x_ini == 0:
            return False
        return True
    if direc == "Left":
        if (50 < x_ini < 430) and y_ini == -240 \
                or (240 < x_ini < 380) and y_ini == -120 \
                or (410 < x_ini < 430) and y_ini == 0 \
                or (130 < x_ini < 220) and y_ini == -40 \
                or (-10 < x_ini < 70) and y_ini == -200 \
                or (280 < x_ini < 370) and y_ini == 200 \
                or (340 < x_ini < 400) and y_ini == 160 \
                or x_ini == 380 and y_ini == -200 \
                or (380 < x_ini < 400) and y_ini == -200:
            return False
        return True
    if direc == "Right":
        if (60 < x_ini < 430) and y_ini == 240 \
                or (-10 < x_ini < 70) and y_ini == 200 \
                or (130 < x_ini < 220) and y_ini == 40 \
                or (240 < x_ini < 290) and y_ini == -240 \
                or (280 < x_ini < 350) and y_ini == 40 \
                or (340 < x_ini < 400) and y_ini == 80 \
                or (410 < x_ini < 430) and y_ini == 80:
            return False
        return True


# Por medios de condicionales se asigan los obstaculas para que la animacion del personaje principal no
# de la apariencia de que atraviesa cosas, un condicional distinto para cada pantalla
def limites_paleta(x_ini, y_ini, direct):
    if direct == "Up":
        if x_ini == 0 and (-100 < y_ini < 0) or x_ini == 0 and 0 < y_ini < 100 \
                or x_ini == 70 and (-350 < y_ini < -200) \
                or x_ini == -120 and (-100 < y_ini < 100) \
                or x_ini == 200 and (-370 < y_ini < -190) \
                or x_ini == 200 and (-100 < y_ini < 80) \
                or x_ini == 370 and (-430 < y_ini < -160) \
                or x_ini == 370 and (-110 < y_ini < 180):
            return False
        return True
    if direct == "Down":
        if x_ini == 160 and (-100 < y_ini < 100) \
                or x_ini == 110 and (-350 < y_ini < -200) \
                or x_ini == -80 and (-100 < y_ini < 100) or x_ini == -60 and (-20 < y_ini < 20) \
                or x_ini == 350 and (-350 < y_ini < -190) \
                or x_ini == 350 and (-80 < y_ini < 80) \
                or x_ini == -180 and (-190 < y_ini < 10) \
                or x_ini == -120 and (0 < y_ini < 160) \
                or x_ini == -30 and (-440 < y_ini < -180) \
                or x_ini == 260 and (-100 < y_ini < -60) \
                or x_ini == 260 and (-370 < y_ini < -330):
            return False
        return True
    if direct == "Left":
        if y_ini == -420 and (-40 < x_ini < 400) \
                or y_ini == -180 and (-190 < x_ini < -30) \
                or y_ini == -200 and (70 < x_ini < 110) \
                or y_ini == 100 and (-120 < x_ini < -80) \
                or y_ini == 20 and (-90 < x_ini < -60) \
                or y_ini == 100 and (0 < x_ini < 160) \
                or y_ini == 80 and (200 < x_ini < 350) \
                or y_ini == -190 and (200 < x_ini < 350) \
                or y_ini == -160 and (370 < x_ini < 450) \
                :
            return False
        return True
    if direct == "Right":
        if y_ini == 140 and (-130 < x_ini < 400) \
                or y_ini == -100 and (0 < x_ini < 160) \
                or y_ini == -100 and (200 < x_ini < 260) \
                or y_ini == -80 and (250 < x_ini < 350) \
                or y_ini == -370 and (200 < x_ini < 260) \
                or y_ini == -350 and (250 < x_ini < 350) \
                or y_ini == -100 and (-120 < x_ini < -80) \
                or y_ini == -20 and (-90 < x_ini < -60) \
                or y_ini == -350 and (70 < x_ini < 110) \
                or y_ini == -110 and (370 < x_ini < 450) \
                or y_ini == 0 and (-200 < x_ini < -120):
            return False
        return True


# Por medios de condicionales se asigan los obstaculas para que la animacion del personaje principal no
# de la apariencia de que atraviesa cosas, un condicional distinto para cada pantalla
def limites_bosque(x_ini, y_ini, direct):
    if direct == "Up":
        if x_ini == 670 and (-170 < y_ini < 240) \
                or x_ini == 100 and (160 < y_ini < 240) \
                or x_ini == 210 and (160 < y_ini < 210) \
                or x_ini == 420 and (130 < y_ini < 200) \
                or x_ini == 570 and (20 < y_ini < 210) \
                or x_ini == 50 and (-20 < y_ini < 20) \
                or x_ini == 80 and (100 < y_ini < 120) \
                or x_ini == 100 and (20 < y_ini < 110) \
                or x_ini == 220 and (-120 < y_ini < 40) \
                or x_ini == 250 and (-250 < y_ini < -110) \
                or x_ini == 100 and (-130 < y_ini < -20) \
                or x_ini == 100 and (-250 < y_ini < -160) \
                or x_ini == 450 and (-50 < y_ini < -10) \
                or x_ini == 340 and (-130 < y_ini < -50) \
                or x_ini == 360 and (-210 < y_ini < -160) \
                or x_ini == 320 and (-200 < y_ini < -170) \
                or x_ini == 10 and (10 < y_ini < 40) \
                or x_ini == 200 and (-20 < y_ini < 10) \
                or x_ini == 660 and (-230 < y_ini < -190):
            return False
        return True

    if direct == "Down":
        if x_ini == 50 and (-240 < y_ini < -20) \
                or x_ini == 40 and (10 < y_ini < 40) \
                or x_ini == 50 and (20 < y_ini < 250) \
                or x_ini == 100 and (-20 < y_ini < 20) \
                or x_ini == 200 and (-130 < y_ini < -20) \
                or x_ini == 230 and (-250 < y_ini < -160) \
                or x_ini == 200 and (160 < y_ini < 240) \
                or x_ini == 410 and (160 < y_ini < 210) \
                or x_ini == 450 and (130 < y_ini < 160) \
                or x_ini == 560 and (140 < y_ini < 200) \
                or x_ini == 640 and (20 < y_ini < 50) \
                or x_ini == 660 and (40 < y_ini < 200) \
                or x_ini == 640 and (190 < y_ini < 210) \
                or x_ini == 560 and (20 < y_ini < 120) \
                or x_ini == 410 and (-90 < y_ini < 40) \
                or x_ini == 650 and (-130 < y_ini < -80) \
                or x_ini == 320 and (-240 < y_ini < -80) \
                or x_ini == 260 and (-90 < y_ini < -50) \
                or x_ini == 350 and (-200 < y_ini < -170):
            return False
        return True

    if direct == "Left":
        if y_ini == -230 and (-240 < x_ini < 700) \
                or y_ini == -170 and (320 < x_ini < 350) \
                or y_ini == -160 and (360 < x_ini < 700) \
                or y_ini == -80 and (400 < x_ini < 650) \
                or y_ini == -10 and (450 < x_ini < 700) \
                or y_ini == 210 and (570 < x_ini < 640) \
                or y_ini == 200 and (630 < x_ini < 660) \
                or y_ini == -80 and (250 < x_ini < 320) \
                or y_ini == 120 and (80 < x_ini < 560) \
                or y_ini == 200 and (420 < x_ini < 560) \
                or y_ini == 210 and (210 < x_ini < 410) \
                or y_ini == 20 and (50 < x_ini < 100) \
                or y_ini == -20 and (100 < x_ini < 200) \
                or y_ini == 10 and (200 < x_ini < 230) \
                or y_ini == -160 and (100 < x_ini < 230) \
                or y_ini == -20 and (-20 < x_ini < 50):
            return False
        return True
    if direct == "Right":
        if y_ini == 220 and (40 < x_ini < 700) \
                or y_ini == 10 and (10 < x_ini < 40) \
                or y_ini == -20 and (50 < x_ini < 100) \
                or y_ini == -130 and (100 < x_ini < 200) \
                or y_ini == -120 and (220 < x_ini < 260) \
                or y_ini == -20 and (200 < x_ini < 240) \
                or y_ini == 20 and (100 < x_ini < 240) \
                or y_ini == 100 and (80 < x_ini < 110) \
                or y_ini == 160 and (100 < x_ini < 200) \
                or y_ini == 160 and (210 < x_ini < 410) \
                or y_ini == 130 and (420 < x_ini < 450) \
                or y_ini == 140 and (440 < x_ini < 560) \
                or y_ini == 20 and (570 < x_ini < 640) \
                or y_ini == 40 and (630 < x_ini < 660) \
                or y_ini == 20 and (400 < x_ini < 560) \
                or y_ini == -50 and (450 < x_ini < 700) \
                or y_ini == -130 and (340 < x_ini < 650) \
                or y_ini == -70 and (250 < x_ini < 350) \
                or y_ini == -200 and (320 < x_ini < 350) \
                or y_ini == -210 and (360 < x_ini < 670) \
                or y_ini == -230 and (660 < x_ini < 700) \
                or y_ini == 20 and (-40 < x_ini < 50):
            return False
        return True


# Por medios de condicionales se asigan los obstaculas para que la animacion del personaje principal no
# de la apariencia de que atraviesa cosas, un condicional distinto para cada pantalla
def limites_paleta_up(x_ini, y_ini, direct):
    if direct == "Up":
        if x_ini == -30 and (-300 < y_ini < -30) or x_ini == -30 and (30 < y_ini < 290) \
                or x_ini == -200 and (30 < y_ini < 210) \
                or x_ini == -200 and (-240 < y_ini < -60) \
                or x_ini == -330 and (-220 < y_ini < -70) \
                or x_ini == -500 and (30 < y_ini < 230) \
                or x_ini == -410 and (30 < y_ini < 130) or x_ini == -410 and (130 < y_ini < 230):
            return False
        return True
    if direct == "Down":
        if x_ini == -580 and (-80 < y_ini < 140) \
                or x_ini == -430 and (-300 < y_ini < -50) \
                or x_ini == -290 and (-220 < y_ini < -70) \
                or x_ini == -480 and (30 < y_ini < 230) \
                or x_ini == -240 and (30 < y_ini < 230) \
                or x_ini == -140 and (30 < y_ini < 60) \
                or x_ini == -50 and (50 < y_ini < 210) \
                or x_ini == -140 and (-240 < y_ini < -210) \
                or x_ini == -50 and (-220 < y_ini < -60) \
                or x_ini == 120 and (120 < y_ini < 300) \
                or x_ini == -460 and (110 < y_ini < 150) \
                or x_ini == -520 and (120 < y_ini < 290):
            return False
        return True
    if direct == "Left":
        if y_ini == -290 and (-440 < x_ini < -20) \
                or y_ini == -60 and (-200 < x_ini < -50) \
                or y_ini == 210 and (-200 < x_ini < -50) \
                or y_ini == 230 and (-410 < x_ini < -240) \
                or y_ini == 230 and (-500 < x_ini < -480) \
                or y_ini == 150 and (-490 < x_ini < -460) \
                or y_ini == -50 and (-590 < x_ini < -430) \
                or y_ini == -70 and (-330 < x_ini < -290) \
                or y_ini == -30 and (-30 < x_ini < 50):
            return False
        return True
    if direct == "Right":
        if y_ini == 270 and (-530 < x_ini < -20) \
                or y_ini == 110 and (-490 < x_ini < -460) \
                or y_ini == 30 and (-500 < x_ini < -480) \
                or y_ini == 120 and (-590 < x_ini < -520) \
                or y_ini == 30 and (-410 < x_ini < -240) \
                or y_ini == -220 and (-330 < x_ini < -290) \
                or y_ini == -240 and (-200 < x_ini < -140) \
                or y_ini == -220 and (-150 < x_ini < -50) \
                or y_ini == 30 and (-200 < x_ini < -140) \
                or y_ini == 50 and (-150 < x_ini < -50) \
                or y_ini == 10 and (-30 < x_ini < 40) \
                or y_ini == -30 and (-30 < x_ini < 40):
            return False
        return True


# Por medio de matricez, funcion de eleccion aleatoria, se escogen los puntos en los que se encontraran los pokemon
def ubicapoke():
    pospoke1 = choice([[randrange(50, 100, 10), randrange(-230, -40, 10)],
                       [randrange(120, 250, 10), choice([-130, -140, -150, -160])],
                       [choice([230, 240, 250]), randrange(-230, -170, 10)],
                       [choice([200, 210, 220]), randrange(-110, 20, 10)],
                       [randrange(100, 200, 10), randrange(-20, 20, 10)]])
    pospoke2 = choice([[randrange(80, 210, 10), 20],
                       [randrange(80, 100, 10), randrange(30, 130, 10)],
                       [randrange(50, 100, 10), randrange(160, 220, 10)],
                       [choice([560, 570]), randrange(40, 100, 10)]])
    pospoke3 = choice([[randrange(440, 610, 10), randrange(-10, 20, 10)],
                       [randrange(440, 610, 10), randrange(-80, -40, 10)], ])
    pospoke4 = choice([[randrange(350, 610, 10), randrange(-160, -130, 10)],
                       [choice([350, 360]), randrange(-230, -190, 10)],
                       [randrange(370, 610, 10), choice([-230, -220, -210])]])
    return [pospoke1, pospoke2, pospoke3, pospoke4]


# Por medio de funciones de eleccion aleatoria se elijen los pokemon que apareceran
def yotelijo():
    salvaje1 = randrange(1, 8, 1)
    salvaje2 = randrange(1, 8, 1)
    salvaje3 = randrange(1, 8, 1)
    salvaje4 = randrange(1, 8, 1)
    return [salvaje1, salvaje2, salvaje3, salvaje4]
