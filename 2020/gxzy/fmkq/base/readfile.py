from .vip import vip
import re
import os


class File:
    def __init__(self, file):
        self.file = file

    def __str__(self):
        return self.file

    def GetName(self):
        return self.file


class readfile():

    def __str__(self):
        filename = self.GetFileName()
        if '..' in filename or 'proc' in filename:
            return "quanbumuda"
        else:
            try:
                file = open("/tmp/" + filename, 'r')
                content = file.read()
                file.close()
                return content
            except:
                return "error"

    def __init__(self, data):
        if re.match(r'file=.*?&vipcode=.*?', data) != None:
            data = data.split('&')
            data = {
                data[0].split('=')[0]: data[0].split('=')[1],
                data[1].split('=')[0]: data[1].split('=')[1]
            }
            if 'file' in data.keys():
                self.file = File(data['file'])

            if 'vipcode' in data.keys():
                self.vipcode = data['vipcode']
            self.vip = vip()

    def test(self):
        if 'file' not in dir(self) or 'vipcode' not in dir(self) or 'vip' not in dir(self):
            return False
        else:
            return True

    def isvip(self):
        if self.vipcode == self.vip.GetCode():
            return True
        else:
            return False

    def GetFileName(self):
        return self.file.GetName()


current_folder_file = []


class vipreadfile():
    def __init__(self, readfile):
        self.filename = readfile.GetFileName()
        self.path = os.path.dirname(os.path.abspath(self.filename))
        self.file = File(os.path.basename(os.path.abspath(self.filename)))
        print(self.path, self.file)
        global current_folder_file
        try:
            current_folder_file = os.listdir(self.path)
        except:
            current_folder_file = current_folder_file

    def __str__(self):
        # (self.path + '/{vipfile}').format(vipfile=self.file)
        # ('/{vipfile.file[0]}xxxxxxx/{vipfile}').format(vipfile=self.file)
        if 'fl4g' in self.path:
            return 'nonono,this folder is a secret!!!'
        else:
            output = '''Welcome,dear vip! Here are what you want:\r\nThe file you read is:\r\n'''
            filepath = (self.path + '/{vipfile}').format(vipfile=self.file)
            output += filepath
            output += '\r\n\r\nThe content is:\r\n'
            try:
                f = open(filepath, 'r')
                content = f.read()
                f.close()
            except:
                content = 'can\'t read'
            output += content
            output += '\r\n\r\nOther files under the same folder:\r\n'
            output += ' '.join(current_folder_file)
            return output
