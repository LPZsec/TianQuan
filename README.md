### 天权
-   “天权” 网络资产探测，采用masscan进行设备存活，通过自建的关键词库去识别资产类别（目前只区分了一般性网络资产和重点网络资产）
-   使用方法
```
sudo duo.py rate input ports output
sudo duo.py 4000 input_IPlist 80,8080,8888,9000,9001 data.csv
```
-   ip只能通过文件读取，支持 CDIR 格式 / 0.0.0.0-255.255.255.255 / 127.0.0.1 
-   这里的速率是指 masscan 的扫描速率一般网络推荐 2000-10000 速率过高会导致目标丢失
-   在厂商识别中有两个模式一个是
    -   getWebinfo() :用于识别Web信息
    -   getType() ； 用于识别目标设备类型（基于banner）
-   web_vulnscan.py 存放漏洞监测模块，目前还处于开发阶段
