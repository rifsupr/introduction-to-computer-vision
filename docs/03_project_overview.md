# Project Overview
# Object Detection & Classification menggunakan YOLOv8

# 1. Deskripsi Project

Project ini merupakan implementasi Computer Vision menggunakan algoritma YOLOv8 untuk melakukan:
- Object detection
- Image classification
- Dan visualisasi hasil deteksi objek secara otomatis

Sistem mampu:
- Mendeteksi objek pada gambar
- Memberikan bounding box
- Menampilkan label objek
- Menampilkan confidence score
- Dan melakukan klasifikasi tambahan menggunakan model classification

# 2. Tujuan Project

Tujuan utama project ini adalah:
- Memahami implementasi Computer Vision
- Memahami konsep CNN
- Mempelajari object detection menggunakan YOLOv8
- Dan membangun sistem AI sederhana berbasis Deep Learning

# 3. Fitur Sistem

Fitur utama project:
- Deteksi objek otomatis
- Klasifikasi objek
- Confidence score
- Visualisasi bounding box
- Top-5 classification prediction
- Dan penyimpanan hasil deteksi

# 4. Teknologi yang Digunakan

| Teknologi | Fungsi |
|---|---|
| Python | Bahasa pemrograman |
| YOLOv8 | Object Detection |
| YOLOv8 Classification | Image Classification |
| OpenCV | Pengolahan gambar |
| Ultralytics | Framework YOLOv8 |

# 5. Model yang Digunakan

Project menggunakan dua model utama:

| Model | Fungsi |
|---|---|
| yolov8m.pt | Object Detection |
| yolov8m-cls.pt | Image Classification |

Model detection digunakan untuk:
- Mendeteksi objek
- Menentukan lokasi objek
- Dan membuat bounding box

Model classification digunakan untuk:
- Mengenali objek lebih detail
- Dan menghasilkan top-5 prediction

# 6. Alur Sistem

Berikut alur kerja sistem:

```text
Input Gambar
      ↓
YOLOv8 Object Detection
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

# 7. Output Sistem

Output yang dihasilkan:
- Gambar hasil deteksi
- Bounding box object
- Label object
- Confidence score
- Dan hasil klasifikasi object

# 8. Hasil yang Diharapkan

Sistem diharapkan mampu:
- Mendeteksi objek secara otomatis
- Mengenali objek dengan baik
- Dan menampilkan hasil visualisasi detection secara realtime maupun berbasis gambar

# 9. Kesimpulan

Project ini merupakan implementasi sederhana Deep Learning berbasis CNN menggunakan YOLOv8 untuk object detection dan classification.

Melalui project ini dapat dipahami bagaimana teknologi Computer Vision bekerja dalam mengenali dan memahami objek pada gambar secara otomatis.