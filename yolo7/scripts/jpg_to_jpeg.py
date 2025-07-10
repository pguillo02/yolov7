import os

folder:str = ""

for item in os.listdir(folder):
    path = os.path.join(folder, item)

    new_image = path.replace(".jpg", ".jpeg")

    os.rename(path, new_image)