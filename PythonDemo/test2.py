# -*- coding: utf-8 -*-

print("sss")
import psutil
print(psutil.cpu_count()) # CPU逻辑数量
print(psutil.cpu_times())  #统计CPU的用户／系统／空闲时间：