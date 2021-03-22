#Augusta Clarissa Silvy Pascalin
#Universitas Kristen Duta Wacana
#Topik : Pengolahan String

'''Rissa ingin membuat bot untuk memudahkannya menghubungi dosen dengan format pesan yang sudah ditentukan.
Ada 3 format pesan yang dibuat Rissa dengan tujuan yang berbeda - beda, yaitu :
1. Mengingatkan waktu kuliah kepada dosen
2. Ijin Sakit
3. Skripsi'''

#input : tujuan chat dosen, tiap tujuan nanti memasukkan inputan sesuai format
#proses : if, method string split
#output : pesan untuk dosen siap kirim

print("Selamat datang di bot chat dosen")
print("Pilih satu format : ")
print("1. Mengingatkan waktu kuliah kepada dosen")
print("2. Ijin Sakit")
print("3. Skripsi")

tujuan = int(input("Masukkan pilihan : "))

if tujuan == 1:
    print("*waktu(pagi/siang/malam) *Bapak/Ibu *nama kamu *kelas *semester *jam *matkul")
    format1 = input("Ketikkan sesuai format : ")
    s1 = format1.split("*")
    print("Selamat ", s1[1] + s1[2], ", mohon maaf mengganggu waktu ", s1[2])
    print("Saya ", s1[3], "Ketua tingkat dari kelas ", s1[4], "semester ", s1[5], "mengingatkan, bahwa besok jam ", s1[6] + s1[2], "punya jadwal mengajar di kelas kami dengan mata kuliah ", s1[7], ". Atas perhatiannya, kami ucapkan terima kasih." )
elif tujuan == 2:
    print("*waktu(pagi/siang/malam) *Bapak/Ibu *nama kamu *prodi *tahun angkatan *kelas *sakit yang dialami")
    format2 = input("Ketikkan sesuai format : ")
    s2 = format2.split("*")
    print("Selamat ", s2[1] + s2[2], ", mohon maaf mengganggu waktu ", s2[2])
    print("Saya ", s2[3], ", Mahasiswa ", s2[4], "angkatan ", s2[5], "kelas ", s2[6], ". Hari ini belum bisa mengikuti perkuliahan yang ", s2[2], "bawakan karena sakit ", s2[7], ", atas perhatiannya saya ucapkan terima kasih.")
elif tujuan == 3:
    print("*waktu(pagi/siang/malam) *Bapak/Ibu *nama kamu *prodi *tahun angkatan *kelas")
    format3 = input("Ketikkan sesuai format : ")
    s3 = format3.split("*")
    print("Selamat ", s3[1] + s3[2], ", mohon maaf mengganggu waktu ", s3[2])
    print("Saya ", s3[3], "Mahasiswa ", s3[4], "angkatan ", s3[5], "kelas ", s3[6], "yang saat ini sedang menulis skripsi dan ", s3[2], "sebagai pembimbingnya. Saya ingin bertanya, kapan kiranya saya bisa konsultasi ke ruangan ", s3[2], "? Terima kasih sebelumnya.")
else:
    pass