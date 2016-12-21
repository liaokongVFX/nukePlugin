# nukePlugin
自己写的一些nuke小插件


## 安装方法：
放入用户文件夹下的.nuke目录下即可

eg：
C:\Users\Liaokong\\.nuke\


## 使用方法：

[correct Read Path](#correctReadPath)

[delete Update](#deleteUpdate)

[file Collector](#fileCollector)

[auto append clip](#auto_append_clip)

[batch render](#batch_render)

[autoBackup](#autoBackup)

[writeToRead](#writeToRead)

##

### correctReadPath
修正多层嵌套的素材无法正确导入的问题

使用方法：

1.把多层嵌套的文件夹拖入节点窗口

2.框选导入进来的所有错误read节点

3.点击correct Read Path(Ctrl+Shift+Z)

### deleteUpdate

用来删除Local File Cache命令的创建的缓存

### fileCollector
nuke工程项目打包，所有文件中所用的素材都会被拷贝到Sources下，打包出来的文件中的素材路径会被修改成当前文件夹的相对路径。

最新版支持了包含“文件名.%04d”、“文件名_%04d”、“文件名_####”、“文件名.####”格式的路径素材的打包。

但不支持带有中文或空格的路径素材的文件打包。

###auto_append_clip
根据素材路径名称中的镜头号，自动排列素材，并且给素材创建AppendClip节点。用于把多个镜头拼接成一条素材输出。

使用方法：
选择所要要拼接的read节点，使用Liaokong/auto_AppendClip（ctrl+alt+shift+a）命令即可。

所支持的素材路径格式:

./../../集数-镜头号.%04d.dpx

./../../集数_镜头号.%04d.dpx

./../../集数-镜头号_%04d.dpx

./../../集数_镜头号 _%04d.dpx

###batch_render
用来批量给每个镜头压上水印并批量渲染多个镜头

使用方法：
渲染所有要压水印的镜头素材，然后执行Liaokong下的batch render按钮，在弹窗对话框中设置渲染要输出的路径，然后点生成。

然后关闭nuke文件，在刚才选择的输出路径下，执行生成的bat文件即可。（渲染出的文件名会和需要压水印的素材名相同，输出的格式是mov）

ps：
使用时需要先导入水印素材，并在水印下面建立Premult节点，名字需为"Premult1"。

在文件中，每执行一次Liaokong下的batch render按钮，就会在输出路径里面创建一个新的bat文件，这样可以生成多个bat文件来同时渲染多个镜头。（bat文件可以同时开启多个）

比如 有4集的镜头需要渲染，每集有50个镜头需要压水印并且输出成mov，就可以每导入一集所有的镜头，执行以下batch render命令，这样，4集就会生成4个bat文件，然后就可以同时执行这4个bat文件，就可以同时渲染这4集的所有镜头了。
nuke输出时没有大量计算型节点时，cpu占有率是很低的，所以同时使用bat调用多个nuke进程来渲染也不会太影响每个镜头渲染的速度。

###autoBackup
当保存工程文件时，会自动保存一个工程文件备份到非C盘外第一个盘的nuke_backups目录下（默认是D:/nuke_backups，但有时有的人没有d盘，有e盘，那么就会保存到e盘的nuke_backups目录下）

可以点击nuke菜单栏中"Liaokong/open backup dir"打开备份文件列表根目录。

备份文件列表根目录下只保留最近的五个备份文件，如需修改请修改autoBackup/autoBackup.py中的number_of_backups的值。

备份文件列表目录结构：

|
|——nuke_backups

    |——项目名
    
        |——集数_镜头号
        
                |——工程文件名_月日_时分.nk
                
如有需要，请根据自身情况修改。

###writeToRead
选择Write节点，然后执行write To Read命令（快捷键：shift+r）即可导入该Write节点渲染输出的素材。