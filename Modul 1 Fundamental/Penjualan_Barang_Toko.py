def showdata(barang): # Function menampilkan Data
    print('''
                            Daftar Barang Di Imigrasi Coffee
''')
    print('| Nomor Data\t| \tKode Barang  \t| \tBarang  \t \t| Stock | Harga(Rp)\t|   Warna \t|')
    for i in range(len(barang)) :
        print(f"| {i+1}         \t| \t{barang[i]['Kode Barang']}\t\t| {barang[i]['Barang']}    \t| {barang[i]['Stock']}\t| {barang[i]['Harga']}  \t| {barang[i]['warna']} \t|")

def checkExitRead() : #Function untuk konfirmasi exit pada menu read
    while True :
        checkExit = input("\napakah anda yakin ingin keluar dari menu Read? (ya/tidak) : ").lower()
        if checkExit == 'ya':
            break
        elif checkExit == 'tidak' :
            return menuRead()
        else:
            print('''
            Masukkan PILIHAN ENTRY YANG SESUAI!
            ''')

def checkExitcreate() : #Function untuk konfirmasi exit pada menu create
    while True :
        checkExit = input("\napakah anda yakin ingin keluar dari menu Create? (ya/tidak) : ").lower()
        if checkExit == 'ya':
            break
        elif checkExit == 'tidak' :
            return menuCreate()
        else:
            print('''
            Masukkan PILIHAN ENTRY YANG SESUAI!
            ''')  

def checkExitUpdate() : # Function untuk konfirmasi exit pada menu update
    while True :
        checkExit = input("\napakah anda yakin ingin keluar dari menu Update? (ya/tidak) : ").lower()
        if checkExit == 'ya':
            break
        elif checkExit == 'tidak' :
            return menuUpdate()
        else:
            print('''
            Masukkan PILIHAN ENTRY YANG SESUAI!
            ''')

def checkExitDelete() : # Function untuk konfirmasi exit pada menu delete
    while True :
        checkExit = input("\napakah anda yakin ingin keluar dari menu Delete? (ya/tidak) : ").lower()
        if checkExit == 'ya':
            break
        elif checkExit == 'tidak' :
            return menuDelete()
        else:
            print('''
            Masukkan PILIHAN ENTRY YANG SESUAI!
            ''')        


def inputKodeBarang() : # Function untuk check tipe data input value kolom kode barang
    while True :
        KodeBarang = input('\nMasukkan Kode Barang :')
        x = KodeBarang.isnumeric()
        if x == True :
            x = KodeBarang
            return x
        else :
            print('''
            HANYA MASUKKAN ANGKA SAJA TIDAK BISA HURUF!
            ''')

def inputNamaBarang() : # Function untuk check tipe data input kolom value
    while True :
        NamaBarang = input('Masukkan Nama Barang :').capitalize()
        x = NamaBarang.isnumeric()
        if x == False :
            x = NamaBarang
            return x
        else :
            print('''
            HANYA MASUKKAN HURUF SAJA TIDAK BISA ANGKA!
            ''')

def inputStockBarang() : # Function untuk check tipe data input  kolom stock
    while True :
        StockBarang = input('Masukkan Stock Barang :')
        x = StockBarang.isnumeric()
        if x == True :
            x = int(StockBarang)
            return x
        else :
            print('''
            HANYA MASUKKAN ANGKA SAJA TIDAK BISA HURUF!
            ''')

def inputHargaBarang() : # Function untuk check tipe data input value kolom harga
    while True :
        HargaBarang = input('Masukkan Harga Barang :')
        x = HargaBarang.isnumeric()
        if x == True :
            x = int(HargaBarang)
            return x
        else :
            print('''
            HANYA MASUKKAN ANGKA SAJA TIDAK BISA HURUF!
            ''')

def inputWarnaBarang() : # Function untuk check tipe data untuk value kolom warna
    while True :
        WarnaBarang = input('Masukkan Warna Barang :').capitalize()
        x = WarnaBarang.isnumeric()
        if x == True :
            print('''
            HANYA MASUKKAN HURUF SAJA TIDAK BISA ANGKA!
            ''')  
        else :
            return WarnaBarang
              

