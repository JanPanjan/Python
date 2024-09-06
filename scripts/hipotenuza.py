import math

def hipotenuza(a, b):
    """funkcija izračuna hipotenuzo (vrne koren od c).
    a in b morata biti števili, ki predstavljata
    kateti v trikotniku."""
    print(f"a:{a}, b:{b},", end=" ")
    if a == 0 or b == 0:
        return "kateti morata biti več kot 0"
    # pitagorov izrek: a**2 + b**2 = c**2
    c_kv = a**2 + b**2
    return f"c:{math.sqrt(c_kv)}"

print(hipotenuza(1,2))
print(hipotenuza(1,0))
print(hipotenuza(4,3))
