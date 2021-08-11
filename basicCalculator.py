import tkinter
import tkinter
from tkinter import font
from tkinter.constants import CENTER, X, Y


#alustetaan muuttuja johon tallennetaan string muodossa numerot jotka halutaan
#laskea yhteen tai vähentää
tulos = ""

väri1 = "#1b2940"
väri2 = "#54688a"
tekstinväri = ""
värivalinta = 0



#metodi jolla lisätään klikattu luku stringinä tulos muuttujaan
def lisääLuku(luku):
    global tulos


    tulos = tulos + str(luku)
    näytä.set(tulos)

#metodi jolla lasketaan tulos. 
#eval-funktio tarkistaa syötteen string muodossa ja muuntaa sen matemaattiseksi laskuksi 
# esim "12+23" = 12 + 23 eval funktion jälkeen
def laskutoimitus():
    try:

        global tulos

        tulostettava = str(eval(tulos))
        #asetetaan näytölle asetettavaksi tiedoksi laskutoimituksen tulos
        näytä.set(tulostettava)
        tulos = ""
    except:
        #mikäli tapahtuu virhe, kutsutaan error ja ruudulle tulostuu " ERROR "
        näytä.set(" ERROR ")
        #asetetaan myös tulosmuuttuja takaisin tyhjäksi
        tulos = ""

#metodi jolla tyhjätään valinnat tulos muuttujasta
def tyhjää():
    global tulos

    tulos = ""
    näytä.set(tulos)


def vaihdaVäri():
    global väri1
    global väri2
    global värivalinta

    värivalinta += 1

    if värivalinta < 8 and värivalinta > -1:
        if värivalinta == 0:
            väri1 = "#1b2940"
            väri2 = "#54688a"

        elif värivalinta == 1:
            väri1 = "#f0073a"
            väri2 = "#0f6605"
            
        elif värivalinta == 2:
            väri1 = "#FDD50B"
            väri2 = "#E870A0"
            
        elif värivalinta == 3:
            väri1 = "#FE0002"
            väri2 = "#0001FC"
            
        elif värivalinta == 4:
            väri1 = "#E0CA4A"
            väri2 = "#10A30C"
            
        elif värivalinta == 5:
            väri1 = "#4cbb17"
            väri2 = "#0001FC"
            
        elif värivalinta == 6:
            väri1 = "#F0F"
            väri2 = "#A0F"
           
        elif värivalinta == 7:
            väri1 = "#ff6522"
            väri2 = "#768cdb"
            
        else:
            väri1 = "##00cc00"
            väri2 = "#000000"
            
    else:
        väri1 = "#1b2940"
        väri2 = "#54688a"
        värivalinta = 0

    canvas.configure(bg=väri1)

    plus.configure(bg=väri2)
    miinus.configure(bg=väri2)
    jako.configure(bg=väri2)
    kerto.configure(bg=väri2)

    yksi.configure(bg=väri2)
    kaksi.configure(bg=väri2)
    kolme.configure(bg=väri2)
    neljä.configure(bg=väri2)
    viisi.configure(bg=väri2)
    kuusi.configure(bg=väri2)
    seitsemän.configure(bg=väri2)
    kahdeksan.configure(bg=väri2)
    ysi.configure(bg=väri2)
    nolla.configure(bg=väri2)
    yhtäkuin.configure(bg=väri2)
    onett.configure(bg=väri2)
    vaihda.configure(bg=väri2)


#alustetaan ikkuna, ikkunan nimi ja sen koko
Window = tkinter.Tk()
Window.resizable(False, False)
Window.title("Perus laskin")
Window.geometry("295x500")

#alustetaan muuttuja joka tulostetaan ruudulle 
näytä = tkinter.StringVar()

#asetetaan universaali fontti
fontti = font.Font(weight="bold")

#tehdään ikkunan päälle canvas, jota voi helpommin käsitellä vaikka ohjelmaa laajennettaessa.
#asetetaan canvasin mittasuhteet ja määritellään väriksi oranssi
canvas = tkinter.Canvas(Window, width=300, height=500)
canvas.configure(bg=väri1)
#sen jälkeen pakataan canvas ikkunan sisään niin että canvasin voi fyysisesti nähdä ja se tulostuu ruudulle.
canvas.pack()

#tehdään syötekenttä, jonka sisään tulee luku joka klikattiin sekä myöhemmin näytä-muuttujan value
syöte = tkinter.Entry(canvas, font=("bold"), textvariable=näytä)
#annetaan syötteelle positioksi ja kooksi allaolevat arvot
syöte.place(x=15, y=20, width=260, height=40)






#ensin tehdään nappi, jolle annetaan koko ja teksti sekä funktio joka suoritettaessa tapahtuu

#------ napit on tehty näin vain ja ainoastaan siitä syystä että se helpotti tekijän lukukokemusta.
#-------nappien declaraamisessa käytetty tyylitys ei vaikuta koodiin mitenkään.

plus = tkinter.Button(canvas, text="+", 
                        padx=20, 
                        pady=15, 
                        bg=väri2, 
                        bd=0, 
                        command=lambda: lisääLuku("+"))

