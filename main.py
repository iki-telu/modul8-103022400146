
def hitung_total(harga, jumlah):
    if harga < 0 or jumlah < 0:
        raise ValueError("Harga dan jumlah tidak boleh negatif")
    return harga * jumlah


def hitung_diskon(total, persen):
    if persen < 0 or persen > 100:
        raise ValueError("Diskon harus antara 0 sampai 100")
    return total * persen / 100


def hitung_pajak(total, persen):
    if persen < 0 or persen > 100:
        raise ValueError("Pajak tidak valid")
    return total * persen / 100


def hitung_pembayaran(total, diskon, pajak):
    hasil_diskon = hitung_diskon(total, diskon)
    sisa = total - hasil_diskon
    biaya_pajak = hitung_pajak(sisa, pajak)
    return sisa + biaya_pajak


def tampilkan_produk(nama, harga, jumlah):
    print("Nama produk:", nama)
    print("Harga:", harga)
    print("Jumlah:", jumlah)


def tampilkan_struk(nama, harga, jumlah, diskon, pajak):
    total = hitung_total(harga, jumlah)
    pembayaran = hitung_pembayaran(total, diskon, pajak)

    print("\n===== STRUK PEMBELIAN =====")
    tampilkan_produk(nama, harga, jumlah)
    print("Total belanja:", total)
    print("Diskon:", diskon, "%")
    print("Pajak:", pajak, "%")
    print("Total pembayaran:", pembayaran)
    print("===========================")


def main():
    nama = "Laptop"
    harga = 5000000
    jumlah = 2
    diskon = 10
    pajak = 11

    tampilkan_struk(
        nama,
        harga,
        jumlah,
        diskon,
        pajak
    )


if __name__ == "__main__":
    main()
