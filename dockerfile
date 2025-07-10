FROM nvidia/cuda:11.3.1-cudnn8-runtime-ubuntu20.04

ENV DEBIAN_FRONTEND=noninteractive

# 1. Instalar Python base y herramientas necesarias
RUN apt-get update && \
    apt-get install -y python3 python3-pip python-is-python3 git nano \
    libgl1 libglib2.0-0 libsm6 libxext6 libxrender-dev && \
    pip install --upgrade pip

# 2. Establecer directorio de trabajo
WORKDIR /app

# 3. Clonar repo yolov7 y copiar el requirements.txt
RUN git clone https://github.com/WongKinYiu/yolov7.git .
COPY requirements.txt .

# 4. Instalar torch y torchvision compatibles con CUDA 11.3
RUN pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 \
    -f https://download.pytorch.org/whl/cu113/torch_stable.html

# 5. Eliminar posibles duplicados de torch/torchvision
RUN sed -i '/^torch/d' requirements.txt && sed -i '/^torchvision/d' requirements.txt

# 6. Instalar el resto de dependencias
RUN pip install -r requirements.txt

# 7. Copiar pesos y dataset config
RUN mkdir -p pt
COPY pt/base/yolov7-e6_training.pt /app/pt/
COPY data/boyas.yaml /app/data/
COPY datasets/ /app/datasets/

# 8. Comando por defecto
CMD ["/bin/bash"]
