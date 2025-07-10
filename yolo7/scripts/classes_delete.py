import os 
import re

l_folder = "id_labels"

labels = ["5","6","7","8","9"]

for item in labels:

    lmargin = int(item) - 1
    rmargin = 10 - lmargin -1 

    pattern = "\.[01]{" + str(lmargin) + "}1[01]{" + str(rmargin) +"}\.txt"

    print(pattern)

    for file in os.listdir(l_folder):
        if bool(re.match(pattern, file)):
            print("hola")
            
