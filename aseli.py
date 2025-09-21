# kuota kursus 
kuota1 = 11
kuota2 = 13  
kuota3 = 1  
kuota4 = 18  
kuota5 = 3  
kuota6 = 0  
# jadwal kursus 
jadwal1 = "Senin 10.00"
jadwal2 = "Senin 10.00"
jadwal3 = "Rabu 13.00"
jadwal4 = "Jumat 09.00"
jadwal5 = "Rabu 14.00"
jadwal6 = "Kamis 15.00"
# untuk menyimpan variabel yang dimasukan
user1 = ""
user2 = ""
user3 = ""
jadwal_user1 = ""
jadwal_user2 = ""
jadwal_user3 = ""

print("=== Sistem Pendaftaran Kursus Online ===")
kapasitas = 1
# melakukan loop sampai mendapatkan maximal 3 hasil atau sampai berhenti
while kapasitas <= 3:
    print("\n--- Status Pendaftaran ---")
    print("Kursus yang sudah didaftarkan:")
    if user1 != "": print(f"- {user1} ({jadwal_user1})")
    if user2 != "": print(f"- {user2} ({jadwal_user2})")
    if user3 != "": print(f"- {user3} ({jadwal_user3})")
    if user1 == "" and user2 == "" and user3 == "":
        print("Belum ada. ⊙﹏⊙∥")
    
    # menampilkan kursus yang tersedia
    print("\nKursus yang tersedia:")
    print(f"=========================================================")
    print(f"1. Basic Python     | Kuota: {kuota1} | Jadwal: {jadwal1}") 
    print(f"2. Basic C++        | Kuota: {kuota2} | Jadwal: {jadwal2}")
    print(f"3. Basic Java       | Kuota: {kuota3} | Jadwal: {jadwal3}")
    print(f"4. Basic PHP        | Kuota: {kuota4} | Jadwal: {jadwal4}")
    print(f"5. Basic JS         | Kuota: {kuota5} | Jadwal: {jadwal5}")
    print(f"6. Basic Laravel    | Kuota: {kuota6} | Jadwal: {jadwal6}")
    print(f"=========================================================")
    
    # memasukan nomor kursus atau berhenti
    pilihan = input("""Masukkan Nomor kursus atau ketik "n" jika ingin berhenti
    >>>>:  """)

    if pilihan.lower() == "n":
        break

    # mengecek variabel yang dimasukan
    if pilihan == "1":
        nama, jadwal = "Basic Python", jadwal1
        if kuota1 <= 0:
            print(f"X Kuota {nama} sudah habis.")
            continue
    elif pilihan == "2":
        nama, jadwal = "Basic C++", jadwal2
        if kuota2 <= 0:
            print(f" X Kuota {nama} sudah habis.")
            continue
    elif pilihan == "3":
        nama, jadwal = "Basic Java", jadwal3
        if kuota3 <= 0:
            print(f"X Kuota {nama} sudah habis.")
            continue
    elif pilihan == "4":
        nama, jadwal = "Basic PHP", jadwal4
        if kuota4 <= 0:
            print(f"X Kuota {nama} sudah habis.")
            continue
    elif pilihan == "5":
        nama, jadwal = "Basic JS", jadwal5
        if kuota5 <= 0:
            print(f"X Kuota {nama} sudah habis.")
            continue
    elif pilihan == "6":
        nama, jadwal = "Basic Laravel", jadwal6
        if kuota6 <= 0:
            print(f"X Kuota {nama} sudah habis.")
            continue
    else:
        print("Kursus tidak ditemukan.")
        continue
    
    # mengecek apakah kursus sudah didaftar
    if nama in user1 or nama in user2 or nama in user3:
        print("\nAnda sudah mendaftar kursus ini!")
        continue

    # mengecek apakah jadwal bentrok
    if (jadwal == jadwal_user1 or jadwal == jadwal_user2 or jadwal == jadwal_user3):
        print("\nKursus yang anda pilih bertabrakan dengan kursus lain.")
        continue

    # Simpan ke penyimpanan user
    if kapasitas == 1:
        user1, jadwal_user1 = nama, jadwal
    elif kapasitas == 2:
        user2, jadwal_user2 = nama, jadwal
    elif kapasitas == 3:
        user3, jadwal_user3 = nama, jadwal

    # Kurangi kuota sesuai pilihan
    if pilihan == "1": kuota1 -= 1
    elif pilihan == "2": kuota2 -= 1
    elif pilihan == "3": kuota3 -= 1
    elif pilihan == "4": kuota4 -= 1
    elif pilihan == "5": kuota5 -= 1
    elif pilihan == "6": kuota6 -= 1

    print(f"Berhasil mendaftar ke kursus {nama}. ヾ(≧▽≦*)o")
    kapasitas += 1

# menampilkan pesan apabila sudah mencapai maksimal pendaftaran
if kapasitas >= 3:
    print("Anda sudah mencapai jumlah maksimal pendaftaran! o((>ω< ))o")


# menampilkan kursus yang diambil
print("\n==========================================")
print("--- Kursus yang diambil ---")
if user1 != "": print(f"- {user1} ({jadwal_user1})")
if user2 != "": print(f"- {user2} ({jadwal_user2})")
if user3 != "": print(f"- {user3} ({jadwal_user3})")
print("\n==========================================")

# Salam penutup kepada pengguna
print("Terima kasih sudah berkunjung di kursus kami! Sampai jumpa kembali! ヾ(≧▽≦*)o")