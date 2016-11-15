# -*- coding:utf-8 -*-
import nuke


def auto_append_clip():
    all_nodes = nuke.selectedNodes("Read")

    all_nodes_list = []
    for i in all_nodes:
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

        # 设置read进来的色彩空间为"Gamma1.8"
        # i["colorspace"].setValue("Gamma1.8")
        all_nodes_list.append((read_num, i))

    # 列表排序
    all_nodes_list.sort(key=lambda x: x[0])

    for k in range(0, len(all_nodes_list)):
        try:
            all_nodes_list[k + 1][1].setXpos(all_nodes_list[k][1].xpos() + 120)
            all_nodes_list[k + 1][1].setYpos(all_nodes_list[k][1].ypos())
        except:
            pass

    ac = nuke.createNode("AppendClip")
    for j in range(0, len(all_nodes_list)):
        ac.setInput(j, all_nodes_list[j][1])

    min_pos = all_nodes_list[0][1]['xpos'].getValue() - 60.0
    max_pos = all_nodes_list[-1][1]['xpos'].getValue() + 60.0
    y_pos = all_nodes_list[0][1]['ypos'].getValue()
    ac.setXpos(int((max_pos - min_pos) / 2 + min_pos))
    ac.setYpos(int(y_pos + 500.0))
