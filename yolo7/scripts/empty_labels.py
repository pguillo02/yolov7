import os

images_path = ""
labels_path = ""

if not os.path.exists(images_path) or not os.path.exists(labels_path):
    print(f"Error: Una de las carpetas no existe.")
    exit()

for image in os.listdir(images_path):
    image = image.strip()
    if image.lower().endswith((".jpeg", ".jpg", ".png")):
        label_filename = os.path.splitext(image)[0] + ".txt"
        label_filepath = os.path.join(labels_path, label_filename)

        if not os.path.exists(label_filepath):
            with open(label_filepath, 'w') as f:
                f.write("")
            print(f"Creada etiqueta: {label_filepath}")

