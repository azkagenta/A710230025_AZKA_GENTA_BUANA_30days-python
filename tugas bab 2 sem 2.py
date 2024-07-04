while True:
    try:
        num = int(input("Masukkan bilangan bulat: "))
        print("Kuadrat dari", num, "adalah", num ** 2)
        break
    except ValueError:
        print("Input yang dimasukkan tidak valid!")