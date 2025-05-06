import datetime

# Tampilan Awal
print("")
print("=" * 76)
print("SELAMAT DATANG DI SYSTEM PEMESANAN TIKET KERETA API".center(76))
print('E - TICKET KERETA API'.center(76))
print("=" * 76)

lanjut = input("Apakah Anda ingin melanjutkan? (y/n): ").lower()
if lanjut != 'y':
    print("Terima kasih, sampai jumpa!")
    exit()

# Daftar Harga
print("")
print("=" * 76)
print("PILIHAN JADWAL KERETA API".center(76))
print("=" * 76)
print("""
_______________DAFTAR HARGA PILIHAN KOTA TUJUAN YANG TERSEDIA_______________
============================================================================
Kota Tujuan                          | Kelas     | Kelas      | Kelas 
                                     | Ekonomi(E)| Bisnis(B)  | Eksekutif(X)
============================================================================
1. Bandung (BDG)                     | 150.000   | 200.000    | 250.000
2. Cirebon (CBE)                     | 170.000   | 220.000    | 270.000
3. Semarang (SMG)                    | 200.000   | 250.000    | 300.000
4. Yogyakarta (YG)                   | 230.000   | 280.000    | 330.000
5. Surabaya (SUB)                    | 250.000   | 300.000    | 350.000
============================================================================
""")

# Input Kota dan Kelas
valid_kota = {
    "BDG": ("Bandung", [150000, 200000, 250000]),
    "CBE": ("Cirebon", [170000, 220000, 270000]),
    "SMG": ("Semarang", [200000, 250000, 300000]),
    "YG":  ("Yogyakarta", [230000, 280000, 330000]),
    "SUB": ("Surabaya", [250000, 300000, 350000])
}

while True:
    kode_kota = input("Masukkan kode kota tujuan (BDG/CBE/SMG/YG/SUB): ").upper()
    if kode_kota in valid_kota:
        tujuan, harga_kelas = valid_kota[kode_kota]
        break
    print("Kode kota tidak valid. Silakan coba lagi.")

while True:
    kelas_input = input("Masukkan kelas (E/B/X): ").upper()
    if kelas_input == "E":
        kelas = "Ekonomi"
        harga = harga_kelas[0]
        break
    elif kelas_input == "B":
        kelas = "Bisnis"
        harga = harga_kelas[1]
        break
    elif kelas_input == "X":
        kelas = "Eksekutif"
        harga = harga_kelas[2]
        break
    print("Kelas tidak valid. Silakan coba lagi.")

# Jadwal Keberangkatan
print("""
============================================================================
_______________________________Jadwal Keberangkatan_________________________
A. Senin  (08:00 - 10:00)               | B. Selasa (09:00 - 11:00)         
C. Rabu (10:00 - 12:00)                 | D. Kamis (11:00 - 13:00)    
E. Jumat (12:00 - 14:00)                | F. Sabtu (13:00 - 15:00)
G. Minggu (14:00 - 16:00)
____________________________________________________________________________
""")

jadwal_dict = {
    "A": "Senin (08:00 - 10:00)",
    "B": "Selasa (09:00 - 11:00)",
    "C": "Rabu (10:00 - 12:00)",
    "D": "Kamis (11:00 - 13:00)",
    "E": "Jumat (12:00 - 14:00)",
    "F": "Sabtu (13:00 - 15:00)",
    "G": "Minggu (14:00 - 16:00)"
}

while True:
    tanggal = input("Masukkan kode tanggal keberangkatan (A-G): ").upper()
    if tanggal in jadwal_dict:
        jadwal = jadwal_dict[tanggal]
        break
    print("Kode tanggal tidak valid. Silakan coba lagi.")

# Data Penumpang
nama = input("Masukkan nama penumpang: ")
nik = input("Masukkan NIK penumpang: ")
no_hp = input("Masukkan nomor handphone penumpang: ")

# Metode Pembayaran
print("""
                     Pilihan Metode Pembayaran

1. Bank BCA Virtual Account
2. Bank BRI Virtual Account
3. Indomaret
4. Alfamart
""")

while True:
    bayar_input = input("Pilih metode pembayaran (1/2/3/4): ")
    if bayar_input == "1":
        bayar = "Bank BCA Virtual Account - Nomor VA: 1234 - 5678 - 9101"
        break
    elif bayar_input == "2":
        bayar = "Bank BRI Virtual Account - Nomor VA: 1234 - 5678 - 9101"
        break
    elif bayar_input == "3":
        bayar = "Indomaret - Kode Pembayaran: 1234 - 5678 - 9101"
        break
    elif bayar_input == "4":
        bayar = "Alfamart - Kode Pembayaran: 1234 - 5678 - 9101"
        break
    print("Metode pembayaran tidak valid. Silakan coba lagi.")

# Cetak Struk
x = datetime.datetime.now()
print("")
print("=" * 76)
print("PT. KERETA API INDONESIA".center(76))
print("E- TICKET".center(76))
print("=" * 76)
print(f"Tanggal Pemesanan: {x.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Nama Penumpang: {nama}")
print(f"NIK Penumpang: {nik}")
print(f"Nomor Handphone: {no_hp}")
print(f"Tujuan: {tujuan}")
print(f"Kelas: {kelas}")
print(f"Jadwal Keberangkatan: {jadwal}")
print("=" * 76)
print(f"Total Harga: Rp {harga:,}")
print(f"Metode Pembayaran: {bayar}")
print("")
print("BATAS WAKTU PEMBAYARAN ANDA 24 JAM".center(76))
print("MOHON SIMPAN BUKTI PEMBAYARAN ANDA".center(76))
print("=" * 76)
print("TERIMAKASIH SUDAH MELAKUKAN PEMESANAN TIKET KERETA API".center(76))
