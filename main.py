# Mendeklarasikan Variabel dan Konstanta
MAX_COURSES = 3
pilih = ""
nambah = "1"
penuh = False
myCourses = [] # Untuk menampung kursus yang telah didaftar

# Deklarasi Fungsi

# Fungsi untuk mengecek apakah nomor kursus yang dimasukkan tersedia
def isNumberValid(value):
    for i in courses:
        if i['id'] == value:
            return True

    return False

# Fungsi untuk mengambil data kursus
def getCourses(course, id):
    for i in course:
        if i['id'] == id:
            return i

    return None

# Fungsu untuk mengecek kesamaan waktu
def checkIfSameTime(time):
    for i in myCourses:
        if i['waktu'] == time:
            return True

    return False

# Fungsi untuk mengecek status kursus
def checkStatus(id):
    for i in courses:
        if i['id'] == id:
            if i['kuota'] == i['pendaftar']:
                return "Kuota Penuh"
            else:
                return "Tersedia"
            
# Fungsi untuk mencetak seluruh kursus yang telah didaftar
def printListMyCourse():
    for i in myCourses:
        print(f"""
        Judul  : {i['judul']}
        Waktu  : Jam {i['waktu']}
        """)

# Mendeklarasikan array untuk menampung list kursus
courses = [
    {
        'id': 1,
        'judul': "Mahir Membuat Website untuk Pemula",
        'kuota': 20,
        'pendaftar': 10,
        'waktu': "06:00"
    },
    {
        'id': 2,
        'judul': "Javascript Dasar untuk Pemrograman Web",
        'kuota': 10,
        'pendaftar': 10,
        'waktu': "08:00"
    },
    {
        'id': 3,
        'judul': "Membuat Tampilan Website yang Menarik dengan Tailwind 4",
        'kuota': 15,
        'pendaftar': 10,
        'waktu': "16:00"
    },
    {
        'id': 4,
        'judul': "Laravel : Dari Pemula hingga Mahir",
        'kuota': 20,
        'pendaftar': 15,
        'waktu': "09:00"
    },
    {
        'id': 5,
        'judul': "Spring Boot : Dari Pemula hingga Mahir",
        'kuota': 20,
        'pendaftar': 5,
        'waktu': "06:00"
    },
]

# Menampilkan list kursus yang bisa didaftarkan
for i in courses:
    print(f"""
    Nomor  : {i['id']}
    Judul  : {i['judul']}
    Kuota  : {i["pendaftar"]}/{i['kuota']}
    Waktu  : Jam {i['waktu']}
    Status : {checkStatus(i['id'])}
    """)

# Menggunakan loop agar pengguna bisa mendaftar lebih dari satu kursus
while nambah == "1" :
    penuh = False
    while pilih.isdigit() == False or isNumberValid(int(pilih)) == False:
        pilih = input("Masukkan nomor kursus yang ingin diikuti!\n")

        if(pilih.isdigit() == True and isNumberValid(int(pilih)) == True):
            break

        print("Silahkan masukkan nomor kursus yang tersedia di atas!\n")
        

    for i in courses:
        if i['id'] == int(pilih):
                if i['kuota'] == i['pendaftar']:
                    penuh = True
                    print("Maaf, kuota kursus sudah penuh!\n")
                    break
                elif i == getCourses(myCourses, i['id']):
                    penuh = True
                    print("Anda sudah mendaftar kursus ini!\n")
                    break
                elif checkIfSameTime(i['waktu']):
                    penuh = True
                    print("Anda mengikuti kursus lain dalam waktu yang sama!\n")
                else:
                    i['pendaftar'] += 1
                    myCourses.append(i)
                    print(f"Selamat, anda telah terdaftar di kursus '{i['judul']}'\n")
                    break    

    pilih = ""
    if penuh:
        continue

    if len(myCourses) < MAX_COURSES:
        nambah = input("Apakah anda ingin mengikuti kursus lain? Ketik 1 jika Iya dan Karakter lain jika tidak.\n")
    else:
        nambah = ""
        print("Anda sudah mencapai batas jumlah kursus yang bisa didaftar!")

print("Terima Kasih sudah mendaftar di Kursus Kami. Berikut adalah list kursus yang anda ikuti:\n")

printListMyCourse()



