# CUDA Installation Guide on Ubuntu 18.04
Before Installing CUDA, make sure your machine has a CUDA supported GPU.
## Remove any previously installed CUDA and nvidia driver

```
sudo rm /etc/apt/sources.list.d/cuda*
sudo apt remove --autoremove nvidia-cuda-toolkit
sudo apt remove --autoremove nvidia-*
```
## Setup the correct CUDA PPA on your system
Upgrade everything in Ubuntu and reboot:
```
$ sudo apt-get update && sudo apt-get -y upgrade && sudo apt-get -y dist-upgrade
$ sudo reboot
```

```
$ sudo add-apt-repository ppa:graphics-drivers/ppa
$ sudo apt-key adv --fetch-keys  http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
$ sudo bash -c 'echo "deb http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64 /" > /etc/apt/sources.list.d/cuda.list'
$ sudo bash -c 'echo "deb http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64 /" > /etc/apt/sources.list.d/cuda_learn.list'
```

After rebooting, your nvidia driver will successfully installed. Type `nvidia-smi` in terminal and you will see this:
![nvidia_driver](/CUDA_Guide/nvidia-driver.png)

**Note that the field of 'CUDA Version' is only showing the current driver's CUDA compatability version, and not indicative of what CUDA is installed.**

## Install CUDA 10.0 and CUDNN 7
```
$ sudo apt update
$ sudo apt install cuda-10-1
$ sudo apt install libcudnn7
```

## Setup PATH to CUDA
Open the '.profile' file:
```
$ nano ~/.profile
```
Add the following lines at the end of the file:
```
if [ -d "/usr/local/cuda-10.0/bin/" ]; then
    export PATH=/usr/local/cuda-10.0/bin${PATH:+:${PATH}}
    export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
fi
```

## Reboot
```
sudo reboot
```

## Check Installation
Check Nvidia Driver:
```
nvidia-smi
```
![nvidia_driver](/CUDA_Guide/nvidia-driver.png)

Check CUDA:
```
nvcc -V
```
![CUDA](/CUDA_Guide/CUDA.png)

Check CUDNN:
```
/sbin/ldconfig -N -v $(sed ‘s/:/ /’ <<< $LD_LIBRARY_PATH) 2>/dev/null | grep libcudnn
```
![CUDNN](/CUDA_Guide/CUDNN.png)

#### Congratulations!
