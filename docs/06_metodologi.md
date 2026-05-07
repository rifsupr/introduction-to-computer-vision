# Metodologi

# 1. Metode Pengembangan

Project ini dikembangkan menggunakan pendekatan implementasi sederhana Computer Vision berbasis Deep Learning menggunakan YOLOv8.

Sistem dirancang untuk:
- Mendeteksi objek pada gambar
- Melakukan klasifikasi objek
- Dan menampilkan hasil deteksi secara visual

Metode utama yang digunakan:
- Object Detection menggunakan YOLOv8
- Image Classification menggunakan YOLOv8 Classification
- Pengolahan gambar menggunakan OpenCV

# 2. Alur Sistem

Berikut alur kerja sistem secara umum:

```text
Input Gambar
      ↓
YOLOv8 Object Detection
      ↓
Bounding Box Object
      ↓
Crop Object
      ↓
YOLOv8 Classification
      ↓
Top-5 Prediction
      ↓
Visualisasi Hasil
```

# 3. Input Sistem

Input utama sistem berupa gambar digital.

Format gambar yang digunakan:
- JPG
- JPEG
- PNG

Gambar dapat berisi:
- Manusia
- Kendaraan
- Hewan
- Perangkat elektronik
- Dan objek lainnya

# 4. Object Detection Menggunakan YOLOv8

Tahap pertama sistem adalah melakukan object detection menggunakan YOLOv8.

Model yang digunakan:

```python
yolov8m.pt
```

Model ini digunakan untuk:
- Mendeteksi objek
- Menentukan lokasi objek
- Dan menghasilkan bounding box

YOLOv8 membaca gambar dan memprediksi:
- Class object
- Confidence score
- Dan koordinat bounding box

# 5. Bounding Box Detection

Setelah objek berhasil dideteksi, sistem akan membuat bounding box pada setiap objek.

Bounding box digunakan untuk:
- Menandai lokasi objek
- Mempermudah visualisasi
- Dan menentukan area crop object

Informasi yang dihasilkan:
- Posisi objek
- Ukuran objek
- Confidence detection

# 6. Crop Object

Setelah bounding box diperoleh, sistem melakukan crop pada area objek.

Tujuan proses crop:
- Mengambil fokus area objek
- Mengurangi noise dari gambar lain
- Meningkatkan akurasi classification

Hasil crop digunakan pada tahap image classification

# 7. Image Classification Menggunakan YOLOv8 Classification

Tahap berikutnya adalah image classification menggunakan model:

```python
yolov8m-cls.pt
```

Model classification digunakan untuk:
- Mengenali objek lebih detail
- Menentukan kategori objek
- Dan menghasilkan top-5 prediction

Dataset yang digunakan model:
- ImageNet
- 1000 class object

# 8. Top-5 Prediction

Sistem menampilkan:
- Prediksi utama
- Dan top-5 classification prediction

Tujuan top-5 prediction:
- Melihat kemungkinan class object lain
- Membandingkan confidence prediction
- Mengevaluasi hasil klasifikasi model

# 9. Confidence Score

Confidence score menunjukkan tingkat keyakinan model terhadap hasil prediksi.

Nilai confidence berada pada rentang:

```text
0.00 — 1.00
```

Semakin tinggi confidence:
- Semakin yakin model terhadap hasil prediksi.

# 10. Pengolahan Gambar Menggunakan OpenCV

OpenCV digunakan untuk:
- Membaca gambar
- Membuat bounding box
- Menampilkan label object
- Dan menyimpan hasil visualisasi detection

OpenCV membantu proses visualisasi agar hasil object detection lebih mudah dipahami.

# 11. Visualisasi Hasil

Hasil detection divisualisasikan dalam bentuk:
- Bounding box
- Label object
- Confidence score
- Dan hasil classification

Output akhir berupa:
- Gambar hasil detection
- Dan informasi object prediction

# 12. Struktur Implementasi Sistem

Struktur implementasi project:

```text
yolov8-object-detection/
│
├── app/
├── docs/
├── images/
├── outputs/
├── models/
├── detect_image.py
├── requirements.txt
└── README.md
```

# 13. Lingkungan Pengembangan

Project dikembangkan menggunakan:

| Komponen | Teknologi |
|---|---|
| Bahasa Pemrograman | Python |
| Framework AI | Ultralytics YOLOv8 |
| Image Processing | OpenCV |
| IDE | VS Code |

# 14. Kesimpulan

Metodologi pada project ini menggunakan pendekatan object detection dan image classification berbasis CNN menggunakan YOLOv8.

Melalui kombinasi YOLOv8 dan OpenCV, sistem mampu mendeteksi objek, mengenali objek, dan menampilkan hasil visualisasi detection secara otomatis.