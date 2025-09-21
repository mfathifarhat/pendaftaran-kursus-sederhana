# Deklarasi Variabel dan Konstanta

# Konstanta untuk maksimum kursus yang dapat diambil
MAX_COURSES = 2
pilihan = "" # Untuk menampung nomor kursus yang dipilih
kursusKu = "" # Untuk menyimpan nomor kursus yang sudah didaftar
jadwalKu = "" # Untuk menyimpan jadwal kursus yang sudah didaftarkan
nambah = "1" # Untuk opsi apakah pengguna ingin mendaftar kursus lain
berhasil = False  # Untuk status pendaftaran apakah sukses atau gagal
message = ""  # Untuk pesan peringatan ketika pendaftaran gagal

# Deklarasi variabel untuk data kursus
kursus1, jadwal1, kuota1 = "Mahir Membuat Website untuk Pemula", "08:00", 1
kursus2, jadwal2, kuota2 = "Javascript Dasar untuk Pemrograman Web", "06:00", 0
kursus3, jadwal3, kuota3 = "Membuat Tampilan Website yang Menarik dengan Tailwind 4", "16:00", 10
kursus4, jadwal4, kuota4 = "Laravel : Dari Pemula hingga Mahir", "09:00", 10
kursus5, jadwal5, kuota5 = "Spring Boot : Dari Pemula hingga Mahir", "08:00", 5

