# Computer Vision
## Pengantar CNN dan Implementasi Object Detection menggunakan YOLOv8

## Deskripsi Repository

Repository ini membahas pengantar dasar **Computer Vision** dan **Convolutional Neural Network (CNN)** serta implementasi nyata project sederhana berbasis **Deep Learning** menggunakan **YOLOv8**.

Project dikembangkan untuk memahami bagaimana teknologi AI modern mampu:
- Mendeteksi objek pada gambar
- Mengenali objek secara otomatis
- Melakukan image classification
- Dan menampilkan visualisasi hasil detection

Selain implementasi sistem, repository ini juga membahas:
- Dasar teori CNN dan Computer Vision
- Cara kerja YOLOv8
- Metodologi implementasi sistem
- Hasil pengujian
- Serta analisis performa model detection dan classification.

## Daftar Isi

| Bab | Judul | File |
|-----|-------|------|
| I | Pengantar CNN dan Computer Vision | [01_pengantar_cnn_dan_cv.md](01_pengantar_cnn_dan_cv.md) |
| II | Pengenalan YOLOv8 | [02_pengenalan_yolov8.md](02_pengenalan_yolov8.md) |
| III | Project Overview | [03_project_overview.md](03_project_overview.md) |
| IV | Pendahuluan | [04_pendahuluan.md](04_pendahuluan.md) |
| V | Landasan Teori | [05_landasan_teori.md](05_landasan_teori.md) |
| VI | Metodologi | [06_metodologi.md](06_metodologi.md) |
| VII | Implementasi Sistem | [07_implementasi.md](07_implementasi.md) |
| VIII | Hasil Pengujian dan Analisis | [08_hasil_pengujian.md](08_hasil_pengujian.md) |
| IX | Penutup | [09_penutup.md](09_penutup.md) |

## Ringkasan Pembahasan

### 1. Pengantar CNN dan Computer Vision
Membahas konsep dasar:
- Computer Vision
- CNN (Convolutional Neural Network)
- Object Detection
- Image Classification
- Dan implementasi AI pada pengolahan citra digital.

### 2. Pengenalan YOLOv8
Menjelaskan:
- Algoritma YOLO
- Cara kerja YOLOv8
- Jenis model YOLOv8
- Object Detection
- Dan Classification menggunakan YOLOv8.

### 3. Implementasi Project Sederhana
Project mengimplementasikan sistem:
- Object Detection
- Bounding Box Visualization
- Image Classification
- Confidence Score
- Dan Top-5 Prediction

menggunakan:
- Python
- YOLOv8
- Dan OpenCV.

### 4. Analisis Hasil Sistem
Repository juga membahas hasil pengujian sistem menggunakan beberapa gambar berbeda untuk menganalisis:
- Akurasi detection
- Kemampuan classification
- Confidence score
- Dan kemampuan visualisasi detection.

Analisis menunjukkan bahwa kombinasi:
- YOLOv8 Detection
- Dan YOLOv8 Classification

mampu meningkatkan kemampuan sistem dalam mengenali objek pada gambar.

## Teknologi yang Digunakan

| Teknologi | Fungsi |
|---|---|
| Python | Bahasa Pemrograman |
| YOLOv8 | Object Detection |
| YOLOv8m-cls | Image Classification |
| OpenCV | Pengolahan Citra |
| Ultralytics | Framework YOLOv8 |

## Model yang Digunakan

| Model | Fungsi |
|---|---|
| yolov8m.pt | Object Detection |
| yolov8m-cls.pt | Image Classification |

## Cara Menjalankan Project

```bash
# Install dependency
pip install -r requirements.txt

# Jalankan program
python detect_image.py