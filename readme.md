# Keras安装

## 首先保证Python是3.6以下版本

pip install virtualenv

## windows打开cmd然后启动虚拟环境

virtualenv keras  
keras\Scripts\activate.bat

## 在目前的环境下安装其它软件包

pip install numpy jupyter keras matplotlib tensorflow -i https://mirrors.aliyun.com/pypi/simple/   
pip uninstall tornado  
pip install tornado==5.1.1 -i https://mirrors.aliyun.com/pypi/simple/  
pip uninstall numpy  
pip install numpy==1.16.1 -i https://mirrors.aliyun.com/pypi/simple/  

## 设置pip安装源为国内

安装步骤：  

在你的电脑的c:\user(或者用户)\你电脑的用户名\，这个目录下创建个命名为“pip”的文件夹（如：C:\Users\gmn\pip），在该文件夹下创建一个命名为“pip.ini”的文件，在该文件中写入以下内容：  

[global]  
index-url=https://mirrors.aliyun.com/pypi/simple/  
[install]    
trusted-host=https://mirrors.aliyun.com/pypi/simple/    
disable-pip-version-check = true    
timeout = 6000  

# OpenCV 安装
打开cmd  或 powershell  
pip install opencv-python

