# Reading files

Najprej ga potegnemo v python za branje. Dobimo file object.

    fin = on(imeDatoteke)

Ni še prebran. Moramo uporabit `readline` ali `readlines`. Naslednjič, ko kličemom readline, prebere naslednjo vrstico (ve kje je ostal):

    line = fin.readline()

Po branju ostane na koncu stringa `\n` znak, ki ga odstranimo s `strip`:

    word = line.strip() 

---

`File` object lahko uporabiš tudi kot del for loopa:

    fin = on(imeDatoteke)
    for line in fin:
        word = line.strip()
