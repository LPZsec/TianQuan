# -*- coding:utf-8 -*-
import csv
import re
import pandas as pd
import numpy as np
import types
import serviceid

def getType(infofie,resfile):

    with open(resfile,"a+") as resfl:
        writer = csv.writer(resfl)
        with open (infofie,"r") as files:
                csv.field_size_limit(500 * 1024 * 1024)
                lines = csv.reader(files)
                for line in lines :
                    ip = line[0]
                    port = line[1]
                    try :
                        for i in range(len(line)) :
                            vul = line[i]
                            vul = vul.strip()
                            if len(vul) >= 100 :
                                line.remove(line[i])

                    except :
                        pass
                    df = pd.read_csv("bestvendor.csv")
                    Routers = np.array(df.Router).tolist()
                    PLC = np.array(df.PLC).tolist()
                    Bacnet = np.array(df.Bacnet).tolist()
                    IOT = np.array(df.IOT_net).tolist()
                    Web_camera = np.array(df.Web_camera).tolist()
                    SQL = np.array(df.SQL).tolist()
                    Utm = np.array(df.Utm).tolist()
                    Electric = np.array(df.Electric).tolist()
                    RTOS = np.array(df.RTOS).tolist()
                    SCADA = np.array(df.RTOS).tolist()
                    SYSTEM = np.array(df.SYSTEM).tolist()
                    vendores = Routers+PLC+Bacnet+IOT+Web_camera+SQL+Utm+Electric+RTOS+SCADA
                    for i in range(len(line)):
                            if i > 1:
                                vu = line[i]
                                for vend in vendores:
                                    try:
                                        ret = re.findall(vend, vu)
                                        if len(ret) > 0:
                                        # for ven in vendor:
                                        #     ret = re.findall('%s?' % ven[0], '%s' % vu)
                                            if vend in Routers:
                                                dev_type = "Router"
                                                res1 = [ip,port,vend,"Focus_system",dev_type]
                                                print res1
                                                writer.writerow(res1)
                                            elif vend in PLC:
                                                dev_type = "PLC"
                                                res1 = [ip,port,vend,"Focus_system",dev_type]
                                                print res1
                                                writer.writerow(res1)
                                            elif vend in Bacnet:
                                                dev_type = "Bacnet"
                                                res1 = [ip,port,vend,"Focus_system",dev_type]
                                                print res1
                                                writer.writerow(res1)
                                            elif vend in IOT:
                                                dev_type = "IOT"
                                                res1 = [ip,port,vend,"Focus_system",dev_type]
                                                print res1
                                                writer.writerow(res1)
                                            elif vend in Web_camera:
                                                dev_type = "Web_camera"
                                                res1 = [ip,port,vend,"Focus_system",dev_type]
                                                print res1
                                                writer.writerow(res1)
                                            elif vend in SQL:
                                                dev_type = "SQL"
                                                res1 = [ip,port,vend,"Focus_system",dev_type]
                                                print res1
                                                writer.writerow(res1)
                                            elif vend in Utm:
                                                dev_type = "Utm"
                                                res1 = [ip,port,vend,"Focus_system",dev_type]
                                                print res1
                                                writer.writerow(res1)
                                            elif vend in Electric:
                                                dev_type = "Electric"
                                                res1 = [ip,port,vend,"Focus_system",dev_type]
                                                print res1
                                                writer.writerow(res1)
                                            elif vend in RTOS:
                                                dev_type = "RTOS"
                                                res1 = [ip,port,vend,"Focus_system",dev_type]
                                                print res1
                                                writer.writerow(res1)
                                            elif vend in SCADA:
                                                dev_type = "SCADA"
                                                res1 = [ip,port,vend,"Focus_system",dev_type]
                                                print res1
                                                writer.writerow(res1)
                                            elif vend in SYSTEM :
                                                dev_type = "SYSTEM"
                                                res1 = [ip,port,vend,"Focus_system",dev_type]
                                                print res1
                                                writer.writerow(res1)

                                    except:
                                        pass
def getWebinfo(infofile,resfile):
    with open(resfile, "w") as resfl:
        writer = csv.writer(resfl)
        writer.writerow(["IP","Port","Server","Applcation","Device_type"])
        with open(infofile, "r") as files:
            csv.field_size_limit(500 * 1024 * 1024)
            lines = csv.reader(files)
            keyinfo = ["管理","平台","监测","工业云","登录","智慧城市","系统","监控","监督","login","Log In","工业互联网","OA","视频","网关","ZXV10","NETSurveillance","admin","大数据","ProCurve","天擎","登陆"]
            for line in lines:
                serc = serviceid.get_server(line[1])
                title = line[2]
                if serc != 0:
                    ai = [line[0], line[1], serc, serc, "Server"]
                    writer.writerow(ai)
                else:
                    try:
                        for i in range(len(keyinfo)):
                            res = re.findall(keyinfo[i], title)
                            res = str(res)
                            if len(res) > 3:
                                result = [line[0], line[1], line[3], "Focus_system", "Web_service", line[2]]
                                writer.writerow(result)
                                break
                            elif i == len(keyinfo)-1:
                                result = [line[0], line[1], line[3], "NormalWeb", "Web_service",line[2]]
                                writer.writerow(result)


                    except:
                        pass

if __name__ == '__main__':

    getWebinfo("bridge.csv","data.csv")






