# Scope ali obseg

Spremenljivke imajo določen obseg znotraj programov in ukazov. Spremenljivke, ki so ustvarjene znotraj funkcij, so _lokalne_ (obstajajo samo, ko se pokliče funkcija).

Tako kot spremenljivke v funkcijah, so tudi parametri lokalni. To pomeni, če imaš parameter `bruce` v definiciji funkcije, ne obstaja izven nje, predstavlja samo ime parametra.

    def bdv(bruce):
        ime = bruce
        return ime

