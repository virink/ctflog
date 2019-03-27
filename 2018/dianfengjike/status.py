import requests as req

webszz = [
    "www.yx-tv.com",
    "www.yx-zhongyiyuan.com",
    "yy.yx-zhongyiyuan.com",
    "www.yx-gcdx.com",
    "tushu.yx-gcdx.com",
    "www.zhaolog.com",
    "www.yx-news.com",
    "www.yx-youyun.com",
    "www.yx-bbs.com"
]

webspt = [
    "www.yx-hticket.com",
    "www.yx-bluenum.com",
    "www.yx-hzconputer.com",
    "www.yx-qiyefangwu.com",
    "www.yx-yiwang.com",
    "www.yx-diya.com",
    "www.yx-penwujinhua.com",
    "www.yx-Kindergarten.com",
    "www.yx-happyshot.com",
    "www.yx-lvyou.com",
    "www.yx-mujuchang.com",
    "www.yx-ranshaoshebei.com",
    "www.yx-viyachuanglian.com",
    "www.yx-huabeistar.com",
    "www.yx-redFinance.com",
    "www.yx-Finance.com",
    "www.yx-restaurantps.com",
    "www.yx-hiweb.com",
    "www.yx-schoolboke.com",
    "www.yx-lierenol.com",
    "www.yx-lvxingshe.com",
    "www.yx-yiqunart.com",
    "www.yx-wangshangshudian.com",
    "www.yx-mhlyz.com",
    "www.yx-Ezhan.com",
    "www.yx-4star.com",
    "www.yx-yxhouse.com",
    "www.yx-baixinghouse.com",
    "www.yx-housezhongjie.com",
    "www.yx-xunfeixiaoshuo.com",
    "www.yx-xchospital.com",
    "www.yx-zaixianmenzhen.com",
    "www.yx-yishuzhuanyin.com",
    "www.yx-chemical.com",
    "www.yx-tea.com",
    "www.yx-guanggaozehua.com",
    "www.yx-gccompany.com",
    "www.yx-Cosmeticsl .com",
    "www.yx-windows.com",
    "www.yx-jianzujianli.com",
    "www.yx-fengwang.com",
    "www.yx-beiyuqiuzhi.com",
    "www.yx-water.com",
    "www.yx-bc.com",
    "www.yx-duanqizufang.com",
    "www.yx-chengshijianshen.com",
    "www.yx-365jd.com",
    "www.yx-qichepeijian.com",
    "www.yx-wenhuaju.com",
    "www.yx-machinfac.com",
    "www.discuz.net",
    "www.yx-tongxunlu.com"
]


def getStatus():
    for i in webspt:
        try:
            res = req.get("http://%s/xjb.aspx" % i, timeout=10)
            if res.status_code == 200:
                print("ok , ", "http://%s" % i)
        except:
            pass
    # for i in webszz:
    #     try:
    #         res = req.get("http://%s" % i)
    #         if res.status_code == 200:
    #             print("ok , ", "http://%s" % i)
    #     except:
    #         pass

if __name__ == '__main__':
    getStatus()
