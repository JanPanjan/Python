def check_fermat(a, b, c, n):
    if n > 2 and (a**n + b**n == c**n):
        print("holy smokes, fermat was wrong!")
        return 
    else:
        print("no, that doesn't work.")
        return

def main():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    n = int(input("n: "))

    check_fermat(a, b, c, n)
    return

if __name__ == "__main__":
    main()
