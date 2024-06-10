counter = 0 
total = 0 

jumlah_barang = int(input('Masukan Jumlah Barang : '))
while counter < jumlah_barang:
    harga = int(input('Masukan harga barang ke-{}: '.format(counter+1)))
    jumlah = int(input('Masukan jumlah barang ke-{}: '.format(counter+1)))
    total = total + (harga*jumlah)
    counter = counter+1

    print('Total Harga Barang :',total)