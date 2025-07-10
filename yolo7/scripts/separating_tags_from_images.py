import os
import shutil

source_dir = ""  

images_dir = os.path.join(source_dir, "images")
labels_dir = os.path.join(source_dir, "labels")

os.makedirs(images_dir, exist_ok=True)
os.makedirs(labels_dir, exist_ok=True)

for file in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file)
    
    if os.path.isfile(file_path):
        if file.lower().endswith(".jpg"):
            shutil.move(file_path, os.path.join(images_dir, file))
        elif file.lower().endswith(".txt"):
            shutil.move(file_path, os.path.join(labels_dir, file))

print("Separación completada.")















        