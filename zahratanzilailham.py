print("----MENU MAKANAN----")

paket_ayam = 20000
print(f"paket a:ayam = Rp {paket_ayam}" )
paket_sapi = 35000
print(f"paket b:sapi = Rp {paket_sapi}")
paket_cumi_cumi = 45000
print(f"paket c:cumi_cumi = Rp {paket_cumi_cumi}")


pesanan = (input("pesanan paket:"))

if pesanan == "ayam":
    harga = 20000
elif pesanan == "sapi":
    harga = 35000
elif pesanan == "cumi-cumi":
    harga = 45000
else :
    print("pilihan tidak tersedia")

print("--- LAMPIRKAN JARAK RUMAH ANDA---")
jarak= float(input("jarak rumah (km): "))

if jarak<1:
    ongkir = 0
elif 1 <= jarak <= 3:
    ongkir = 7000
else:
    ongkir = 15000
    print(f"ongkir anda :{ongkir}")


total_biaya = harga + ongkir
print(f"total biaya = Rp{total_biaya}")