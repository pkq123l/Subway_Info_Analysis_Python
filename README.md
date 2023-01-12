

中国城市轨道交通数据可视化分析—Python
=====

> - A demo based on data visualized analysis written in Python language.



## 概述

> - 本项目是一个基于 Python 的简单数据可视化分析的小Demo。通过这个项目可以练习使用Python数据可视化分析相关的强大的库和模块，练习绘制简单的GUI界面并且连接数据库，更加深了对Python语言的学习和拓展。本项目也可作为学校的大作业、大实验实践或者课程设计等的选题项目。
> - 本项目通过多线程爬虫获取了高德地图中的中国轨道交通的一些数据信息，高德地图这个权威的网站也保证了数据的完整可靠性，然后进行了一些简单并且有趣的数据可视化分析，另外还设计了一个GUI界面，查询数据库或者文件中的一些信息。
>
> - 如发现文档中或者源代码中有错误，欢迎大家在 `Issues` 中研究讨论，欢迎大家 `Fork` 和 `Pull requests` 改善代码，十分感谢！

## 使用语言

- Python 3

## 主要技术

* **网络编程**
* **多线程**
* **文件操作**
* **数据库编程**
* **GUI**
* **数据分析**

## 导入的库和模块
```python
import json
import requests
from bs4 import BeautifulSoup
import sqlite3
import threading

import tkinter as tk
from tkinter import scrolledtext

import pandas as pd
from pyecharts import Line, Bar, Geo
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
import jieba
import matplotlib.pyplot as plt
import seaborn as sns
```

## 项目整体思路

1. 网页分析

2. 多线程爬虫爬取信息

3. 数据保存至文件中和数据库中

4. 利用 tkinter 绘制 GUI 界面，实现查询线路和站点两个功能

5. 数据可视化分析

   （1）直接控制台显示分析结果

   （2）绘制中国地图、柱状图等，生成 .html 文件

   （3）绘制词云

   （4）绘制柱状图、饼状图、折线图、散点图、双变量图等，生成 .png 文件

## 运行

- 分别运行`src`文件夹中的`.py`文件即可

## 部分运行结果样例

- `res`文件夹中的文件

## 待上传文件

- [ ] 总结报告.docx，预计5000字左右
- [ ] 答辩演示.ppt，预计20页左右

  
