from prettytable import PrettyTable
bukutamu = []

def tambah_tamu():
    nama = input("Masukkan Nama Tamu: ")
    alamat = input("Masukkan Alamat Tamu: ")
    bukutamu.append({"nama":nama, "alamat":alamat})
    print("=====Berhasil Menambahkan Tamu=====")

def daftar_tamu():
    if len(bukutamu)<=0:
        print("=====Data masih kosong=====")
    else:
        table = PrettyTable()
        table.field_names = ["No", "Nama" , "Alamat"]
        for idx, tamu in enumerate(bukutamu, start=0):
            table.add_row([idx, tamu["nama"], tamu["alamat"]])
        print(table)

def edit_tamu():
    daftar_tamu()
    ubah = int(input("Masukkan nomor yang ingin diubah: ")) - 1
    if 0 <= ubah < len(bukutamu):
        nama = input("Masukkan nama baru: ")
        alamat = input("Masukkan alamat baru: ")
        bukutamu[ubah] = {"nama":nama, "alamat":alamat}
        print("=====Data berhasil diubah=====")

def hapus_tamu():
    daftar_tamu()
    hapus = int(input("Masukkan nomor yang ingin di hapus: ")) - 1
    if 0 <= hapus < len(bukutamu):
        bukutamu.pop(hapus)
        print("=====Data tamu berhasil dihapus=====")
        
def admin():
    while True:
        print("=====Menu Admin=====")
        print("1. Tambah data tamu")
        print("2. Lihat data tamu")
        print("3. Ubah data tamu")
        print("4. Hapus data tamu")
        print("5. Logout sebagai admin")
        fitur_admin = input("Silahkan pilih opsi: ")

        if fitur_admin == "1":
            tambah_tamu()
        elif fitur_admin == "2":
            daftar_tamu()
        elif fitur_admin == "3":
            edit_tamu()
        elif fitur_admin == "4":
            hapus_tamu()
        elif fitur_admin == "5":
            print("=====Logout berhasil=====")
            break
        else:
            print("Pilihan salah")

def tamu():
    while True:
        print("=====Menu Tamu======")
        print("1. Lihat data tamu")
        print("2. Logout sebagai tamu")
        fitur_tamu = input("Silahkan pilih opsi: ")

        if fitur_tamu == "1":
            daftar_tamu()
        elif fitur_tamu == "2":
            print("=====Logout berhasil======")
            break
        else:
            print("Pilihan salah")

admin_login = {"username" : "dapa", "password" : "123"}
tamu_login = {"username" : "tamu", "password" : "123"}

while True:
    print("Pilih Login Sebagai Apa:")
    print("1. Admin")
    print("2. Tamu")
    print("3. Keluar dari program")
    pilih_role = input("Masukkan Pilihan: ")
    if pilih_role == "1":
        print("Masukkan Username dan Password")
        username = input("Masukkan username: ").lower()
        password = input("Masukkan password: ")

        if username == admin_login["username"] and password == admin_login["password"]:
            print("Login sebagai Admin berhasil")
            admin()
        else:
            print("Username atau Password yang anda masukkan salah")

    elif pilih_role == "2":
        print("Masukkan Username dan Password")
        username = input("Masukkan username: ").lower()
        password = input("Masukkan password: ")
    
        if username == tamu_login["username"] and password == tamu_login["password"]:
            print("Login sebagai Tamu berhasil")
            tamu()
        else:
            print("Username atau Password yang anda masukkan salah")
    
    elif pilih_role == "3":
        print("Terimakasih sudah berkunjung")
        break
    else:
        print("Pilihan salah")