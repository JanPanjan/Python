def is_triangle(a, b, c):
    if a + b == c or a + c == b or b + c == a:
        print("yes")
        return
    else:
        print("No")
        return

def main():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    is_triangle(a, b, c)

if __name__ == "__main__":
    main()
