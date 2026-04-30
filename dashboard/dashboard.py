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

weather_map = {
    1: "Clear",
    2: "Mist/Cloudy",
    3: "Light Snow/Rain",
    4: "Heavy Rain"
}

workingday_map = {
    0: "Holiday / Weekend",
    1: "Working Day"
}

df["weather_label"] = df["weathersit"].map(weather_map)
df["workingday_label"] = df["workingday"].map(workingday_map)

st.sidebar.header("Filter Data")

date_range = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    value=[df["dteday"].min(), df["dteday"].max()],
    min_value=df["dteday"].min(),
    max_value=df["dteday"].max()
)

selected_weather = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca",
    options=df["weather_label"].unique(),
    default=df["weather_label"].unique()
)

selected_day = st.sidebar.multiselect(
    "Pilih Jenis Hari",
    options=df["workingday_label"].unique(),
    default=df["workingday_label"].unique()
)

filtered_df = df.copy()

if len(date_range) == 2:
    start_date, end_date = date_range
    filtered_df = filtered_df[
        (filtered_df["dteday"] >= pd.to_datetime(start_date)) &
        (filtered_df["dteday"] <= pd.to_datetime(end_date))
    ]

filtered_df = filtered_df[
    (filtered_df["weather_label"].isin(selected_weather)) &
    (filtered_df["workingday_label"].isin(selected_day))
].copy()

st.title("🚲 Bike Sharing Dashboard")
st.write("Dashboard interaktif untuk menganalisis penyewaan sepeda berdasarkan waktu, cuaca, hari kerja, dan kategori suhu.")

col1, col2, col3 = st.columns(3)
col1.metric("Total Penyewaan", f"{filtered_df['cnt'].sum():,}")
col2.metric("Rata-rata Penyewaan Harian", round(filtered_df["cnt"].mean(), 2))
col3.metric("Penyewaan Tertinggi", f"{filtered_df['cnt'].max():,}")

st.divider()

st.subheader("Tren Penyewaan Sepeda Harian")

fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(data=filtered_df, x="dteday", y="cnt", ax=ax)
ax.set_title("Tren Penyewaan Sepeda Harian")
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

st.subheader("Pertanyaan 1: Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda")

weather_agg = filtered_df.groupby("weather_label")["cnt"].mean().sort_values(ascending=False).reset_index()

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(
    data=weather_agg,
    x="weather_label",
    y="cnt",
    hue="weather_label",
    palette="viridis",
    legend=False,
    ax=ax
)
ax.set_title("Rata-rata Penyewaan Berdasarkan Kondisi Cuaca")
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Rata-rata Jumlah Penyewaan")
plt.xticks(rotation=15)
st.pyplot(fig)

best_weather = weather_agg.iloc[0]
worst_weather = weather_agg.iloc[-1]

st.write(f"""
**Insight Pertanyaan 1:**  
Kondisi cuaca dengan rata-rata penyewaan tertinggi adalah **{best_weather['weather_label']}**
dengan rata-rata **{best_weather['cnt']:.2f}** penyewaan.  
Kondisi cuaca dengan rata-rata penyewaan terendah adalah **{worst_weather['weather_label']}**
dengan rata-rata **{worst_weather['cnt']:.2f}** penyewaan.
""")

st.subheader("Pertanyaan 2: Hari Kerja vs Hari Libur")

workingday_agg = filtered_df.groupby("workingday_label")["cnt"].mean().sort_values(ascending=False).reset_index()

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(
    data=workingday_agg,
    x="workingday_label",
    y="cnt",
    hue="workingday_label",
    palette="coolwarm",
    legend=False,
    ax=ax
)
ax.set_title("Rata-rata Penyewaan Hari Kerja dan Hari Libur")
ax.set_xlabel("Jenis Hari")
ax.set_ylabel("Rata-rata Jumlah Penyewaan")
st.pyplot(fig)

best_day = workingday_agg.iloc[0]
worst_day = workingday_agg.iloc[-1]

st.write(f"""
**Insight Pertanyaan 2:**  
Jenis hari dengan rata-rata penyewaan tertinggi adalah **{best_day['workingday_label']}**
dengan rata-rata **{best_day['cnt']:.2f}** penyewaan.  
Jenis hari dengan rata-rata penyewaan terendah adalah **{worst_day['workingday_label']}**
dengan rata-rata **{worst_day['cnt']:.2f}** penyewaan.
""")

st.subheader("Analisis Lanjutan: Binning Suhu")

filtered_df["temp_category"] = pd.cut(
    filtered_df["temp"],
    bins=3,
    labels=["Low", "Medium", "High"]
)

temp_agg = filtered_df.groupby("temp_category", observed=True)["cnt"].mean().reset_index()

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(
    data=temp_agg,
    x="temp_category",
    y="cnt",
    hue="temp_category",
    palette="magma",
    legend=False,
    ax=ax
)
ax.set_title("Rata-rata Penyewaan Berdasarkan Kategori Suhu")
ax.set_xlabel("Kategori Suhu")
ax.set_ylabel("Rata-rata Jumlah Penyewaan")
st.pyplot(fig)

best_temp = temp_agg.sort_values("cnt", ascending=False).iloc[0]

st.write(f"""
**Insight Analisis Lanjutan:**  
Kategori suhu dengan rata-rata penyewaan tertinggi adalah **{best_temp['temp_category']}**
dengan rata-rata **{best_temp['cnt']:.2f}** penyewaan.  
Analisis ini menggunakan teknik **binning**, yaitu pengelompokan suhu ke dalam kategori Low, Medium, dan High tanpa algoritma machine learning.
""")

st.divider()

st.subheader("Conclusion")

st.write(f"""
1. Kondisi cuaca memengaruhi jumlah penyewaan sepeda. Kondisi **{best_weather['weather_label']}**
memiliki rata-rata penyewaan tertinggi sebesar **{best_weather['cnt']:.2f}**.

2. Jenis hari juga memengaruhi penyewaan. **{best_day['workingday_label']}**
memiliki rata-rata penyewaan tertinggi sebesar **{best_day['cnt']:.2f}**.

3. Berdasarkan analisis binning suhu, kategori suhu **{best_temp['temp_category']}**
memiliki rata-rata penyewaan tertinggi sebesar **{best_temp['cnt']:.2f}**.
""")

st.subheader("Recommendation Action Item")

st.write("""
- Menambah ketersediaan sepeda pada periode dengan permintaan tinggi.
- Mengoptimalkan distribusi sepeda berdasarkan kondisi cuaca dan jenis hari.
- Memberikan promo saat cuaca buruk atau saat permintaan rendah.
- Menyesuaikan strategi operasional berdasarkan pola suhu dan tren penyewaan.
""")