plus.place(x=5, y=80)
#asetetaan napille fontti joka on kaikille sama jotka käyttävät muuttujaa fontti koska se määriteltiin 
#ensimmäisten asioiden joukossa.
plus["font"] = fontti

#toistetaan samaa useasti jotta saadaan tarvittavat nappulat.
miinus = tkinter.Button(canvas,
                        text="-", 
                        padx=20, 
                        pady=15, 
                        bg=väri2, 
                        bd=0, command=lambda: lisääLuku("-"))
miinus.place(x=75, y=80)
miinus["font"] = fontti

jako = tkinter.Button(canvas, 
                        text="/", 
                        padx=22, 
                        pady=15, 
                        bg=väri2, 
                        bd=0, 
                        command=lambda: lisääLuku("/"))
jako.place(x=150, y=80)
jako["font"] = fontti

kerto = tkinter.Button(canvas, 
                        text="X", 
                        padx=20, 
                        pady=15, 
                        bg=väri2, 
                        bd=0, 
                        command=lambda: lisääLuku("*"))
kerto.place(x=225, y=80)
kerto["font"] = fontti

#------- numerot ----------

yksi = tkinter.Button(canvas, 
                        text="1", 
                        padx=20, 
                        pady=15, 
                        bg=väri2, 
                        bd=0, 
                        command=lambda: lisääLuku(1))
yksi.place(x=5, y=160)
yksi["font"] = fontti

kaksi = tkinter.Button(canvas, 
                        text="2", 
                        padx=20, 
                        pady=15, 
                        bg=väri2, 
                        bd=0, 
                        command=lambda: lisääLuku(2))

kaksi.place(x=75, y=160)
kaksi["font"] = fontti

kolme = tkinter.Button(canvas, 
                        text="3", 
                        padx=20, 
                        pady=15, 
                        bg=väri2, 
                        bd=0, 
                        command=lambda: lisääLuku(3))

kolme.place(x=150, y=160)
kolme["font"] = fontti

neljä = tkinter.Button(canvas, 
                        text="4", 
                        padx=20, 
                        pady=15, 
                        bg=väri2, 
                        bd=0, 
                        command=lambda: lisääLuku(4))

neljä.place(x=225, y=160)
neljä["font"] = fontti

viisi = tkinter.Button(canvas, 
                        text="5", 
                        padx=20, 
                        pady=15, 
                        bg=väri2, 
                        bd=0, 
                        command=lambda: lisääLuku(5))

viisi.place(x=5, y=240)
viisi["font"] = fontti

kuusi = tkinter.Button(canvas, 
                        text="6", 
                        padx=20, 
                        pady=15, 
                        bg=väri2, 
                        bd=0, 
                        command=lambda: lisääLuku(6))
                        
kuusi.place(x=75, y=240)
kuusi["font"] = fontti

seitsemän = tkinter.Button(canvas, 
                            text="7", 
                            padx=20, 
                            pady=15, 
                            bg=väri2, 
                            bd=0, 
                            command=lambda: lisääLuku(7))

seitsemän.place(x=150, y=240)
seitsemän["font"] = fontti

kahdeksan = tkinter.Button(canvas, 
                            text="8", 
                            padx=20, 
                            pady=15, 
                            bg=väri2, 
                            bd=0, 
                            command=lambda: lisääLuku(8))

kahdeksan.place(x=225, y=240)
kahdeksan["font"] = fontti

ysi = tkinter.Button(canvas, 
                    text="9", 
                    padx=20, 
                    pady=15, 
                    bg=väri2,
                    bd=0, 
                    command=lambda: lisääLuku(9))

ysi.place(x=5, y=320)
ysi["font"] = fontti

nolla = tkinter.Button(canvas, 
                        text="0", 
                        padx=20, 
                        pady=15, 
                        bg=väri2, 
                        bd=0, 
                        command=lambda: lisääLuku(0))

nolla.place(x=75, y=320)
nolla["font"] = fontti

onett = tkinter.Button(canvas, 
                        text="?", 
                        padx=20, 
                        pady=15, 
                        bg=väri2, 
                        bd=0, 
                        command=lambda: tyhjää())

onett.place(x=150, y=320)
onett["font"] = fontti

yhtäkuin = tkinter.Button(canvas, 
                            text="=", 
                            padx=20, 
                            pady=15, 
                            bg=väri2, 
                            bd=0, 
                            command=lambda: laskutoimitus())

yhtäkuin.place(x=225, y=320)
yhtäkuin["font"] = fontti


vaihda = tkinter.Button(canvas, 
                        text="RGB MODE ACTIVATE", 
                        padx=25, 
                        pady=15, 
                        bg=väri2, 
                        bd=0, 
                        anchor=CENTER,
                        command=lambda: vaihdaVäri())
                        
vaihda.place(x=10, y=400)
vaihda["font"] = fontti


#ohjelman looppikutsu, ilman tätä ohjelma ei tee mitään vaan päättää itsensä automaattisesti
Window.mainloop()