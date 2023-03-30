# Setup guide of this project
## Install poetry
See [poetry oficial installation guide](https://python-poetry.org/docs/#installing-with-the-official-installer)

## setup cuda(for windows)
**If your OS is windows, DO NOT install nvidia-driver of linux**
### Install nvidia-driver
Download nvidia-driver from https://www.nvidia.co.jp/Download/index.aspx?lang=jp  
(Recommended driver is NVIDIA Studio)  

### Install nvidia-cuda-toolkit
See [CUDA Toolkit 11.7 Downloads](https://developer.nvidia.com/cuda-11-7-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_network)    
**Note that the last command is different from the official guide !!**

```shell
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/3bf863cc.pub
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/ /"
sudo apt-get update
sudo apt-get -y install cuda-11-7
```

### Install cuDNN
See [official guide](https://developer.nvidia.com/rdp/cudnn-download).  
If you haven't registered to NVIDIA DEVELOPER, you will be asked to register for it.

## Install libraries.
```shell
poetry install
```

## Install BLAS implemetation
"BLAS" stands for Basic Linear Algebra Subprograms.  
This project uses Intel MKL as the BLAS implementation.  
To install Intel MKL, execute below scripts.
```shell
curl -sfL https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB | sudo apt-key add -
sudo curl -sfL https://apt.repos.intel.com/setup/intelproducts.list -o /etc/apt/sources.list.d/intelproducts.list
sudo apt update
sudo apt install -y intel-mkl-64bit-2020.4-912
```

Add following lines to `.bashrc` to set PATH.  

```
export MKL_ROOT_DIR=/opt/intel/mkl
export LD_LIBRARY_PATH=$MKL_ROOT_DIR/lib/intel64:/opt/intel/lib/intel64_lin:$LD_LIBRARY_PATH
export LIBRARY_PATH=$MKL_ROOT_DIR/lib/intel64:$LIBRARY_PATH
export LD_PRELOAD=/opt/intel/mkl/lib/intel64/libmkl_def.so:/opt/intel/mkl/lib/intel64/libmkl_avx2.so:/opt/intel/mkl/lib/intel64/libmkl_core.so:/opt/intel/mkl/lib/intel64/libmkl_intel_lp64.so:/opt/intel/mkl/lib/intel64/libmkl_intel_thread.so:/opt/intel/lib/intel64_lin/libiomp5.so
```

## Install swig
```
sudo apt update
sudo apt install swig -y
```

## Build faiss and Python wrapper
Build Faiss
```shell
git clone https://github.com/facebookresearch/faiss
cd faiss
poetry run cmake -B build .
poetry run make -C build -j faiss

```
Build Python wrapper
```shell
poetry run make -C build -j swigfaiss
```

## Install Faiss
```shell
poetry add $(pwd)/build/faiss/python
```
