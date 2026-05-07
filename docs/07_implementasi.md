# Implementasi Sistem

# 1. Gambaran Implementasi

Implementasi sistem dilakukan menggunakan Python dengan framework YOLOv8 dari Ultralytics dan OpenCV untuk pengolahan citra.

Sistem dirancang untuk:
- Mendeteksi objek pada gambar
- Melakukan klasifikasi objek
- Menampilkan bounding box
- Dan menghasilkan confidence score

# 2. Struktur Implementasi

Struktur project yang digunakan:

```text
yolov8-object-detection/
│
├── images/
├── outputs/
├── detect_image.py
├── requirements.txt
└── README.md
```

# 3. Library yang Digunakan

Berikut library utama yang digunakan:

| Library | Fungsi |
|---|---|
| ultralytics | Framework YOLOv8 |
| OpenCV | Pengolahan gambar |
| pathlib | Manajemen path file |
| os | Manajemen folder |

# 4. Model yang Digunakan

Project menggunakan dua model utama:

| Model | Fungsi |
|---|---|
| yolov8m.pt | Object Detection |
| yolov8m-cls.pt | Image Classification |

# 5. Implementasi Object Detection

Tahap pertama sistem adalah melakukan object detection menggunakan:

```python
detect_model = YOLO("yolov8m.pt")
```

Model ini digunakan untuk:
- Mendeteksi objek
- Menghasilkan bounding box
- Menentukan class object
- Dan memberikan confidence score

# 6. Implementasi Image Classification

Setelah objek berhasil dideteksi, sistem melakukan crop pada area object dan menjalankan proses classification menggunakan:

```python
cls_model = YOLO("yolov8m-cls.pt")
```

Model classification digunakan untuk:
- Mengenali objek lebih detail
- Menghasilkan top-5 prediction
- Dan meningkatkan informasi hasil detection

# 7. Proses Crop Object

Setelah bounding box diperoleh, sistem melakukan crop object menggunakan koordinat hasil detection.

Tujuan crop:
- Mengambil fokus area object
- Mengurangi noise
- Dan meningkatkan akurasi classification

# 8. Visualisasi Detection

Sistem menggunakan OpenCV untuk:
- Membuat bounding box
- Menampilkan label object
- Dan menampilkan confidence score

Bounding box ditampilkan menggunakan warna hijau pada setiap object yang berhasil dideteksi.

# 9. Output Sistem

Output utama sistem:
- Gambar hasil detection
- Bounding box object
- Label classification
- Confidence score
- Dan top-5 prediction

Hasil detection disimpan secara otomatis ke folder:

```text
outputs/
```
# 10. Implementasi Top-5 Prediction

Sistem menampilkan top-5 prediction dari model classification.

Tujuan top-5 prediction:
- Melihat kemungkinan class lain
- Membandingkan confidence prediction
- Dan membantu analisis hasil model

# 11. Alur Implementasi Sistem

Berikut alur implementasi sistem:

```text
Input Gambar
      ↓
YOLOv8 Detection
      ↓
Bounding Box
      ↓
Crop Object
      ↓
YOLOv8 Classification
      ↓
Top-5 Prediction
      ↓
Visualisasi Hasil
```
# 12. Hasil Implementasi

Sistem berhasil:
- Mendeteksi objek pada gambar,
- Melakukan classification object,
- Dan menampilkan hasil detection secara visual.

Object yang berhasil dikenali:
- Manusia
- Kucing
- Singa
- Dan berbagai objek lainnya

# 13. Kesimpulan Implementasi

Implementasi sistem berhasil dilakukan menggunakan kombinasi YOLOv8 dan OpenCV.

Sistem mampu melakukan:
- Object detection
- Image classification
- Visualisasi detection
- Dan menampilkan confidence score secara otomatis