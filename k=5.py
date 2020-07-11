import string


def penerjemah(formatnya, stringnya):
    huruf = list(string.ascii_lowercase)
    formatnya = formatnya
    kata = stringnya
    angka_terpilih = int(formatnya[2:]) - 1  # -1 biar meneyesuaikan list yang dimulai dari 0
    huruf_terpilih = formatnya[0].lower()
    posisi_huruf = huruf.index(huruf_terpilih)
    angka_terpilih -= posisi_huruf
    # if positif buat nentuin ngeprint dari huruf terpilih sampai pengganti z (paling belakangnya)
    # else buat nentuin sebelum huruf sampai pengganti a, dibelakang untuk append sampai pengganti z
    if angka_terpilih > 0:
        huruf_baru = [huruf[i] for i in range(posisi_huruf, 26 - angka_terpilih)]
        for i in range(posisi_huruf - 1, -1, -1):  # start sebelum huurf terpilih, sampai indeks ke 0 makanya -1, mundur
            huruf_baru.insert(0, huruf[i])
        for i in range(25, huruf.index(huruf_baru[-1]), -1):
            huruf_baru.insert(0, huruf[i])  # nyetak kebalik mulai dari z sampai ke yang jadi index 1 alias pengganti a
    else:
        huruf_baru = [huruf[i] for i in range(posisi_huruf, 26)]
        angka_terpilih *= -1
        for i in range(posisi_huruf - 1, angka_terpilih - 1, -1):
            # pos_huruf -1 biar huruf yang sudah ke print gak ketut
            # angka terpilih -1 biar huruf yang pengganti a juga ketut
            huruf_baru.insert(0, huruf[i])
        sisa = [huruf[x] for x in range(0, angka_terpilih)]
        huruf_baru.extend(sisa)

    index_kata = []
    for i in kata:
        for j in range(len(huruf_baru)):
            if i == huruf_baru[j]:
                index_kata.append(j)
    for i in index_kata:
        kata_barunya = i
        print(huruf[kata_barunya], end='')
    print()


keluar = False
while not keluar:
    print("Penerjemah bahasa panda tipe k=5")
    try:
        sarat = input('Masukkan rumus dengan format \'k=5\'')
        kata = input('Masukkan kata : ')
        penerjemah(sarat, kata)
    except(ValueError, ) as ex:
        print("Errornya: {}".format(ex))
    finally:
        lagi = input("Hitung lagi? (y/n) : ")
        if lagi == 'n':
            print("Gamsahamida")
            keluar = True
