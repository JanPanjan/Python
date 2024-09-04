# Compiling

Python program compilaš tako, da pišeš:

    python3 nameOfPythonFile.py

To bo zagnalo program in izvedlo vse ukaze. če hočeš it v interactive okolje, moraš podati prefix `-i`:

    python3 -i

Tako si v nekem separate okolju. Če hočeš najprej zagnati program in nato s shranjenimi spremenljivkami in vsem v interactive mode, moraš dodati ime skripte:

    python3 -i nameOfPythonFile.py

Tako boš npr. imel v spominu `a = 3`. In shell bo izgledal:

    >>> print(a)
    3
    >>>
