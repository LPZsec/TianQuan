# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import csv
import threadpool
import subprocess
from multiprocessing import Process, Pool
from multiprocessing import Manager
import sys
import venorse
import libnmap
import serviceid

def getserv(url):
    info = []
    try:
        response = requests.head(url, timeout=10)
        try:
            head = response.headers
            info = head["Server"]
            return info
        except AttributeError:
            return 0
    except :
        print('Crawling Failed', url)
        return 0


def get_blog_content(url):
    info = []
    try:
        response = requests.get(url,timeout=10)
        Struts = response.status_code
        try:
            if Struts != 404 or Struts != 403 or Struts != 401:
                soup = BeautifulSoup(response.text, 'html.parser')
                head = soup.title.get_text()
                for str in head:
                    info.append(str.encode("utf-8"))
                return info
        except AttributeError:
            return 0
    except requests.exceptions.RequestException:
        print('Crawling Failed', url)
        return 0

def ser_ip(infofile):
    goals = []
    with open(infofile,"r") as resf:
        lines = resf.readlines()
        try:
            for line in lines:
                    result = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", line)

                    port = re.findall(r'\btcp \S*? \b',line)
                    if len(result) > 0:
                        result1 = re.findall(r"[0-9]",port[0])
                        str_convert = ''.join(result1)
                        goal = [result[0],str_convert]
                        goals.append(goal)
        except :
            pass
        return goals

def writcsv(ip):
    with open("bridge.csv","a+") as res1:
        writer = csv.writer(res1)
        sertype = serviceid.get_server(ip[1])
        if sertype == 0 :
            title = get_blog_content("http://%s:%s/" % (ip[0], ip[1]))
            service = getserv("http://%s:%s/" % (ip[0], ip[1]))
            if title != 0:
                title = "".join(title)
                if service !=0:
                    service = "".join(service)
                    ai = [ip[0], ip[1],title,service]
                else:
                    ai = [ip[0], ip[1], title,"Unkown"]
                print ai
                writer.writerow(ai)
        else:
            ai = [ip[0], ip[1],sertype]
            writer.writerow(ai)



if __name__ == '__main__':

    print "duo.py rate input ports output"
    cmd = "masscan --rate %s -iL %s -p %s -oL %s" % (sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    masscan = subprocess.Popen(cmd,shell=True)
    masscan.wait()
    ips = ser_ip(sys.argv[4])
    pool = Pool(50)
    pool.map(writcsv, ips)
    pool.close()
    pool.join()
    venorse.getWebinfo("bridge.csv","data.csv")
    venorse.getType("bridge.csv","data.csv")
