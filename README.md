#### Daffa Syahrandy Husain (2409116069)
#### Mini Project 2
#### Flowchart Program
![minpro2 GACORRRR](https://github.com/user-attachments/assets/f599e946-0ac6-49c1-a53c-cdd26c1bd8f9)


### Penjelasan Code
#### Menggunnakan prettytable sebagai table daftar tamu
from prettytable import PrettyTable

#### Daftar tamu
```bukutamu = []```

#### Function fitur menambahkan data tamu
```def tambah_tamu():```

```nama = input("Masukkan Nama Tamu: ")```

```alamat = input("Masukkan Alamat Tamu: ")```

```bukutamu.append({"nama":nama, "alamat":alamat})```

```print("=====Berhasil Menambahkan Tamu=====")```

#### Output ketika berhasil menambahkan data tamu
![Screenshot 2024-10-13 155920](https://github.com/user-attachments/assets/53364e73-830d-40cb-8260-a1b52477acc3)

#### Function fitur menampilkan daftar tamu menggunakan table
```def daftar_tamu():```

```if len(bukutamu)<=0:```

```print("=====Data masih kosong=====")```

```else:```

```table = PrettyTable()```

```table.field_names = ["No", "Nama" , "Alamat"]```

```for idx, tamu in enumerate(bukutamu, start=1):```

```table.add_row([idx, tamu["nama"], tamu["alamat"]])```

```print(table)```

#### Daftar tamu ketika masih kosonng
![Screenshot 2024-10-13 160606](https://github.com/user-attachments/assets/31dcfe3f-9d88-4f63-8d52-fb9c263e4613)
#### Daftar tamu ketika ada data
![Screenshot 2024-10-13 160810](https://github.com/user-attachments/assets/3b004cee-0b05-4047-8075-7b660d693669)

#### Function fitur Mengubah data tamu (jika ada yang salah)
```def edit_tamu():```

```daftar_tamu()```

```ubah = int(input("Masukkan nomor yang ingin diubah: ")) - 1```

```if 0 <= ubah < len(bukutamu):```

```nama = input("Masukkan nama baru: ")```

```alamat = input("Masukkan alamat baru: ")```

```bukutamu[ubah] = {"nama":nama, "alamat":alamat}```

```print("=====Data berhasil diubah=====")```
#### Contoh mengubah data tamu
![Screenshot 2024-10-13 161628](https://github.com/user-attachments/assets/34dfe48d-6a1d-4578-94a4-269d78e5a8b5)

#### Functiom fitur menghapus data tamu (jika diinginkan)
```def hapus_tamu():```

```daftar_tamu()```

```hapus = int(input("Masukkan nomor yang ingin di hapus: ")) - 1```

```if 0 <= hapus < len(bukutamu):```

```bukutamu.pop(hapus)```

```print("=====Data tamu berhasil dihapus=====")```
#### Contoh berhasl menghapus data tamu
![Screenshot 2024-10-13 162122](https://github.com/user-attachments/assets/a9c725da-3b73-4dc3-8226-8bab98a4f2a0)

#### Berfungsi sebagai role admin ketika login sebagai admin berhasil dan menampilkan fitur fitur admin yaitu CRUD, dengan memanggil function yang sudah dibuat sebelumnya
```def admin():```

```while True:```

```print("=====Menu Admin=====")```

```print("1. Tambah data tamu")```

```print("2. Lihat data tamu")```

```print("3. Ubah data tamu")```

```print("4. Hapus data tamu")```

```print("5. Logout sebagai admin")```

```fitur_admin = input("Silahkan pilih opsi: ")```

```if fitur_admin == "1":```

```tambah_tamu()```

```elif fitur_admin == "2":```

```daftar_tamu()```

```elif fitur_admin == "3":```

```edit_tamu()```

```elif fitur_admin == "4":```

```hapus_tamu()```

```elif fitur_admin == "5":```

```print("=====Logout berhasil=====")```

```break```

```else:```

```print("Pilihan salah")```
#### Output
![Screenshot 2024-10-13 162626](https://github.com/user-attachments/assets/2614e3ff-528d-48aa-a37a-be4069077e92)

##### Berfungsi sebagai role tamu yang hanya menampilkan fitur read saja
```def tamu():```

```while True:```

```print("=====Menu Tamu======")```

```print("1. Lihat data tamu")```

```print("2. Logout sebagai tamu")```

```fitur_tamu = input("Silahkan pilih opsi: ")```

```if fitur_tamu == "1":```

```daftar_tamu()```

```elif fitur_tamu == "2":```

```print("=====Logout berhasil======")```

```break```

```else:```

```print("Pilihan salah")```

#### Output
![Screenshot 2024-10-13 163203](https://github.com/user-attachments/assets/35a1940b-825e-4f63-9116-82bdcd1d8537)

#### Berfungsi sebagai data yang ditetapkan untuk login sebagai admin atau tamu
```admin_login = {"username" : "dapa", "password" : "123"}```

```tamu_login = {"username" : "tamu", "password" : "123"}```

#### Menampilkan Menu utama yang memilih role
while True:
print("Pilih Login Sebagai Apa:")
print("1. Admin")
print("2. Tamu")
print("3. Keluar dari program")
pilih_role = input("Masukkan Pilihan: ")

#### Jika pilihan adalah login sebagai admin dan data yang dimasukkan sesuai maka memanggil fungsi admin dan menampilkan fiturnya, ketika data login yang dimasukkan salah maka kembali ke menu utama
if pilih_role == "1":
print("Masukkan Username dan Password")
username = input("Masukkan username: ").lower()
password = input("Masukkan password: ")

if username == admin_login["username"] and password == admin_login["password"]:
print("Login sebagai Admin berhasil")
admin()
else:
print("Username atau Password yang anda masukkan salah")
#### Output
![Screenshot 2024-10-13 163923](https://github.com/user-attachments/assets/be4573bd-9011-473a-a684-0f3a45950231)

#### Jika pilihan adalah login sebagai tamu dan data yang dimasukkan sesuai maka memanggil fungsi tamu dan menampilkan fiturnya, ketika data login yang dimasukkan salah maka akan kembali ke menu utama
elif pilih_role == "2":
print("Masukkan Username dan Password")
username = input("Masukkan username: ").lower()
password = input("Masukkan password: ")
if username == tamu_login["username"] and password == tamu_login["password"]:
print("Login sebagai Tamu berhasil")
tamu()
else:
print("Username atau Password yang anda masukkan salah")
#### Output
![Screenshot 2024-10-13 164212](https://github.com/user-attachments/assets/976e0801-dfb9-4b11-b93c-bce668b0d50f)

#### Mwmilih berhenti dari program
elif pilih_role == "3":
print("Terimakasih sudah berkunjung")
break
#### Output
![Screenshot 2024-10-13 164359](https://github.com/user-attachments/assets/398c236d-6724-4ab3-ad23-fa352564edc8)

#### Ketika inputan tidak sesuai dengan yang tersedia maka akan kembali ke menu utama
else:
print("Pilihan salah")
#### Output
![Screenshot 2024-10-13 164605](https://github.com/user-attachments/assets/8af84abc-fc6a-4136-b53e-319a558b54ec)
