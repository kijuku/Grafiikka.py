from GKirjasto import *


#***********************************
def SateenkaariSpiraali(t, Size, Angle):
    max = 255
    r = 255
    g = 0
    b = 0
    #Rajoitetaan kokoa
    if Size > 50:
        Size = 50
    if Angle < 60:
        Angle = 61
    for i in range(max * 2):
        t.screen.colormode(max)
        if i < max // 3:
            g += 3
        elif i < max * 2 // 3:
            r -= 3
        elif i < max:
            b += 3
        elif i < max * 4 // 3:
            g -= 3
        elif i < max * 5 // 3:
            r += 3
        else:
            b -= 3
        t.forward(Size + i)
        t.left(Angle)
        t.pencolor(r, g, b)

    return None


#***********************************
def CoolTube(t, c1 = 'orange', c2 = 'red', Angle = 3, Step = 3, Value = 0.8, Max = 120):
    for i in range(Max):
        t.color(c1)
        t.circle(i)
        t.color(c2)
        t.circle(i * Value)
        t.right(Angle)
        t.forward(Step)

    return None


#***********************************
def PaaOhjelma():
    nimi = "Graafiikka Kirjaston testiohjelma"
    # Alustetaan piirto alusta.
    t = Alusta(100)
    vari = PUNAINEN
    koko = 30
    AsetaTausta(t, MUSTA)
    pos = AsetaPaikka(t)

    #SateenkaariSpiraali(t, 1, 155)
    CoolTube(t, VIHREA, KELTAINEN,11,2)
    # Kirjoitetaan tekstiä
    KirjoitaXY(t, nimi, SININEN, -200, 200)

    Paraabeli(t, PUNAINEN)

    SiirryPaikkaan(t, pos)

    for i in range(0, 360, 45):
        Nuoli(t, 60, ORANSSI)
        SiirryPaikkaan(t, pos)
        Kaanny(t, 45, OIKEA)

    Liiku(t, 100)

    AsetaSuunta(t, LANSI)

    for i in range(0, 60, 5):
        Nuoli(t, 10, SININEN)
        Kaanny(t, 5, OIKEA)
    KirjoitaXY(t, "Kompassi", PUNAINEN, -100, -50)
    Kompassi(t, koko, PUNAINEN)

    Liiku(t, 100)
    # Piirrellään eri kuvioita
    VarikasNelio(t, 10)

    SiirryPaikkaan(t, pos)
    AsetaSuunta(t, LANSI)

    #t.screen.cleanscreen()
    Nelio(t, koko, vari)
    Liiku(t, 100)
    Ympyra(t, koko, vari)
    KaannyOikealle(t, 45)
    Liiku(t, 20)
    Ympyra(t, 30, SININEN)
    KaannyVasemmalle(t, 90)
    Liiku(t, 40)
    Ympyra(t, 40, VIHREA)
    KaannyVasemmalle(t, 90)
    Liiku(t, 40)
    Tahti(t, 30, PUNAINEN)
    KaannyVasemmalle(t, 90)
    Liiku(t, 20)
    VarikasTahti(t, 40)

    # SiirryPaikkaan(t, pos)
    # KierraVarikasKolmio(t, 10, 10, 10, 5, 0, 200)
    #  SiirryPaikkaan(t, pos)
    #  KierraVarikasNelio(t, 10, 10, 10, 10)
    #  SiirryPaikkaan(t, pos)
    #  KierraVarikasTahti(t, 20, 20, 10, 30, 300, 360)
    # SiirryPaikkaanXY(t, -200, 100)
    Liiku(t, 50)

    #for i in range(0, 30, 1):
    #    Ympyra(t, koko, SININEN)
    #    Liiku(t, 10)

    pos = AsetaPaikka(t)

    Liiku(t, 50)

    #for i in range(0, 30, 1):
    #    VarikasNelio(t, koko)
    #    Liiku(t, 2)
    #    Kaanny(t, 10, OIKEA)

    SiirryPaikkaan(t, pos)

    KaannyVasemmalle(t, 90)
    Liiku(t, 40)
    Kolmio(t, 30, PUNAINEN)
    Liiku(t, 40)
    VarikasKolmio(t, 40)

    KaannyVasemmalle(t, 90)
    Liiku(t, 40)
    Kompassi(t, koko, VIHREA)
    Liiku(t, 80)
    return None


PaaOhjelma()
