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
pip install numpy==1.6.1 -i https://mirrors.aliyun.com/pypi/simple/  
