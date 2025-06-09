#  MENULIS DATA PRAKTIKAN KE FILE
data = [
    "2410431019,Lxania Nazila,85,80,89",
    "2410431039,Zazkia Avris Yaumi,90,90,0",
    "2410432041,Melda Afrilia,100,100,95",
    "2410431003,Aisyah Ashari,70,100,0",
    "2410433011,Khesya Chayara,90,100,82",
    "2410431013,Aisy Fitria,70,70,91",
    "2410433001,Zahra Adelia,70,100,0",
    "2410431001,Rifqa Humairah,90,70,85",
    "2410432038,Desy Fadilla,90,90,80",
    "2410432039,Aulya Rizky,100,100,55"
]

with open("data_praktikan.txt", "w") as f:
    for line in data:
        f.write(line + "\n")

# menyimpan ke file dan Membaca ke dictionary
praktikan_dict = {}

with open("data_praktikan.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    bagian = line.strip().split(",")
    nim = bagian[0]
    nama = bagian[1]
    pretest = int(bagian[2])
    postest = int(bagian[3])
    tugas = int(bagian[4])

    praktikan_dict[nim] = {
        "nama": nama,
        "pretest": pretest,
        "postest": postest,
        "tugas": tugas
    }

# 3. Hitung nilai akhir dan simpan ke file
with open("data_nilai_akhir.txt", "w") as f:
    f.write("NIM,Nama,Pretest,Postest,Tugas,Nilai Akhir\n")

    for nim in praktikan_dict:
        pre = praktikan_dict[nim]["pretest"]
        post = praktikan_dict[nim]["postest"]
        tugas = praktikan_dict[nim]["tugas"]
        total = (35 * pre + 35 * post + 30 * tugas) / 100
        praktikan_dict[nim]["nilai_akhir"] = total

        f.write(nim + "," + praktikan_dict[nim]["nama"] + "," +
                str(pre) + "," + str(post) + "," + str(tugas) + "," + str(total) + "\n")

# 4.Hasil Analisis Data
total_nilai = 0
jumlah = 0

for nim in praktikan_dict:
    total_nilai += praktikan_dict[nim]["nilai_akhir"]
    jumlah += 1

rata_rata = total_nilai / jumlah

# Nilai tertinggi dan terendah dan terendah data praktikan
pertama = True
for nim in praktikan_dict:
    nilai = praktikan_dict[nim]["nilai_akhir"]

    if pertama:
        tertinggi_nilai = nilai
        tertinggi_nim = nim
        terendah_nilai = nilai
        terendah_nim = nim
        pertama = False
    else:
        if nilai > tertinggi_nilai:
            tertinggi_nilai = nilai
            tertinggi_nim = nim
        if nilai < terendah_nilai:
            terendah_nilai = nilai
            terendah_nim = nim

jumlah_bawah_rata = 0
for nim in praktikan_dict:
    if praktikan_dict[nim]["nilai_akhir"] < rata_rata:
        jumlah_bawah_rata += 1

# 5. Cetak hasil
print("=== HASIL ANALISIS DATA  PRAKTIKAN===")
print(f"Rata-rata nilai akhir : {rata_rata:.2f}")
print(f"Nilai tertinggi       : {praktikan_dict[tertinggi_nim]['nama']} ({tertinggi_nim}) = {praktikan_dict[tertinggi_nim]['nilai_akhir']:.2f}")
print(f"Nilai terendah        : {praktikan_dict[terendah_nim]['nama']} ({terendah_nim}) = {praktikan_dict[terendah_nim]['nilai_akhir']:.2f}")
print(f"Jumlah yang di bawah rata-rata: {jumlah_bawah_rata}")
