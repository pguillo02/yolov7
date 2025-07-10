#!/usr/bin/env python3
import os

DATASET_ROOT = 'benchmark_multidistancia'  
def update_yolo_labels(root_dir, splits=('train', 'val')):
    """
    Recorre root_dir/labels/<split>/*.txt y cambia
    la primera columna '0' por '1' en cada línea,
    sobrescribiendo directamente el fichero.
    """
    for split in splits:
        label_dir = os.path.join(root_dir, 'labels', split)
        if not os.path.isdir(label_dir):
            print(f"[!] Directorio no encontrado: {label_dir}")
            continue

        for fname in sorted(os.listdir(label_dir)):
            if not fname.lower().endswith('.txt'):
                continue

            path = os.path.join(label_dir, fname)
            with open(path, 'r') as f:
                lines = f.readlines()

            new_lines = []
            changed = False
            for line in lines:
                parts = line.strip().split()
                if not parts:
                    continue
                if parts[0] == '1':
                    parts[0] = '0'
                    changed = True
                new_lines.append(' '.join(parts) + '\n')

            if changed:
                with open(path, 'w') as f:
                    f.writelines(new_lines)
                print(f"[✓] Actualizado: {path}")
            else:
                print(f"[ ] Sin cambios: {path}")

if __name__ == '__main__':
    update_yolo_labels(DATASET_ROOT)
