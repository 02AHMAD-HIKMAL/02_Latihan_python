#x = int (input("angka: "))

#if x % 2 == 0:
    #print(f"{x} adalah bilangan GENAP.")
#else:
#print(f"{x} adalah bilangan GANJIL.")

#while True:
    #x = int (input("angka: "))
    #if x % 2 == 0:
        #print(f"{x} adalah bilangan GENAP.")
    #else:
        #print(f"{x} adalah bilangan GANJIL.")
        
    #push = input("tekan 'x' untuk keluar atau tekan tombol lain untuk melanjutkan")
    #if push == "x" :
        #break



#Modul ganjilgenap
def ganjil_genap(a):
    while True:
        ank = int(input("angkamu = "))
        if ank % 2 == 0:
            print(f"{ank} adalah bilangan GENAP")
        else:
            print(f"{ank} adalah bilangan GANJIL")
            
        # Hentikan program jika pengguna mengetik 'stop'    
        pilihan = input("Lanjut atau Stop? (lanjut/stop): ")   
        
        if pilihan == 'stop':
            print("Program selesai.")
            break
                

#Modul Pembagian
def pembagian(c):
    while True:
        angka = int(input("angkamu = "))
        ank = int(input("dibagi dengan angka = "))
        print(f"{angka} / {ank} = {angka / ank}")
        
        # Hentikan program jika pengguna mengetik 'stop'    
        pilihan = input("Lanjut atau Stop? (lanjut/stop): ")   
                
        if pilihan == 'stop':
            print("Program selesai.")
            break
        
    if x == 500:
        "break"
        
        
#Modul Perkalian
def perkalian(b):
    while True:
        angka = int(input("angkamu = "))
        ank = int(input("dikali dengan angka = "))
        print(f"{angka} * {ank} = {angka * ank}")
        
        # Hentikan program jika pengguna mengetik 'stop'    
        pilihan = input("Lanjut atau Stop? (lanjut/stop): ")   
                
        if pilihan == 'stop':
            print("Program selesai.")
            break

print("selesai")
