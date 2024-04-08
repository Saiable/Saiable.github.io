---
title: 'ppocrlabel安装及使用'
cover: false
typora-root-url: ppocrlabel安装及使用
---

https://github.com/PaddlePaddle/PaddleOCR

python版本：3.8.10

注：之前有安装过3.11、3.10、3.9版本，但使用ppocrlabel标注时，存在闪退情况

numpy版本：1.19.5

注：使用pip install numpy安装最新版，使用ppocrlabel标注时会报错误：AttributeError:

module 'numpy' has no attribute 'int'

pandas版本：1.4.3

注：pandas版本依赖numpy版本，需要适当降低pandas版本



安装过程：

1、安装python版本：需要把python添加到环境变量path中

2、安装paddlepaddle包：pip install paddlepaddle

3、安装ppocrlabel包：pip install ppocrlabel

4、使用命令：ppocrlabel --lang ch --kie True







