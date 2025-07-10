import os
import shutil
import sys

directorio_datasets = ""
directorio_salida = os.path.join(directorio_datasets, "")
# ==============================================================

subcarpetas = [
    ("images/train", "labels/train"),
    ("images/val", "labels/val"),
]

print("Renombrando archivos .jpg a .jpeg...\n")
renombrados = []

datasets = [
    d for d in os.listdir(directorio_datasets)
    if os.path.isdir(os.path.join(directorio_datasets, d)) and d != ""
]

for dataset in datasets:
    for img_sub, _ in subcarpetas:
        ruta_imgs = os.path.join(directorio_datasets, dataset, img_sub)
        if not os.path.exists(ruta_imgs):
            continue
        for archivo in os.listdir(ruta_imgs):
            if archivo.lower().endswith(".jpg"):
                nombre_base = os.path.splitext(archivo)[0]
                origen = os.path.join(ruta_imgs, archivo)
                destino = os.path.join(ruta_imgs, nombre_base + ".jpeg")
                os.rename(origen, destino)
                renombrados.append(os.path.join(dataset, img_sub, archivo))

if renombrados:
    print(f"Se renombraron {len(renombrados)} archivo(s):")
    for r in renombrados:
        print(" -", r)
else:
    print("No se encontraron archivos .jpg para renombrar.")

for img_sub, lbl_sub in subcarpetas:
    os.makedirs(os.path.join(directorio_salida, img_sub), exist_ok=True)
    os.makedirs(os.path.join(directorio_salida, lbl_sub), exist_ok=True)


print("Verificando que todas las imágenes tengan su etiqueta...")

for dataset in datasets:
    for img_sub, lbl_sub in subcarpetas:
        ruta_imgs = os.path.join(directorio_datasets, dataset, img_sub)
        ruta_lbls = os.path.join(directorio_datasets, dataset, lbl_sub)

        if not os.path.exists(ruta_imgs) or not os.path.exists(ruta_lbls):
            continue

        for nombre_img in os.listdir(ruta_imgs):
            ruta_img = os.path.join(ruta_imgs, nombre_img)
            if not os.path.isfile(ruta_img):
                continue

            nombre_lbl = os.path.splitext(nombre_img)[0] + ".txt"
            ruta_lbl = os.path.join(ruta_lbls, nombre_lbl)

            if not os.path.exists(ruta_lbl):
                print(f"Falta etiqueta para: {os.path.join(dataset, img_sub, nombre_img)}")
                print("Proceso detenido. Corrige el problema y vuelve a ejecutar.")
                sys.exit(1)

print("Todas las imágenes tienen su etiqueta correspondiente. Procediendo a fusionar...\n")

copiados = set()  

for dataset in datasets:
    print(f"Copiando desde: {dataset}")
    for img_sub, lbl_sub in subcarpetas:
        ruta_imgs = os.path.join(directorio_datasets, dataset, img_sub)
        ruta_lbls = os.path.join(directorio_datasets, dataset, lbl_sub)

        for nombre_img in os.listdir(ruta_imgs):
            if nombre_img in copiados:
                print(f"Duplicado ignorado: {nombre_img}")
                continue

            ruta_img = os.path.join(ruta_imgs, nombre_img)
            if not os.path.isfile(ruta_img):
                continue

            nombre_lbl = os.path.splitext(nombre_img)[0] + ".txt"
            ruta_lbl = os.path.join(ruta_lbls, nombre_lbl)

            destino_img = os.path.join(directorio_salida, img_sub, nombre_img)
            destino_lbl = os.path.join(directorio_salida, lbl_sub, nombre_lbl)

            shutil.copy2(ruta_img, destino_img)
            shutil.copy2(ruta_lbl, destino_lbl)
            copiados.add(nombre_img)
            print(f"Copiado: {nombre_img} y {nombre_lbl}")

print(f"Fusión completada correctamente en ''")
print(f"Total único de imágenes copiados: {len(copiados)}")
