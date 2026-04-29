# 🚲 Bike Sharing Data Analysis & Dashboard

## 📌 Project Overview

Proyek ini bertujuan untuk menganalisis data penyewaan sepeda (Bike Sharing Dataset) dan menyajikan hasil analisis dalam bentuk dashboard interaktif menggunakan Streamlit.

Analisis difokuskan pada faktor-faktor yang memengaruhi jumlah penyewaan sepeda, seperti kondisi cuaca, hari kerja, dan suhu.

---

## ❓ Business Questions

1. Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda?
2. Apakah terdapat perbedaan jumlah penyewaan sepeda antara hari kerja dan hari libur?

---

## 📊 Data Understanding

Dataset yang digunakan adalah Bike Sharing Dataset yang berisi informasi:

* Tanggal (dteday)
* Kondisi cuaca (weathersit)
* Suhu (temp)
* Hari kerja/libur (workingday)
* Jumlah penyewaan (cnt)
* dan fitur lainnya

---

## 🛠 Data Preparation

Tahapan yang dilakukan:

* Memuat dataset (day.csv)
* Mengubah tipe data tanggal menjadi datetime
* Mengecek kualitas data (missing value & duplikasi)
* Menyimpan data hasil olahan ke main_data.csv untuk dashboard

---

## 📈 Exploratory Data Analysis (EDA)

Analisis dilakukan untuk:

* Melihat tren penyewaan sepeda
* Menganalisis pengaruh cuaca
* Membandingkan hari kerja vs hari libur

---

## 📊 Visualization & Analysis

Visualisasi yang digunakan:

* Line chart untuk tren penyewaan
* Bar chart untuk analisis cuaca
* Bar chart untuk hari kerja vs libur

Semua visualisasi dilengkapi dengan:

* Judul (title)
* Label sumbu (xlabel & ylabel)

---

## 🔍 Advanced Analysis

Menggunakan teknik **binning (clustering sederhana tanpa machine learning)**:

* Mengelompokkan suhu menjadi:

  * Low
  * Medium
  * High

Tujuan:

* Mengetahui pengaruh suhu terhadap penyewaan sepeda

---

## 📌 Conclusion

* Cuaca memengaruhi jumlah penyewaan sepeda
* Hari kerja memiliki penyewaan lebih tinggi dibanding hari libur
* Suhu yang nyaman meningkatkan jumlah penyewaan

---

## 💡 Recommendations

* Menambah jumlah sepeda pada hari kerja
* Memberikan promo saat hari libur atau cuaca buruk
* Mengoptimalkan distribusi sepeda berdasarkan kondisi

---

## 🖥️ Dashboard

Dashboard dibuat menggunakan Streamlit dengan fitur:

* KPI (Total, Rata-rata, Maksimum)
* Tren penyewaan
* Analisis cuaca
* Analisis hari kerja
* Analisis suhu
* Filter interaktif

---

## ▶️ Cara Menjalankan Dashboard

1. Masuk ke folder:
   cd submission

2. Jalankan:
   streamlit run dashboard/dashboard.py

3. Buka di browser:
   http://localhost:8501

---

## 📁 Struktur Direktori

submission/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── data/
│   ├── day.csv
│   └── hour.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt

---

## 📦 Requirements

Install library:

pip install -r requirements.txt

---

## 🌐 Deployment

Link dashboard terdapat pada file url.txt

---

## 👨‍💻 Author

Nama: Ilham Sanusi