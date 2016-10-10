import nuke
import deleteUpdata

nuke.menu("Nuke").addMenu("&Cache").addCommand("Clear Local File Cache", "deleteUpdata.deleteUpdata()", "Shift+v")
