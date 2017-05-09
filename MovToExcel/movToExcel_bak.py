# -*- coding:utf-8 -*-
__date__ = '2017/3/17 18:52'
__author__ = 'liaokong'

import os
import subprocess
import re
import math
import sys
import shutil

from PySide import QtGui
from PySide import QtCore

libs_path = os.path.dirname(os.path.abspath(__file__)) + "/Libs/"
sys.path.insert(0, libs_path)

import xlsxwriter

from Ui_MovToExcel import Ui_MovToExcel


class JobThread(QtCore.QThread):
	def __init__(self, parent=None):
		super(JobThread, self).__init__(parent)

	def run(self):
		self.to_excel_btn_clicked()
		os.startfile("/".join(self.parent().excel_path_line.text().split("/")[:-1]))

	def to_excel_btn_clicked(self):
		parent = self.parent()

		head_list = [u"镜头号", u"缩略图", u"时长", u"难度", u"制作内容", u"制作人员", u"提交日期", u"制作状态", u"客户反馈"]
		img_path = (os.path.dirname(os.path.abspath(__file__)) + "/img/").replace("\\", "/")

		# 获取所有镜头列表
		video_file_list = []
		for root_name, dir_name, file_name in os.walk(parent.path_line.text()):
			if dir_name == []:
				if "Thumbs.db" in file_name:
					file_name.remove("Thumbs.db")
				for one_file in file_name:
					if os.path.splitext(one_file)[1] == ".mov":
						video_file_list.append(os.path.join(root_name, one_file).replace("/", "\\"))

		# 设置进度条最大值
		parent.progressBar.setMaximum(len(video_file_list))
		parent.excel_sig.connect(parent.progressBar.setValue)

		if not os.path.exists(img_path):
			os.mkdir(img_path)

		shot_list = []
		for index, i in enumerate(video_file_list):
			shot_info_list = []
			shot_info_list.append(i.split(".")[0].split("\\")[-1])

			# 生成视频缩略图
			os.popen("%sffmpeg.exe -i %s -t 00:00:1 -s 150*87 -r 1 %s.bmp" % (
				libs_path, i, (img_path + os.path.splitext(i)[0].split("\\")[-1])))

			# 获取视频秒数
			shot_len = os.popen(
				'%sffprobe.exe -i %s -show_entries format=duration -v quiet -of csv="p=0"' % (libs_path, i)).read()

			# 获取视频帧速率
			process = subprocess.Popen(['%sffmpeg.exe' % libs_path, '-i', i], stdout=subprocess.PIPE,
									   stderr=subprocess.STDOUT)
			stdout, _ = process.communicate()
			frame_rate = re.search(r'(\d+) fps', stdout)

			# # 获取视频总帧数
			shot_frame_len = int(math.ceil(int(frame_rate.group(1)) * float(shot_len.split("\n")[0])))

			shot_info_list.append(shot_frame_len)
			shot_list.append(shot_info_list)

			# 设置当前进度条
			parent.excel_sig.emit(index + 1)

		# shot_list返回值
		# [['S05_06bu_fx_00100', 119], ['S05_06bu_fx_00200', 50], ['S05_06bu_fx_00201', 50]]

		# 生成表格
		workbook = xlsxwriter.Workbook(parent.excel_path_line.text())
		worksheet = workbook.add_worksheet()

		# 添加字体居中风格
		center_style = workbook.add_format()

		center_style.set_align('center')
		center_style.set_align('vcenter')

		# 添加头部信息
		for head_index, head_item in enumerate(head_list):
			worksheet.write(0, head_index, head_item, center_style)
			worksheet.set_row(0, 25)
			worksheet.set_column(0, head_index, 20.5)

		# 添加内容
		for excel_index, excel_item in enumerate(shot_list):
			bmp_path = "%s.bmp" % (img_path + excel_item[0])
			worksheet.write(excel_index + 1, 0, excel_item[0], center_style)
			worksheet.set_row(excel_index + 1, 66)
			worksheet.insert_image(excel_index + 1, 1, bmp_path)
			worksheet.write(excel_index + 1, 2, str(excel_item[1]), center_style)

		worksheet.set_column(4, 4, 50)

		workbook.close()
		shutil.rmtree(img_path)

		QtGui.QMessageBox.information(parent, u"提示", u"excel已生成完成！")
		parent.close()


class MovToExcel(QtGui.QDialog, Ui_MovToExcel):
	excel_sig = QtCore.Signal(int)

	def __init__(self, parent=None):
		super(MovToExcel, self).__init__(parent)
		self.setupUi(self)

		self.job_thread = JobThread(self)

		self.setFixedSize(572, 125)
		self.progressBar.setMinimum(0)
		self.progressBar.setValue(0)

		self.path_btn.clicked.connect(self.path_btn_clicked)
		self.excel_path_btn.clicked.connect(self.excel_path_btn_clicked)
		self.to_excel_btn.clicked.connect(self.job_thread.start)

	def path_btn_clicked(self):
		source_path = str(QtGui.QFileDialog.getExistingDirectory(self, u"请选择素材的路径", "Z:\Plates"))
		self.path_line.setText((source_path + "/").replace("\\", "/"))

	def excel_path_btn_clicked(self):
		excel_path = str(
			(QtGui.QFileDialog.getSaveFileName(self, u"请选择素材的路径", "Z:\Plates", "xls files (*.xlsx)"))[0].encode("utf8"))
		self.excel_path_line.setText(excel_path)


def start():
	start.mov_to_excel = MovToExcel()
	start.mov_to_excel.show()


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)

	mov_to_excel = MovToExcel()
	mov_to_excel.show()

	app.exec_()
