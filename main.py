
def hitung_total(harga, jumlah):
    return harga * jumlah


def hitung_diskon(total, persen=10):
    return total * persen / 100


def cetak_ringkasan(nama, harga, jumlah):
    total = hitung_total(harga, jumlah)
    diskon = hitung_diskon(total)

    print("Pelanggan:", nama)
    print("Total:", total)
    print("Diskon:", diskon)
    print("Bayar:", total - diskon)


if __name__ == "__main__":
    cetak_ringkasan("Andi", 15000, 2)
