# -*- coding:utf-8 -*-

import nuke
import os
import getpass
import time
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def auto_render_panel():
    cp = nuke.Panel("自动渲染文件生成      by jgcy", 450)

    dirTemp = "c:/"
    cp.addFilenameSearch("输出路径:", dirTemp)

    cp.addButton("取消")
    cp.addButton("生成")

    result = cp.show()

    if result == 1:
        outDir = cp.value("输出路径:") + "/"

        # 判断输出路径是否存在
        if os.path.exists(outDir):
            auto_render(outDir)

        else:
            os.mkdir(outDir)
            auto_render(outDir)


def auto_render(render_path):
    read_nodes = nuke.selectedNodes("Read")
    all_nodes_list = []

    for i in read_nodes:
        read_path = i["file"].getValue()
        if len(read_path.split(".")) == 2:
            if read_path.split(".")[0].find("-") != -1:
                read_num = read_path.split(".")[0].split("-")[-1].split("_")[0]
            else:
                read_num = read_path.split(".")[0].split("_")[-2]


        elif len(read_path.split(".")) == 3:
            if read_path.split(".")[0].find("-") != -1:
                read_num = read_path.split(".")[0].split("-")[-1]
            else:
                read_num = read_path.split(".")[0].split("_")[-1]

        i["colorspace"].setValue("Gamma1.8")
        all_nodes_list.append((read_num, i))

    all_nodes_list.sort(key=lambda x: x[0])

    write_num = []

    for k in range(0, len(all_nodes_list)):
        try:
            all_nodes_list[k + 1][1].setXpos(all_nodes_list[k][1].xpos() + 120)
            all_nodes_list[k + 1][1].setYpos(all_nodes_list[k][1].ypos())

            merge_node = nuke.createNode("Merge")
            merge_node.setInput(1, nuke.toNode("Premult1"))
            merge_node.setInput(0, all_nodes_list[k][1])
            merge_node.setXpos(all_nodes_list[k][1].xpos())
            merge_node.setYpos(all_nodes_list[k][1].ypos() + 120)

            write_node = nuke.createNode("Write")
            read_name = all_nodes_list[k][1]["file"].getValue()

            name = read_name.split("/")[-1]
            if len(name.split(".")) == 3:
                write_name = render_path + name.split(".")[0] + ".mov"
            elif len(name.split(".")) == 2:
                if len(name.split("_")) == 3:
                    write_name = render_path + name.split("_")[0] + "_" + name.split("_")[1] + ".mov"
                elif len(name.split("_")) == 2:
                    write_name = render_path + name.split("_")[0] + ".mov"

            write_node["file"].setValue(write_name)
            write_node["mov64_fps"].setValue(25)
            write_node["mov32_fps"].setValue(25)
            write_num.append(write_node["name"].getValue())

        except:
            merge_node = nuke.createNode("Merge")
            merge_node.setInput(1, nuke.toNode("Premult1"))
            merge_node.setInput(0, all_nodes_list[k][1])
            merge_node.setXpos(all_nodes_list[k][1].xpos())
            merge_node.setYpos(all_nodes_list[k][1].ypos() + 120)

            write_node = nuke.createNode("Write")
            read_name = all_nodes_list[k][1]["file"].getValue()

            name = read_name.split("/")[-1]
            if len(name.split(".")) == 3:
                write_name = render_path + name.split(".")[0] + ".mov"
            elif len(name.split(".")) == 2:
                if len(name.split("_")) == 3:
                    write_name = render_path + name.split("_")[0] + "_" + name.split("_")[1] + ".mov"
                elif len(name.split("_")) == 2:
                    write_name = render_path + name.split("_")[0] + ".mov"

            write_node["file"].setValue(write_name)
            write_node["mov64_fps"].setValue(25)
            write_node["mov32_fps"].setValue(25)
            write_num.append(write_node["name"].getValue())
    nuke.scriptSaveAs(render_path + 'render_%s.nk' % getpass.getuser())

    ft = open(render_path + "render_%s_%d.bat" % (getpass.getuser(), int(time.time())), 'w')
    for g in xrange(0, len(all_nodes_list)):
        nuke_path = '\"C:\\Program Files\\Nuke9.0v1\\Nuke9.0.exe\" -x -m 8 -F %s' % str(
            int(all_nodes_list[g][1]["first"].getValue())) + "-" + str(int(all_nodes_list[g][1]["last"].getValue()))

        nuke_name1 = " -X %s " % write_num[g]
        nuke_name2 = render_path + "render_%s.nk" % getpass.getuser()
        full_path = nuke_path + nuke_name1 + nuke_name2

        ft.write(full_path + '\n')
    ft.write("pause" + '\n')
    ft.close()
    # os.system("start"+temp_bat_name)


def batch_render_main():
    auto_render_go = auto_render_panel()
    if auto_render_go != None:
        auto_render(auto_render_go[0])
