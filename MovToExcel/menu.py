﻿# -*- coding:utf-8 -*-
__date__ = '2017/3/20 15:35'
__author__ = 'liaokong'

import nuke
import movToExcel
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

nuke.menu("Nuke").addCommand(u"Liaokong/项目表格生成工具", "movToExcel.start()")

