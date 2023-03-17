class Node:
      # constructor for Node class
        def __init__(self, data):
            self.data = data
            self.ref = None

class NomorKursi():
      # constructor for LinkedList class
        def __init__(self):
            self.head = None
        
        def tampil(self):
            if self.head is None:
                print("Data tidak tersedia")
            
            else:
                n = self.head
                while n is not None:
                    print(n.data, end=" <--- ")
                    n = n.ref
        
        def tambahkursi(self, data):
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node

        def hapuskursi(self):
            if self.head is None:
                print("Kosong")
            else:
                self.head = self.head.ref

ticket_list = NomorKursi()

while True:
    print("============================================================")
    print("Welcome to the Blackpink concert seat number system!")
    print("============================================================")
    print("1. Tambah data kursi")
    print("2. Lihat Susunan Kursi")
    print("3. Hapus Kursi")
    choice = int(input("Pilih Menu : "))
    
    if choice == 1:
        ticket_number = input("Masukan kode kursi : ")
        ticket_list.tambahkursi(ticket_number)
        print("Data berhasil ditambahkan")
        
    elif choice == 2:
        print("Berikut Data yang sudah diinput :")
        ticket_list.tampil()
        print("\n Thank You, the seats have been arranged!")
        
    elif choice == 3:
        ticket_list.hapuskursi()
        print("Data Berhasil dihapus")
        ticket_list.tampil()
        print("\n")
        
    