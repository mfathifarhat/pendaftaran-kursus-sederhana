# Deklarasi Variabel dan Konstanta

# Konstanta untuk maksimum kursus yang dapat diambil
MAX_COURSES = 2
pilihan = "" # Untuk menampung nomor kursus yang dipilih
kursusKu = "" # Untuk menyimpan nomor kursus yang sudah didaftar
jadwalKu = "" # Untuk menyimpan jadwal kursus yang sudah didaftarkan
nambah = "1" # Untuk opsi apakah pengguna ingin mendaftar kursus lain
berhasil = False  # Untuk status pendaftaran apakah sukses atau gagal
message = ""  # Untuk pesan peringatan ketika pendaftaran gagal

print("""
Pilih nomor kursus yang ingin anda ikuti :

Nomor   : 1
Judul   : Mahir Membuat Website untuk Pemula
Jadwal  : 08:00
Kuota   : 1

Nomor   : 2
Judul   : Javascript Dasar untuk Pemrograman Web
Jadwal  : 06:00
Kuota   : 0

Nomor   : 3
Judul   : Membuat Tampilan Website yang Menarik dengan Tailwind 4
Jadwal  : 16:00
Kuota   : 10

Nomor   : 4
Judul   : Laravel : Dari Pemula hingga Mahir
Jadwal  : 09:00
Kuota   : 10

Nomor   : 5
Judul   : Spring Boot : Dari Pemula hingga Mahir
Jadwal  : 08:00
Kuota   : 5
      """)

while len(kursusKu) < MAX_COURSES and nambah == "1":
    pilihan = input("Silahkan masukkan nomor kursus yang ingin anda ikuti\n")

    match pilihan:
        case "1":
            kuota = 1
            jadwal = "08:00"

            if "1" in kursusKu.split():
                berhasil = False
                message = "Anda sudah mendaftar di kursus ini!"
            elif kuota <= 0:
                berhasil = False
                message = "Maaf, kuota sudah penuh!"
            elif jadwal in jadwalKu.split():
                berhasil = False
                message = "Anda sudah mendaftar kursus lain di waktu yang sama!"
            else:
                kursusKu += "1"
                jadwalKu += jadwal + " "
                berhasil = True
        case "2":
            kuota = 0
            jadwal = "06:00"

            if "2" in kursusKu.split():
                berhasil = False
                message = "Anda sudah mendaftar di kursus ini!"
            elif kuota <= 0:
                berhasil = False
                message = "Maaf, kuota sudah penuh!"
            elif jadwal in jadwalKu.split():
                berhasil = False
                message = "Anda sudah mendaftar kursus lain di waktu yang sama!"
            else:
                kursusKu += "2"
                jadwalKu += jadwal + " "
                berhasil = True
        case "3":
            kuota = 10
            jadwal = "16:00"

            if "3" in kursusKu.split():
                berhasil = False
                message = "Anda sudah mendaftar di kursus ini!"
            elif kuota <= 0:
                berhasil = False
                message = "Maaf, kuota sudah penuh!"
            elif jadwal in jadwalKu.split():
                berhasil = False
                message = "Anda sudah mendaftar kursus lain di waktu yang sama!"
            else:
                kursusKu += "3"
                jadwalKu += jadwal + " "
                berhasil = True
        case "4":
            kuota = 10
            jadwal = "09:00"

            if "4" in kursusKu.split():
                berhasil = False
                message = "Anda sudah mendaftar di kursus ini!"
            elif kuota <= 0:
                berhasil = False
                message = "Maaf, kuota sudah penuh!"
            elif jadwal in jadwalKu.split():
                berhasil = False
                message = "Anda sudah mendaftar kursus lain di waktu yang sama!"
            else:
                kursusKu += "4"
                jadwalKu += jadwal + " "
                berhasil = True
        case "5":
            kuota = 5
            jadwal = "08:00"

            if "5" in kursusKu.split():
                berhasil = False
                message = "Anda sudah mendaftar di kursus ini!"
            elif kuota <= 0:
                berhasil = False
                message = "Maaf, kuota sudah penuh!"
            elif jadwal in jadwalKu.split():
                berhasil = False
                message = "Anda sudah mendaftar kursus lain di waktu yang sama!"
            else:
                kursusKu += "5"
                jadwalKu += jadwal + " "
                berhasil = True
        case _:
            berhasil = False
            message = "Silahkan masukkan nomor kursus yang sudah tertera di atas!"

    if berhasil == False:
        print(message)
        continue
    else:
        if len(kursusKu) < MAX_COURSES:
            nambah = input(
                "Apakah anda ingin mendaftar kursus lain? Ketik 1 jika iya dan ketik karakter lain jika tidak\n")
        else:
            break

print("Terima kasih sudah mendaftar kursus kami. Berikut adalah kursus yang sudah anda daftar:\n")

for kursus in kursusKu:
    match kursus:
        case "1":
            print("Judul   : Mahir Membuat Website untuk Pemula")
            print("Jadwal  : 08:00\n")

        case "2":
            print("Judul   : Javascript Dasar untuk Pemrograman Web")
            print("Jadwal  : 06:00\n")

        case "3":
            print("Judul   : Membuat Tampilan Website yang Menarik dengan Tailwind 4")
            print("Jadwal  : 16:00\n")

        case "4":
            print("Judul   : Laravel : Dari Pemula hingga Mahir")
            print("Jadwal  : 09:00\n")

        case "5":
            print("Judul   : Spring Boot : Dari Pemula hingga Mahir")
            print("Jadwal  : 08:00\n")

        case _:
            print("Kursus sudah tidak tersedia\n")