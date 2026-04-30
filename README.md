# 🚲 Bike Sharing Dashboard

Proyek ini merupakan submission analisis data Bike Sharing Dataset.  
Analisis dilakukan menggunakan Jupyter Notebook, kemudian hasil data yang sudah diolah digunakan untuk membuat dashboard interaktif menggunakan Streamlit.

---

## 📌 Alur Pengerjaan Project

Project ini dikerjakan melalui beberapa tahap berikut:

1. Mengimpor library yang dibutuhkan.
2. Memuat dataset Bike Sharing.
3. Melakukan data wrangling:
   - Gathering data
   - Assessing data
   - Cleaning data
4. Melakukan Exploratory Data Analysis (EDA).
5. Membuat visualisasi data untuk menjawab pertanyaan bisnis.
6. Membuat conclusion dan recommendation.
7. Menyimpan data hasil olahan ke file `main_data.csv`.
8. Membuat dashboard menggunakan Streamlit.
9. Menjalankan dashboard secara lokal.
10. Deploy dashboard ke Streamlit Cloud.

---

## ❓ Business Questions

1. Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda?
2. Apakah terdapat perbedaan jumlah penyewaan sepeda antara hari kerja dan hari libur?

---

## 📁 Struktur Folder

```bash
submission/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── data/
│   ├── data_1.csv
│   └── data_2.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

---

## ⚙️ Setup Environment

Sebelum menjalankan project, pastikan Python sudah terinstall.

Install semua library yang dibutuhkan dengan command berikut:

```bash
pip install -r requirements.txt
```

Isi library utama yang digunakan:

```bash
pandas
numpy
matplotlib
seaborn
streamlit
```

---

## 📓 Menjalankan Notebook

Notebook utama berada pada file:

```bash
notebook.ipynb
```

Pada notebook ini dilakukan proses:
- Import library
- Load dataset
- Data wrangling
- EDA
- Visualisasi data
- Analisis lanjutan menggunakan binning
- Conclusion dan recommendation

Dataset yang digunakan berada pada folder:

```bash
data/
```

File dataset:
```bash
data_1.csv
data_2.csv
```

---

## 💾 Membuat main_data.csv

Setelah proses analisis dan cleaning selesai, data hasil olahan disimpan ke folder dashboard menggunakan kode berikut:

```python
import os

os.makedirs("dashboard", exist_ok=True)
day_df.to_csv("dashboard/main_data.csv", index=False)
```

File `main_data.csv` ini digunakan sebagai sumber data utama pada dashboard Streamlit.

---

## 📊 Menjalankan Dashboard Streamlit

File dashboard berada pada:

```bash
dashboard/dashboard.py
```

Untuk menjalankan dashboard secara lokal, masuk ke folder project:

```bash
cd submission
```

Lalu jalankan command berikut:

```bash
streamlit run dashboard/dashboard.py
```

Setelah dijalankan, Streamlit akan menampilkan URL lokal seperti:

```bash
http://localhost:8501
```

Buka URL tersebut di browser untuk melihat dashboard.

---

## 🖥️ Fitur Dashboard

Dashboard menampilkan:

- Total penyewaan sepeda
- Rata-rata penyewaan harian
- Penyewaan tertinggi
- Tren penyewaan sepeda
- Pengaruh cuaca terhadap penyewaan
- Perbandingan hari kerja dan hari libur
- Analisis lanjutan kategori suhu
- Filter interaktif berdasarkan tahun, bulan, cuaca, dan jenis hari

---

## 🔍 Analisis Lanjutan

Analisis lanjutan yang digunakan adalah **binning**, yaitu teknik pengelompokan data tanpa algoritma machine learning.

Pada project ini, kolom suhu (`temp`) dikelompokkan menjadi tiga kategori:

```bash
Low
Medium
High
```

Tujuannya adalah untuk melihat pengaruh kategori suhu terhadap jumlah penyewaan sepeda.

---

## 📌 Insight

Beberapa insight yang diperoleh:

- Kondisi cuaca memengaruhi jumlah penyewaan sepeda.
- Cuaca yang lebih baik cenderung menghasilkan penyewaan yang lebih tinggi.
- Hari kerja memiliki jumlah penyewaan lebih tinggi dibandingkan hari libur.
- Suhu yang lebih nyaman cenderung meningkatkan jumlah penyewaan sepeda.

---

## ✅ Conclusion

1. Kondisi cuaca berpengaruh terhadap jumlah penyewaan sepeda. Cuaca yang lebih baik menghasilkan penyewaan yang lebih tinggi.
2. Hari kerja memiliki jumlah penyewaan lebih tinggi dibandingkan hari libur, sehingga sepeda kemungkinan banyak digunakan untuk aktivitas rutin.
3. Suhu juga berpengaruh terhadap penggunaan sepeda, terutama pada kategori suhu yang lebih nyaman.

---

## 💡 Recommendation

- Menambah ketersediaan sepeda pada hari kerja karena permintaan lebih tinggi.
- Memberikan promo pada hari libur atau saat cuaca buruk untuk meningkatkan penyewaan.
- Mengoptimalkan distribusi sepeda berdasarkan cuaca, hari kerja, dan kategori suhu.

---

## 🌐 Dashboard Online

Dashboard sudah dideploy menggunakan Streamlit Cloud dan dapat diakses melalui link berikut:

```bash
https://bike-sharing-dashboard-300426.streamlit.app/
```

Link dashboard juga tersedia pada file:

```bash
url.txt
```
