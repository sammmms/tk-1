# CHECKED BY SAM, 2025-22-4

# Already moved to tk-1.py

from PIL import Image, ImageEnhance
import os
import numpy as np

# Dataset : Dataset merupakan dataset Wiki-Art yang telah di refine pada penelitian ART-GAN https://github.com/cs-chan/ArtGAN/blob/master/WikiArt%20Dataset/README.md
# Deskripsi: Script ini mengubah ukuran gambar menjadi 15x15 piksel, mengubahnya menjadi grayscale, dan meningkatkan kontrasnya.

# Path folder input dan output
input_folder = 'images'
output_folder = 'resized_images'
new_size = (15, 15)

# Buat folder output jika belum ada
os.makedirs(output_folder, exist_ok=True)

# Loop semua file di folder input
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # filter gambar
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert('L')  # ubah ke grayscale

        # TODO : Jangan resize lagi karena kita pakai library untuk enhance contrast dan segala macem
        # img_resized = img.resize(new_size)

        # 🔧 Peningkatan Kontras (contoh: tingkatkan 1.5x)
        enhancer = ImageEnhance.Contrast(img)
        img_contrast = enhancer.enhance(1.5)

        # TODO : Tambahkan normalisasi
        # Normalisasi (skala piksel ke rentang 0-1)
        img_array = np.array(img_contrast) / 255.0
        img_normalized = Image.fromarray((img_array * 255).astype('uint8'))

        # TODO : Tambahkan sharpening
        
        # Path tujuan simpan
        save_path = os.path.join(output_folder, filename)
        img.save(save_path)
        

print("Semua gambar berhasil di-resize ke folder:", output_folder)
