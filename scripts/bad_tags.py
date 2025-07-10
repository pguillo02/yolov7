import os

path = ""

for file in os.listdir(path):
    if not file.endswith(".txt"):  
        continue

    file_path = os.path.join(path, file)

    bad_tag = False
    line_count = 0
    
   
    if os.stat(file_path).st_size == 0:
        print(f"Archivo vacío: {file}")
        bad_tag = True
    else:
        with open(file_path, 'r') as f:
            for line in f:
                numbers = line.strip().split()
                print(numbers)
                count = len(numbers)

                if count != 5:  
                    bad_tag = True

                line_count += 1 

    if bad_tag:
        print(f"Archivo incorrecto: {file}")
        with open(file_path, 'w') as f: 
            f.write(" ")  
