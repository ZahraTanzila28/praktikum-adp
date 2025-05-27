def menu():
    print("\nMenu:")
    print("1. Tabel perkalian modulo n")
    print("2. Mencari nilai Σ x")
    print("3. Mencari nilai n!")
    print("4. Total dan rata-rata suatu data")
    print("5. Keluar")

def tabel_modulo():
    while True:
        n = int(input("Masukkan nilai n (1-10): "))
        if 1 <= n <= 10:
            break
        print("Input tidak sesuai. Masukkan n antara 1 sampai 10.")
    
    print(f"\nTabel Perkalian Modulo {n} (Cayley Table):")
    for i in range(n):
        for j in range(n):
            print((i * j) % n, end=" ")
        print()

def Σχ ():
    while True:
        bawah = int(input("Masukkan batas bawah: "))
        atas = int(input("Masukkan batas atas: "))
        if atas >= bawah:
            break
        print("Batas atas harus lebih besar dari batas bawah.")
        
    total = 0
    for x in range(bawah, atas + 1):
        total += x
    print(f"Σχ dari {bawah} sampai {atas} adalah {total}")

def faktorial():
    while True:
        n = int(input("Masukkan nilai n (n ≥ 0): "))
        if n >= 0:
            break
        print("Input salah. n harus ≥ 0.")
    
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    print(f"{n}! = {hasil}")

def total_rata():
    while True:
        n = int(input("Masukkan banyak data: "))
        if n > 0:
            break
        print("Jumlah data harus lebih dari 0.")
    
    data = []
    for i in range(n):
        nilai = float(input(f"Data ke-{i+1}: "))
        data.append(nilai)
    
    total = len(data)
    rata = total / n

    print("\nData:", data)
    print("Total =", total)
    print("Rata-rata =", rata)

def pilih_menu():
    while True:
        menu()
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            tabel_modulo()
        elif pilihan == "2":
            Σχ()
        elif pilihan == "3":
            faktorial()
        elif pilihan == "4":
            total_rata()
        elif pilihan == "5":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "---pilih_menu---":
    pilih_menu()