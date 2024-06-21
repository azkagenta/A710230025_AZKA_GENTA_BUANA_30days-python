def cek_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def aapakah_prima(n):
    if cek_prima(n):
        print("Bilangan Prima")
    else:
        print("Bukan Bilangan Prima")