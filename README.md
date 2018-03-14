# Attendance System

## Contributors
* Salman Shah
* Aiman A.
* Rashika C.
* Aniket K.
* Renu C.

## Setup

### Libraries Used
* gevent
* Flask_HTTPAuth
* face_recognition
* Flask
* flask_migrate

### Instructions to install the Face Recognition Library

* Make sure you have dlib installed with Python Bindings

* To install dlib, make sure you have **Python 3 pre-installed**. This is usually built-in for Linux.

* After that run the following commands on your terminal.
```
sudo apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
&& apt-get clean && rm -rf /tmp/* /var/tmp/*
```

```
cd ~ && \
    mkdir -p dlib && \
    git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ 
```

```
mkdir build; cd build; cmake .. -DDLIB_USE_CUDA=0 -DUSE_AVX_INSTRUCTIONS=1; cmake --build .
cd ..
python3 setup.py install --yes USE_AVX_INSTRUCTIONS --no DLIB_USE_CUDA
```

## Using Virtual Environment

* It is preferable to use a Virtual Environment rather than use your core Python Environment. Run the following instructions in the terminal to create and install all dependencies in the Virtual Environment.

```bash
virtualenv venv
pip install -r requirements.txt
source venv/bin/activate
```

* After installing the dependencies all you need to do is start the server to get your code running. To start the server, you can run the following command:
```
python server.py
```