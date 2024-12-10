# labpy08

Nama        : M.Ridho Febrian <p>

Kelas       : TI.24.A.5 <p>

Nim         : 312410500 <p>

Mata kuliah : Bahasa Pemrograman <p>

# Praktikum 8

# Program daftar nilai Mahasiswa

Pada praktikum 8, kita membuat program sederhana dengan mengaplikasikan penggunaan class. Buatlah
class untuk menampilkan daftar nilai mahasiswa,

# diagram class:
![diagram class](https://github.com/ridhofebriann/labpy08/blob/main/diagram%20class.png?raw=true)

# flowchart saya:
![flowchart](https://github.com/ridhofebriann/labpy08/blob/main/flowchart.daftar.drawio.png?raw=true)
#### Codingan Praktikum 8

```python
class DaftarMahasiswa:
    def __init__(self):
        """Inisialisasi daftar mahasiswa."""
        self.daftar_mahasiswa = []

    def tambah(self, nama, nilai):
        """Method untuk menambah data mahasiswa."""
        mahasiswa = {'nama': nama, 'nilai': nilai}
        self.daftar_mahasiswa.append(mahasiswa)
        print(f"Data mahasiswa {nama} telah ditambahkan.")

    def tampilkan(self):
        """Method untuk menampilkan data mahasiswa."""
        if not self.daftar_mahasiswa:
            print("Tidak ada data mahasiswa.")
            return
        print("\nDaftar Mahasiswa:")
        for mahasiswa in self.daftar_mahasiswa:
            print(f"Nama: {mahasiswa['nama']}, Nilai: {mahasiswa['nilai']}")

    def hapus(self, nama):
        """Method untuk menghapus data mahasiswa berdasarkan nama."""
        self.daftar_mahasiswa = [mahasiswa for mahasiswa in self.daftar_mahasiswa if mahasiswa['nama'] != nama]
        print(f"Data mahasiswa dengan nama {nama} telah dihapus.")

    def ubah(self, nama, nilai_baru):
        """Method untuk mengubah data mahasiswa berdasarkan nama."""
        for mahasiswa in self.daftar_mahasiswa:
            if mahasiswa['nama'] == nama:
                mahasiswa['nilai'] = nilai_baru
                print(f"Data mahasiswa {nama} telah diubah menjadi nilai {nilai_baru}.")
                return
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

# Penggunaan class
daftar = DaftarMahasiswa()


daftar.tambah("ridho", 85)
daftar.tambah("bagus", 90)
daftar.tambah("kia", 78)


daftar.tampilkan()

daftar.hapus("bagus")
daftar.tampilkan()


daftar.ubah("ridho", 88)
daftar.tampilkan()

```

#### Penjelasan Kode Program

1. Inisialisasi Class
```python
class DaftarMahasiswa:
    def __init__(self):
        """Inisialisasi daftar mahasiswa."""
        self.daftar_mahasiswa = []
```

Class DaftarMahasiswa memiliki satu atribut yaitu daftar_mahasiswa yang diinisialisasi sebagai daftar kosong untuk menyimpan data mahasiswa.

2. Method untuk menambahkan data
```python
  def tambah(self, nama, nilai):
        """Method untuk menambah data mahasiswa."""
        mahasiswa = {'nama': nama, 'nilai': nilai}
        self.daftar_mahasiswa.append(mahasiswa)
        print(f"Data mahasiswa {nama} telah ditambahkan.")
```

Method tambah menerima dua parameter: nama, dan nilai. Method ini membuat dictionary mahasiswa yang menyimpan informasi tersebut dan menambahkannya ke daftar_mahasiswa.

3. Method untuk menampilkan data
```python
   def tampilkan(self):
        """Method untuk menampilkan data mahasiswa."""
        if not self.daftar_mahasiswa:
            print("Tidak ada data mahasiswa.")
            return
        print("\nDaftar Mahasiswa:")
        for mahasiswa in self.daftar_mahasiswa:
            print(f"Nama: {mahasiswa['nama']}, Nilai: {mahasiswa['nilai']}")
```

Method tampilkan menampilkan data semua mahasiswa yang ada di daftar_mahasiswa. Jika daftar kosong, akan muncul pesan "Tidak ada data mahasiswa."


4. Method untuk menghapus data
```python
def hapus(self, nama):
        """Method untuk menghapus data mahasiswa berdasarkan nama."""
        self.daftar_mahasiswa = [mahasiswa for mahasiswa in self.daftar_mahasiswa if mahasiswa['nama'] != nama]
        print(f"Data mahasiswa dengan nama {nama} telah dihapus.")
```

Method hapus menghapus data mahasiswa dari daftar_mahasiswa berdasarkan nama. Jika ditemukan mahasiswa dengan nama tersebut, data akan dihapus dan daftar diperbarui.


5. Method untuk mengubah data
```python
  def ubah(self, nama, nilai_baru):
        """Method untuk mengubah data mahasiswa berdasarkan nama."""
        for mahasiswa in self.daftar_mahasiswa:
            if mahasiswa['nama'] == nama:
                mahasiswa['nilai'] = nilai_baru
                print(f"Data mahasiswa {nama} telah diubah menjadi nilai {nilai_baru}.")
                return
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")
```

Method ubah memungkinkan perubahan data mahasiswa berdasarkan nama. Jika nama ditemukan dalam daftar_mahasiswa, data akan diperbarui sesuai dengan parameter yang diberikan dan kemudian method akan berhenti (return).

6. Contoh Penggunaan
Berikut contoh penggunaan class DaftarMahasiswa:
```python
# Penggunaan class
daftar = DaftarMahasiswa()


daftar.tambah("ridho", 85)
daftar.tambah("bagus", 90)
daftar.tambah("kia", 78)


daftar.tampilkan()


daftar.hapus("bagus")
daftar.tampilkan()

daftar.ubah("ridho", 88)
daftar.tampilkan()

```

## ini hasil output saya:

![hasil](https://github.com/ridhofebriann/labpy08/blob/main/hasill%20kode%20program%20saya.png?raw=true)
