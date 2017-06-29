# -*- coding: UTF-8 -*-
#代码写分割后图片信息的读写模式为追加，不要多次运行，否则写入的信息会重复
import os
from PIL import Image
import string 
import numpy as np

def splitimage(src, rownum, colnum, dstpath):
	img = Image.open(src)
	w, h = img.size
	if rownum <= h and colnum <= w:
		s = os.path.split(src)
		if dstpath == '':
			dstpath = s[0]
		fn = s[1].split('.')
		basename = fn[0]
		ext = fn[-1]

		num = 0
		rowheight = h // rownum
		colwidth = w // colnum
		for r in range(rownum):
			for c in range(colnum):
				box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)			
				img.crop(box).save(os.path.join(dstpath, basename + '_' + str(num) + '.jpg' ), 'jpeg')	#将原来的ext改为了'.jpg'和'jpeg'
				num = num + 1
	return colwidth,rowheight,basename



def read(file_path):
	#input_dir = os.path.dirname(os.path.abspath(__file__))
	src_txt_dir = file_path
	widthsize, heightsize,base = splitimage(src, row, col, dstpath)

	#widthsize = 624
	#heightsize = 534
	newtest = np.empty([0,7])
	with open(src_txt_dir, "r") as f:
		save_path1 = os.path.dirname(os.path.abspath(__file__))
		#doc = open(save_path1+ "/results" +"/" + base + '_' + str(num) +".txt",'w') ----------------
		i = 0
		for line in f.readlines():
			i+=1
			#doc.write(arr[0])   ---------------------
			if(i>6):

				#print line
				arr = line.split(" ")
				num, cartype, center_x, center_y, width, height, angle = int(arr[0]), int(arr[1]), int(arr[2]), int(arr[3]), int(arr[4]), int(arr[5]), float(arr[6])


				#print center_x, center_y
				#print "colsize",widthsize,heightsize
				row_num = center_y / heightsize		#切割后所在的行 行列均从0开始
				col_num = center_x / widthsize		#切割后所在的列
				#print row_num,col_num
				num = row_num*col + col_num			#切割后图片的编号
				#print num
				#if (num==68):
					#print line  		序号为117的数据有问题

				#-----------save_path1 = os.path.dirname(os.path.abspath(__file__))
				
				new_center_x = center_x - col_num * widthsize
				new_center_y = center_y - row_num * heightsize 
				#doc = open(save_path1+ "/results" +"/" + base + '_' + str(num) +".txt",'w')   #open会覆盖上次内容
	
				doc = open(save_path1+ "/results" +"/" + base + '_' + str(num) +".txt",'a')    #读写模式用了追加模式，不要多次运行
				doc.write(arr[0])															   
				doc.write(" " + arr[1])
				doc.write(" " + str(new_center_x))
				doc.write(" " + str(new_center_y))
				doc.write(" " + arr[4])
				doc.write(" " + arr[5])
				doc.write(" " + arr[6])
		#doc.write(" \n")



src = "/home/gnss/learn/aerial-image/imgsplit/2012-04-26-Muenchen-Tunnel_4K0G0120.JPG"  #需要分割的图片
if os.path.isfile(src):

	dstpath = "/home/gnss/learn/aerial-image/imgsplit/results"         #分割后图片存放位置
	if (dstpath == '') or os.path.exists(dstpath):

		row = 7   #切割行数
		col = 9   #切割列数
		splitimage(src, row, col, dstpath)

read("/home/gnss/learn/aerial-image/imgsplit/2012-04-26-Muenchen-Tunnel_4K0G0120_pkw.samp")     #读取的坐标文件





			
 
























