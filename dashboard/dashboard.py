import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

sns.set(style="whitegrid")

df = pd.read_csv("dashboard/main_data.csv")
df["dteday"] = pd.to_datetime(df["dteday"])

st.sidebar.header("Filter Data")

year_options = sorted(df["dteday"].dt.year.unique())
selected_year = st.sidebar.multiselect(
    "Pilih Tahun",
    options=year_options,
    default=year_options
)

month_options = sorted(df["mnth"].unique())
selected_month = st.sidebar.multiselect(
    "Pilih Bulan",
    options=month_options,
    default=month_options
)

weather_options = sorted(df["weathersit"].unique())
selected_weather = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca",
    options=weather_options,
    default=weather_options
)

workingday_options = sorted(df["workingday"].unique())
selected_workingday = st.sidebar.multiselect(
    "Pilih Jenis Hari",
    options=workingday_options,
    default=workingday_options
)

filtered_df = df[
    (df["dteday"].dt.year.isin(selected_year)) &
    (df["mnth"].isin(selected_month)) &
    (df["weathersit"].isin(selected_weather)) &
    (df["workingday"].isin(selected_workingday))
].copy()

st.title("🚲 Bike Sharing Dashboard")
st.write("Analisis penyewaan sepeda berdasarkan cuaca, hari kerja, dan kategori suhu.")

col1, col2, col3 = st.columns(3)

col1.metric("Total Penyewaan", f"{filtered_df['cnt'].sum():,}")
col2.metric("Rata-rata Harian", round(filtered_df["cnt"].mean(), 2))
col3.metric("Penyewaan Tertinggi", f"{filtered_df['cnt'].max():,}")

st.divider()

st.subheader("Tren Penyewaan Sepeda")

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=filtered_df, x="dteday", y="cnt", ax=ax)
ax.set_title("Tren Penyewaan Sepeda Harian")
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

st.subheader("Pengaruh Cuaca terhadap Penyewaan")

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(
    data=filtered_df,
    x="weathersit",
    y="cnt",
    hue="weathersit",
    palette="viridis",
    legend=False,
    ax=ax
)
ax.set_title("Rata-rata Penyewaan Berdasarkan Cuaca")
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

st.write("""
**Insight:**  
Cuaca yang lebih baik menghasilkan jumlah penyewaan sepeda yang lebih tinggi.
""")

st.subheader("Hari Kerja vs Hari Libur")

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(
    data=filtered_df,
    x="workingday",
    y="cnt",
    hue="workingday",
    palette="coolwarm",
    legend=False,
    ax=ax
)
ax.set_title("Perbandingan Penyewaan Hari Kerja dan Hari Libur")
ax.set_xlabel("Working Day (0 = Libur, 1 = Hari Kerja)")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

st.write("""
**Insight:**  
Hari kerja memiliki jumlah penyewaan lebih tinggi dibandingkan hari libur.
""")

st.subheader("Analisis Lanjutan: Kategori Suhu")

filtered_df["temp_category"] = pd.cut(
    filtered_df["temp"],
    bins=3,
    labels=["Low", "Medium", "High"]
)

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(
    data=filtered_df,
    x="temp_category",
    y="cnt",
    hue="temp_category",
    palette="magma",
    legend=False,
    ax=ax
)
ax.set_title("Penyewaan Berdasarkan Kategori Suhu")
ax.set_xlabel("Kategori Suhu")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

st.write("""
**Insight:**  
Jumlah penyewaan sepeda cenderung meningkat pada kategori suhu yang lebih nyaman.
Analisis ini menggunakan teknik binning tanpa algoritma machine learning.
""")

st.subheader("Kesimpulan")

st.write("""
- Cuaca memengaruhi jumlah penyewaan sepeda.
- Hari kerja memiliki jumlah penyewaan lebih tinggi dibandingkan hari libur.
- Suhu juga berpengaruh terhadap penggunaan sepeda.
""")

st.subheader("Rekomendasi Action Item")

st.write("""
- Menambah ketersediaan sepeda pada hari kerja karena permintaan lebih tinggi.
- Memberikan promo pada hari libur atau saat cuaca buruk untuk meningkatkan penyewaan.
- Mengoptimalkan distribusi sepeda berdasarkan cuaca, hari kerja, dan kategori suhu.
""")