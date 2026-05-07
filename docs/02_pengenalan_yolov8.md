# Pengenalan YOLOv8

# 1. Apa Itu YOLO?

YOLO (You Only Look Once) adalah algoritma Object Detection berbasis Deep Learning yang mampu mendeteksi objek secara realtime.

YOLO bekerja dengan:
- Membaca gambar
- Mendeteksi lokasi objek
- Memberikan label objek
- Menghasilkan confidence score

# 2. Keunggulan YOLO

YOLO memiliki beberapa keunggulan:
- Proses deteksi sangat cepat
- Mampu bekerja realtime
- Akurasi tinggi
- Mudah digunakan

Karena keunggulan tersebut, YOLO banyak digunakan pada:
- CCTV
- Kendaraan otomatis
- Monitoring lalu lintas
- Sistem keamanan
- Dan aplikasi AI realtime.

# 3. Perkembangan YOLO

YOLO terus berkembang dari versi ke versi:

| Versi | Keterangan |
|---|---|
| YOLOv1 | Versi pertama YOLO |
| YOLOv3 | Mulai populer digunakan |
| YOLOv5 | Ringan dan cepat |
| YOLOv7 | Performa meningkat |
| YOLOv8 | Versi modern dari Ultralytics |

# 4. YOLOv8

YOLOv8 merupakan versi terbaru dari YOLO yang dikembangkan oleh Ultralytics.

YOLOv8 memiliki:
- Performa tinggi
- Struktur lebih sederhana
- Support classification
- Segmentation
- Dan object detection

# 5. Cara Kerja YOLOv8

YOLOv8 bekerja dengan membagi gambar menjadi beberapa grid.

Model akan:
- Mencari objek
- Menentukan posisi objek
- Memberikan probabilitas class

Output utama:
- Bounding box
- Class object
- Confidence score

# 6. Jenis Model YOLOv8

YOLOv8 memiliki beberapa jenis model:

| Model | Keterangan |
|---|---|
| YOLOv8n | Nano (ringan) |
| YOLOv8s | Small |
| YOLOv8m | Medium |
| YOLOv8l | Large |
| YOLOv8x | Extra Large |

Pada project ini digunakan:
- YOLOv8m untuk object detection
- YOLOv8m-cls untuk classification

# 7. Object Detection pada YOLOv8

Object Detection digunakan untuk:
- Mendeteksi lokasi objek
- Membuat bounding box
- Mengenali class object

Contoh objek:
- Person
- Car
- Laptop
- Bottle
- Chair

---

# 8. Classification pada YOLOv8

Classification digunakan untuk:
- Mengenali isi gambar
- Menentukan kategori objek

Pada project ini classification dilakukan menggunakan:
```python
yolov8m-cls.pt
```

Model classification menggunakan dataset ImageNet dengan 1000 class object.

# 9. Kesimpulan

YOLOv8 merupakan algoritma Computer Vision modern yang mampu melakukan object detection dan image classification secara realtime dengan performa yang baik.

Karena ringan dan mudah digunakan, YOLOv8 sangat cocok digunakan untuk pembelajaran Deep Learning dan Computer Vision.