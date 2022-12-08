import turtle

# GKirjasto.py Versio 1.0
# (c) Kimmo Kulmala 2022
# Luvian yhtenäiskoulu
#
#Värimääritykset
#*******************************************************************
SININEN = "blue"
PUNAINEN = "red"
VIHREA = "green"
KELTAINEN = "yellow"
MUSTA = "black"
PINKKI = "pink"
SYAANI = "cyan"
MAGENTA = "magenta"
HARMAA = "grey"
ORANSSI = "orange"

VARIT = (SININEN, PUNAINEN, VIHREA, KELTAINEN, MUSTA, PINKKI, MAGENTA, SYAANI,
         HARMAA,ORANSSI)

#Suunnat
#*******************************************************************
OIKEA = -1
VASEN = 1
SUUNNAT = (OIKEA, VASEN)

# Ilmansuunnat, pohjoinen on kompassin 0 astetta, kierto oikealle.
#*******************************************************************
POHJOINEN = 0
KOILLINEN = -45
ITA = -90
KAAKKO = -135
ETELA = -180
LOUNAS = -225
LANSI = -270
LUODE = -315

ILMANSUUNNAT = (POHJOINEN, KOILLINEN, ITA, KAAKKO, ETELA, LOUNAS, LANSI, LUODE)


# Alustus funktio tarvitaan aina ensin.
# Funktio luo scrollattavan  Canvasin
# Esim: t = Alusta()
#********************************
def Alusta(nopeus=10):
    t = turtle.Turtle()
    t.speed(nopeus)
    return t


#********************************
def AsetaTausta(t, vari):
    t.screen.bgcolor(vari)
    return None


#********************************
def AsetaTaustaKuva(t, picname):
    t.screen.bgpic(picname)
    return None


#********************************
def Ympyra(t, koko, vari):
    t.color(vari)
    t.circle(koko)
    return None


#********************************
def Kolmio(t, koko, vari):
    for i in range(3):
        t.color(vari)
        t.forward(koko)
        t.left(120)
    return None


#********************************
def VarikasKolmio(t, koko):
    for c in ['red', 'green', 'blue']:
        t.color(c)
        t.forward(koko)
        t.left(120)
    return None


#********************************
def VarikasNelio(t, koko):
    for c in ['red', 'green', 'blue', 'yellow']:
        t.color(c)
        t.forward(koko)
        t.left(90)
    return None


#********************************
def KaannyOikealle(t, asteet):
    t.left(-asteet)
    return None


#********************************
def KaannyVasemmalle(t, asteet):
    t.left(asteet)
    return None


#********************************
def Kaanny(t, asteet, suunta):
    if suunta == OIKEA:
        t.left(-asteet)
    else:
        t.left(asteet)

    return None


#********************************
def Liiku(t, maara):
    t.penup()
    t.forward(maara)
    t.pendown()
    return None


#********************************
def Nelio(t, koko, vari):
    for i in range(4):
        t.color(vari)
        t.forward(koko)
        t.left(90)
    return None

# kirjasin = "Arial", "Verdana",'Courier', "Calibri", "Time New Roman"
# koko =
# style = 'normal', 'bold', 'italic', 'underline'
#*************************************
def KirjoitaXY(t, text, vari, x, y, kirjasin="Arial", koko=16, tyyli='bold'):

    font = (kirjasin, koko, tyyli)
    pos = t.pos()
    SiirryPaikkaanXY(t, x, y)
    t.color(vari)
    t.write(text, font, align="left")

    SiirryPaikkaan(t, pos)
    return None


#***********************************
def AsetaSuunta(t, suunta):
    t.setheading(suunta)
    return None


#***********************************
def Paraabeli(t, vari, x= 0, y=0):
    t.color(vari)

    for i in range(-20, 20, 1):
        j = 0.5 * i**2 + i - 10
        t.penup()
        t.goto(12 * i+x, j+y)
        t.pendown()
        t.circle(5)

    return None

#********************************
def Tahti(t, koko, vari):
    for i in range(5):
        t.color(vari)
        t.forward(koko)
        t.left(144)

    return None

#***********************************
def VarikasTahti(t, koko):
    for c in ['red', 'green', 'blue', 'yellow', 'pink']:
        t.color(c)
        t.forward(koko)
        t.left(144)

    return None


#********************************
def KierraVarikasTahti(t, kierto, askel, siirto, koko=40, alku=0, loppu=360):
    for kulma in range(alku, loppu, askel):
        VarikasTahti(t, koko)
        KaannyVasemmalle(t, kierto)
        Liiku(t, siirto)
    return None


#********************************
def KierraVarikasNelio(t, kierto, askel, siirto, koko=40, alku=0, loppu=360):
    for kulma in range(alku, loppu, 10):
        VarikasNelio(t, koko)
        KaannyVasemmalle(t, kierto)
        Liiku(t, siirto)
    return None


#********************************
def KierraVarikasKolmio(t, kierto, askel, siirto, koko=40, alku=0, loppu=360):
    for kulma in range(alku, loppu, askel):
        VarikasKolmio(t, koko)
        Kaanny(t, kierto, OIKEA)
        Liiku(t, siirto)
    return None


#********************************
def AsetaPaikka(t):
    return t.pos()


#********************************
def SiirryPaikkaan(t, pos):
    t.penup()
    t.setpos(pos)
    t.pendown()
    return None


#********************************
def SiirryPaikkaanXY(t, x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    return None


#********************************
def Nuoli(t, koko, vari):
    t.pensize(3)
    t.color(vari)
    t.forward(koko)
    t.left(120)
    pos = t.pos()
    t.forward(koko / 3)
    t.setpos(pos)
    t.left(120)
    t.forward(koko / 3)
    t.setpos(pos)
    t.pensize(1)
    t.left(120)
    return None


#********************************
def Kompassi(t, koko, vari):
    t.color(vari)
    pos = t.pos()
    for ilma in range(0, 360, 45):
        Kaanny(t, 45, OIKEA)
        if ilma % 90 == 0:
          Nuoli(t,koko,vari)
          SiirryPaikkaan(t,pos)
        else:  
          t.forward(koko)
          t.left(180)
          Liiku(t, koko)
          t.left(180)

    return None


#********************************
