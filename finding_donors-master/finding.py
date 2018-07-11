#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:41:00 2018

@author: apple
"""

# 为这个项目导入需要的库
import numpy as np
import pandas as pd
from time import time
from IPython.display import display # 允许为DataFrame使用display()

# 导入附加的可视化代码visuals.py
import visuals as vs

# 导入人口普查数据
data = pd.read_csv("census.csv")

# 成功 - 显示第一条记录
display(data.head(n=1))

# 将数据切分成特征和对应的标签
income_raw = data['income']
features_raw = data.drop('income', axis = 1)

# 可视化 'capital-gain'和'capital-loss' 两个特征
vs.distribution(features_raw)