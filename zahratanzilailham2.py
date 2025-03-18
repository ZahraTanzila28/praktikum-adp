while True:
    angka1 = float(input("\nmasukan angka pertama: "))
    angka2 = float(input("masukan anka kedua: "))

    print("\npilih operasi")
    print("1. penjumlahan")
    print("2. pengurangan")
    print("3. perkalian")
    print("4. pembagian")
    print("5. keluar")

    pilihan= input("pilih(1/2/3/4/5): ")

    if pilihan == "1":
        hasil = angka1 + angka2
        print("\nhasil : ", hasil)
    elif pilihan == "2":
        hasil = angka1 - angka2
        print("\nhasil : ", hasil)
    elif pilihan == "3":
        hasil = angka1 * angka2
        print("\nhasil : ", hasil)
    elif pilihan == "4":
        if angka2 == 0 :
            print("kesalahan : pembagaian tidak boleh nol") 
        else :
            hasil = angka1 / angka2
            print("\nhasil : ", hasil)
    elif pilihan == "5":
        print("Thank You! program selesai")
        break
    else :
        print("pilihan tidak valid, silahkan coba lagi\n")



    
            
       


    
            
