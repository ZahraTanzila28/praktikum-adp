titik = []
for i in range(3):
    x = float(input(f"masukkan x{i+1}: "))
    y = float(input(f"masukkan y{i+1}: "))
    titik.append([x,y])

AB = (titik[0][0] - titik[1][0])**2 + (titik[0][1] - titik[1][1])**2
BC = (titik[1][0] - titik[2][0])**2 + (titik[1][1] - titik[2][1])**2
AC = (titik[0][0] - titik[2][0])**2 + (titik[0][1] - titik[2][1])**2

if AB == BC or AB == AC or BC == AC:
    print("segitiga tersebut adalah SEGITIGA SAMA KAKI.")
else:
    print("segitiga tersebut BUKAN SEGITIGA SAMA KAKI.")
