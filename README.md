# posttest-3


Cara Kerja Program : 
Program bekerja saat kita menjalankan program tersebut, dan pengunjung diminta memilih menu lalu menambahkan nomor/kode kursi dan pengunjung dapat melihat serta menghapus nomor kursi yang sudah diinput

Fungsi dari program ini yaitu : 
untuk mengatur kursi yang tersedia pada saat konser. pengunjung juga diminta memasukkan kode kursi. dan kode kursi yang dimasukkan paling pertama akan keluar paling akhir.


Bagaimana Aplikasi/Program bekerja?
Pengunjung diminta memilih menu tambahkan nomor kursi, lalu menuliskan nomor kursi, dan Pilih Tampilkan Kursi. Jika sudah, data yang tertampil adalah data yang sudah diinput oleh pengunjung. Jika pengunjung ingin menghapus maka pilih menu 3 dan Kursi akan terhapus mulai dari Data yang baru saja ditambahkan. Karena, dalam hal ini menggunakan First in Last Out. data yang dimasukkan pertama akan keluar terakhir


Penjelasan Program :
# fungsi constructor, yang berfungsi untuk mengisi nilai ke variabel tiap pembuatan objek baru

class Node:
        def __init__(self, data):
            self.data = data
            self.ref = None

#fungsi constructor untuk kelas NomorKursi

class NomorKursi():
        def __init__(self):
            self.head = None


#fungsi tampil, yang berfungsi untuk menampilkan data2nya.
Head berisi None, berarti listnya kosong
jika bukan None, Print Data dalam list

        def tampil(self):
            if self.head is None:
                print("Data tidak tersedia")

            else:
                n = self.head
                while n is not None:
                    print(n.data, end=" <--- ")
                    n = n.ref

#Berfungsi untuk menambahkan Kursi

        def tambahkursi(self, data):
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node

#Berfungsi untuk menghapus kursi

        def hapuskursi(self):
            if self.head is None:
                print("Kosong")
            else:
                self.head = self.head.ref

#Pembuatan Objek
Ticket_list adalah objek dari NomorKursi()

ticket_list = NomorKursi()



while True:

#Tampilan Awal

   print("============================================================")
    print("Welcome to the Blackpink concert seat number system!")
    print("============================================================")
    print("1. Tambah data kursi")
    print("2. Lihat Susunan Kursi")
    print("3. Hapus Kursi")
    choice = int(input("Pilih Menu : "))



    #Jika memilih menu 1 maka anda diminta memasukkan nomer kursi 

    if choice == 1:
        ticket_number = input("Masukan kode kursi : ")
        ticket_list.tambahkursi(ticket_number)
        print("Data berhasil ditambahkan")


    #Jika memilih menu 2 maka data yang sudah anda tambahkan akan ditampilkan  

    elif choice == 2:
        print("Berikut Data yang sudah diinput :")
        ticket_list.tampil()
        print("\n Thank You, the seats have been arranged!")


    #Jika memilih menu 3 maka anda menghapus kursi dimulai dari kursi yang paling terakhir diinput   

    elif choice == 3:
        ticket_list.hapuskursi()
        print("Data Berhasil dihapus")
        ticket_list.tampil()
        print("\n")



Elemen penting yang digunakan dalam program :

# fungsi constructor, yang berfungsi untuk mengisi nilai ke variabel tiap pembuatan objek baru

class Node:
        def __init__(self, data):
            self.data = data
            self.ref = None

#fungsi constructor untuk kelas NomorKursi

class NomorKursi():
        def __init__(self):
            self.head = None





OUTPUT PROGRAM :

<img width="357" alt="menu awal" src="https://user-images.githubusercontent.com/127472591/225962467-909939a3-a821-4013-894c-56f085fc8b0a.png">
<img width="343" alt="menu 1 kursi" src="https://user-images.githubusercontent.com/127472591/225962897-3f233427-e258-4a85-b5ac-06e498d67f5c.png">
<img width="198" alt="data berhasil" src="https://user-images.githubusercontent.com/127472591/225962994-7b51103d-c01c-445c-a88b-b7390451e46e.png">
<img width="260" alt="Data AB" src="https://user-images.githubusercontent.com/127472591/225963073-b1e4f5cc-3bbd-4bfb-9b3c-378a3f2761e1.png">
<img width="242" alt="data ac" src="https://user-images.githubusercontent.com/127472591/225963126-bf68a473-f3e2-4d03-bcd4-f675bc308967.png">
<img width="284" alt="menu tampil kursi" src="https://user-images.githubusercontent.com/127472591/225963189-7e0cecfb-2d03-4da1-b332-5bcc89251015.png">
<img width="161" alt="data AC terhapus" src="https://user-images.githubusercontent.com/127472591/225963313-c81f9ef9-c1c1-44f3-93f2-c8d3b1ef032f.png">
<img width="133" alt="data AB terhapus" src="https://user-images.githubusercontent.com/127472591/225963390-83d59e22-7311-4c79-bc5d-62219c7386e7.png">
<img width="152" alt="data AA terhapus" src="https://user-images.githubusercontent.com/127472591/225963424-c83ea419-9ee2-4a7d-86af-247535b62d1f.png">



