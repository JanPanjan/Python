# Interface design

Proces, kako designat funkcije, ki delujejo skupaj. Uproablja se _turtle_ builtin modul.

>Vem, da so interface-i neke druge stvari v sklopu programiranja, ampak tako je v pdf-ju. Ne govorim o Java interfacem, ki je nek abstract class npr., ampak bolj splošno kako urediti kodo.

## Turtle modul

Probaj zagnati `turtle.Turtle()`, nastal naj bi nov window in v sredini puščica. Ta puščica je naš turtle.

Turtle() funkcija ustvari turtle objekt. Če printaš:

    print(turtle.Turtle())

boš videl, da je turtle objekt

    <turtle.Turtle object at 0x000001FBC2E76390>

Funkcija `turtle.mainloop()` pove programu naj počaka na user input. Zdaj lahko samo zapreš program.

## Premikanje želvice

Naredi spremenljivko bob, ki bo želva.

    bob = turtle.Turtle()

Zdaj ko imamo želvico, lahko kličemo funkcije, da jo premaknemo po ekranu. 

Npr. da ji rečemo, da se premakne 100 pixlov naprej:

    bob.fd(100)

Da gre nazaj, kličemo `bk`

Levo `lt`, desno `rt` sprejmeta argument v kotnih stopinjah.

## Pen trail

Prav tako ima vsaka želvica kuli ali _pen_, ki je postavljen gor ali dol (če je dol, pušča za sabo sled).

`pu` in `pd` sta _pen up_ in _pen down_

# Kaj je point interface-a

Interface funkcije je njen summary.

- kaj so parametri
- kaj naredi
- kaj je return value

_Clean_ interface dovoli userju, da naredi bistvo s funkcijo in ni overwhelmed s podatki.

Hočeš naredit kvadrat? Say less. Pokliči `square(t, lenght)`, kjer je t tvoja želvica in lenght dolžina kvadrata. Funkcija:

    def square(t, lenght):
        for i in range(4):
            t.forward(lenght)
            t.left(90)

Hočeš naredit krog? Say less. Pokliči `circle(t, radius)`, kjer je t želvica in radius premer kroga. Funkcija:

    def initCircle(t, radius):
        t.forward(radius)
        t.left(90)

    # naredi krog iz radiusa
    def circle(t, radius):
        initCircle(t, radius)
        # obseg = 2 x pi x r
        # obseg delimo na 360 delov
        # vsako iteracijo se premakne za eno enoto
        obseg = 2 * math.pi * radius
        enota = obseg/360
        for i in range(360):
            t.forward(enota)
            t.left(1)

## Refactoring

(Glej [turtle1.py](turtle1.py) za vse funkcije)

Funkcija `circleMod` je bila definirana s pomočjo `polygon` funkcije. Lahko bi spremenil polygon v `polyline` (zaradi clarity), ji dodal parameter _angle_ in jo uporabil v `arc` funkciji, nato pa arc v `circle`.

Takemu sistemu se reče **refactoring**, ko reuse-aš kodo, da ohraniš clean interface funkcij.

## Docstring

To je string na začetku funckije, ki opiše njeno delovanje. V pythonu to naredimo s `"""..."""`. besedilo se potem prikaže z LSP quick documentation/description.

(Triple string, da je lahko dokumentacija multiline)

Primer:

    def tvojaMama(ime):
        """Pove lepo stvar o tvoji mami.
        Priporočeno je, da uporabiš ime v imenovalniku"""
        return f"{ime} je zelo lepa"

Vedno, ko naletiš na težavo z dokumentiranjem funkcije, se vprašaj **kaj lahko izboljšam znotraj funkcije, da bo bolj preprosto za opisat**.

## Debugging

Dokumentacija pomaga pri odpravljanju bugs v programu, saj deluje nekako kot _pogodba_ med uporabnikom in funkcijo. Ti podaš parametre, funkcija ti vrne delo in rezultat.

Zato, ko odpravljaš bugs, najprej pogledaš v dokumentacijo in preveriš ali si ti, kot uporabnik funkcije podal pravilne parametre - izpolnil svoj del posla.

V kolikor funkcija kljub pravilnim parametrom ne dela, je bug v kodi funkcije.

---

*Glej stran 38 za vaje z želvicami.*

