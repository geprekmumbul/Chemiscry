def get_rantai(nama):
    # Rantai karbon utama
    rantai = [2 for i in range(nama[1])]
    rantai[0] += 1
    rantai[-1] += 1

    # Mengurangi kaki pada ikatan
    jenis = nama[0]
    letak = nama[2]
    rantai[letak - 1] -= (jenis - 1)
    if nama[0] > 1:
        rantai[letak] -= (jenis - 1)

    # Mengurangi kaki pada cabang
    for i in range(4, len(nama), 2):
        for j in range(len(nama[i])):
            rantai[nama[i][j] - 1] -= 1

    return rantai

def struktur_standar(nama):
    # Baris struktur
    struk = [""]
    rantai = get_rantai(nama)

    # Mengubah angka ke struktur CH
    for kaki in rantai:
        if kaki == 0:
            tmp = " C "
        elif kaki == 1:
            tmp = "CH "
        else:
            tmp = "CH" + str(kaki)
        struk[0] += (tmp + "-")

    struk[0] = struk[0][:-1]

    # Menyesuaikan ikatan
    jenis = nama[0]
    letak = nama[2]
    if nama[1] > 1:
        ikatan = ["", "-", "=", "≡"]
        struk[0] = struk[0][:4 * letak - 1] + ikatan[jenis] + struk[0][4 * letak:]


    # Mencari rantai terpanjang
    maks = 0
    for i in range(3, len(nama), 2):
        if maks < nama[i]:
            maks = nama[i]

    # Menambahkan baris untuk cabang:
    for i in range(2 * maks):
        struk.insert(1, " " * (4 * nama[1] - 1))
    for i in range(2 * maks):
        struk.insert(0, " " * (4 * nama[1] - 1))


    # Posisi rantai utama dalam struktur
    rantai = get_rantai(nama)
    pos = 2 * maks
    for i in range(4, len(nama), 2):
        for j in nama[i]:
            temp = 2 * nama[i - 1] - 1

            # Menentukan letak cabang di atas atau di bawah
            if struk[pos - 1][4 * j - 4: 4 * j - 1] == " | ":
                atas = 1
            else:
                atas = -1

            for k in range(temp):
                # Ujung cabang
                if k == temp - 1:
                    tmp0 = struk[pos + atas * (k + 2)]
                    struk[pos + atas * (k + 2)] = tmp0[:4 * j - 4] + "CH3" + tmp0[4 * j - 4:]

                # Memasukkan bagian cabang
                if k % 2 == 0:
                    string = " | "
                else:
                    string = "CH2"
                tmp1 = struk[pos + atas * (k + 1)]
                struk[pos + atas * (k + 1)] = tmp1[:4 * j - 4] + string + tmp1[4 * j - 4:]

    # Menghilangkan baris kosong
    while True:
        if (" " * (4 * nama[1] - 1)) in struk:
            struk.remove(" " * (4 * nama[1] - 1))
        else:
            break

    return struk