def updateBarangBaru(data) : # Function untuk update value kolom barang
    barangBaru = inputNamaBarang()
    print ('\nNomor Data \t| Kode Barang \t| Barang  \t| Stock \t|  Harga(Rp) \t| Warna')
    for i in range(len(data)) :
        print(f"{i+1}       \t| {data[i]['Kode Barang']}        \t| {barangBaru}        \t| {data[i]['Stock']}      \t| {data[i]['Harga']}      \t| {data[i]['warna']}")
    while True :
        checkUpdate = input("\nApakah anda yakin untuk mengupdate data ini? (ya/tidak) : ").lower()
        if checkUpdate == 'ya' :
            data[0]['Barang'] = barangBaru
            showdata(listBarang)
            print('''
            DATA SUDAH TERUPDATE
            ''')
            return menuUpdate()
        elif checkUpdate == 'Tidak' :
            return menuUpdate()
        else:
            print('''
            MASUKKAN ANGKA DENGAN DENGAN BENAR!
            ''')

def updateStockBaru(data): # Function untuk update value kolom stock
    stockBaru = inputStockBarang()
    print('\nNomor Data \t| Kode Barang \t| Barang  \t| Stock   \t| Harga   \t| Warna')
    for i in range(len(data)) :
        print(f"{i+1}       \t| {data[i]['Kode Barang']}        \t| {data[i]['Barang']}     \t| {stockBaru}     \t| {data[i]['Harga']}      \t| {data[i]['warna']}")
    while True :
        checkUpdate = input("\nApakah anda sudah yakin untuk mengupdate data tersebut? (ya/tidak) :").lower()
        if checkUpdate == 'ya':
            data[0]['Stock'] = stockBaru
            showdata(listBarang)
            print('''
                            DATA SUDAH TERUPDATE''')
            return menuUpdate()
        elif checkUpdate == ' tidak':
            return menuUpdate()
        else :
            print('''
                            MASUKKAN ANGKA YANG BENAR!''')    

def updateHargaBaru(data) : # Function untuk update value kolom harga
    hargaBaru = inputHargaBarang()
    print ('\nNomor Data \t| Kode Barang \t| Barang \t| Stock \t| Harga(Rp) \t| Warna')
    for i in range(len(data)) :
        print(f"{i+1}       \t| {data[i]['Kode Barang']}        \t| {data[i]['Barang']}        \t| {data[i]['Stock']}      \t| {hargaBaru}      \t| {data[i]['warna']}")
    while True :
        checkUpdate = input("\nApakah anda yakin untuk mengupdate data ini? (ya/tidak) : ").lower()
        if checkUpdate == 'ya' :
            data[0]['Harga'] = hargaBaru
            showdata(listBarang)
            print('''
                            DATA SUDAH TERUPDATE
            ''')
            return menuUpdate()
        elif checkUpdate == 'Tidak' :
            return menuUpdate()
        else:
            print('''
                            MASUKKAN ANGKA DENGAN DENGAN BENAR!
            ''')     

def updateWarnaBaru(data) : # Function untuk update value kolom warna
    warnaBaru = inputWarnaBarang()
    print ("\nNomor Data \t| Kode Barang \t| Barang \t| Stock \t| Harga(Rp) \t| Warna")
    for i in range(len(data)) :
        print(f"{i+1}       \t| {data[i]['Kode Barang']}        \t| {data[i]['Barang']}        \t| {data[i]['Stock']}      \t| {data[i]['Harga']}      \t| {warnaBaru}")
    while True :
        checkUpdate = input("\nApakah anda yakin untuk mengupdate data ini? (ya/tidak) : ").lower()
        if checkUpdate == 'ya' :
            data[0]['Warna'] = warnaBaru
            showdata(listBarang)
            print('''
                            DATA SUDAH TERUPDATE
            ''')
            return menuUpdate()
        elif checkUpdate == 'Tidak' :
            return menuUpdate()
        else:
            print('''
                            MASUKKAN ANGKA DENGAN DENGAN BENAR!
            ''')

