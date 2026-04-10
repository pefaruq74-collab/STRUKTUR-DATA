def binary_search(arr, target):
    awal = 0
    akhir = len(arr) - 1

    while awal <= akhir:
        tengah = (awal + akhir) // 2

        if arr[tengah] == target:
            return tengah
        elif arr[tengah] < target:
            awal = tengah + 1
        else:
            akhir = tengah - 1

    return -1

nama = input("Masukkan nama: ").lower()

huruf = sorted(list(nama))

cari = input("Masukkan huruf yang dicari: ").lower()

hasil = binary_search(huruf, cari)

print("Array huruf:", huruf)

if hasil != -1:
    print("Huruf ditemukan di index ke-", hasil)
else:
    print("Huruf tidak ditemukan")