# Functions

Funkcija je neka sekvenca ukazov, ki se izvedejo, ko je poklicana. 

Ko hočeš ustvarit funkcijo, moraš podat ime in ukaze.

Argumenti funkcij so lahko kakršnikoli izrazi, tudi aritmetične operacije, lahko tudi klici drugih funkcij.

## Pretvarjanje tipov

Nekatere osnovne builtin funkcije so uporabne za pretvarjanje med podatkovnimi tipi spremenljivk.

- `str`: naredi string
- `int`: naredi int
- `float`: naredi float

int bo spremenil string, če bo string število (npr `int("Hello")` bo vrgel error). če uporabiš na float, bo shranil le število pred decimalko.

    >>> int(3.4567)
    3

## Moduli

Python vsebuje module ali posebne datoteke, ki hranijo razne funkcije in spremenljivke.

Da jih lahko uporabljamo, moramo pisati (pred klicom ukazov):

    import imeModula

### Math module

Math modul ima veliko funkcij in spremenljivk za matematične operacije. Da dostopaš do teh stvari, moraš pisati _dot operator_:

    math.imeStvari

Drugače povedano, uporabiti moraš _dot notation_ (keep in mind, da je zgrajen na osnovi C-ja; glej [repository](https://github.com/JanPanjan/C))

## Ustvarjanje funkcij

Sintaksa:

    def imeFunkcije(argument1, argument2):
        ukaz 1
        ukaz 2
        return nekaj

Prvi line je _header_ funkcije, ki se začne z `def` in konča z `:`. Vse naslednje vrstice morajo biti indented 4 mesta.

V interpreterju bo izgledalo tako:

    >>> def imeFunkcije(argument1, argument2):
    ...     ukaz 1
    ...     ukaz 2
    ...     return nekaj
    ...

Da jo končaš, vstaviš prazno vrstico na koncu. Zdaj obstaja nek objekt tipa **funkcija**.

    >>> type(imeFunkcije)
    <class 'function'>

Prav tako je pomembno, da definiraš funkcije preden jih pokličeš (tako kot moraš importat modul), drugače compiler ne ve kaj je ta stvar.

Funkcija bo izvedla vse ukaze in se zaprla, če ni return ukaza. Da jo končaš prej, lahko daš return prej v funkciji

    def func():
        ukaz1
        return
        ukaz 2      # ne bo se izvedel

Koda, ki se pojavi po return ukazu se imenuje _Dead code_.

## Return values and expressions

Funckije v pythonu, ki so void (`return` brez vsega), vrnejo `None` type, drugače pa lahko vrnejo funkcije vrednosti. 

## Debugging

Tmp variables so priročne pri debugganju funkcij, namesto da clusterfuckaš vse v return statement.

Prav tako je pomembno, da testiraš program del po del. Da ne izgradiš celega naenkrat, ampak najprej preveriš, če dela osnovna funkcionalnost in nato dodajah funkcije.

Debugging ko uporabljaš print da prikažeš kaj se dogaja z vrednostmi, se imenuje _Scaffolding_.

## Boolean functions

Primerne kot utility functions I guess. Npr.:

    def is_divisible(x,y):
        if x % y == 0:
            return True
        else
            return False

Zgornjo funkcijo lahko napišemo krajše, tako da vrnemo kaj bo evaluacija conditiona:

    def is_divisible(x,y):
        return x % y == 0

Prav tako je primerno, da so imena taka kot _yes/no_ vprašanja, saj se vrne ja ali ne.

