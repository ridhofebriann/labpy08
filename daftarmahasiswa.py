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

