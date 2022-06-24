# Global-DNA-Sequence-Alignment
Desktop App written in Python with Tkinter for GUI using Needleman-Wunsch Algorithm
## Table of Contents
- [Global-DNA-Sequence-Alignment](#global-dna-sequence-alignment)
  - [Table of Contents](#table-of-contents)
  - [Setup](#setup)
  - [Cara Penggunaan Program](#cara-penggunaan-program)
  - [Algoritma NeedlemanWunsch](#algoritma-needlemanwunsch)
  - [Referensi Framework Library](#referensi-framework-library)
  - [Contributor](#contributor)

## Setup
  - Clone repository ini ke dalam komputer anda dengan cara memasukkan sintaks berikut pada powershell atau terminal:
```
git clone https://github.com/saulsayerz/Global-DNA-Sequence-Alignment
```
- Install library tkinter terlebih dahulu apabila belum dengan cara memasukkan sintaks berikut pada powershell atau terminal:
```
pip install tkinter
```
- Sediakan testcase DNA yang akan diperiksa dalam folder test, berbentuk file .txt

## Cara Penggunaan Program
- Membuka root dari repository yang telah anda clone dan jalankan program dengan memanfaatkan run.bat yang tersedia.
- Desktop App akan berjalan
- Ambil file input berisi DNA yang akan diperiksa penyelarasan optimalnya. Program akan mendeteksi file input yang salah dan memberikan popup apabila input tidak berupa DNA
- Setelah memilih kedua file input, silahkan klik tombol solve. Apabila mengklik tombol solve sebelum memilih input, program akan menampilkan popup error
- Output yang diharapkan akan ditampilkan oleh program, berupa alignment,runtime program, matriks tracebacknya. Untuk kolom yang berisi warna merah merupakan kolom yang diambil rute tracebacknya. Dengan catatan, karena rute diagonal bisa diambil saat mismatch ataupun match, maka sebagai pembeda kolom biru merupakan rute diagonal yang diakibatkan karena mismatch sementara merah karena match
- Disediakan tombol User yang menampilkan halaman penjelasan pengguna
- Disediakan tombol Guide yang menampilkan cara penggunaan program

## Algoritma NeedlemanWunsch
NeedlemanWunsch adalah suatu algoritma yang digunakan dalam dunia bioinformatika untuk mendapatkan alignment dari rantaian basa nitrogen (DNA)
### Proses Pembuatan Matriks
Matriks dibuat dengan pendekatan Dynamic Programming
Matriks dibentuk dengan cara membuat dimensinya sebesar :
- Baris = PanjangDNA1 + 2
- Kolom = PanjangDNA2 + 2
Baris dan Kolom pertama dari matriks akan diisi dengan teks nama DNA nya

Kemudian, pada tahap Basis akan dilakukan pengisian pada baris dan kolom kedua. Pengisian mengikuti formula sebagai berikut :
```
F(0,0) = 0
F(i,0) = F(i-1,0) - d
F(0,j) = F(0,j-1) - d
```

Kemudian, pada tahap Rekursi akan dilakukan pengisian untuk sisa cell yang masih kosong. Cell F(i,j) diisi dengan nilai maksimum antara:
- F(i-1,j) - d
- F(i,j-1) - d
- F(i-1, j-1) + s(x_i,y_j)

Keterangan:
```
d: skor gap penalty
s(x; y): skor penyelarasan suatu basa x dari rantai S dengan basa y dari rantai T. Nilai ini akan menjadi positif apabila huruf yang diperiksa match dan negatif bila tidak
F: matrix dimana F (x, y) mengacu pada posisi-x pada S and posisi-y pada T
```
### Cara Memanfaatkan Rute Traceback
Traceback dimulai dari paling bawah kanan matriks. Kemudian akan terjadi dua kasus :
- Match : Langsung mengambil rute cell sebelah atas kiri
- Mismatch : Ambil yang terbesar di antara sebelah kiri, sebelah atas, dan diagonal kiri atasnya.

Hal tersebut dilakukan hingga baris dan kolom tercapai di paling atas kiri (nilai awal)
Dengan catatan : 
Apabila traceback sudah mentok di baris pertama atau kolom pertama maka ambil rute lurus menuju start

Rute tersebut dapat dimanfaatkan untuk memperoleh alignment yang benar. Untuk rute diagonal, maka dibiarkan saja karena sudah pasti benar/salah. Untuk rute atas ataupun kiri maka kita menggeser alignment dna nya sebanyak 1 (sehingga timbul gap)
### Alasan Penetapan Skema Scoring
Sesuai dengan aturan pada spesifikasi, skema skoring yang digunakan adalah : +1 (match), -1 (mismatch), -2 (gap).

Adapun pengaruh dari skema yang digunakan adalah terhadap alignment yang diinginkan.
Rasio antara match/mismatch dan gap sangat berpengaruh dengan preferensi alignment.
Apabila match dan mismatch memiliki value yang lebih tinggi, maka algoritma akan memilihkan alignment yang lebih banyak benar, namun pergeseran yang lebih banyak.

Dalam konteks DNA, pergeseran basa DNA memiliki cost yang sangat besar dan hanya terjadi apabila mutasi genetik. Dengan demikian, digunakan rasio di mana gap memiliki skor yang lebih besar dibanding yang lain (2 dibanding 1). Dengan demikian, alignment yang diperoleh akan memiliki pergeseran yang lebih sedikit. 

Skema skoring yang digunakan ini merupakan skema yang umum digunakan, sesuai dengan beberapa referensi yang disediakan di bawah. Alternatif skema skoring lain yang umum adalah +1 (match), -1 (mismatch), -1 (gap) di mana skema skoring ini memberikan alignment yang lebih seimbang.

## Referensi Framework Library
### Referensi 
- <a href="https://www.youtube.com/watch?v=ipp-pNRIp4g">Global Sequence Alignment & Needleman-Wunsch || Algorithm and Example
</a>
- <a href="https://www.cs.sjsu.edu/~aid/cs152/NeedlemanWunsch.pdf">The Needleman-Wunsch algorithm for
sequence alignment | 7th Melbourne Bioinformatics Course
</a>
- <a href="https://www.youtube.com/watch?v=BYdTqq8AGgc">HOW TO Sequence Alignment (Global) - NEEDLEMAN WUNSCH
</a>

### Library
Bahasa pemrograman yang digunakan adalah python
- Tkinter : Untuk GUI Desktop App
- Regex : Memastikan DNA hanya berisi karakter AGCT
- Time : Menghitung Runtime Program
- OS : Mendapatkan input file

## Contributor :
> Saul Sayers (13520094), K01 - Informatika ITB 2020. 

More detailed contact: 
- Line : saulsayerz
- Instagram : <a href="https://www.instagram.com/saulsayers/?hl=en">saulsayers</a> 
- Linkedin : <a href="https://www.linkedin.com/in/saulsayers/?originalSubdomain=id">saulsayers</a>
- github : <a href="https://github.com/saulsayerz">saulsayerz</a>
- email : saulsayers@gmail.com
