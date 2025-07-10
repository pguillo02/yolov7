import os 

l_folder: str = ""
i_folder: str = ""

counter: int = 0

for file in os.listdir(l_folder):
    if os.path.getsize(os.path.join(l_folder, file)) == 0:
        elabel: str = os.path.join(l_folder, file)
        eimage: str = os.path.join(i_folder, file.replace(".txt", ".jpeg"))
        #os.remove(elabel)
        #os.remove(eimage)
        counter += 1
print(counter)