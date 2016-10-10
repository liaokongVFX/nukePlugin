# -*- coding: utf=8 -*-

"""
#########################

修正多层嵌套的素材无法正确导入的问题

使用方法：
1.把多层嵌套的文件夹拖入节点窗口
2.框选导入进来的所有错误read节点
3.点击correct Read Path(Ctrl+Shift+Z)

by:了空

#########################

"""

import nuke
import os


def correctReadPath():
    selNodes = nuke.selectedNodes("Read")

    if selNodes != []:

        for readNode in selNodes:
            errorPath = readNode["file"].getValue()
            for rootName, dirName, fileName in os.walk(errorPath):
                if dirName == []:
                    if os.listdir(rootName):
                        if "Thumbs.db" in fileName:
                            fileName.remove("Thumbs.db")

                        if len(fileName[0].split(".")) == 3:
                            readFileName = fileName[0].split(".")[0]
                            padd = len(fileName[-1].split(".")[1])
                            houzhui = fileName[0].split(".")[2]
                            firstFrame = fileName[0].split(".")[1]
                            endFrame = fileName[-1].split(".")[1]

                            readNode = nuke.createNode("Read", inpanel=False)
                            fileFullPath = rootName + "/" + readFileName + ".%0{}d.".format(padd) + houzhui
                            readNode["file"].setValue(fileFullPath.replace("\\", "/"))
                            readNode["first"].setValue(int(firstFrame))
                            readNode["last"].setValue(int(endFrame))
                            readNode["origfirst"].setValue(int(firstFrame))
                            readNode["origlast"].setValue(int(endFrame))


                        else:
                            for stillFile in fileName:
                                if stillFile != "Thumbs.db":
                                    readFileName = stillFile.split(".")[0]
                                    houzhui = stillFile.split(".")[1]
                                    readNode = nuke.createNode("Read", inpanel=False)
                                    fileFullPath = os.path.join(rootName, stillFile)
                                    readNode["file"].setValue(fileFullPath.replace("\\", "/"))

        for delNode in selNodes:
            nuke.delete(delNode)

    else:
        nuke.message("请选择要修正的Read节点")