def deleteData(data, kode) : # Function untuk delete data spesifik
    for i in range(len(data)) :
        if data[i]['Kode Barang'] == kode:
            del data[i]
            break
    showdata(data)    
    print('''
                    DATA SUDAH BERHASIL DI DELETE''')
    return menuDelete()

# Function untuk menu Read
def menuRead():
    menuPencarian = input('''
Menu Pencarian Daftar Penjualan Barang

1. Daftar Penjualan Barang
2. Mencari Daftar Barang
3. Exit Menu Pencarian

Masukkan Angka Yang Ingin Di Jalankan :''')

    if menuPencarian == '1' :
        if len(listBarang) == 0:
            print('''\n
            TIDAK ADA DATA
            ''')
            return menuRead()
        else:
            showdata(listBarang) # line 1
            return menuRead()
    elif menuPencarian == '2' :
        if len(listBarang) == 0:
            print('''\n
            TIDAK ADA DATA
            ''')
            menuRead()
        else :
            kodeBarang = inputKodeBarang() # line 68
            pencarianData = (list(filter(lambda data: data['Kode Barang'] == kodeBarang, listBarang)))
            if len(pencarianData):
                showdata(pencarianData)
                return menuRead()
            else :
                print('''
                TIDAK ADA DATA''')
                return menuRead()       
    elif menuPencarian == '3' :
        return menuUtama() # Line 9  

# Function Menu Create
def menuCreate():
    menuTambahBarang = input('''
Menu Tambah Daftar  Barang

1. Tambah Daftar Barang
2. Exit Menu Tambah Barang

Masukkan Angka Yang Ingin Di Jalankan :''')
    
    if menuTambahBarang == '2' :
        return menuUtama()
    else:
        kodeBarang = inputKodeBarang()
        if len(pencarianData) :
            showdata(pencarianData)
            print('''
            DATA SUDAH ANDA
            ''')
        else :

            namaBarang = inputNamaBarang()
            stockBarang = inputStockBarang()
            hargaBarang = inputHargaBarang()
            warnaBarang = inputWarnaBarang()
            listBarangBaru = [{
            'Kode Barang': kodeBarang,
            'Barang': namaBarang,
            'Stock': stockBarang,
            'Harga': hargaBarang,
            'warna': warnaBarang
            }]
            showdata(listBarangBaru)
            while True:
                tambahdata = input("\nApakah anda yakin ingin menambahkan Data Barang Yang Sudah Ada? (ya/tidak) :").lower()
                if tambahdata == 'ya':
                    listBarang.extend(listBarangBaru)
                    showdata(listBarang)
                    print ('''
                    DATA SUDAH TERSIMPAN 
                    ''')
                    return menuCreate()
                elif tambahdata == 'tidak' :
                    return menuCreate()
                else :
                    print ('''
                    MASUKKAN PILIHAN YANG BENAR!''')
              
# Function Menu Update
def menuUpdate():
    while True:
        menuUpdateBarang = input('''
Menu Update Daftar Barang :

1. Update Data Barang
2. Exit Menu Update

Masukkan Angka Menu Yang Di Jalankan! ''')

        if menuUpdateBarang == '2':
            return menuUtama()
        else:
            if len(listBarang) == 0:
                print('''
                DATA KOSONG MOHON INPUT DATA TERLEBIH DAHULU ''')
            showdata(listBarang) #line 1
            KodeBarang = inputKodeBarang()
            if len(pencarianData):
                showdata(pencarianData)
                while True :
                    updateData = input("Apakah anda yakin ingin mengubah Data Barang Tersebut? (ya/tidak) : ").lower()
                    if updateData == 'ya' :
                        while True :
                            updateBarang = input("\nMasukkan nama kolom data yang ingin diubah (Barang/Stock/Harga/Warna) : ").capitalize()
                            if updateBarang == 'Barang':
                                updateBarangBaru(listBarang)
                                break
                            elif updateBarang == 'Stock':
                                updateStockBaru(listBarang)
                                break
                            elif updateBarang == 'Harga':
                                updateHargaBaru(listBarang)
                                break
                            elif updateBarang == 'Warna' :###
                                updateWarnaBaru(listBarang)
                                break
                            else :
                                print('''
                                MASUKKAN PILIHAN YANG BENAR!''')
                    elif updateData =='tidak' :
                        return menuUpdate()
                    else :
                        print('''
                        DATA YANG ANDA CARI TIDAK ADA!''')
                        return menuUpdate()            
                    break

