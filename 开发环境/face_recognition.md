###  安装dlib
```
wget https://github.com/davisking/dlib/archive/v19.21.tar.gz
tar -xvf v19.21.tar.gz
mv dlib-19.21 dlib
cd dlib
mkdir build
cd build
cmake .. -DDLIB_USE_CUDA=1 -DUSE_AVX_INSTRUCTIONS=1
cmake --build .
cd ..
sudo python3 setup.py install
```

### 安装face_recognition
```
pip3 install face_recognition
```

