#Modul luaspersegi        
def luaspersegi(d):
    while True:
        sisi = float(input("masukkan panjang sisi persegi: "))
        luas = sisi * sisi
        print(f"keliling persegi dengan sisi {sisi} adalah {luas}")
        
        # Hentikan program jika pengguna mengetik 'stop'
        pilihan = input("Lanjut atau Stop? (lanjut/stop): ")
        if pilihan == 'stop':
            print("program selesai.")
            break  
        
#Modul luas segitiga
def luassegitiga(e):
    while True:
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = 0.5 * alas * tinggi
        print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas}")

        # Hentikan program jika pengguna mengetik 'stop'
        pilihan = input("Lanjut atau Stop? (lanjut/stop): ")
        if pilihan == 'stop':
             print("program selesai.")
             break
         
#Modul keliling persegi
def kelilingpersegi(f):
    while True:
        sisi = float(input("Masukkan panjang sisi persegi: "))
        keliling = 4 * sisi
        print(f"Keliling persegi dengan sisi {sisi} adalah {keliling}")
        
        # Hentikan program jika pengguna mengetik 'stop'
        pilihan = input("Lanjut atau Stop? (lanjut/stop): ")
        if pilihan == 'stop':
             print("program selesai.")
             break
    
    
print("selesai")