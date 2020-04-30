# CUDA Installation Guide on Ubuntu 18.04

Before Installing CUDA, make sure your machine has a CUDA supported GPU.

Upgrade everything in Ubuntu and reboot:
```
$ sudo apt-get update && sudo apt-get -y upgrade && sudo apt-get -y dist-upgrade
$ sudo reboot
```

Then, type in the following command to display your GPU information:
```
sudo lshw -c display
```
You would see a few lines similar to the following. If you have not installed any of the Nvidia driver, the configuration part will display "driver=nouveau".


