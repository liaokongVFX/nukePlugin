# nukePlugin
自己写的一些nuke小插件


## 安装方法：
放入用户文件夹下的.nuke目录下即可

eg：
C:\Users\Liaokong\\.nuke\


## 使用方法：

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