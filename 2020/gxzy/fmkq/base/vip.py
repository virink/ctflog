import random
import string


vipcode = ''


class vip:
    def __init__(self):
        global vipcode
        if vipcode == '':
            vipcode = ''.join(random.sample(
                string.ascii_letters+string.digits, 48))
            self.truevipcode = vipcode
        else:
            self.truevipcode = vipcode

    def GetCode(self):
        return self.truevipcode
