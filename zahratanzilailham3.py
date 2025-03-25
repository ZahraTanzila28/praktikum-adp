n= int(input("\nmasukan pola ukuran ( minimal 4) : "))

if n < 4:
    print("nilai n harus minimal 4.")
total_boom = 0

for i  in range(n):
        for j in range(n):
            if i == j:
                if n % 2 == 1 and i == n // 2:
                    print(" HORE ,", end=" ")
                else:
                    print(" 1 ", end=" ")
            elif i + j == n - 1:
                print(" 2 ", end=" ")
            else:
                print(" BOOM ", end=" ")
                total_boom += 1
        print()
print("total BOOM yang muncul sebanyak = ", total_boom)

