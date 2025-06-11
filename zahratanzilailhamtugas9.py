import os
import time
from termcolor import colored

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

lebar_kotak = 40
tinggi_kotak_vertikal = 3

teks_asli = "HAPPY EID"
teks_untuk_digulir = " " * lebar_kotak + teks_asli + " " * lebar_kotak

durasi_animasi_detik = 20
total_langkah_gulir = len(teks_untuk_digulir) - lebar_kotak
jeda_per_langkah = durasi_animasi_detik / total_langkah_gulir

garis_horizontal = "+" + "-" * (lebar_kotak + 2) + "+"

for langkah_saat_ini in range(total_langkah_gulir):
    bersihkan_layar()

    teks_yang_terlihat = teks_untuk_digulir[langkah_saat_ini : langkah_saat_ini + lebar_kotak]

    print(garis_horizontal)

    for _ in range(tinggi_kotak_vertikal // 2):
        print("|" + " " * (lebar_kotak + 2) + "|")

    print("| " + colored(teks_yang_terlihat, "green") + " |")

    for _ in range(tinggi_kotak_vertikal - tinggi_kotak_vertikal // 2):
        print("|" + " " * (lebar_kotak + 2) + "|")

    print(garis_horizontal)

    time.sleep(jeda_per_langkah)