from struk import get_rantai

class Salah(Exception):
   def __init__(self, value):
      self.value = value
   def __str__(self):
      return(repr(self.value))

def input_nama():
    nama = ""
    def debug(i):
        #print(str(i) + ". ", end="")
        #print(nama)
        pass

    # Input nama huruf kecil
    nama = input("Masukkan nama senyawa hidrokarbon : ")
    nama = nama.lower()
    debug(1)

    # Nama terlalu pendek
    if len(nama) < 5:
        raise Salah("Nama senyawa tidak dikenali")

    # Cek penulisan
    char = "abcdefghijklmnopqrstuvwxyz0123456789-,"
    for ch in nama:
        if ch not in char:
            raise Salah("Nama senyawa tidak dikenali")


    # Urutan penamaan dari belakang
    nama = nama.split("-")
    nama.reverse()
    debug(2)

    # Menambahkan jenis HC
    jenis = {"ana": 1, "ena": 2, "una": 3}
    if nama[0][-3:] in jenis:
        nama.insert(0, jenis[nama[0][-3:]])
        nama[1] = nama[1][:-3]
    else:
        raise Salah("Nama senyawa tidak dikenali")
    debug(3)


    # Menstandarkan alkana
    tmp = nama[1].split("il")
    tmp.reverse()
    if len(tmp) > 1:
        nama[1] = tmp[0]
        nama.insert(2, tmp[1])
    debug(4)

    # Menyamakan penomoran alkana
    if nama[0] == 1:
        nama.insert(2, "1")
    debug(5)


    # Mengubah bagian angka jadi list
    for i in range(2, len(nama), 2):
        lst = nama[i].split(",")
        for j in range(len(lst)):
            if lst[j].isnumeric():
                lst[j] = int(lst[j])
            else:
                raise Salah("Nama senyawa tidak dikenali")
        nama[i] = lst
    debug(6)

    # Posisi ikatan belum dimasukkan
    if (len(nama) < 3) and (nama[1] != "met"):
        raise Salah("Letak ikatan rangkap harus dimasukkan")

    # Ikatan rangkap panjangnya harus lebih dari 1
    if (nama[0] > 1) and (nama[1] == "met"):
        raise Salah("Ikatan rangkap minimal memiliki panjang 2")


    # Mengubah nama[2] dari list jadi int
    nama[2] = nama[2][0]
    debug(7)

    # Mencocokan nama dengan list
    prefiks = ["", "", "di", "tri", "tetra", "penta", "heksa",
                "hepta", "okta", "nona", "deka", "il"]
    for i in range(4, len(nama), 2):
        tmp = len(nama[i])
        pref = prefiks[tmp]
        if not nama[i - 1].startswith(pref):
            raise Salah("Nama hidrokarbon tidak sesuai IUPAC")

    # Menghilangkan prefiks dan suffiks
    for i in range(1, len(nama), 2):
        for pref in prefiks:
            nama[i] = nama[i].replace(pref, "")
    debug(8)

    # Mengubah gugus alkil menjadi angka
    alkil = {"met": 1, "et": 2, "prop": 3, "but": 4, "pent": 5,
             "heks": 6, "hept": 7, "okt": 8, "non": 9, "dek": 10}
    for i in range(1, len(nama), 2):
        if nama[i] in alkil:
            nama[i] = alkil[nama[i]]
        else:
            raise Salah("Nama seenyawa tidak dikenali")
    debug(9)


    # Urutan nomor harus dari kecil
    for i in range(4, len(nama), 2):
        min = -1000
        for j in range(len(nama[i])):
            if min <= nama[i][j]:
                min = nama[i][j]
            else:
                raise Salah("Urutan penomoran kurang tepat")

            # Nomor cabang antara 1 sampai panjang rantai
            if (min < 1) or (min > nama[1]):
                raise Salah("Letak cabang melebihi panjang rantai")

    # Pada alkana, letak cabang harus di angka terkecil
    if nama[0] == 1:
        min_kiri = 1000
        min_kanan = 1000
        for i in range(4, len(nama), 2):
            # Mencari ujung terdekat
            min = nama[i][0]
            max = nama[1] - nama[i][-1] + 1
            if min < min_kiri:
                min_kiri = min
            if max < min_kanan:
                min_kanan = max

            # Urutan cabang di harus dekat 1
            if min_kiri > min_kanan:
                raise Salah("Letak cabang harus dimulai dari angka terkecil")

    # "Cabang" mestinya rantai utama
    for i in range(4, len(nama), 2):
        min = nama[i][0]
        max = nama[1] - nama[i][-1] + 1
        if (min < (nama[i - 1] + 1)) or (max < (nama[i - 1] + 1)):
            raise Salah("Penamaan cabang kurang tepat")


    # Jumlah kaki tidak cukup
    rantai = get_rantai(nama)
    for num in rantai:
        if num < 0:
            raise Salah("Banyak kaki ikatan karbon tidak cukup")

    # Letak ikatan harus dekat ujung
    if (nama[0] > 1) and (nama[2] * 2 > nama[1]):
        raise Salah("Letak ikatan harus yang paling dekat dengan ujung")

    print("Selesai")
    return nama
