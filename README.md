# Pipeline ETL Data Penjualan Ritel Menggunakan Python dan PostgreSQL

Proyek ini merupakan implementasi sederhana proses **ETL (Extract, Transform, Load)** untuk mengolah data penjualan menggunakan Python dan PostgreSQL. Data yang telah diproses disimpan ke dalam database agar dapat digunakan untuk analisis bisnis.

## 1. Business Understanding

RetailMart membutuhkan informasi mengenai kinerja penjualannya berdasarkan data transaksi. Namun, data mentah yang tersedia dalam format CSV perlu dibersihkan, divalidasi, dan disimpan ke dalam database sebelum dapat dianalisis.

Melalui proyek ini, proses pengolahan data dibuat secara terstruktur agar data lebih konsisten dan siap digunakan untuk mendukung pengambilan keputusan bisnis.

## 2. Tujuan Proyek

- Membangun alur ETL sederhana menggunakan Python dan Pandas.
- Membersihkan dan memvalidasi data penjualan.
- Menyimpan data hasil transformasi ke dalam PostgreSQL.
- Melakukan analisis data menggunakan SQL untuk memperoleh informasi bisnis.

## 3. Dataset

- **Nama Dataset:** Sample Superstore
- **Sumber:** [Kaggle – Sample Superstore](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **Format:** CSV
- **Jumlah Data Awal:** 9.994 baris dan 21 kolom.

*Catatan: Dataset ini merupakan data sampel untuk keperluan pembelajaran.*

## 4. Teknologi yang Digunakan

- **Python:** Bahasa pemrograman untuk membangun proses ETL.
- **Pandas:** Library untuk pengolahan dan transformasi data.
- **PostgreSQL:** Database untuk menyimpan data hasil pengolahan.
- **SQLAlchemy:** Penghubung antara Python dan PostgreSQL.
- **SQL:** Digunakan untuk melakukan analisis data.
- **Git & GitHub:** Digunakan untuk pengelolaan dan dokumentasi proyek.

## 5. Alur ETL

Proses ETL dalam proyek ini terdiri dari tiga tahapan:

1. **Extract:** Membaca data penjualan dari file CSV menggunakan Pandas.
2. **Transform:** Membersihkan data, menyeragamkan nama kolom, menyesuaikan tipe data, serta membuat kolom tambahan seperti `delivery_days` dan `profit_margin`.
3. **Load:** Memuat data yang telah diproses ke dalam tabel `sales_transactions` pada PostgreSQL.

## 6. Hasil Validasi Data

Berikut merupakan hasil pemeriksaan kualitas data setelah proses transformasi:

| Pemeriksaan | Hasil |
|---|---:|
| Jumlah data awal | 9.994 |
| Jumlah data akhir | 9.994 |
| Data duplikat yang dihapus | 0 |
| Data tidak valid yang dihapus | 0 |
| Data berhasil dimuat ke PostgreSQL | 9.994 |

## 7. Analisis Bisnis Menggunakan SQL

1. Berapa total pendapatan penjualan?
2. Kategori produk apa yang menghasilkan penjualan tertinggi?
3. Produk apa yang memiliki jumlah penjualan terbanyak?
4. Wilayah mana yang menghasilkan penjualan tertinggi?
5. Bagaimana tren penjualan dari bulan ke bulan?

Seluruh query analisis tersedia pada file `sql/sales_analysis.sql`.

Jalankan query analisis pada file `sql/sales_analysis.sql` menggunakan pgAdmin atau editor SQL yang mendukung PostgreSQL.

## 8. Penulis

**Nama:** Marisa Muharomah
**Proyek:** Retail Sales ETL Pipeline Using Python & PostgreSQL