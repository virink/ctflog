import jwt
import time

secret = b'M'
expire_time = int(time.time() + 3600)  # 1 小时后超时

encoded = jwt.encode({'id': 4294967296, 'exp': expire_time},
                     secret, algorithm='HS256')
encoded_str = str(encoded, encoding='ascii')
print(encoded_str)
