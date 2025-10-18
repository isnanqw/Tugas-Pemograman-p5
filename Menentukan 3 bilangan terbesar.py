# Program menentukan apakah bilangan termasuk kelipatan 3
# dan menentukan hasil terbesar dari dua bilangan

print("=== Program Pembagi 3 dan Pembanding ===")
bilangan = int(input("Masukkan bilangan: "))

# Langkah 1: Periksa apakah bilangan habis dibagi 3
if bilangan % 3 == 0:
    print(f"{bilangan} adalah kelipatan 3 (HASIL BESAR)")
    hasil = "BESAR"
else:
    print(f"{bilangan} bukan kelipatan 3 (HASIL KECIL)")
    hasil = "KECIL"

# Langkah 2: Jika bilangan adalah 1, 2, atau 3, masukkan A, B, C dan bandingkan terbesar
if bilangan in [1, 2, 3]:
    A = int(input("Masukkan bilangan A: "))
    B = int(input("Masukkan bilangan B: "))
    C = int(input("Masukkan bilangan C: "))

    # Logika untuk menentukan terbesar dari A, B, C
    if A > B and A > C:
        terbesar = A
    elif B > C:
        terbesar = B
    else:
        terbesar = C

    print(f"Hasil terbesar adalah: {terbesar}")
else:
    print("Bilangan bukan 1, 2, atau 3, sehingga pembandingan dilewati.")

print("=== SELESAI ===")
