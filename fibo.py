def fiboo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fiboo(n - 1) + fiboo(n - 2)
print(fiboo(18))

def main():
    number = int(input("Zadej číslo:"))
    vystup = []
    for i in range(number + 1):
        vystup.append(fiboo(i))
    print(vystup)
    pass


if __name__ == "__main__":
    main()
