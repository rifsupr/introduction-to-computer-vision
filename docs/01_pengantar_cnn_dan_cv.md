# Pengantar CNN dan Computer Vision

# 1. Apa Itu Computer Vision?

Computer Vision (CV) adalah salah satu cabang Artificial Intelligence (AI) yang memungkinkan komputer untuk memahami dan menganalisis gambar maupun video seperti cara manusia melihat dunia.

Computer Vision digunakan untuk:
- Mendeteksi objek
- Mengenali wajah
- Membaca teks
- Melakukan tracking
- Hingga memahami isi gambar secara otomatis

Teknologi ini banyak digunakan dalam:
- Kendaraan otomatis
- Sistem keamanan
- Smart city
- Kesehatan
- Industri
- Retail
- Dan media sosial


# 2. Cara Kerja Computer Vision

Secara umum, Computer Vision bekerja dengan tahapan berikut:

```text
Input Gambar/Video
        ↓
Preprocessing
        ↓
Ekstraksi Fitur
        ↓
Model AI / Deep Learning
        ↓
Hasil Prediksi
```

Komputer akan mempelajari pola visual dari gambar menggunakan algoritma Machine Learning maupun Deep Learning.

# 3. Apa Itu CNN?

CNN (Convolutional Neural Network) adalah algoritma Deep Learning yang dirancang khusus untuk pengolahan gambar.

CNN mampu:
- Mengenali pola visual
- Mendeteksi bentuk
- Mengenali objek
- Dan melakukan klasifikasi gambar secara otomatis

CNN menjadi dasar utama dalam banyak teknologi Computer Vision modern.

# 4. Kenapa CNN Sangat Populer?

CNN sangat populer karena:
- Mampu mengenali gambar dengan akurasi tinggi
- Dapat belajar otomatis dari data
- Cocok untuk object detection dan classification
- Lebih efektif dibanding metode image processing tradisional

CNN banyak digunakan pada:
- Face recognition
- Object detection
- Image classification
- OCR
- Segmentation
- Dan medical imaging

# 5. Struktur Dasar CNN

CNN terdiri dari beberapa layer utama:

| Layer | Fungsi |
|---|---|
| Convolution Layer | Mengambil fitur gambar |
| Activation Function | Menambahkan non-linearitas |
| Pooling Layer | Mengurangi dimensi data |
| Fully Connected Layer | Melakukan klasifikasi |

# 6. Convolution Layer

Convolution Layer merupakan inti dari CNN.

Layer ini bekerja dengan:
- Membaca pola
- Mendeteksi edge
- Mengenali bentuk
- Dan mengekstraksi fitur visual dari gambar

Contoh fitur:
- Garis
- Sudut
- Tekstur
- Warna
- Bentuk objek

# 7. Pooling Layer

Pooling digunakan untuk:
- mengurangi ukuran data
- Mempercepat proses training
- Mengurangi overfitting

Jenis pooling yang sering digunakan:
- Max Pooling
- Average Pooling

# 8. Activation Function

Activation Function digunakan agar model mampu mempelajari pola kompleks.

Contoh activation function:
- ReLU
- Sigmoid
- Softmax

Pada CNN modern, ReLU menjadi activation function yang paling umum digunakan.

# 9. Object Detection

Object Detection adalah teknik Computer Vision untuk:
- Mendeteksi lokasi objek
- Mengenali jenis objek pada gambar

Output object detection:
- Bounding box
- Label object
- Confidence score

# 10. Image Classification

Image Classification adalah proses mengenali isi utama suatu gambar.

Contoh:
- Gambar kucing
- Gambar mobil
- Gambar laptop

Model akan memprediksi class tertentu berdasarkan isi gambar.

# 11. YOLO dalam Computer Vision

YOLO (You Only Look Once) merupakan algoritma object detection modern yang:
- Cepat
- Ringan
- Dan memiliki akurasi tinggi

YOLO banyak digunakan karena:
- Mampu mendeteksi objek secara realtime
- Cocok untuk video dan webcam
- Dan mudah diimplementasikan

Versi terbaru yang digunakan pada project ini adalah YOLOv8.

# 12. Kesimpulan

Computer Vision merupakan teknologi penting dalam Artificial Intelligence yang memungkinkan komputer memahami gambar dan video.

CNN menjadi dasar utama dalam pengolahan citra modern karena mampu mengenali pola visual dengan baik.

Pada project ini digunakan YOLOv8 sebagai implementasi CNN untuk melakukan object detection dan image classification secara otomatis.