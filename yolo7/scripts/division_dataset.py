import os
import shutil
import random


carpeta_base = "C:/Users/pablo/Downloads/boyas_multiplataforma" 
carpeta_salida = os.path.join(os.path.dirname(carpeta_base), "boyas_multiplataforma")

ruta_images_base = os.path.join(carpeta_base, "images")
ruta_labels_base = os.path.join(carpeta_base, "labels")

ruta_images_out = os.path.join(carpeta_salida, "images")
ruta_labels_out = os.path.join(carpeta_salida, "labels")

for split in ["train", "val"]:
    os.makedirs(os.path.join(ruta_images_out, split), exist_ok=True)
    os.makedirs(os.path.join(ruta_labels_out, split), exist_ok=True)

imagenes = sorted([f for f in os.listdir(ruta_images_base) if os.path.isfile(os.path.join(ruta_images_base, f))])
random.shuffle(imagenes)

n_train = int(0.7 * len(imagenes))
imagenes_train = imagenes[:n_train]
imagenes_val = imagenes[n_train:]

def copiar(imagenes_lista, split):
    for img in imagenes_lista:
        nombre_lbl = os.path.splitext(img)[0] + ".txt"

        origen_img = os.path.join(ruta_images_base, img)
        destino_img = os.path.join(ruta_images_out, split, img)

        origen_lbl = os.path.join(ruta_labels_base, nombre_lbl)
        destino_lbl = os.path.join(ruta_labels_out, split, nombre_lbl)

        shutil.copy2(origen_img, destino_img)

        if os.path.exists(origen_lbl):
            shutil.copy2(origen_lbl, destino_lbl)
        else:
            print(f"Etiqueta no encontrada para {img}")

copiar(imagenes_train, "train")
copiar(imagenes_val, "val")

print(f"Dataset dividido y copiado en 'boyas de uso libre'")
print(f"   Train: {len(imagenes_train)} imágenes")
print(f"   Val:   {len(imagenes_val)} imágenes")
