import os
import time
from termcolor import colored

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def text_LED(teks, langkah, durasi, text_color, highlight_color, lebar):
    delay = durasi / langkah

    teks_terisi = ' ' * lebar + teks + ' ' * lebar
    teks_len = len(teks_terisi)

    garis_atas_kotak = "+" + "-" * (lebar + 2) + "+"
    garis_bawah_kotak = "+" + "-" * (lebar + 2) + "+"

    tinggi_kotak = 3

    for step in range(langkah):
        clear()
        posisi = teks_len - lebar - step
        if posisi < 0:
            posisi = 0
        window = teks_terisi[posisi:posisi + lebar]

        print(garis_atas_kotak)

        for _ in range(tinggi_kotak // 2):
            print("|" + " " * (lebar + 2) + "|")

        print('| ', end="")
        for karakter in window:
            print(colored(karakter, text_color, highlight_color), end="")
        print(' |')

        for _ in range(tinggi_kotak - tinggi_kotak // 2):
            print("|" + " " * (lebar + 2) + "|")

        print(garis_bawah_kotak)
        time.sleep(delay)

text_LED(
    teks="HAPPY EID",
    langkah=40,
    durasi=20,
    text_color='green',
    highlight_color=None,
    lebar=40
)