while len(kursusKu) < MAX_COURSES and nambah == "1":
    print(f"""
    Nomor   : 1 {"(Sudah daftar)" if "1" in kursusKu else ""}
    Judul   : {kursus1}
    Jadwal  : {jadwal1}
    Kuota   : {kuota1}

    Nomor   : 2 {"(Sudah daftar)" if "2" in kursusKu else ""}
    Judul   : {kursus2}
    Jadwal  : {jadwal2}
    Kuota   : {kuota2}

    Nomor   : 3 {"(Sudah daftar)" if "3" in kursusKu else ""}
    Judul   : {kursus3}
    Jadwal  : {jadwal3}
    Kuota   : {kuota3}

    Nomor   : 4 {"(Sudah daftar)" if "4" in kursusKu else ""}
    Judul   : {kursus4}
    Jadwal  : {jadwal4}
    Kuota   : {kuota4}

    Nomor   : 5 {"(Sudah daftar)" if "5" in kursusKu else ""}
    Judul   : {kursus5}
    Jadwal  : {jadwal5}
    Kuota   : {kuota5}
    """)

    pilihan = input("Silahkan masukkan nomor kursus yang ingin anda ikuti\n")

    match pilihan:
        case "1":
            if "1" in kursusKu.split():
                berhasil = False
                message = "Anda sudah mendaftar di kursus ini!"
            elif kuota1 <= 0:
                berhasil = False
                message = "Maaf, kuota sudah penuh!"
            elif jadwal1 in jadwalKu.split():
                berhasil = False
                message = "Anda sudah mendaftar kursus lain di waktu yang sama!"
            else:
                kursusKu += "1"
                jadwalKu += jadwal1 + " "
                kuota1 -= 1
                berhasil = True
                print(f"Selamat, anda sudah terdaftar di kursus '{kursus1}'")
        case "2":
            if "2" in kursusKu.split():
                berhasil = False
                message = "Anda sudah mendaftar di kursus ini!"
            elif kuota2 <= 0:
                berhasil = False
                message = "Maaf, kuota sudah penuh!"
            elif jadwal2 in jadwalKu.split():
                berhasil = False
                message = "Anda sudah mendaftar kursus lain di waktu yang sama!"
            else:
                kursusKu += "2"
                jadwalKu += jadwal2 + " "
                kuota2 -= 1
                berhasil = True
                print(f"Selamat, anda sudah terdaftar di kursus '{kursus2}'")
        case "3":
            if "3" in kursusKu.split():
                berhasil = False
                message = "Anda sudah mendaftar di kursus ini!"
            elif kuota3 <= 0:
                berhasil = False
                message = "Maaf, kuota sudah penuh!"
            elif jadwal3 in jadwalKu.split():
                berhasil = False
                message = "Anda sudah mendaftar kursus lain di waktu yang sama!"
            else:
                kursusKu += "3"
                jadwalKu += jadwal3 + " "
                kuota3 -= 1
                berhasil = True
                print(f"Selamat, anda sudah terdaftar di kursus '{kursus3}'")
        case "4":
            if "4" in kursusKu.split():
                berhasil = False
                message = "Anda sudah mendaftar di kursus ini!"
            elif kuota4 <= 0:
                berhasil = False
                message = "Maaf, kuota sudah penuh!"
            elif jadwal4 in jadwalKu.split():
                berhasil = False
                message = "Anda sudah mendaftar kursus lain di waktu yang sama!"
            else:
                kursusKu += "4"
                jadwalKu += jadwal4 + " "
                kuota4 -= 1
                berhasil = True
                print(f"Selamat, anda sudah terdaftar di kursus '{kursus4}'")
        case "5":
            if "5" in kursusKu.split():
                berhasil = False
                message = "Anda sudah mendaftar di kursus ini!"
            elif kuota5 <= 0:
                berhasil = False
                message = "Maaf, kuota sudah penuh!"
            elif jadwal5 in jadwalKu.split():
                berhasil = False
                message = "Anda sudah mendaftar kursus lain di waktu yang sama!"
            else:
                kursusKu += "5"
                jadwalKu += jadwal5 + " "
                kuota5 -= 1
                berhasil = True
                print(f"Selamat, anda sudah terdaftar di kursus '{kursus5}'")
        case _:
            berhasil = False
            message = "Silahkan masukkan nomor kursus yang sudah tertera di atas!"

    if berhasil == False:
        print(message)
        continue
    else:
        if len(kursusKu) < MAX_COURSES:
            print("Berikut adalah kursus yang sudah anda daftarkan: \n")
            for kursus in kursusKu:
                match kursus:
                    case "1":
                        print(f"Judul   : {kursus1}")
                        print(f"Jadwal  : {jadwal1}\n")

                    case "2":
                        print(f"Judul   : {kursus2}")
                        print(f"Jadwal  : {jadwal2}\n")

                    case "3":
                        print(f"Judul   : {kursus3}")
                        print(f"Jadwal  : {jadwal3}\n")

                    case "4":
                        print(f"Judul   : {kursus4}")
                        print(f"Jadwal  : {jadwal4}\n")

                    case "5":
                        print(f"Judul   : {kursus5}")
                        print(f"Jadwal  : {jadwal5}\n")

                    case _:
                        print("Kursus sudah tidak tersedia\n")
            nambah = input(
                "Apakah anda ingin mendaftar kursus lain? Ketik 1 jika iya dan ketik karakter lain jika tidak\n")
        else:
            print("Anda sudah mencapai batas maksimal jumlah kursus yang bisa didaftar!")
            break

print("Terima kasih sudah mendaftar kursus kami. Berikut adalah kursus yang sudah anda daftar:\n")

for kursus in kursusKu:
    match kursus:
        case "1":
            print(f"Judul   : {kursus1}")
            print(f"Jadwal  : {jadwal1}\n")

        case "2":
            print(f"Judul   : {kursus2}")
            print(f"Jadwal  : {jadwal2}\n")

        case "3":
            print(f"Judul   : {kursus3}")
            print(f"Jadwal  : {jadwal3}\n")

        case "4":
            print(f"Judul   : {kursus4}")
            print(f"Jadwal  : {jadwal4}\n")

        case "5":
            print(f"Judul   : {kursus5}")
            print(f"Jadwal  : {jadwal5}\n")

        case _:
            print("Kursus sudah tidak tersedia\n")

print("Semoga harimu menyenangkan! ヾ(≧▽≦*)o")