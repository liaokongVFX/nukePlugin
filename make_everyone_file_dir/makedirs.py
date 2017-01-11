# -*- coding:utf-8 -*-

import os
import shutil
import time
import threading

import sys
import nuke

reload(sys)
sys.setdefaultencoding("utf-8")


def my_makedirs_panel():
	cp = nuke.Panel("文件整理      by jgcy", 450)

	dirTemp = "Z:/Plates/"
	cp.addFilenameSearch("文件整理路径:", dirTemp)

	cp.addButton("取消")
	cp.addButton("生成")

	result = cp.show()

	if result == 1:
		outDir = cp.value("文件整理路径:")

		# 判断路径是否存在
		if os.path.exists(outDir):
			do_makedirs(outDir)

		else:
			nuke.message(u"请重新选择正确路径！")


def my_makedirs(filename):
	"""
	创建文件夹并拷贝文件（同时删除原始文件）
	"""
	os.makedirs(filename.split(".")[0])
	shutil.copyfile(filename, os.path.join(filename.split(".")[0], filename.split("/")[-1]))
	# 删除原始文件
	# os.remove(filename)


def do_makedirs(dirpath):
	"""
	多线程执行 my_makedirs 命令
	"""
	file_list = [os.path.join(dirpath, f) for f in os.listdir(dirpath)]
	for filename in file_list:
		if filename != dirpath + "Thumbs.db":
			p = threading.Thread(target=my_makedirs, args=(filename,))
			p.setDaemon(True)
			p.start()

		elif filename == dirpath + "Thumbs.db":
			try:
				os.remove(dirpath + "Thumbs.db")
			except:
				pass

	nuke.message(u"文件整理完成，共整理了%d个文件。" % len(os.listdir(dirpath)))


def my_makedirs_main():
	my_makedirs_go = my_makedirs_panel()
	if my_makedirs_go != None:
		do_makedirs(my_makedirs_go[0])

