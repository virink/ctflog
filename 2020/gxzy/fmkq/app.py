import web
from urllib.parse import unquote
from base.readfile import *

urls = (
    '/', 'help',
    '/read/(.*)', 'read'
)
web.config.debug = True
web.config.port = 8801


class help:
    def GET(self):
        help_information = '''
        Welcome to our FMKQ api, you could use the help information below
        To read file:
            /read/file=example&vipcode=example
            if you are not vip,let vipcode=0,and you can only read /tmp/{file}
        Other functions only for the vip!!!
        '''
        return help_information


class read:
    def GET(self, text):
        file2read = readfile(text)
        if file2read.test() == False:
            return "error"
        else:
            if file2read.isvip() == False:
                return ("The content of " + file2read.GetFileName() + " is {file}").format(file=file2read)
            else:
                vipfile2read = vipreadfile(file2read)
                return (str(vipfile2read))


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
