#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2
from numpy import *
import random

'''	
对输入图像作移动平均分割
image为单通道灰度图像
num表示计算平均的点数
'''
def movingthresh(image, num): 
	#print(data)
	width = image.shape[0]
	height = image.shape[1]
	widthStep = width
	data = image.flatten()  # 转换成一维向量
	dstdata = data.copy()
	#print(height)
	#print(width)
	while widthStep % 2 != 0: #widthStep必须是4的倍数
		widthStep += 1
	n = float(num)
	m_pre = data[0]/n
	b = 0.5
	for i in range(height):
		for j in range(width):
			index = i * widthStep + j
			if index < num + 1:
				dif = data[index]
			else:
				dif = int(data[index]) - int(data[index-num-1])
			dif *= 1/n
			m_now = m_pre + dif
			m_pre = m_now
			if data[index] > round(b * m_now):
				dstdata[index] = 255
			else:
				dstdata[index] = 0
	return array(dstdata).reshape(width, height)



if __name__ == '__main__':
	# 读入图像
	srcImage = cv2.imread("1.png", 0)
	if srcImage is None:
		print("Failed to read source image.")
		exit()
	cv2.imshow("source image", srcImage)

	dstImage = movingthresh(srcImage,2)
	cv2.imshow("dstImage", dstImage)
	cv2.waitKey(0)