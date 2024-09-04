# Conditional and logical operations

## Boolean expressions

To so izrazi, ki vrnejo `true` ali `false`. 
    >>> 1 == 1
    True

## Relational operators

Relacije.....ew

    ==
    !=
    ===
    >
    <
    >=
    <=

## Logical operators

    and (&)
    or  (|)
    not (!)

Vsako nenegativno število bo vrnilo true:

    >>> 42 and True
    True

# Conditional statements

If statements...

    if izraz_je_true:
        naredi_to
    elif drugi_izraz_ki_mora_bit_true:
        naredi_to
    else:
        naredi_TO

`else` ni potreben, ampak ko je prisoten, mora bit na koncu.

`pass` ukaz preskoči izraz. Ponavadi uporabno za TODO...

    if izraz:
        pass

---

Recimo, da imaš:

    if 0 < x:
        if x < 10:
            print("ta jajca")

To lahko napišeš drugače:

    if 0 < x < 10:
        print("ta jajca")

Kar je v bistvu

    if 0 < x and x < 10
        print("ta jajca")

## Rekurzija

Rekurzivne funkcije izkoriščajo logiko, da se izvajajo, dokler nek pogoj ni zadovoljen. Pogoj, ki jo ustavi, se imenuje **base case**.

Primer:

    def recurse(n):
        if (n <= 0):
            return
        print(f"še {n} števil do konca")
        recurse(n-1)

V primeru, da ustavitveni pogoj ne dela, dobimo error `RuntimeError: Maximum recursion depth exceeded` - funkcija se je izvedla 1000-krat in nato python compiler ustavi izvajanje.



