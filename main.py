while True:
    import ModulMath
    import ModulBangunDatar

    print("Menu Modul")
    print("1.Ganjil Genap\n2.Pembagian\n3.Perkalian\n4.Luas Persegi\n5.Luas Segitiga\n6.Keliling Persegi")
    print("")
    a = int(input("No = "))
    if a == 1:
        print(ModulMath.ganjil_genap(print("Ganjil Genap\nMasukkan angkamu")))
    if a == 2:
        print(ModulMath.pembagian(print("Pembagian\nMasukkan Angkamu")))
    if a == 3:
        print(ModulMath.perkalian(print("Perkalian\nMasukkan Angkamu")))
    if a == 4:
        print(ModulBangunDatar.luaspersegi(print("Hitung Luas Persegimu\nMasukkan Angkamu")))
    if a == 5:
        print(ModulBangunDatar.luassegitiga(print("Hitung Luas Segitigamu\nMsukkan Angkamu")))
    if a == 6:
        print(ModulBangunDatar.kelilingpersegi(print("Hitung Keliling Persegimu\nMasukkan Angkamu")))
    pilihan = input("Lanjut atau Stop? (lanjut/stop perkalian): ")   
                
    if pilihan == 'stop':
        print("Program selesai.")
        break  
