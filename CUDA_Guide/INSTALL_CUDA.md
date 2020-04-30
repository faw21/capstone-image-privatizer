# CUDA Installation Guide on Ubuntu 18.04

Before Installing CUDA, make sure your machine has a CUDA supported GPU.

Upgrade everything in Ubuntu and reboot:
```
$ sudo apt-get update && sudo apt-get -y upgrade && sudo apt-get -y dist-upgrade
$ sudo reboot
```

Then, type in the following command to display your GPU information:
```
$ sudo lshw -c display
```
You would see a few lines similar to the following. If you have not installed any of the Nvidia driver, the configuration part will display "driver=nouveau".

![display_GPU_info](/CUDA_Guide/display_GPU_info.png)

Then run the following command to display nvidia drivers that are compatible with your GPU:
```
$ sudo ubuntu-drivers devices
```
You shall see the following:

![display_available_driver](/CUDA_Guide/display_available_driver.png)

We want the lastest version of nvidia driver, that is, `nvidia-driver-440`. Type the following command to install the driver:
```
$ sudo apt install nvidia-driver-440
```
After installing the driver, you should use the following command to reboot your machine. PS. Some machines may occur problems here if use `sudo reboot`
```
$ sudo shutdown -r now
```
After rebooting, type `nvidia-smi` in terminal and you will see this:
![nvidia_driver](/CUDA_Guide/nvidia-driver.png)

**Note that the field of 'CUDA Version' is only showing the current driver's CUDA compatability version, and not indicative of what CUDA is installed.**
