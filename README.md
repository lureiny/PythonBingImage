# PythonBingImage
### 脚本概况

1、基于Python3编写

2、设置桌面壁纸命令仅适用于MacOS

3、默认调用系统Crontab壁纸周期性下载以及设置

4、主执行文件以及执行记录文件放在用户的根目录下

5、图片保存目录为根目录下图片文件夹下默认新建的`Bing_Pictures`文件夹下

### 使用方法

打开MacOS的终端，在终端依次输入

```sh
git clone git@github.com:lureiny/PythonBingImage.git
cd PythonBingImage/
python3 start.py
```

上述命令执行后，终端会进入Crontab文件的编辑页面。如下图，期中[UserName]为用户的用户名。默认为每小时的0、20、40分。各种输出信息放在用户根目录下的`BingPicture.log`文件中。[Crontab文件](https://www.ibm.com/support/knowledgecenter/zh/ssw_aix_71/com.ibm.aix.cmds1/crontab.htm#crontab__rrnpi36bmary)。输入`:wq`，实现对Crontab文件的保存并退出。

