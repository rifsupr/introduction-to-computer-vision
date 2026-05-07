# Hasil Pengujian dan Analisis

# 1. Pengujian Sistem

Pengujian dilakukan untuk mengetahui kemampuan sistem dalam:
- Mendeteksi objek
- Melakukan classification object
- Dan menampilkan hasil detection secara visual

Pengujian dilakukan menggunakan 4 gambar berbeda.

# 2. Skenario Pengujian

Berikut skenario pengujian yang dilakukan:

| No | Jenis Gambar | Tujuan |
|---|---|---|
| 1 | Gambar manusia | Menguji detection person |
| 2 | Gambar kucing Siamese | Menguji classification cat |
| 3 | Gambar kucing Egyptian | Menguji classification cat |
| 4 | Gambar singa | Menguji detection hewan besar |

# 3. Pengujian 1 — Gambar Manusia

## Hasil Detection

Model berhasil mendeteksi object:
- person

Confidence detection:
```text
97.22%
```

Namun hasil classification menunjukkan:
```text
sweatshirt
```

dengan confidence:
```text
51.29%
```

## Analisis

Hal ini terjadi karena:
- Model classification lebih fokus pada objek dominan
- Dan pakaian menjadi fitur visual paling dominan pada gambar

Walaupun object detection berhasil mengenali manusia dengan baik, classification model lebih memprioritaskan atribut visual tertentu.

# 4. Pengujian 2 — Gambar Kucing Siamese

## Hasil Detection

Model berhasil mendeteksi:
```text
cat
```

dengan confidence:
```text
96.04%
```

Hasil classification:
```text
Siamese_cat
```

dengan confidence:
```text
99.19%
```

## Analisis

Pada pengujian ini sistem bekerja sangat baik.

Model classification berhasil mengenali jenis kucing secara spesifik dengan confidence yang sangat tinggi.

Hal ini menunjukkan bahwa:
- Object crop berjalan baik
- Dan model ImageNet memiliki kemampuan klasifikasi hewan yang cukup akurat

# 5. Pengujian 3 — Gambar Kucing Egyptian

## Hasil Detection

Model berhasil mendeteksi:
```text
cat
```

dengan confidence:
```text
93.91%
```

Hasil classification:
```text
Egyptian_cat
```

dengan confidence:
```text
95.39%
```

## Analisis

Sistem berhasil mengenali jenis kucing Egyptian dengan cukup baik.

Top-5 prediction juga menunjukkan class lain yang masih berkaitan dengan keluarga kucing seperti:
- Tabby
- Tiger cat
- Lynx

Hal ini menunjukkan bahwa model memiliki kemampuan generalisasi visual yang baik.

# 6. Pengujian 4 — Gambar Singa

## Hasil Detection

Pada pengujian gambar singa, object detection mengalami kesalahan klasifikasi awal.

Model detection mendeteksi:
```text
dog
```

dan:
```text
cow
```

dengan confidence rendah.

Namun model classification berhasil mengenali:
```text
lion
```

dengan confidence:
```text
99.99%
```

## Analisis

Pengujian ini menunjukkan bahwa:
- object detection tidak selalu akurat,
- terutama jika objek memiliki kemiripan visual dengan class lain.

Namun model classification mampu memperbaiki hasil prediksi dengan sangat baik.

Hal ini menunjukkan kombinasi:
- detection + classification

Mampu meningkatkan hasil akhir sistem.

# 7. Analisis Umum Sistem

Berdasarkan hasil pengujian:
- Sistem mampu mendeteksi objek dengan baik
- Classification model bekerja cukup akurat
- Dan visualisasi detection berjalan dengan baik

Namun masih terdapat beberapa keterbatasan:
- Detection dapat salah klasifikasi
- Confidence dapat menurun pada objek tertentu
- Dan hasil sangat dipengaruhi kualitas gambar

# 8. Kelebihan Sistem

Kelebihan sistem:
- Implementasi sederhana
- Realtime object detection
- Classification cukup akurat
- Visualisasi mudah dipahami
- Dan mudah dikembangkan lebih lanjut

# 9. Kekurangan Sistem

Kekurangan sistem:
- Masih menggunakan pretrained model
- Belum menggunakan custom dataset
- Beberapa object masih salah detection
- Dan classification kadang fokus pada atribut tertentu

# 10. Kesimpulan Pengujian

Berdasarkan hasil pengujian, sistem berhasil melakukan:
- Object detection
- Image classification
- Visualisasi object
- Dan top-5 prediction

Kombinasi YOLOv8 Detection dan YOLOv8 Classification mampu menghasilkan sistem Computer Vision sederhana yang cukup baik untuk implementasi pembelajaran Deep Learning dan CNN.