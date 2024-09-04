# Operations

## Aritmetične operacije

Basic `+,-,*,/,%`.

Python uporablja standardno matematično prakso, kar se tiče zaporedja operacij - **PEMDAS**

    [p]arenthesis
    [e]qponentiation
    [m]ultiplication
    [d]ivision
    [a]ddition
    [s]ubtraction

Ampak notice, da preden deli, pretvori števila v `float`, zato je rezultat decimalno število.

Prav tako dobiš `ZeroDivisionError`, če probaš delit z 0.

---

Eksponente pišeš z `**`:

    2 ** 10
    4 ** 0.5

---

Modulo operator je uporaben, ko hočeš, da se nekaj zgodi vsak _nth_ time. Npr. vsako sedmo ponovitvijo, kar pomeni, da ko bo

    število % 7 == 0

se bo nekaj zgodilo.

---

S `+` lahko seštevaš tudi strings (ekvivalentno `strcpy` v C-ju). Če hočeš dodat število nekemu nizu, ga moraš najprej spremenit v string type.

To narediš s `str` funkcijo:

    a = 12
    b = " bla bla"
    print(str(a) + b)

Ali pa dodaš vejice v print funkciji:

    print(a, b)

---

Znak `*` uporabljen s strings pomeni _repetition_ - nek string se bo ponovil `* n` n-krat:

    >>> a = "Bugga"
    >>> a * 3
    'BuggaBuggaBugga'


