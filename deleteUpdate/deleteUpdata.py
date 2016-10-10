# -*- coding:utf-8 -*-

import nuke
import os
import shutil


# 用来删除Local File Cache命令的缓存
#
# by：了空


def deleteUpdata():
    pref = nuke.toNode("preferences")

    localisePath = pref["localCachePath"].getValue()

    if localisePath == "[getenv NUKE_TEMP_DIR]/localise":
        shutil.rmtree(os.environ['NUKE_TEMP_DIR'] + '/localise')

    else:
        shutil.rmtree(localisePath)
