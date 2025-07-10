# Modelo de Detección de Boyas

En este repositorio encontrarás el código base de YOLOv7 usado para entrenar las diversas versiones de un modelo de detección de boyas, además de los scripts utilizados para preparar los diversos conjuntos de datos. 

## Introducción

Este proyecto a formado parte de mi Trabajo de Fin de Grado (TFG), financiado por la Plataforma Oceánica de Canarias (PLOCAN), y a contado con el apoyo logístico y técnico de la empresa Qualitas Artificial Intelligence and Science. El objetivo ha sido el desarrollo de un modelo de Visión por Computador basado en deep learning capaz de detectar boyas y otros elementos flotantes en el medio acuático, bajo la presencia de oclusiones u otras condiciones adversas. 

## Tecnologías Utilizadas

Este proyecto ha sido principalmente desarrollado en python bajo el framework pytorch y emplea librerías muy comunes en el mundo de la Visión por Computador y la Ciencia de Datos, como OpenCV y Pandas. Además, Docker a jugado un papel clave en el empaquetado y distribución del proyecto. 

 [![Python][Python.com]][Python-url] [![Docker][Docker.com]][Docker-url] [![NumPy][NumPy.com]][NumPy-url]  [![OpenCV][OpenCV.com]][OpenCV-url] [![Pandas][Pandas.com]][Pandas-url] [![Jupyter Notebook][JupyterNotebook.com]][JupyterNotebook-url][![PyTorch][PyTorch.com]][PyTorch-url] [![scikit-learn][scikit-learn.com]][scikit-learn-url] [![TensorBoard][TensorBoard.com]][TensorBoard-url] [![IPython][IPython.com]][IPython-url] [![TorchVision][TorchVision.com]][TorchVision-url]

## Análisis y Comparativa

Nuestro modelo presenta resultados positivos en todos los contextos y distancias. Realizar inferencia sobre el arroja grandes resultados y sale vencedor en comparativas con otras arquitecturas típicas. 

### Desempeño de arquitecturas de detección populares con BuoyCAT

| Modelo     | Precisión (P) | Recall (R) | mAP@0.5 | mAP@0.5:0.95 |
|------------|---------------|------------|---------|--------------|
| **YOLOv7-e6**   | **0.841**     | **0.771**  | **0.796** | 0.411        |
| YOLOv9-e   | 0.776         | 0.505      | 0.638   | 0.415        |
| YOLOv10-l  | 0.767         | 0.571      | 0.689   | 0.423        |
| YOLOv11-l  | 0.778         | 0.552      | 0.689   | **0.430**    |
| RE-DETR-l | 0.691         | 0.520      | 0.597   | 0.358        |


## Configuración y uso

Para poder realizar inferencia con nuestro modelo es importante llevar a cabo los siguientes pasos:

```sh
git clone git@github.com:pguillo02/yolov7.git
cd yolov7
pip install -r requirements.txt
```

Tras la configuración del entorno, si se desea realizar inferencia:

```sh
python detect.py --weights modelo.pt --conf 0.25 --img-size 1280 --source inference/boya1.jpg
```

Los resultados se encontrarán en runs/detect:

<div align="center">
    <a href="./">
        <img src="runs/detect//pexels-magi-dobreva-89810117-18852093.jpg" width="70%"/>
    </a>
</div>

Si lo que se busca es evaluar el modelo se recurrirá a:

```sh
python test.py --data data/data.yaml --img 1280 --batch 32 --conf 0.001 --iou 0.65 --device 0 --weights modelo.pt 
```

Para llevar a cabo un posible fine-tunning sobre nuestro modelo: 

```sh
python train_aux.py --workers 8 --device 0 --batch-size 16 --data data/data.yaml --img 1280 1280 --cfg cfg/training/yolov7-e6.yaml --weights modelo.py --hyp data/custom_hyp.yaml
```

## Despliegue

Si se quiere desplegar con Docker, se puede emplear el dockerfile presente en este repositorio:

```sh
docker build -t buoynet .
docker run -it buoynet
```

Para despues operarlo desde dentro.
 
## Autor

Pablo Guilló Jiménez - pablo.guillo101@alu.ulpgc.es

[Python.com]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[Docker.com]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/

[NumPy.com]: https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/

[OpenCV.com]: https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white
[OpenCV-url]: https://opencv.org/

[Pandas.com]: https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/

[JupyterNotebook.com]: https://img.shields.io/badge/Jupyter-FFFFFF?style=for-the-badge&logo=jupyter&logoColor=orange
[JupyterNotebook-url]: https://jupyter.org/

[PyTorch.com]: https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white
[PyTorch-url]: https://pytorch.org/

[scikit-learn.com]: https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white
[scikit-learn-url]: https://scikit-learn.org/

[TensorBoard.com]: https://img.shields.io/badge/TensorBoard-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white
[TensorBoard-url]: https://www.tensorflow.org/tensorboard

[IPython.com]: https://img.shields.io/badge/IPython-FFA500?style=for-the-badge&logo=ipython&logoColor=white
[IPython-url]: https://ipython.org/

[TorchVision.com]: https://img.shields.io/badge/TorchVision-EE4C2C?style=for-the-badge&logo=python&logoColor=white
[TorchVision-url]: https://pytorch.org/vision/stable/
