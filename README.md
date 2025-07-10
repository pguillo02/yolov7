# Modelo de Detección de Boyas

En este repositorio encontrarás el código base de YOLOv7 usado para entrenar las diversas versiones de un modelo de detección de boyas, además de los scripts utilizados para preparar los diversos conjuntos de datos. 

## Introducción

Este proyecto a formado parte de mi Trabajo de Fin de Grado (TFG), financiado por la Plataforma Oceánica de Canarias (PLOCAN), y a contado con el apoyo logístico y técnico de la empresa Qualitas Artificial Intelligence and Science. El objetivo ha sido el desarrollo de un modelo de Visión por Computador basado en deep learning capaz de detectar boyas y otros elementos flotantes en el medio acuático, bajo la presencia de oclusiones u otras condiciones adversas. 

## Tecnologías Utilizadas

Este proyecto ha sido principalmente desarrollado en python bajo el framework pytorch y emplea librerías muy comunes en el mundo de la Visión por Computador y la Ciencia de Datos, como OpenCV y Pandas.

 [![Python][Python.com]][Python-url] [![Docker][Docker.com]][Docker-url] [![NumPy][NumPy.com]][NumPy-url]  [![OpenCV][OpenCV.com]][OpenCV-url] [![Pandas][Pandas.com]][Pandas-url] [![Jupyter Notebook][JupyterNotebook.com]][JupyterNotebook-url][![PyTorch][PyTorch.com]][PyTorch-url] [![scikit-learn][scikit-learn.com]][scikit-learn-url] [![TensorBoard][TensorBoard.com]][TensorBoard-url] [![IPython][IPython.com]][IPython-url] [![TorchVision][TorchVision.com]][TorchVision-url]

[ONVIF.com]: https://img.shields.io/badge/ONVIF-blue?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAA6lBMVEVHcEwUIiYsiLwrkMYTYpEWDgAFhL4QicQMjswYjMkZgr8QdLIUZqQJVpQLQX8AeK0Ak9QAj9IAg8MAaKAAZJ0ORokAU5QKSpAaEUIAktEAmdoAmt4AjcwJEioFP3gZPYYnMIEkDlEAoOMAlNIMFDAdM3kyHXgrF2gyG3UAnuAvGW8rFWorF2UxGnQaIl05JHpLOob58/8Ag8UAfrpfUJLDutu8s9YAdrgAaawwGXRYSI7LwuEAVIs0HHlFMoIAVpwAXaEAYKMzHnEGUZgxGnIyG3QZQo0VRY8lNYUlHWMxG3UyIHo0HHkxGHh7gQqnAAAATXRSTlMADDVHIwZqpMjq9+PFkVFe9f/bpYqv2ucxevL/1RNbzeM6/6kdpvKu3NvGk2fTKG+aCP+5vhki///qrRR7/4r//+Nb/7i+////e+P/+J+1zdQAAAEkSURBVHgBrY8DtgMxFECT2naa2m7Hntr7X85HxzjuPQjuI/gGMBAMBgOhsI8KRaKxeCKRTKUz0O2ysVw+XyiW0uVKtVxzunoDoWY2hMMQh1rtTtfhUK/XHwAdPBzZcrONP2cfZDwxI0Mx1JtiYAPP5sY1kkO9CHCwWOqFYTSPEHTK1XKtXQKxfL4JnODxZvu5BOO7POGScE5Smkzsdj6S1iXDJD1ldRlIsgyDnXLF8YK2ZoplWdEpF5KsXcJpRVX3K0fiZHTQr5nq8aiUB5YLn6Sz8YTDy/V6LZu5g7E0WpiRtc7tj879E43vD0kah4FJ9/F8PiVJ4mazh/THSXd67lKyGOl5JoP58iW9/5C488LhtOT1hidJXj4MgB9biqYF8BV+AcQZJp07IJ0ZAAAAAElFTkSuQmCC&link=https://www.onvif.org/
[ONVIF-url]: https://www.onvif.org/

[Python.com]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[Docker.com]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/

[NumPy.com]: https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/

[MATLAB.com]: https://img.shields.io/badge/MATLAB-0076A8?style=for-the-badge&logo=mathworks&logoColor=white
[MATLAB-url]: https://www.mathworks.com/products/matlab.html

[OpenCV.com]: https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white
[OpenCV-url]: https://opencv.org/

[Pandas.com]: https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/

[JupyterNotebook.com]: https://img.shields.io/badge/Jupyter-FFFFFF?style=for-the-badge&logo=jupyter&logoColor=orange
[JupyterNotebook-url]: https://jupyter.org/

[Cpp.com]: https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white
[Cpp-url]: https://isocpp.org/

[PyTorch.com]: https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white
[PyTorch-url]: https://pytorch.org/

[SciPy.com]: https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white
[SciPy-url]: https://scipy.org/

[Seaborn.com]: https://img.shields.io/badge/Seaborn-6495ED?style=for-the-badge&logo=python&logoColor=white
[Seaborn-url]: https://seaborn.pydata.org/

[scikit-learn.com]: https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white
[scikit-learn-url]: https://scikit-learn.org/

[TensorBoard.com]: https://img.shields.io/badge/TensorBoard-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white
[TensorBoard-url]: https://www.tensorflow.org/tensorboard

[IPython.com]: https://img.shields.io/badge/IPython-FFA500?style=for-the-badge&logo=ipython&logoColor=white
[IPython-url]: https://ipython.org/

[TorchVision.com]: https://img.shields.io/badge/TorchVision-EE4C2C?style=for-the-badge&logo=python&logoColor=white
[TorchVision-url]: https://pytorch.org/vision/stable/
