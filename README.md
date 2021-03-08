# jd-session-capture
Android7.0版本以上的手机进行某东抓包

## 安装[frida](https://github.com/frida/frida)

```shell
pip install frida-tools

```
在frida release里下载对应CPU版本的frida-server
将frida-server下载下来并解压，为了方便操作重命名为frida

```shell
# adb连接手机，开启USB调试并进行端口转发
adb forward tcp:27042 tcp:27042
# 执行下面命令把frida文件放到下面文件夹
adb push E:frida /data/local/tmp

# 进入shell命令
adb shell
# 修改权限
chmod 777 /data/local/tmp/frida
# 运行frida
/data/local/tmp/frida

# 如需修改frida监听端口
./frida -l 0.0.0.0:8888
adb forward tcp:8888 tcp:8888
```

再开一个窗口
```shell
frida-ps -U # USB设备
frida-ps -R # 远程设置-Remote
```
显示进程信息表示成功

直接运行main.py或者
```shell
frida -U com.jingdong.app.mall -l e:\sslunpinning.js --no-pause
```
