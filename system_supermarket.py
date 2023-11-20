#Sistem Supermarket
def view_items():
    print('------------------View Items------------------')
    print('Jumlah item dalam penyimpanan adalah : ', len(items))
    while len(items) != 0:
        print('Berikut adalah semua barang yang tersedia di supermarket.')
        for item in items:
            for key, value in item.items():
                print(key, ':', value)
        break

def add_items():
    print('------------------Add items------------------')
    print('Untuk menambahkan barang, isi data berikut')
    item = {}
    item['name'] = input('nama barang : ')
    while True:
        try:
            item['quantity'] = int(input('jumlah barang : '))
            break
        except ValueError:
            print('Jumlah barang hanya boleh dalam digit')
    while True:
        try:
            item['price'] = int(input('Harga(Rp) : '))
            break
        except ValueError:
            print('Harga hanya boleh dalam digit')
    print('barang telah berhasil ditambahkan.')
    items.append(item)

def purchase_items():
    print('------------------purchase items------------------')
    print(items)
    purchase_item = input('Masukkan nama barang yang ingin Anda beli? : ')
    for item in items:
        if purchase_item.lower() == item['name'].lower():
            if item['quantity'] != 0:
                purchase_quantity = int(input("Berapa jumlah barang yang dibeli: "))
                item['quantity'] -= purchase_quantity
                multiply = item['price'] * purchase_quantity
                pay.append(multiply)
            else:
                print('Barang kehabisan stok.')

def search_items():
    print('------------------search items------------------')
    find_item = input('Masukkan nama barang yang dicari : ')
    for item in items:
        if item['name'].lower() == find_item.lower():
            print('nama barang ' + find_item + ' sebagai berikut')
            print(item)
        else:
            print('barang tidak ditemukan.')

def add(op1, op2):
    return op1 + op2

from functools import reduce
items = []
pay = []
while True:
    display = input('Tekan enter untuk melanjutkan.')
    print('------------------Selamat datang di supermarket------------------')
    print('1. Menampilkan barang\n2. Menambahkan barang-barang untuk dijual\n3. Membeli barang\n4. Cari barang \n5. Selesai')
    choice = input('Masukkan nomor pilihan Anda : ')

    hasil = lambda choice: view_items() if choice == '1' else (add_items() if choice == '2' else (
        purchase_items() if choice == '3' else (search_items() if choice == '4' else 'Nomer yang Anda memasukkan tidak sesuai ')))

    if choice == '5':
        print('------------------exited------------------')
        break

    print(hasil(choice))

result = reduce(add, pay)
print('Silahkan membayar sebesar RP.', result, 'di meja kasir')
