with open('windows.jpg', 'rb') as f:
    a = f.read()
    with open('1.jpg', 'wb') as ff:
        ff.write(a[0:0x6E6B9E])
