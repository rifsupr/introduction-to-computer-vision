from ultralytics import YOLO
import cv2
import os
from pathlib import Path
# =====================================
# SETUP
# =====================================
IMAGE_PATH = "images/4.png"
OUTPUT_FOLDER = "outputs"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
# =====================================
# LOAD MODELS
# =====================================
# Model deteksi  → bounding box (80 kelas COCO)
# Model klasifikasi → identifikasi objek (1000 kelas ImageNet)
detect_model = YOLO("models/yolov8m.pt")
cls_model    = YOLO("models/yolov8m-cls.pt")
# =====================================
# LOAD IMAGE
# =====================================
image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Gambar tidak ditemukan")
    exit()

img_h, img_w = image.shape[:2]
# =====================================
# OBJECT DETECTION
# =====================================
results = detect_model(image)
# =====================================
# PROCESS RESULT
# =====================================
obj_count = 0

for result in results:
    boxes = result.boxes
    for box in boxes:
        obj_count += 1
        # ----------------
        # Bounding box
        # ----------------
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        det_confidence = float(box.conf[0])
        det_class = detect_model.names[int(box.cls[0])]
        # ----------------
        # Crop objek untuk klasifikasi ulang
        # ----------------
        x1c, y1c = max(0, x1), max(0, y1)
        x2c, y2c = min(img_w, x2), min(img_h, y2)
        crop = image[y1c:y2c, x1c:x2c]
        # ----------------
        # Klasifikasi dengan ImageNet (1000 kelas)
        # ----------------
        cls_result = cls_model(crop, verbose=False)[0]
        top5_indices = cls_result.probs.top5
        top5_confs   = cls_result.probs.top5conf.tolist()
        # ----------------
        # Ambil prediksi terbaik
        # ----------------
        best_cls_name = cls_model.names[top5_indices[0]]
        best_cls_conf = top5_confs[0]
        # ----------------
        # Label menggunakan hasil klasifikasi
        # ----------------
        label = f"{best_cls_name} {best_cls_conf:.2f}"
        # ----------------
        # Draw rectangle
        # ----------------
        cv2.rectangle(
            image,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )
        # ----------------
        # Put label
        # ----------------
        cv2.putText(
            image,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2
        )
        # ----------------
        # Print result
        # ----------------
        print(f"\n── Objek #{obj_count} ──────────────────")
        print(f"  Deteksi (COCO)      : {det_class} ({det_confidence:.2%})")
        print(f"  Klasifikasi (ImageNet): {best_cls_name} ({best_cls_conf:.2%})")
        print(f"  Top-5 prediksi:")
        for rank, (idx, conf) in enumerate(zip(top5_indices, top5_confs), 1):
            name = cls_model.names[idx]
            bar  = "█" * int(conf * 20)
            print(f"    {rank}. {name:<20s} {conf:.2%}  {bar}")

# =====================================
# KLASIFIKASI GAMBAR PENUH (fallback)
# =====================================
if obj_count == 0:
    print("\n[INFO] Tidak ada objek terdeteksi, klasifikasi gambar penuh...")
    cls_result = cls_model(image, verbose=False)[0]
    top5_indices = cls_result.probs.top5
    top5_confs   = cls_result.probs.top5conf.tolist()

    best_cls_name = cls_model.names[top5_indices[0]]
    best_cls_conf = top5_confs[0]

    print(f"\n  Hasil klasifikasi: {best_cls_name} ({best_cls_conf:.2%})")
    print(f"  Top-5 prediksi:")
    for rank, (idx, conf) in enumerate(zip(top5_indices, top5_confs), 1):
        name = cls_model.names[idx]
        bar  = "█" * int(conf * 20)
        print(f"    {rank}. {name:<20s} {conf:.2%}  {bar}")

    label = f"{best_cls_name} {best_cls_conf:.2f}"
    cv2.putText(image, label, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

# =====================================
# SAVE RESULT
# =====================================
image_name = Path(IMAGE_PATH).stem
output_path = f"{OUTPUT_FOLDER}/{image_name}_result.jpg"
cv2.imwrite(output_path, image)
# ----------------
print(f"\nHasil disimpan di: {output_path}")