import os
import cv2

def recortar_marca_inferior_derecha(imagen):
    alto, ancho = imagen.shape[:2]
    altura_recorte = 80
    ancho_recorte = 160
    # Recortar desde (0,0) hasta donde empieza la marca
    return imagen[0:alto - altura_recorte, 0:ancho - ancho_recorte]

def procesar_directorio(raiz):
    for carpeta in os.listdir(raiz):
        ruta_carpeta = os.path.join(raiz, carpeta)
        if not os.path.isdir(ruta_carpeta):
            continue

        for archivo in os.listdir(ruta_carpeta):
            if archivo.lower().endswith(('.jpg', '.jpeg', '.png')):
                ruta_imagen = os.path.join(ruta_carpeta, archivo)
                imagen = cv2.imread(ruta_imagen)
                if imagen is None:
                    print(f"No se pudo leer: {ruta_imagen}")
                    continue

                imagen_recortada = recortar_marca_inferior_derecha(imagen)
                cv2.imwrite(ruta_imagen, imagen_recortada)
                print(f"Recortada: {ruta_imagen}")



carpeta_raiz = "C:/Users/pablo/Downloads/frames/frames"
procesar_directorio(carpeta_raiz)

