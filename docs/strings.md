# Strings

String je sekvenca znakov znotraj `"..."` ali `'...'`. Do posameznih znakov dostopamo preko indexiranja:

    string[index]

Index mora bit **integer**.

## len()

Vrne dolžino niza

    >>> fruit = 'banana'
    >>> len(fruit)
    6

Zadnji element dobimo, tako da rečemo:

    fruit[len(fruit) - 1]

Ali pa uporabljamo negativne indexe, da se pomikamo v obratno smer:

    >>> fruit[-1]
    a
    >>> fruit[-2]
    n

## String slices

Kot v R-ju, nek obseg dobiš:

    string[start:end]

Npr.:

    >>> fruit[0:2]
    ba

Slici excludajo zadnji element: `[start, end)`.

Če spustiš start index, gre od začetka do end. Če spustiš end index, gre od start do konca.

## Imutabilnost nizov

Ne moreš jim spreminjat znakov:

    >>> fruit[0] = 'z'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'str' object does not support item assignment

# Builtin string functions

## upper

## lower

## count

## find

    word.find(znak, start, end)

Vrne index znaka. dela tudi s substrings. `-1` vrne, ko ne najde znaka.

Načeloma začne na začetku niza, a lahko podaš drugi parameter - kje naj začne in tretji - kje naj konča.

## in

Kot v R-ju `%in%`, in pove, če je znak v nizu.

    znak in niz


