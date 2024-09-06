# Lists

Polje, array, sekvenca vrednosti, whatever. Lahko imajo mešane elemente, lahko ima nested list.

    polje = [1,2,3]
    polje2 = [False, "ena", 2]

Prazen list:

    prazenList = []

## Traversing a list

    for i in list:
        print(i)

Zdaj se v `i` shrani element lista in ne index. Če hočemo indexe, moramo uporabiti `range` in `len`:

    for i in range(len(list)):
        print(list[i])

Range vrne seznam indeksov od 0 do $n-1$.

# List operations

Kot strings.

Concatenation:

    >>> a = [1,2]
    >>> b = [3,4]
    >>> a + b
    [1, 2, 3, 4]

Repeating:

    >>> a * 3
    [1,2,1,2,1,2]

# List functions

Večino list funkcij je void (returna none), zato ni treba assignat posodobljen list v variable.

## Append:

    >>> a.append(3)
    >>> a 
    [1,2,3]

## Extend 

Enako kot append, le da vzame list kot argument.

## Sort

Sortira po velikosti od najmanjšega do največjega ali po abecedi.

## Sum

Sešteje vrednosti.

## Pop

Odfuka zadnji element lista, razen če podaš index. Vrne element, ki je bil odstranjen, poleg tega, da spremeni list:

    >>> t = ['a', 'b', 'c']
    >>> x = t.pop(1)
    >>> t
    ['a', 'c']
    >>> x
    'b'

## Remove

Ko veš value, ampak ne poznaš indexa:

    >>> t = ['a', 'b', 'c']
    >>> t.remove('b')
    >>> t
    ['a', 'c']



