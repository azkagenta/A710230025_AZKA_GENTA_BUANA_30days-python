total = 0

def sum(nominal):
    global total
    total += float(nominal)

while True:
    price = input("Masukkan Harga (atau ketik 'selesai' untuk berhenti): ")
    if price.lower() == 'selesai':
        break
    sum(price)

print("Total Harga : {0}".format(total))