# Function untuk Menu Delete
def menuDelete() :
    while True :
        menuHapusBarang = input('''
Menu Delete Daftar Barang :
1. Hapus Data Barang
2. Exit Menu Hapus Data

Masukkan Angka Menu Yang Ingin Di Jalankan:''')

        if menuHapusBarang == '2' :
            return menuUtama()
        else:
            if len(listBarang) =='0' :
                print('''
                DATA KOSONG! MOHON INPUT DATA TERLEBIH DAHULU!''')
            else :
                KodeBarang = input('masukkan kode barang : ')
                showdata(pencarianData)
                while True :
                    hapusData = input("\nApakah anda yakin ingin menghapus data barang tersebut? (ya/tidak) : ").capitalize()
                    if hapusData == 'Ya' :
                        deleteData(listBarang, KodeBarang)
                        break
                    elif hapusData == 'Tidak':
                        return menuDelete()
                    else:
                        print('''
                            MASUKKAN PILIHAN DENGAN BENAR ''')

def  inputNomorData(): # Function untuk cek input value Nomor Data
    while True:
        nomorData = input("\nMasukkan Jumlah Yang Ingin Dibeli :")
        x = nomorData.isnumeric()
        if x == True:
            x == int(nomorData)
            return x 
        else:
            print('''
            HANYA MASUKKAN ANGKA TIDAK BISA HURUF! ''')

def  inputQtyBarang(): # Function untuk cek input value Qty Barang
    while True:
        qtyBarang = input("\nMasukkan Jumlah Yang Ingin Dibeli :")
        x = qtyBarang.isnumeric()
        if x == True:
            x == int(qtyBarang)
            return x 
        else:
            print('''
            HANYA MASUKKAN ANGKA TIDAK BISA HURUF! ''')            

listBarang = [
    {
        'Kode Barang': '1001',
        'Barang': 'Biji Kopi Sumatera ',
        'Stock': 50,
        'Harga': 125000,
        'warna': 'Hitam' 
    },
    {
        'Kode Barang': '1002',
        'Barang': 'Biji Kopi Colombia ',
        'Stock': 60,
        'Harga': 150000,
        'warna': 'Cokelat' 
    },
    {
        'Kode Barang': '1003',
        'Barang': 'Biji Kopi veranda ',
        'Stock': 70,
        'Harga': 175000,
        'warna': 'Emas'
    },
    {
        'Kode Barang': '1004',
        'Barang': 'Biji Kopi Italian Roast ',
        'Stock': 80,
        'Harga': 200000,
        'warna': 'Merah' 
    },
    {
        'Kode Barang': '1005',
        'Barang': 'Biji Kopi HouseBlend ',
        'Stock': 90,
        'Harga': 225000,
        'warna': 'Hijau' 
    }
]

keranjang = []

def menuUtama (): # Menu Awal
    print('''
            SELAMAT DATANG DI IMIGRASI COFFEE

                    DAFTAR PILIHAN :

        1. Menu Read Data Barang
        2. Menu Create Barang
        3. Menu Update Barang
        4. Menu Delete Barang
        5. Exit''')

    while True :
        PilihanMenu = input('\nMasukkan Nomor Yang Dipilih (1-5): ')
        if PilihanMenu == '1':
            menuRead()
        elif PilihanMenu == '2':
            menuCreate()
        elif PilihanMenu == '3':
            menuUpdate()
        elif PilihanMenu == '4':
            menuDelete()
        elif PilihanMenu == '5':
            print('\n Terimakasih Kasih Senang Bertemu Dengan Anda :  \n')
            exit()
        else:
            print('Anda Memasukkan Angka Yang Salah\nSilahkan Masukkan Pilihan Menu Yang Benar (1-5) ')
menuUtama()   




