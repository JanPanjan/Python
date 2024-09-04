def recurse(n):
    """rekurzivna funkcija"""
    if (n > 0):
        if (n <= 0):
            print("konec")
            return
        print(f"še {n} števil do konca")
        recurse(n-1)
    elif (n < 0):
        if (n >= 0):
            print("konec")
            return
        print(f"še {n} števil do konca")
        recurse(n+1)

recurse(10)
