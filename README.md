# Pengecekan API Secara Otomatis dengan Python
## Cara Penggunaan
### install package / dependency
Pastikan Repository sudah di download / di clone

Ketikkan kode berikut di terminal untuk install package :
> pip install -r requirements.txt

### Menjalankan Test
Untuk menjalankan testing api, ketikkan kode di bawah ini di terminal :
>pytest -v -s namafile.py

agar program dapat di eksekusi, nama file harus ada kata 'test', sebagai contoh, bisa menggunakan 'test_contoh.py' atau 'contoh_test.py'

### Membuat Dokumentasi report dengan html
Untuk membuat dokumentasi report dengan format html, ketikkan kode di bawah ini :
>pytest --html=report.html 


#### Package tambahan 
>jsonpath <br>
> pytest <br>
> requests <br>
> pytest-html <br>
> assertpy <br>
> curlify <br>
> faker

